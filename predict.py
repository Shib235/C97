import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_log_error,mean_squared_error,confusion_matrix,classification_report

def prediction(carsdf , carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick):
	x = carsdf.iloc[:,:-1]
	y = carsdf['price']
	xtrain,xtest,ytrain,ytest = train_test_split(x,y,train_size=0.67,random_state=42)

	lr = LinearRegression()
	lr.fit(xtrain,ytrain)
	score=lr.score(xtrain,ytrain)

	price = lr.predict([[carwidth, enginesize, horsepower, drivewheel_fwd, car_company_buick]])
	price = price[0]
	ytestp = lr.predict(xtest)

	r2score = r2_score(ytest,ytestp)
	mae = mean_absolute_error(ytest,ytestp)
	msle = mean_squared_log_error(ytest,ytestp)
	mse = np.sqrt(mean_squared_error(ytest,ytestp))

	return price,score,r2score,mae,msle,mse



def app(carsdf): 
    st.markdown("<p style='color:red;font-size:30px'>This app uses <b>Linear regression</b> to predict the price of a car based on your inputs.", unsafe_allow_html = True) 
    st.subheader("Select Values:")
    car_wid = st.slider("Car Width", float(carsdf["carwidth"].min()), float(carsdf["carwidth"].max()))     
    eng_siz = st.slider("Engine Size", int(carsdf["enginesize"].min()), int(carsdf["enginesize"].max()))
    hor_pow = st.slider("Horse Power", int(carsdf["horsepower"].min()), int(carsdf["horsepower"].max()))    
    drw_fwd = st.radio("Is it a forward drive wheel car?", ("Yes", "No"))
    if drw_fwd == 'No':
        drw_fwd = 0
    else:
        drw_fwd = 1
    com_bui = st.radio("Is the car manufactured by Buick?", ("Yes", "No"))
    if com_bui == 'No':
        com_bui = 0
    else:
        com_bui = 1
    
    # When 'Predict' button is clicked, the 'prediction()' function must be called 
    # and the value returned by it must be stored in a variable, say 'price'. 
    # Print the value of 'price' and 'score' variable using the 'st.success()' and 'st.info()' functions respectively.
    if st.button("Predict"):
        st.subheader("Prediction results:")
        price, score, car_r2, car_mae, car_msle, car_rmse = prediction(carsdf, car_wid, eng_siz, hor_pow, drw_fwd, com_bui)
        st.success("The predicted price of the car: ${:,}".format(int(price)))
        st.info("Accuracy score of this model is: {:2.2%}".format(score))
        st.info(f"R-squared score of this model is: {car_r2:.3f}")  
        st.info(f"Mean absolute error of this model is: {car_mae:.3f}")  
        st.info(f"Mean squared log error of this model is: {car_msle:.3f}")  
        st.info(f"Root mean squared error of this model is: {car_rmse:.3f}")



