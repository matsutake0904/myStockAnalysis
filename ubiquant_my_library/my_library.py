import pandas as pd

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
