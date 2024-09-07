
import streamlit as st
from lib.pages.Home import Home_page
from lib.pages.Load_Data import load_data_page
from lib.pages.Visualization import visualization_page
from lib.pages.Feature_Selection import Feature_Selection_page
from lib.pages.Classification import classification
from lib.pages.About import About_page

def main():
    
    st.title("Data Mining and Analysis Application")


    # Sidebar for navigation
    page = st.sidebar.selectbox("Choose a page", ["Home", "Data Loder", "Visualization", "Feature Selection", "Classification", "About"], )

    if page == "Home":
        Home_page()

    elif page == "Data Loder":
        load_data_page()

    elif page == "Visualization":
        visualization_page()

    elif page == "Feature Selection":
        Feature_Selection_page()

    elif page == "Classification":
        classification()

    elif page == "About":
        About_page()

if __name__ == "__main__":
    main()
