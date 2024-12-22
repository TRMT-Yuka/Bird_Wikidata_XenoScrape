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

# =================================================================================================
import os
from concurrent.futures import ProcessPoolExecutor, as_completed
from pydub import AudioSegment
from pydub.silence import split_on_silence

def process_audio(input_tuple):
    try:
        bird_id, sound_id = input_tuple
        if os.path.exists("E:\\xeno_data\\"+bird_id+"\\"+sound_id) and not os.path.exists("E:\\trimmed_xeno_data\\"+bird_id+"\\"+sound_id):
            sound = AudioSegment.from_mp3("E:\\xeno_data\\"+bird_id+"\\"+sound_id)
            chunks = split_on_silence(
                sound,
                min_silence_len=500,  # 0.5秒以上の無音を検出
                silence_thresh=-90    # -90dBFS 以下を無音と判定
            )

            combined = AudioSegment.empty()
            for chunk in chunks:
                combined += chunk

            if len(combined) > 30_000:
                combined = combined[:30_000]
            
            if not os.path.exists("E:\\trimmed_xeno_data\\"+bird_id):
                os.makedirs("E:\\trimmed_xeno_data\\"+bird_id)
                
            combined.export("E:\\trimmed_xeno_data\\"+bird_id+"\\"+sound_id, format="mp3")

    except:
        return input_tuple