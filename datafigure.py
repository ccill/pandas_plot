import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def data_plot(file):
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    df=pd.read_json(file)
    df_groupby=df[['user_id','minutes']].groupby('user_id').sum()
    ax.set_title('StudyData')
    ax.set_xlabel('User ID')
    ax.set_ylabel('Study Time')
    ax.plot(df_groupby)
    fig.show()
    return ax


data_plot('user_study.json')

