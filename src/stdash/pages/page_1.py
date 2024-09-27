import streamlit as st
import pandas as pd
from app import load_data
import matplotlib.pyplot as plt


st.markdown("# Page 1 ")
st.sidebar.markdown("# Page 1")

data = load_data()
df = pd.DataFrame(data)

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

# request_time을 인덱스로 설정
df_time.set_index('request_time', inplace=True)

# st.bar_chart를 사용하여 막대 그래프 그리기
st.bar_chart(df_time['count'])


