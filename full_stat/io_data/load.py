__author__ = 'yarnaid'

import pandas as pd
from data_model import Data


def read_csv(file_name):
    '''
    :param file_name: file with input data
    :return: pandas.DataFrame with data

    TODO: Add feature to select column names

    '''

    names = ['x', 'y', 'y_err']
    df = pd.read_csv(file_name, names=names)
    df.dropna()
    # columns = df.columns.values

    return df