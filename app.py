import streamlit as st
import joblib
import numpy as np

# Load the model and preprocessing objects
bag_clf = joblib.load('bagging_classifier.pkl')
scaler = joblib.load('scaler.pkl')
pca = joblib.load('pca.pkl')
imputer = joblib.load('imputer.pkl')

# Streamlit applicationipi
st.title('Bankruptcy Prediction')

# Collect user input
debt_ratio = st.number_input('Enter Debt Ratio:', format="%.2f")
net_income_to_assets = st.number_input('Enter Net Income to Total Assets:', format="%.2f")
net_worth_to_assets = st.number_input('Enter Net Worth to Total Assets:', format="%.2f")

# Button for prediction
if st.button('Predict'):
    # Transform input data
    input_data = np.array([[debt_ratio, net_income_to_assets, net_worth_to_assets, 0, 0, 0, 0, 0, 0, 0, 0]])
    input_data_scaled = scaler.transform(input_data)
    input_data_pca = pca.transform(input_data_scaled)
    input_data_imputed = imputer.transform(input_data_pca)

    # Make prediction
    prediction = bag_clf.predict(input_data_imputed)
    result = "Bankrupt" if prediction == 1 else "Not Bankrupt"

    # Display the prediction
    st.write(f"Prediction: {result}")

# Run the Streamlit app using: streamlit run app.py
