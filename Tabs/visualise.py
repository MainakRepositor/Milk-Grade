"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import tree
import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Milk Quality Prediction Web app")

    # Create a checkbox to show correlation heatmap
    if st.checkbox("Show the correlation heatmap"):
        st.subheader("Correlation Heatmap")

        fig = plt.figure(figsize = (10, 6))
        ax = sns.heatmap(df.iloc[:, 1:].corr(), annot = True)   # Creating an object of seaborn axis and storing it in 'ax' variable
        bottom, top = ax.get_ylim()                             # Getting the top and bottom margin limits.
        ax.set_ylim(bottom + 0.5, top - 0.5)                    # Increasing the bottom and decreasing the top margins respectively.
        st.pyplot(fig)

    if st.checkbox("Temperature vs Grade"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Temperature",y="Grade",data=df)
        st.pyplot()

    if st.checkbox("Turbidity vs Grade"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Turbidity",y="Grade",data=df)
        st.pyplot()

    if st.checkbox("pH vs Grade"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.lineplot(x="pH",y="Grade",data=df)
        st.pyplot()

    
  
