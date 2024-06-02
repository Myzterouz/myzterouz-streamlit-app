import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

hide_header="""
<style>
header {
    z-index:-1 !important
    } 
.block-container {
    padding-top:.1rem !important;
    padding-bottom:.5rem !important
    } 
</style>
"""
st.markdown(hide_header, unsafe_allow_html=True)

selected = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
# Sample user data
user_data = {
    'User ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Email': ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'david@example.com', 'eve@example.com'],
    'Age': [25, 30, 35, 40, 28],
    'Join Date': ['2022-01-15', '2021-12-22', '2023-03-10', '2020-05-18', '2021-11-23']
}

# Convert to DataFrame
df = pd.DataFrame(user_data)

# App title
st.title('User Dashboard')

if selected == "Home":
# Display user table
 st.subheader('User Information')
 st.write(df)

if selected == "Upload":
# Age distribution
 st.subheader('Age Distribution')
 age_histogram = np.histogram(df['Age'], bins=np.arange(20, 50, 5))
 st.bar_chart(pd.DataFrame({'count': age_histogram[0]}, index=age_histogram[1][:-1]))

if selected == "Tasks":
# User selection
 st.subheader('Select a User')
 user_id = st.selectbox('Select User ID', df['User ID'])

 selected_user = df[df['User ID'] == user_id].iloc[0]

 st.write(f"**Name:** {selected_user['Name']}")
 st.write(f"**Email:** {selected_user['Email']}")
 st.write(f"**Age:** {selected_user['Age']}")
 st.write(f"**Join Date:** {selected_user['Join Date']}")

if selected == "Settings":
# Display statistics
 st.subheader('Statistics')
 average_age = df['Age'].mean()
 st.write(f"**Average Age:** {average_age:.2f}")

 most_recent_join_date = df['Join Date'].max()
 st.write(f"**Most Recent Join Date:** {most_recent_join_date}")
hide__header="""
<style>
header {z-index:-1 !important}
.block-container {padding:1rem !important}
</style>
"""
