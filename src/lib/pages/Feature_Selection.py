try:
    from streamlit import header, session_state, warning, write, button, slider
    from lib.functions.run_feature_selection import run_feature_selection
    from pandas import DataFrame
except ImportError:
    print("Error in Feature Selection page make sure all the libraries (pandas, streamlit, lib.functions.run_feature_selection) is installed and in the correct place.")
    exit()

def Feature_Selection_page():
    header("Feature Selection")
    if 'data' in session_state:
        data = session_state['data']
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        k = slider("Select number of features to keep", 1, X.shape[1], X.shape[1]//2)
        if button("Run Feature Selection"):
            X_new, selected_features = run_feature_selection(X, y, k)
            write(f"Selected features: {selected_features}")
            session_state['X_reduced'] = DataFrame(X_new, columns=selected_features)
            session_state['y'] = y
    else:
        warning("Please load data first.")