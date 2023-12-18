from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import streamlit as st
import warnings

# TODO: Which terms are the most frequent?
# TODO: Which terms correlate with highest median pay?
# TODO: Which companies pay the most? (top 5)
# TODO: Which roles pay the most (top 3)
# TODO: Which geographic area pays the most? (1, with a runner-up)
# TODO: Highest Max Salary


# filter warnings
warnings.filterwarnings("ignore")


def show_word_cloud(df):
    st.write(df)