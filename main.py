import librosa
import soundfile as sf
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_dir = '../LibriMix/storage_dir/LibriSpeech/dev-clean/84/121123/'
# df1=pd.read_csv(data_dir+'train_tp.csv')
# show = df1.iloc[0]
# df1.head()
# 'LibriMix/storage_dir/LibriSpeech/dev-clean/84/121123/84-121123-0000.flac'


data, samplerate = sf.read(data_dir+'84-121123-0000.flac')
times = np.linspace(0,len(data),len(data))/samplerate
plt.plot(times,data)
plt.xlim(1.0, 2.0)
plt.ylim(-.5,.5)
plt.ylabel('Time (s)')
plt.show()