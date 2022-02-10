import numpy as np
import pandas as pd

class simulator:
    def __init__(self):
        self.greeting = "hello"

    def __call__(self, *args, **kwargs):
        return self.greeting

    ''' 
     関数名：移動平均計算
     dataset: 時系列データ（list or numpy）
     window: 移動平均窓
     reverseFlg: 移動平均の方向を決めるフラグ。
                True: 基準日よりwindow日間後の期間の平均
                False: 基準日よりwindow日間前の期間の平均
    '''
    def moving_ave(self, dataset, window, reverseFlg):
        if reverseFlg:
            dataset = np.array(dataset[::-1])
        else:
            dataset = np.array(dataset)
        return_set = np.ndarray([dataset.size])
        for i in range(len(dataset)):
            if i + window < len(dataset):
                return_set[i] = np.average(dataset[i :i + window])
            else:
                return_set[i] = np.average(dataset[i:])
        if reverseFlg:
            return return_set[::-1]
        else:

            return return_set
    ''' 
     関数名：rsi計算
     dataset: 時系列データ（list or numpy）
     n: RSIを計算する期間
    '''
    def rsi(self, dataset, n=14):
        return_set = np.ndarray([len(dataset)])
        data_0 = dataset[0]
        for i in range(len(dataset)):
            rs_up = np.array([0])
            rs_down = np.array([0])
            if i - n < 0:
                dataset_n = dataset[:i+1]
            else:
                dataset_n = dataset[i-n:i+1]
            for data in dataset_n:
                if data > data_0:
                    if rs_up[0] == 0:
                        rs_up[0]=data - data_0
                    else:
                        rs_up = np.append(rs_up, (data - data_0))
                elif data < data_0:
                    if rs_down[0] == 0:
                        rs_down[0]= data_0 - data
                    else:
                        rs_down = np.append(rs_down, (data_0 - data))
                data_0 = data
            rs = rs_up.mean() / (rs_down.mean() + 10.**-20)
            print(rs_up)
            print(rs_down)
            return_set[i] = int(100. - (100. / (rs+1.)))
        return return_set