"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Milk Quality Detection System")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
           Milk quality detection and grade analysis through machine learning has revolutionized the dairy industry by providing rapid and accurate assessment of milk properties. This technology employs advanced algorithms to analyze key parameters such as fat content, protein levels, bacterial load, and contaminants in milk samples. By training on vast datasets, machine learning models can swiftly classify milk into different quality grades, enabling early detection of potential issues and facilitating prompt corrective actions. These models enhance efficiency by reducing the need for manual testing and human intervention, leading to improved consistency and precision in grading. Additionally, the system's adaptability allows it to evolve with changing production conditions and standards. In essence, the integration of machine learning into milk quality detection streamlines operations, guarantees product quality, and ultimately boosts consumer confidence in dairy products.
        </p>
    """, unsafe_allow_html=True)
