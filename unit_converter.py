import streamlit as st
st.title("Unit Converter App")
st.markdown("###Converts Lenght, Weight And Time")
st.write("Welcome! Select a category, Enter a value and get the converted result")

category = st.selectbox("Select a category", ["Length", "Weight", "Time"])                         

def convert_units(category, value, unit):
 if category == "Length":
  if unit == "kilometres to miles":
    return value * 0.621371
  elif unit == "miles to kilometres":
    return value * 0.621371
 elif category == "Weight":
  if unit == "kilograms to pounds":
    return value * 2.20462
  elif unit == "pounds to kilograms":
    return value * 2.20462
 elif category == "Time":
  if unit == "seconds to minutes":
    return value / 60
  elif unit == "minutes to seconds":
    return value * 60
  elif unit == "minutes to hours":
    return value / 60
  elif unit == "hours to minutes":
    return value * 60
  elif  unit == "hours to days":
    return value / 24
  elif unit == "days to hours":
    return value * 24

if category == "Length":
  unit = st.selectbox("Select a unit", ["kilometres to miles", "miles to kilometres"])
elif category == "Weight":
  unit = st.selectbox("Select a unit", ["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
  unit = st.selectbox("Select a unit", ["seconds to minutes", "minutes to seconds", "minutes to hours", "hours to minutes", "hours to days", "days to hours"])

value = st.number_input("Enter the value to convert")

if st.button("Convert"):
  result = convert_units(category, value, unit)
  st.write(f"The converted value is {result}")