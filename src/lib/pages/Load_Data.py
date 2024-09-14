try:
    from lib.functions.load_data import load_data
    from streamlit import header, file_uploader, write, dataframe, session_state, cache_data, error
except ImportError:
    print("Error in Load Data page make sure all the libraries (streamlit, lib.functions.load_data) is installed.")
    exit()

# Only cache the data loading part
@cache_data
def load_data_cached(file):
    # Process the file and return the data (reading CSV/Excel/TSV)
    return load_data(file)

def load_data_page():
    header("Data Loading")
    
    # This widget should not be inside a cached function
    uploaded_file = file_uploader("Choose a file", type=["csv", "xlsx", "tsv"])
    
    # Only process the file if one is uploaded
    if uploaded_file is not None:
        # Cache the data loading process, but keep the widget logic outside
        data = load_data_cached(uploaded_file)
        
        if data is not None and data.shape[1] > 2:
            write("Data loaded successfully!")
            dataframe(data)
            
            # Save data in session state for future use across pages
            session_state['data'] = data
        else:
            error("The uploaded file does not have at least 2 collums: 1.features and 2.lables")