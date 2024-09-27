import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('CNN JOB MON')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)


# TODO
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
# 즉 시간별 GROUB BY COUNT 하여 plt 차트 그려보기

#df['request_time'] = pd.to_datetime()
#df['request_time'].dt.strftime('%Y-%m-%d %H')
#df.groupby('ABC').size()

#plt.bar()
#plt.plot()
#plt.xlabel()

#st.pyplot(plt)