import streamlit as st
import pandas as pd
import numpy as np
import datetime
from datetime import date


st.title("Matches of the Day")

dia = st.date_input("Date: ", date.today())

def load_data_matches():
  data_matches = pd.read_csv("")
