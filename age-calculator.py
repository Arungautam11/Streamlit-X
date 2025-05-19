import streamlit as st
from datetime import datetime


# Set the title of the app
st.title("Age :rainbow[Calculator]")
# Get the current date
current_date = datetime.now()
st.write(f":rainbow[Current Year]: {current_date.strftime('%Y')}")
# Get the user's date of birth
dob = st.date_input("Enter your date of birth:")
# Calculate the age
if dob:
    age = current_date.year - dob.year
    st.write(f":rainbow[Your age is]: {age} years")
    st.balloons()