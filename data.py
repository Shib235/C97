import streamlit as st
import numpy as np
import pandas as pd

def app(carsdf):
	st.header('View data')
	with st.beta_expander('View dataset'):
		st.table(carsdf)
	st.subheader('Column description')
	if st.checkbox('Show summary'):
		st.table(carsdf.describe())


	beta_col1,beta_col2,beta_col3 = st.beta_columns(3)
	with beta_col1:
		if st.checkbox('Show column names'):
			st.table(carsdf.columns)
	with beta_col2:
		if st.checkbox('Show column datatypes'):
			st.table(carsdf.dtypes)
	with beta_col3:
		if st.checkbox('View column data'):
			cols = st.selectbox('Select column',(carsdf.columns))
			st.table(carsdf[cols])		