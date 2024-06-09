import streamlit as st
from functions import add_img

img_dir = "/home/szeming/personal/crochet/crochet_imgs/"

# Title of the app
st.title("You're a crocheter, Ogin!")

# Add text
st.write("Small: $30")
st.write("Medium: $60")
st.write("Large: $100")

# Add image
add_img("cat1.jpg", "Cute Cat (Medium)")

# Get user input
# name = st.text_input("Enter your name")
# age = st.number_input("Enter your age", min_value=0)

# Display output based on user input
# if st.button("Submit"):
#     st.write(f"Hello, {name}!")
#     st.write(f"You are {age * 12} months old.")

# # Display a progress bar
# import time
# progress_bar = st.progress(0)
# for percent_complete in range(100):
#     time.sleep(0.01)
#     progress_bar.progress(percent_complete + 1)
