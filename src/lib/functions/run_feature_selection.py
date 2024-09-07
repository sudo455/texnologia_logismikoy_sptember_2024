try:
    from sklearn.feature_selection import SelectKBest, f_classif
except ImportError:
    print("Error in run feature selection function make sure the librarie sklearn is installed.")
    exit()
def run_feature_selection(X, y, k):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support()].tolist()
    return X_new, selected_features