import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Load data
data = pd.read_csv('covid.csv')  # Pastikan file 'covid.csv' ada di direktori yang sama dengan 'app.py'

# Convert 'Date' column to datetime
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Set seaborn style
sns.set(style='dark')

# Streamlit app title
st.title('Visualisasi Data COVID-19')

# 1. Visualisasi tren jumlah kasus baru harian
st.subheader('Tren Jumlah Kasus Baru Harian')
fig = px.line(data, x='Date', y='New Cases', color='Location',
              title='Tren Jumlah Kasus Baru Harian',
              labels={'Date': 'Tanggal', 'New Cases': 'Jumlah Kasus Baru'})
fig.update_traces(mode='lines+markers')  # Menambahkan titik pada garis
fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Jumlah Kasus Baru",
    hovermode="x unified")
st.plotly_chart(fig)

# 2. Visualisasi tren jumlah kematian baru harian
st.subheader('Tren Jumlah Kematian Baru Harian')
fig = px.line(data, x='Date', y='New Deaths', color='Location',
              title='Tren Jumlah Kematian Baru Harian',
              labels={'Date': 'Tanggal', 'New Deaths': 'Jumlah Kematian Baru'})
fig.update_traces(mode='lines+markers')
fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Jumlah Kematian Baru",
    hovermode="x unified"
)
st.plotly_chart(fig)

# 3. Visualisasi total kasus dan total kematian dari waktu ke waktu
st.subheader('Tren Total Kasus dan Total Kematian dari Waktu ke Waktu')
fig = px.line(data, x='Date', y='Total Cases', color='Location',
              title='Tren Total Kasus dari Waktu ke Waktu',
              labels={'Date': 'Tanggal', 'Total Cases': 'Total Kasus'})
fig.update_traces(mode='lines+markers')
fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Total Kasus",
    hovermode="x unified"
)
st.plotly_chart(fig)

fig = px.line(data, x='Date', y='Total Deaths', color='Location',
              title='Tren Total Kematian dari Waktu ke Waktu',
              labels={'Date': 'Tanggal', 'Total Deaths': 'Total Kematian'})
fig.update_traces(mode='lines+markers')
fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Total Kematian",
    hovermode="x unified"
)
st.plotly_chart(fig)

# 4. Perbandingan kasus baru, kematian baru, dan pemulihan baru
st.subheader('Perbandingan Kasus Baru, Kematian Baru, dan Pemulihan Baru')
fig = px.line(data, x='Date', y='New Cases', color='Location',
              title='Perbandingan Kasus Baru, Kematian Baru, dan Pemulihan Baru',
              labels={'Date': 'Tanggal', 'New Cases': 'Kasus Baru'})
fig.add_scatter(x=data['Date'], y=data['New Deaths'], mode='lines+markers', name='Kematian Baru')
fig.add_scatter(x=data['Date'], y=data['New Recovered'], mode='lines+markers', name='Pemulihan Baru')
fig.update_layout(
    xaxis_title="Tanggal",
    yaxis_title="Jumlah",
    hovermode="x unified"
)
st.plotly_chart(fig)