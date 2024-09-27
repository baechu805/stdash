import pandas as pd
import matplotlib.pyplot as plt
import requests
import streamlit as st


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


df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

df_time = df.groupby('request_time').size().reset_index(name='count')
df_time

# 그래프 그리기
fig, ax = plt.subplots(figsize=(10,6))
df_time.plot(kind='bar', x='request_time', y='count', ax=ax)
plt.plot(df_time.index, df_time['count'], 'ro-')
ax.set_title('Requests by Date and Time')
ax.set_xlabel('Date and Time')
ax.set_ylabel('Number of Requests')
plt.xticks(rotation=45)
plt.tight_layout()

# Streamlit을 통해 차트 표시
st.pyplot(fig)

# 요청자, 처리자간의 통계 / 불균형
df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['prediction_time'] = df['prediction_time'].dt.strftime('%Y-%m-%d-%H')

# request_time과 prediction_time이 일치하지 않는 경우만 필터링
dif_diff = df[df['request_time'] != df['prediction_time']]

dif_user = dif_diff.groupby('request_user').size().reset_index(name='count')
dif_user

fig, ax = plt.subplots(figsize=(10,6))
ax.pie(dif_user['count'], labels=dif_user['request_user'], autopct='%1.1f%%', startangle=90)
ax.set_title('Users experiencing processing problems')

st.pyplot(fig)




