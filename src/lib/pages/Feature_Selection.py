try:
    from streamlit import header, session_state, warning, write, button, slider
    from lib.functions.run_feature_selection import run_feature_selection
    from pandas import DataFrame
except ImportError:
    print("Error in Feature Selection page make sure all the libraries (pandas, streamlit, lib.functions.run_feature_selection) is installed and in the correct place.")
    exit()

def Feature_Selection_page():
    """
    Renders the Feature Selection page.

    This page allows users to select a subset of features from the loaded data.
    """
    
    header("Feature Selection")

    # Check if data has been loaded
    if 'data' in session_state:
        data = session_state['data']

        # Extract features and labels from the data
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        # Use a slider to select the number of features to keep
        k = slider("Select number of features to keep", 1, X.shape[1], X.shape[1]//2)

        if button("Run Feature Selection"):
            X_new, selected_features = run_feature_selection(X, y, k)
            write(f"Selected features: {selected_features}")

            # Update session state with the reduced data and labels
            session_state['X_reduced'] = DataFrame(X_new, columns=selected_features)
            session_state['y'] = y

    else:
        warning("Please load data first.")