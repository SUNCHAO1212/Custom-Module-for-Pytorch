
from data_processing import DataProcessing as DP


if __name__ == '__main__':

    dp = DP(cut_level='word')

    dp.dataset_dir('usrfiles', 'newfiles')

