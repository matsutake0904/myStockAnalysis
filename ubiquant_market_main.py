from AnalyStockLib.simulator import simulator
from ubiquant_my_library import my_library
import pandas as pd

if __name__ == '__main__':
    # path = '/Users/ryo/Work/python_work/kaggle/ubiquant_market/train_head1000.csv'
    path_w = f'/Users/ryo/Work/python_work/kaggle/ubiquant_market/train_mabiki100.csv'
    df0 = pd.read_csv(path_w)

    df = my_library.add_diff_columns(df0)
    print("____end add_diff_columns_____")

    from sklearn.model_selection import train_test_split
    import lightgbm as lgb
    from lightgbm import *

    features = [f'f_{i}' for i in range(300)]
    for i in range(300):
        features.append(f'diff_f_{i}')
    target = 'target'
    df_features = df[features]
    X_train, X, Y_train, Y = train_test_split(df_features, df[target], train_size=0.6, shuffle=False)
    X_val, X_test, Y_val, Y_test = train_test_split(X, Y, train_size=0.5, shuffle=False)

    print("______end split data_____")

    import warnings
    import lightgbm as lgb
    from scipy.stats import pearsonr

    warnings.filterwarnings('ignore')

    lgb_train = lgb.Dataset(X_train, Y_train)
    lgb_eval = lgb.Dataset(X_val, Y_val, reference=lgb_train)


    params = {'seed': 1,
               'objective': "regression",
               'learning_rate': 0.02,
               'bagging_fraction': 0.2,
               'bagging_freq': 1,
               'feature_fraction': 0.3,
               'max_depth': 10,
               'min_child_samples': 50,
               'num_leaves': 128} #64}

    gbm = lgb.train(params,
                    lgb_train,
                    num_boost_round=19450815,
                    valid_sets=lgb_eval,
                    #verbose_eval=False,
                    early_stopping_rounds=10,
                    )

    Y_pred = gbm.predict(X_test, num_iteration=gbm.best_iteration)

    score_tuple = pearsonr(Y_test, Y_pred)
    score = score_tuple[0]
    print(f"Validation Pearsonr score : {score:.4f}")


    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn.model_selection import train_test_split

    #特徴量の重要度
    feature = gbm.feature_importance(importance_type='gain')

    #特徴量の重要度を上から順に出力する
    f = pd.DataFrame({'number': range(0, len(feature)),
                 'feature': feature[:]})
    f2 = f.sort_values('feature',ascending=False)

    #特徴量の名前
    label = X_train.columns[0:]

    #特徴量の重要度順（降順）
    indices = np.argsort(feature)[::-1]

    for i in range(len(feature)):
        print(str(i + 1) + "   " + str(label[indices[i]]) + "   " + str(feature[indices[i]]))

    plt.title('Feature Importance')
    plt.bar(range(len(feature)),feature[indices], color='lightblue', align='center')
    plt.xticks(range(len(feature)), label[indices], rotation = 90)
    plt.xlim([-1, len(feature)])
    plt.tight_layout()
    plt.show()

