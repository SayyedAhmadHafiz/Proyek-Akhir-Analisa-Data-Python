import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_busiest_hour(df):
    penyewaan_per_jam = df.groupby('hr')['cnt'].sum()
    penyewaan_per_jam_df = pd.DataFrame({'Jam': penyewaan_per_jam.index, 'Total Penyewaan': penyewaan_per_jam.values})
    jam_tertinggi = penyewaan_per_jam_df['Total Penyewaan'].idxmax()

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(penyewaan_per_jam_df['Jam'], penyewaan_per_jam_df['Total Penyewaan'], color='lightblue')

    ax.set_xlabel('Jam')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Sepeda per Jam')

    bars[jam_tertinggi].set_color('blue')

    ax.set_xticks(penyewaan_per_jam_df['Jam'])

    st.pyplot(fig)

def create_daily_trend_plot(df):
    daily_rentals = df.groupby('dteday')['cnt'].sum()

    daily_rentals.index = pd.to_datetime(daily_rentals.index)

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(daily_rentals.index, daily_rentals)
    ax.set_title('Tren Peningkatan atau Penurunan Penyewaan Sepeda')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewaan Sepeda')
    ax.grid(True)

    st.pyplot(fig)

def create_hours_analyst(df):
    hourly_rentals = df.groupby('hr')['cnt'].sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(hourly_rentals.index, hourly_rentals.values)
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Sepeda per Jam dalam Sehari')
    ax.grid(True)

    st.pyplot(fig)

def create_months_analyst(df):
    monthly_rentals = df.groupby('mnth')['cnt'].sum()

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(monthly_rentals.index, monthly_rentals.values)
    ax.set_xlabel('Bulan dalam Setahun')
    ax.set_ylabel('Total Penyewaan')
    ax.set_title('Total Penyewaan Sepeda per Bulan dalam Setahun')
    ax.grid(True)

    st.pyplot(fig)

def create_holiday_workday(df):
    holiday_data = df[df['holiday'] == 1]
    non_holiday_data = df[df['holiday'] == 0]

    average_rental_holiday = holiday_data['cnt'].mean()
    average_rental_non_holiday = non_holiday_data['cnt'].mean()

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(['Holiday', 'Non-Holiday'], [average_rental_holiday, average_rental_non_holiday])
    ax.set_xlabel('Tipe Hari')
    ax.set_ylabel('Rata-rata Penyewaan')
    ax.set_title('Perbandingan Rata-rata Penyewaan Selama Hari Libur dan Hari Kerja')
    ax.grid(True)

    st.pyplot(fig)

with st.sidebar:
    st.image("https://png.pngtree.com/png-vector/20220730/ourmid/pngtree-vector-illustration-of-a-bike-rental-logo-on-a-white-background-vector-png-image_28066930.png")

st.title("Analisis Data Penyewaan Sepeda")
df = pd.read_csv("Dashboard/new_hours.csv")

st.subheader("Jam Tersibuk")
create_busiest_hour(df)

st.subheader("Tren Harian")
create_daily_trend_plot(df)

st.subheader("Pola Penyewaan Setiap Jam")
create_hours_analyst(df)

st.subheader("Pola Penyewaan Setiap Bulan")
create_months_analyst(df)

st.subheader("Perbandingan Rata-rata Penyewaan Selama Hari Libur dan Hari Kerja")
create_holiday_workday(df)

st.caption('Copyright (c) Dicoding 2023')
