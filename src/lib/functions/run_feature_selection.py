try:
    from sklearn.feature_selection import SelectKBest, f_classif
except ImportError:
    print("Error in run feature selection function make sure the librarie sklearn is installed.")
    exit()
def run_feature_selection(X, y, k):
    """
    Perform feature selection using SelectKBest and score_func=f_classif.

    Parameters:
        X (array-like): The input data to be reduced.
        y (array-like): The target variable.
        k (int): The number of features to select.

    Returns:
        tuple: A tuple containing the selected data and a list of selected feature names.
    """

    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)

    # Get the indices of the selected features
    selected_features = X.columns[selector.get_support()].tolist()

    return X_new, selected_features