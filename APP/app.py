import streamlit as st
import pandas as pd
import numpy as np

st.title("ODD-SIDE")

st.sidebar.header("Leagues")
selected_league = st.sidebar.selectbox('League', ['England', 'Scotland', 'Germany', 'Italy', 'Spain', 'France', 'Netherlands', 'Belgium', 'Portugal', 'Turkey', 'Greece', 'Argentina', 'Austria', 'Brazil', 'China', 'Denmark', 'Finland', 'Ireland', 'Japan', 'Mexico', 'Norway', 'Poland', 'Romania', 'Russia', 'Sweden', 'Switzerland', 'USA', 'ALL'])
st.sidebar.header("Season")
selected_season = st.sidebar.selectbox('Season', ['2022/2023', '2021/2022', '2020/2021', '2019/2020'])


#Webscrapping for football-data.co.uk
#https://www.football-data.co.uk/mmz4281/2223/E0.csv

def load_data(league, season):
  if selected_league == 'England':
    league = 'E0'

  if selected_season == '2022/2023':
    season = '2223'
    
  url = "https://www.football-data.co.uk/mmz4281/"+season+"/"+league+".csv"
  data = pd.read_csv(url)
  return data

df = load_data(selected_league, selected_season)

st.subheader("Country: " +selected_league)
st.dataframe(df)


