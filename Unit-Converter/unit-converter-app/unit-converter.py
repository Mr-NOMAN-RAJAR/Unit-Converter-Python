import streamlit as st

st.title("Unit Converter App")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Welcome! Select a category, enter a value, and get the converted result in real-time")

# Category selection
category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])

# Input for value
value = st.number_input("Enter a value", min_value=0.0)

# Units for conversion based on category selection
if category == "Length":
    unit = st.selectbox("Choose conversion unit", ["kilometers to miles", "miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Choose conversion unit", ["kilograms to Gram", "Gram to kilograms"])
elif category == "Time":
    unit = st.selectbox("Choose conversion unit", ["Hours to minutes", "minutes to hours"])

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "kilograms to Gram":
            return value * 1000
        elif unit == "Gram to kilograms":
            return value / 1000
        
    elif category == "Time":
        if unit == "Hours to minutes":
            return value * 60
        elif unit == "minutes to hours":
            return value / 60

# Call conversion function and display result
if value > 0:
    result = convert_units(category, value, unit)
    st.write(f"Converted Value: {result}")
else:
    st.write("Please enter a valid value to convert.")
