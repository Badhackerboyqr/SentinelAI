
import streamlit as st, pandas as pd
st.title("Alerts")
st.dataframe(pd.DataFrame(columns=["id","severity","type"]))
