import pandas as pd
import datetime as dt
import os


def read_dir(path):

    path = "."
    return os.listdir(path)


def to_date_obj(timestamp):
     return dt.datetime.strptime(str(timestamp), '%Y%m%d%H%M%S')

def tranform(fileName):
     try:
               
          df=pd.read_csv(fileName, delimiter=' ')
          df.columns=["urlkey","timestamp","original","mimetype","statuscode","digest","length"]
          df['data'] = df['timestamp'].apply(lambda x: to_date_obj(x))
          df['quarter'] = df['data'].dt.to_period('Q')
          df=df.loc[df.groupby(['quarter', 'original'])['data'].idxmax()]
          csv_name=fileName.split('.txt')[0]
          df.to_csv('./csv/{}.csv'.format(csv_name))
     except Exception as e: print(e)

def main():
     files=read_dir()

     for file in files:
          tranform(file) 

if __name__ == "__main__":
     main()