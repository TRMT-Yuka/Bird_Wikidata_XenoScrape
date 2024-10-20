import pickle
import pandas as pd
import os

#バイナリファイルの読み書き
def read_bin(filename):
    with open(filename,'rb') as bf:
        bin_data = pd.read_pickle(bf)
    return bin_data

def save_bin(filename,data):
    with open(filename,'wb') as bf:
        pickle.dump(data,bf)

# 指定pathのディレクトリをkey，その下のファイル名一覧のリストをvalueに
def directory_to_dict(path):
    dir_dict = {}
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            sub_dir_path = os.path.join(root, directory)
            dir_dict[directory] = os.listdir(sub_dir_path)
        break
    return dir_dict