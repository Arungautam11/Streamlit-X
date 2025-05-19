import streamlit as st
from datetime import datetime, date

# Set the title of the app
st.title("Age :rainbow[Calculator]")

# Get the current date
current_date = datetime.now().date()
st.write(f":rainbow[Current Year]: {current_date.strftime('%Y')}")

# Set min and max date range for date input
min_date = date(1900, 1, 1)
max_date = current_date

# Get the user's date of birth
dob = st.date_input("Enter your date of birth:", min_value=min_date, max_value=max_date)

# Function to calculate age in years, months, and days
def calculate_age(dob, today):
    years = today.year - dob.year
    months = today.month - dob.month
    days = today.day - dob.day

    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - date(today.year if today.month > 1 else today.year - 1,
                                                         today.month - 1 if today.month > 1 else 12, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

# Calculate and display the age
if dob:
    years, months, days = calculate_age(dob, current_date)

    st.write(f":rainbow[Your age is]: **{years} years, {months} months, and {days} days**.")
    
    st.balloons()
    st.snow()
