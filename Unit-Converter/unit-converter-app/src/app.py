import streamlit as st
from utils.conversions import convert_units

st.title("Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a Category, Enter a Value, and Get the Converted Result in Real Time")

category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])
value = st.number_input("Enter the value to convert", min_value=0.0)

if category == "Length":
    unit = st.selectbox("Select the conversion", ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select the conversion", ["kilograms to pounds", "pounds to kilograms"])
else:  # Time
    unit = st.selectbox("Select the conversion", ["hours to minutes", "minutes to hours"])

if st.button("Convert"):
    result = convert_units(category.lower(), value, unit)
    st.write(f"The converted value is: {result}")