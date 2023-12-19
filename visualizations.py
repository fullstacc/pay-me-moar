from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import streamlit as st
import warnings
from utilities.load_variables import init_stopwords

# TODO: Which terms are the most frequent?
# TODO: Which terms correlate with highest median pay?
# TODO: Which companies pay the most? (top 5)
# TODO: Which roles pay the most (top 3)
# TODO: Which geographic area pays the most? (1, with a runner-up)
# TODO: Highest Max Salary
# TODO: Wordcloud: Improve the approach and implement N-Grams or Phrase Detection
"""
Use Bi-gram or N-gram Models: N-grams are continuous sequences of n items from a given sample of text. 
Using 2-grams (bi-grams) or 3-grams (tri-grams) can help you identify common two-word or three-word
phrases that appear in your text.
"""


# filter warnings
warnings.filterwarnings("ignore")


def show_word_cloud(df):
    stopwords = init_stopwords()

    st.write("There are {} observations and {} features in this dataset. \n".format(df.shape[0],df.shape[1]))

    st.write("There are {} types of locations in this dataset such as {}... \n".format(len(df.location.unique()),
                                                                           ", ".join(df.location.unique()[0:5])))

    st.write("There are {} companies with positions in this dataset, such as {}. \n".format(len(df.company.unique()),
                                                                                      ", ".join(df.company.unique()[0:5])))
    st.write(df)


    st.header("Groups and Features")
    # Groupby by company
    st.write('company summary metrics')
    company = df.groupby("company")

    st.write('highest median_pay by company')
    # company.mean().sort_values(by="company",ascending=False).head()

    # Summary statistic of all companies
    st.write(company.describe().head())
    

    # Groupby location
    st.write('location summary metrics')
    location = df.groupby("location")

    st.write('highest median_pay by location')
    # location.mean().sort_values(by="median_pay",ascending=False).head()

    # Summary statistic of all locations
    st.write(location.describe().head())


    # Create the figure and axes
    fig1, ax = plt.subplots(figsize=(15, 10))
    location.size().sort_values(ascending=False).plot.bar(ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=50)
    ax.set_xlabel("Location")
    ax.set_ylabel("Number of Positions Listed")

    # Display the plot in Streamlit
    st.pyplot(fig1)

    # Display the highest paying job per company
    st.write('highest paying job per company')
    fig2, ax = plt.subplots(figsize=(15, 10))
    company.max().sort_values(by="max_pay", ascending=False)["max_pay"].plot.bar(ax=ax)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=50)
    ax.set_xlabel("Company")
    ax.set_ylabel("Highest Max Pay")
    st.pyplot(fig2)

    # WORD CLOUD
    st.write('word cloud below')
    # Start with one description:
    text = df.description[0]

    # Create and generate a word cloud image:
    # wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)

    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

    # Display the generated image:
    # the matplotlib way:


    # Display the generated image:
    fig3, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(fig3)

    # data combination
    all_descriptions = " ".join(desc for desc in df.description)
    st.write("There are {} words in the combination of all review.".format(len(all_descriptions)))

