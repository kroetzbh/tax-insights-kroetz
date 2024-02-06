import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import csv

with open('Single_Filer_Income_Tax_2023.csv','r') as f:
  reader = csv.reader(f)
  data = list(reader)

data_array = np.array(data, dtype = float)

limit = (data_array[0:3,0])
print(limit)

st.title('2023 Tax Insights for A Single Filer')

st.sidebar.title('Inputs')

state = st.sidebar.selectbox(
  'What state do you live in?',
  ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
  )

income_type = st.sidebar.radio("How do you get paid?",
                              ["Hourly", "Salary"])
if income_type == 'Hourly':
  salary_gross = st.sidebar.number_input('Hourly Wage ($):', step = 0.01, min_value=0.00) * 40 * 52
if income_type == 'Salary':
  salary_gross = st.sidebar.number_input('Annual Wage ($):', step = 1, min_value=0)

option_401k = st.sidebar.radio("Do you contribute to a Pre-Tax 401k?",
                              ["Yes", "No"])
if option_401k == 'Yes':
  contribution_401k = st.sidebar.number_input('Yearly 401k Contribution ($):', step = 1, max_value=22500, min_value=0)
if option_401k == 'No':
  contribution_401k = 0

option_ira = st.sidebar.radio("Do you contribute to a Pre-Tax IRA?",
                              ["Yes", "No"])
if option_ira == 'Yes':
  contribution_ira = st.sidebar.number_input('Yearly IRA Contribution ($):', step = 1, max_value=7500, min_value=0)
if option_ira == 'No':
  contribution_ira = 0

option_hsa = st.sidebar.radio("Do you contribute to an HSA?",
                              ["Yes", "No"])
if option_hsa == 'Yes':
  contribution_hsa = st.sidebar.number_input('Yearly HSA Contribution ($):', step = 1, max_value=3850, min_value=0)
if option_hsa == 'No':
  contribution_hsa = 0

salary = salary_gross - contribution_401k - contribution_ira - contribution_hsa

st.text("""
Gross Income:         ${:,.2f}        
Taxable Income:       ${:,.2f} """.format(salary_gross, salary))

if state == 'Alabama':
  limit = data_array[0:3,1]
  rate = data_array[0:3,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Arizona':
  rate = data_array[3,0]
  tax_state = salary * rate
if state == 'Arkansas':
  limit = data_array[4:7,1]
  rate = data_array[4:7,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'California':
  limit = data_array[7:17,1]
  rate = data_array[7:17,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6] and salary <= limit[7]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[7] and salary <= limit[8]:
    tax_state = ((salary - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[8] and salary <= limit[9]:
    tax_state = ((salary - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[9]:
    tax_state = ((salary - limit[9]) * rate[9]) + ((limit[9] - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Colorado':
  rate = data_array[17,0]
  tax_state = salary * rate
if state == 'Connecticut':
  limit = data_array[18:25,1]
  rate = data_array[18:25,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Delaware':
  limit = data_array[25:31,1]
  rate = data_array[25:31,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Georgia':
  limit = data_array[31:37,1]
  rate = data_array[31:37,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Hawaii':
  limit = data_array[37:49,1]
  rate = data_array[37:49,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6] and salary <= limit[7]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[7] and salary <= limit[8]:
    tax_state = ((salary - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[8] and salary <= limit[9]:
    tax_state = ((salary - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[9] and salary <= limit[10]:
    tax_state = ((salary - limit[9]) * rate[9]) + ((limit[9] - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[10] and salary <= limit[11]:
    tax_state = ((salary - limit[10]) * rate[10]) + ((limit[10] - limit[9]) * rate[9]) + ((limit[9] - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[11]:
    tax_state = ((salary - limit[11]) * rate[11]) + ((limit[11] - limit[10]) * rate[10]) + ((limit[10] - limit[9]) * rate[9]) + ((limit[9] - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Idaho':
  rate = data_array[49,0]
  tax_state = salary * rate
if state == 'Illinois':
  rate = data_array[50,0]
  tax_state = salary * rate
if state == 'Indiana':
  rate = data_array[51,0]
  tax_state = salary * rate
if state == 'Iowa':
  limit = data_array[52:56,1]
  rate = data_array[52:56,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Kansas':
  limit = data_array[56:59,1]
  rate = data_array[56:59,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Kentucky':
  rate = data_array[59,0]
  tax_state = salary * rate
if state == 'Louisiana':
  limit = data_array[60:63,1]
  rate = data_array[60:63,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Maine':
  limit = data_array[63:66,1]
  rate = data_array[63:66,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Maryland':
  limit = data_array[66:74,1]
  rate = data_array[66:74,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6] and salary <= limit[7]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[7]:
    tax_state = ((salary - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Massachusetts':
  limit = data_array[74:76,1]
  rate = data_array[74:76,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Michigan':
  rate = data_array[76,0]
  tax_state = salary * rate 
if state == 'Minnesota':
  limit = data_array[77:81,1]
  rate = data_array[77:81,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Mississippi':
  rate = data_array[81,0]
  tax_state = salary * rate 
if state == 'Missouri':
  limit = data_array[82:89,1]
  rate = data_array[82:89,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Montana':
  limit = data_array[89:96,1]
  rate = data_array[89:96,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Nebraska':
  limit = data_array[96:100,1]
  rate = data_array[96:100,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'New Jersey':
  limit = data_array[100:107,1]
  rate = data_array[100:107,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'New Mexico':
  limit = data_array[107:112,1]
  rate = data_array[107:112,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'New York':
  limit = data_array[112:121,1]
  rate = data_array[112:121,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6] and salary <= limit[7]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[7] and salary <= limit[8]:
    tax_state = ((salary - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[8]:
    tax_state = ((salary - limit[8]) * rate[8]) + ((limit[8] - limit[7]) * rate[7]) + ((limit[7] - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'North Carolina':
  rate = data_array[121,0]
  tax_state = salary * rate    
if state == 'North Dakota':
  limit = data_array[122:127,1]
  rate = data_array[122:127,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Ohio':
  limit = data_array[127:131,1]
  rate = data_array[127:131,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Oklahoma':
  limit = data_array[131:137,1]
  rate = data_array[131:137,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Oregon':
  limit = data_array[137:141,1]
  rate = data_array[137:141,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Pennsylvania':
  rate = data_array[141,0]
  tax_state = salary * rate  
if state == 'Rhode Island':
  limit = data_array[142:145,1]
  rate = data_array[142:145,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'South Carolina':
  limit = data_array[145:148,1]
  rate = data_array[145:148,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Utah':
  rate = data_array[148,0]
  tax_state = salary * rate 
if state == 'Vermont':
  limit = data_array[149:153,1]
  rate = data_array[149:153,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Virginia':
  limit = data_array[153:157,1]
  rate = data_array[153:157,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'West Virginia':
  limit = data_array[157:162,1]
  rate = data_array[157:162,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Wisconsin':
  limit = data_array[162:166,1]
  rate = data_array[162:166,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'District of Columbia':
  limit = data_array[166:173,1]
  rate = data_array[166:173,0]
  if salary <= limit[1]:
    tax_state = salary * rate[0]
  if salary > limit[1] and salary <= limit[2]:
    tax_state = ((salary - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[2] and salary <= limit[3]:
    tax_state = ((salary - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[3] and salary <= limit[4]:
    tax_state = ((salary - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[4] and salary <= limit[5]:
    tax_state = ((salary - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[5] and salary <= limit[6]:
    tax_state = ((salary - limit[5]) * rate[5]) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
  if salary > limit[6]:
    tax_state = ((salary - limit[6]) * rate[6]) + ((limit[6] - limit[5]) * 9/3/100) + ((limit[5] - limit[4]) * rate[4]) + ((limit[4] - limit[3]) * rate[3]) + ((limit[3] - limit[2]) * rate[2]) + ((limit[2] - limit[1]) * rate[1]) + (limit[1] * rate[0])
if state == 'Alaska' or state == 'Florida' or state == 'Nevada' or state == 'New Hampshire' or state == 'South Dakota' or state == 'Tennessee' or state == 'Texas' or state == 'Washington' or state == 'Wyoming':
  rate = 0
  tax_state = 0

social_security = 0.062 * salary
medicare = 0.0145 * salary

limit_fed = [0, 11000, 44725, 95375, 182100, 231250, 578125]
rate_fed = [.1, .12, .22, .24, .32, .35, .37]
if salary <= limit_fed[1]:
  tax_fed = salary * rate_fed[0]
if salary > limit_fed[1] and salary <= limit_fed[2]:
  tax_fed = ((salary - limit_fed[1]) * rate_fed[1]) + (limit_fed[1] * rate_fed[0])
if salary > limit_fed[2] and salary <= limit_fed[3]:
  tax_fed = ((salary - limit_fed[2]) * rate_fed[2]) + ((limit_fed[2] - limit_fed[1]) * rate_fed[1]) + (limit_fed[1] * rate_fed[0])
if salary > limit_fed[3] and salary <= limit_fed[4]:
  tax_fed = ((salary - limit_fed[3]) * rate_fed[3]) + ((limit_fed[3] - limit_fed[2]) * rate_fed[2]) + ((limit_fed[2] - limit_fed[1]) * rate_fed[1]) + (limit_fed[1] * rate_fed[0])
if salary > limit_fed[4] and salary <= limit_fed[5]:
  tax_fed = ((salary - limit_fed[4]) * rate_fed[4]) + ((limit_fed[4] - limit_fed[3]) * rate_fed[3]) + ((limit_fed[3] - limit_fed[2]) * rate_fed[2]) + ((limit_fed[2] - limit_fed[1]) * rate_fed[1]) + (limit_fed[1] * rate_fed[0])
if salary > limit_fed[5] and salary <= limit_fed[6]:
  tax_fed = ((salary - limit_fed[5]) * rate_fed[5]) + ((limit_fed[5] - limit_fed[4]) * rate_fed[4]) + ((limit_fed[4] - limit_fed[3]) * rate_fed[3]) + ((limit_fed[3] - limit_fed[2]) * rate_fed[2]) + ((limit_fed[2] - limit_fed[1]) * rate_fed[1]) + (limit_fed[1] * rate_fed[0])
if salary > limit_fed[6]:
  tax_fed = ((salary - limit_fed[6]) * rate_fed[6]) + ((limit_fed[6] - limit_fed[5]) * 9/3/100) + ((limit_fed[5] - limit_fed[4]) * rate_fed[4]) + ((limit_fed[4] - limit_fed[3]) * rate_fed[3]) + ((limit_fed[3] - limit_fed[2]) * rate_fed[2]) + ((limit_fed[2] - limit_fed[1]) * rate_fed[1]) + (limit_fed[1] * rate_fed[0])


st.text("""        
State Income Tax:     ${:,.2f}
Federal Income Tax:   ${:,.2f}
Social Security:      ${:,.2f}
Medicare:             ${:,.2f}

Total Taxes Paid:     ${:,.2f}      
        """.format(tax_state, tax_fed, social_security, medicare, (tax_state+tax_fed+social_security+medicare)))

source = pd.DataFrame({"Taxes": ('Federal','State','Social Security','Medicare'), "value": (tax_fed,tax_state,social_security,medicare)})

c = alt.Chart(source).mark_arc().encode(
    alt.Theta("value:Q").stack(True),
    alt.Color("Taxes:N").legend()
)
pie = c.mark_arc(outerRadius=120)
text = c.mark_text(radius=165, size=15).encode(text="Taxes:N")

if salary > 1:
  st.altair_chart(pie+text, use_container_width=True)