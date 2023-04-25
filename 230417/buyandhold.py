import numpy as np
from datetime import datetime
import pandas as pd

def bnh(df,column,start,end):
    # 인덱스 시계열로 변경
    df.index = pd.to_datetime(df.index)
    start = datetime.strptime(start,"%Y%m%d").isoformat()
    end = datetime.strptime(end,"%Y%m%d").isoformat()
    df = df.loc[start:end]
    # 결측치, 무한대 제외
    df = df.loc[~df.isin([np.nan,np.inf,-np.inf]).any(axis='columns')]
    # 수정 종가만 있는 데이터프레임으로 변경
    df = df[[column]]
    # 일별 수익률 변수 생성
    df['daily_rtn'] = df[[column]].pct_change()
    # 누적 수익률 변수 생성
    df['st_rtn'] = (1 + df[['daily_rtn']]).cumprod()
    # 데이터프레임을 리턴
    return df                