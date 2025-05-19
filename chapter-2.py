import streamlit as st

st.title("Chai Streamlit Maker")

if st.button("Make Chai"):
    st.success("Your chai is being brewed!")

add_masala = st.checkbox("Add masala")
if add_masala:
    st.write("Masala added to your chai!")


tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Almond Milk"])
st.write(f"Selected base: {tea_type}")
flavour = st.selectbox("Select your chai flavour:", ["Ginger", "Cardamom", "Mint"])
st.write(f"Selected flavour: {flavour}")
milk_type = st.selectbox("Select your milk type:", ["Full Cream", "Low Fat", "Soy"])
st.write(f"Selected milk type: {milk_type}")
sweetness = st.slider("Select sweetness level (spoon):", 0, 10, 5)
st.write(f"Sweetness level: {sweetness}")

cups = st.number_input("Number of cups:", min_value=1, max_value=10, value=1)
st.write(f"Number of cups: {cups}")
if st.button("Confirm Order"):
    st.success(f"Your order for {cups} cup(s) of {tea_type} chai with {flavour} flavour and {sweetness} spoons of sweetness is confirmed!")
    st.write("Enjoy your chai!")
