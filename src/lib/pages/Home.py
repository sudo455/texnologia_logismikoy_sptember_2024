try:
    from streamlit import write
except ImportError:
    print("Error in Feature Selection page make sure the librarie streamlit is installed.")
    exit()
def Home_page():
    """
    Renders the home page of the application.

    This function displays a welcome message and provides instructions on how to navigate through different functionalities using the sidebar.
    """
    write("Welcome to the Data Mining and Analysis Application.")
    write("Use the sidebar to navigate through different functionalities.")
