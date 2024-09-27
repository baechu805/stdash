import streamlit as st
import pandas as pd
from app import load_data
import matplotlib.pyplot as plt

st.markdown("# Page 2 ")
st.sidebar.markdown("# Page 2 ")

data = load_data()
df = pd.DataFrame(data)

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

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