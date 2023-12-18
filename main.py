import os
import streamlit as st
import pandas as pd
from utilities.supabase_connection import init_supabase
from visualizations import show_word_cloud

# TODO: Take-aways (TL;DR) - How do I increase my salary if this is my goal?
# README: Document approach 


# Initialize Supabase and get access token
supabase = init_supabase()

# Define table name
table_name = "jobs"

# Try fetching data and creating DataFrame
try:
  # Fetch data from Supabase
  response = supabase.table(table_name).select("*").execute()
  
  # Get data and create DataFrame
  data = response.data
  df = pd.DataFrame(data)


  # ---------------------------
  st.header('PAY ME MOAR.')
  st.subheader('An interactive analysis of the most high-paying tech jobs')

  
  # Success message
  # st.success(f"Fetched {len(df)} jobs from {table_name} table.")
  
  # Use the DataFrame for further analysis or visualization in your Streamlit app
  df

  st.header('Word Cloud')
  st.write(f"These are the most frequent terms used across {len(df)} jobs.")
  show_word_cloud(df)

  st.header('Map')



except Exception as e:
  st.error(f"Error fetching and processing data: {e}")

# Handle any other top-level exceptions
except Exception as e:
  st.exception(e)

