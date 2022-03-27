import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def app(carsdf):
	st.subheader('Visualise Data')
	st.set_option('deprecation.showPyplotGlobalUse', False)
	st.subheader('Scatter Plot')
	featuresl = st.multiselect('Select x axis value',('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
	for i in featuresl:
		st.subheader(f'Scatter plot between {i} and price')
		plt.figure(figsize=(20,5))
		plt.scatter(carsdf[i],carsdf['price'])
		st.pyplot()

	st.subheader('Visualisation Selector')
	plots = st.multiselect('Select plot',('correlation heatmap','histogram','boxplot'))
	if 'correlation heatmap' in plots:
		st.subheader('Correlation Heatmap')
		plt.figure(figsize=(20,5))
		sns.heatmap(carsdf.corr(),annot=True)
		st.pyplot()
	if 'histogram' in plots:
		featuresl2 = st.selectbox('Select x axis value for histogram',('carwidth', 'enginesize', 'horsepower'))
		plt.figure(figsize=(20,5))
		plt.hist(carsdf[featuresl2],bins='sturges',edgecolor='black')
		st.pyplot()
	if 'boxplot' in plots:
		featuresl3 = st.selectbox('Select x axis value for boxplot',('carwidth', 'enginesize', 'horsepower'))
		plt.figure(figsize=(20,5))
		sns.boxplot(carsdf[featuresl3])
		st.pyplot()	