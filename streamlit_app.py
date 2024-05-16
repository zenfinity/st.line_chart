import streamlit as st
import pandas as pd
# import numpy as np

st.header('Monthly Energy Use, 2021-2023')

data = pd.read_csv("data/MonthlyUseXcelRows.csv")

chart_data = data.filter(['date','kWh'], axis=1)

st.line_chart(chart_data, x="date", y="kWh")
