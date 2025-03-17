# import streamlit as st

# # Set the title of the app
# st.title("\b Simple Calculator")

# # Create input boxes for the user to enter numbers
# num1 = st.number_input("Enter first number", value=0)
# num2 = st.number_input("Enter second number", value=0)

# # Create a dropdown menu for selecting the operation
# operation = st.selectbox(
#     "Select operation", ["Add", "Subtract", "Multiply", "Divide"]
# )

# # Perform the calculation based on the operation
# if operation == "Add":
#     result = num1 + num2
# elif operation == "Subtract":
#     result = num1 - num2
# elif operation == "Multiply":
#     result = num1 * num2
# elif operation == "Divide":
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Cannot divide by zero"

# # Display the result
# st.write(f"Result: {result}")


import streamlit as st # type: ignore

# Set page title
st.set_page_config(page_title="SIMPLE CALCULATOR", page_icon=":guardsman:", layout="wide")

# Add some custom CSS for styling
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            color: #4CAF50;
            text-align: center;
            font-weight: bold;
        }
        .result {
            font-size: 30px;
            color: #FF5722;
            font-weight: bold;
            text-align: center;
        }
        .input-box {
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 10px;
        }
        .container {
            background-color: #f1f1f1;
            padding: 20px;
            border-radius: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Title of the calculator app
st.markdown('<p class="title">🎯 SIMPLE CALCULATOR</p>', unsafe_allow_html=True)

# Input fields for the numbers
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter First Number", value=0.0, format="%.2f", key="num1", step=0.01)  # Set value as float
with col2:
    num2 = st.number_input("Enter Second Number", value=0.0, format="%.2f", key="num2", step=0.01)  # Set value as float

# Dropdown for operation selection
operation = st.selectbox(
    "Choose an operation",
    ["Add", "Subtract", "Multiply", "Divide"],
    key="operation",
    index=0
)

# Perform the calculation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Cannot divide by zero"

# Display the result with custom formatting and styling
st.markdown(f'<p class="result">Result: {result}</p>', unsafe_allow_html=True)

# Add some more decorative text and instructions
st.markdown("""
    <div class="container">
        <p style="font-size: 16px; color: #333;">This is a simple calculator application built using Streamlit.</p>
        <p style="font-size: 16px; color: #333;">Select an operation, enter numbers, and get the result in real-time!</p>
        <p style="font-size: 14px; color: #666;">Created with 💚 by Streamlit</p>
    </div>
""", unsafe_allow_html=True)
