import streamlit as st

st.title("Chai Streamlit App")
st.write("This is a simple Streamlit app that uses the Chai API.")
st.write("You can use this app to interact with the Chai API and get responses from the model.")
st.write("Please enter your message below:")
user_input = st.text_input("Message", "")
if st.button("Send"):
    if user_input:
        # Call the Chai API with the user input
        response = st.session_state.chai_api.send_message(user_input)
        st.write("Response from Chai API:")
        st.write(response)
    else:
        st.write("Please enter a message before sending.")


date = st.date_input("Pick a date")
st.write("You selected:", date)

lang = st.selectbox(
    "Select a language",
    ("Python", "Java", "JavaScript", "C++", "Ruby"),
)
st.write("You selected:", lang)

st.success(f"You selected: {lang}")
st.info("This is a success message.")
st.warning("This is a warning message.")
st.error("This is an error message.")