import streamlit as st
from lib.pages.Home import Home_page
from lib.pages.Load_Data import load_data_page
from lib.pages.Visualization import visualization_page
from lib.pages.Feature_Selection import Feature_Selection_page
from lib.pages.Classification import classification
from lib.pages.About import About_page

def main():
    """
    The main function of the application, responsible for rendering the Streamlit app.

    It sets up a sidebar with navigation options and renders the corresponding page based on user selection.
    """

    st.title("Data Mining and Analysis Application")

    # Sidebar for navigation
    page = st.sidebar.selectbox(
        "Choose a page", 
        ["Home", "Data Loader", "Visualization", "Feature Selection", "Classification", "About"], 
        key="page"
    )

    if page == "Home":
        Home_page()  # Render the home page

    elif page == "Data Loader":
        load_data_page()  # Render the data loader page

    elif page == "Visualization":
        visualization_page()  # Render the visualization page

    elif page == "Feature Selection":
        Feature_Selection_page()  # Render the feature selection page

    elif page == "Classification":
        classification()  # Render the classification page

    elif page == "About":
        About_page()  # Render the about page

if __name__ == "__main__":
    main()