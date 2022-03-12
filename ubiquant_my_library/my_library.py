import numpy as np
import pandas as pd
import statistics


def reduce_mem_usage(df):
    """ iterate through all the columns of a dataframe and modify the data type
        to reduce memory usage.
    """
    start_mem = df.memory_usage().sum() / 1024 ** 2
    print('Memory usage of dataframe is {:.2f} MB'.format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if c_min > np.finfo(np.float16).min and c_max < np.finfo(np.float16).max:
                    df[col] = df[col].astype(np.float16)
                elif c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
        else:
            df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024 ** 2
    print('Memory usage after optimization is: {:.2f} MB'.format(end_mem))
    print('Decreased by {:.1f}%'.format(100 * (start_mem - end_mem) / start_mem))

    return df

# def add_diff_average_columns(reader):
#     # 各investment_idごと
#     investment_id_list = list(reader['investment_id'].loc[~reader['investment_id'].duplicated()])
#     # 追加カラムの初期化
#     after_ind = 'diff_average'
#     reader[after_ind] = pd.Series()
#
#     # 追加カラムへの値挿入
#     for inv_id in investment_id_list:
#         # 各investment_idのレコードを抽出
#         ins_list = reader['investment_id'] == inv_id
#         # 各investment_idでdiffを計算し、カラムへ挿入
#         diff_list = []
#         reader.loc[ins_list, after_ind] = 0
#         for i in range(300):
#             ind = 'f_' + str(i)
#             # reader.loc[reader['row_id'] == data_01['row_id']][after_ind] = data_01[data_01.columns[data_01.columns != 'row_id']].diff()[ind]
#             reader.loc[ins_list, after_ind] += reader[reader.columns[reader.columns != 'row_id']].loc[ins_list].diff()[ind]
#         reader.loc[ins_list, after_ind] = reader.loc[ins_list, after_ind]/300.
#         # reader.loc[ins_list, after_ind] = statistics.mean([float(x) for x in diff_list])
#     reader.loc[reader[after_ind].isna(), after_ind] = 0
#     return reader

# diffカラムを追加する関数
def add_diff_columns(reader):
    # 各investment_idごと
    investment_id_list = list(reader['investment_id'].loc[~reader['investment_id'].duplicated()])
    # 追加カラムの初期化
    for i in range(300):
        after_ind = 'diff_f_' + str(i)
        reader[after_ind] = pd.Series()

    # 追加カラムへの値挿入
    for inv_id in investment_id_list:
        # 各investment_idのレコードを抽出
        ins_list = reader['investment_id'] == inv_id
        # 各investment_idでdiffを計算し、カラムへ挿入
        for i in range(300):
            ind = 'f_' + str(i)
            after_ind = 'diff_f_' + str(i)
            # reader.loc[reader['row_id'] == data_01['row_id']][after_ind] = data_01[data_01.columns[data_01.columns != 'row_id']].diff()[ind]
            reader.loc[ins_list, after_ind] = reader[reader.columns[reader.columns != 'row_id']].loc[ins_list].diff()[ind]
    for i in range(300):
        ind = 'f_' + str(i)
        after_ind = 'diff_f_' + str(i)
        reader.loc[reader[after_ind].isna(), after_ind] = 0
    return reader


# diffカラムを追加する関数
def add_diff_average_columns(reader):
    # 各investment_idごと
    investment_id_list = list(reader['investment_id'].loc[~reader['investment_id'].duplicated()])
    # 追加カラムの初期化
    after_ind = 'diff_average'
    reader[after_ind] = pd.Series()

    # 追加カラムへの値挿入
    for inv_id in investment_id_list:
        # 各investment_idのレコードを抽出
        ins_list = reader['investment_id'] == inv_id
        # 各investment_idでdiffを計算し、カラムへ挿入
        diff_list = []
        reader.loc[ins_list, after_ind] = 0
        for i in range(300):
            ind = 'f_' + str(i)
            # reader.loc[reader['row_id'] == data_01['row_id']][after_ind] = data_01[data_01.columns[data_01.columns != 'row_id']].diff()[ind]
            reader.loc[ins_list, after_ind] += reader[reader.columns[reader.columns != 'row_id']].loc[ins_list].diff()[ind]
        reader.loc[ins_list, after_ind] = reader.loc[ins_list, after_ind]/300.
        # reader.loc[ins_list, after_ind] = statistics.mean([float(x) for x in diff_list])
    reader.loc[reader[after_ind].isna(), after_ind] = 0
    return reader
