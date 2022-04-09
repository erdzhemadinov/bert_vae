from .base import AbstractDataset

import pandas as pd

from datetime import date


class ML1MDataset(AbstractDataset):
    @classmethod
    def code(cls):
        return 'ml-1m'

    @classmethod
    def url(cls):
        return 'http://files.grouplens.org/datasets/movielens/ml-1m.zip'

    @classmethod
    def zip_file_content_is_folder(cls):
        return True

    @classmethod
    def all_raw_file_names(cls):
        return ['README',
                'movies.dat',
                'ratings.dat',
                'users.dat']

    def load_ratings_df(self):
        folder_path = self._get_rawdata_folder_path()
        # file_path = folder_path.joinpath('ratings.dat')
        # df = pd.read_csv(file_path, sep='::', header=None)
        #
        file_path = folder_path.joinpath('transactions_train.csv')

        df = pd.read_csv(file_path).drop(['sales_channel_id'], axis=1).head(1000000)
        print(df.head())

        df.rename(columns={'t_dat': 'timestamp',
                           'customer_id': 'uid',
                           'article_id':  'sid',
                           'price': 'rating'})


        df.columns = ['uid', 'sid', 'rating', 'timestamp']
        return df


