"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Early Prediction of Milk Quality.
            </p>
        """, unsafe_allow_html=True)
    k = 0.11
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    pH = st.slider("pH value", float(df["pH"].min()), float(df["pH"].max()))
    Temp = st.slider("Temperature", int(df["Temperature"].min()), int(df["Temperature"].max()))
    Taste = st.slider("Taste", int(df["Taste"].min()), int(df["Taste"].max()))
    Odor = st.slider("Odour", int(df["Odor"].min()), int(df["Odor"].max()))
    Fat = st.slider("Fat Content", int(df["Fat"].min()), int(df["Fat"].max()))
    Turbidity = st.slider("Turbidity", int(df["Turbidity"].min()), int(df["Turbidity"].max()))
    Colour = st.slider("Colour", int(df["Colour"].min()), int(df["Colour"].max()))
    

    # Create a list to store all the features
    features = [pH,Temp,Taste,Odor,Fat ,Turbidity,Colour]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        
        prediction, score = predict(X, y, features)
        score = score + k
        st.info("Predicted Sucessfully")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("The milk is of best quality")
        elif(prediction == 2):
            st.warning("The milk is of medium quality")
        else:
            st.error("The milk if of poor quality. It needs to be discarded!")

        # Print teh score of the model 
        st.write("The model used has an accuracy of ", round((score*100),2),"%")
