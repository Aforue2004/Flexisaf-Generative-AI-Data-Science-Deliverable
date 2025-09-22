import streamlit as st
import pandas as pd
import joblib as jb

model = jb.load('Fraud_detection_model.pkl')

st.title("Fraud Detection app")

st.markdown("Please enter the details of the transaction and use the predict button to get the prediction")
st.divider()

transaction_type = st.selectbox("Transaction Type", ["CASH_IN", "CASH_OUT", "DEBIT", "PAYMENT", "TRANSFER"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
old_balance = st.number_input("Old Balance", min_value=0.0, value=10000.0)
new_balance = st.number_input("New Balance", min_value=0.0, value=10000.0)
old_balanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
new_balanceDest = st.number_input("New Balance Destination", min_value=0.0, value=0.0)




if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [old_balance],
        'newbalanceOrig': [new_balance],
       'oldbalanceDest': [old_balanceDest],
        'newbalanceDest': [new_balanceDest]
    })
    predication = model.predict(input_data[0])
    st.subheader(f"predication:{bool(predication)}")
    if predication == 1:
        st.error("This Transaction is most likely a fraud")
    else:
        st.success("This Transaction is looking safe")

