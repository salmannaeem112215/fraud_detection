import streamlit as st
import pandas as pd
import joblib 

model = joblib.load('fraud_detection_model.pkl')

st.title("Fraud Detection Application")
st.markdown("Please Enter Transaction Details Below:")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT", "CASH_IN"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=1000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=0.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0,value= 1000.0)

if st.button("Predict Fraud"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    if prediction[0] == 1:
        st.error(f"Fraudulent Transaction Detected! (Confidence: {prediction_proba[0][1]:.2f})")
    else:
        st.success(f"Transaction is Legitimate. (Confidence: {prediction_proba[0][0]:.2f})")
