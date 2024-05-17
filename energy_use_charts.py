import streamlit as st
import pandas as pd
# import numpy as np
st.title('Exploring Home Energy Use')

st.write('I lived in an 800 sq ft condo for four years and obtained the monthly energy use data from the utility company (XCel). I wanted to explore what it looked like and glean some insights.')

st.subheader('Summary kWh Usage Per Year')
summary_data = pd.read_csv("data/SummaryUseXCel.csv", dtype={'year': str})
# pd.to_numeric(summary_data['year'], downcast='integer')
summary_chart_data = summary_data.set_index('year')
st.dataframe(summary_chart_data)
percentReduced = ((summary_chart_data['sum'][0] - summary_chart_data['sum'][2]) / summary_chart_data['sum'][0]) * 100;
# st.bar_chart(summary_chart_data, x="year")
st.caption(f'I was able to bring down use {percentReduced:.0f}%')

st.subheader('Monthly Energy Use, 2021-2023')
data = pd.read_csv("data/MonthlyUseXcelRows.csv")
chart_data = data.filter(['date','kWh'], axis=1)
st.line_chart(chart_data, x="date", y="kWh", color='#992399')



