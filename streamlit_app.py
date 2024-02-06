import streamlit as st
import pandas as pd
import numpy as np

st.title('Tax Insights for Single Filer')

st.sidebar.title('Inputs')

income_type = st.radio("How do you get paid?",
                       ["Hourly", "Salary"])
if income_type == 'Hourly':
  salary = st.number_input('Hourly Wage ($):', step = 0.5) * 40 * 52
if income_type == 'Salary':
  salary = st.number_input('Annual Wage ($):', step = 500)

st.text("""
Your annual wage:  ${:,.2f} """.format(salary))
  
