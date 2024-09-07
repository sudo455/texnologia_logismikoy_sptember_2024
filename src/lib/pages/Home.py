try:
    from streamlit import write
except ImportError:
    print("Error in Feature Selection page make sure the librarie streamlit is installed.")
    exit()
def Home_page():
    write("Welcome to the Data Mining and Analysis Application.")
    write("Use the sidebar to navigate through different functionalities.")
