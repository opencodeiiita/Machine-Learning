# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 11:21:42 2019

@author: Manish Jagnani
"""

import pandas as pd

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
train_data_x = train_data.iloc[0:,0].values
train_y = train_data.iloc[0:,1].values
test_data_x = test_data.iloc[0:, 0].values
test_y = test_data.iloc[0:, 1].values