import numpy as np
import pandas as pd

class simulator:
    def __init__(self):
        self.greeting = "hello"

    def __call__(self, *args, **kwargs):
        return self.greeting

    #
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
        return return_set

