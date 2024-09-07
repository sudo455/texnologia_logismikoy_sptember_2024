try:
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
    from sklearn.svm import SVC
except ImportError:
    print("Error in run classification function make sure the librarie sklearn is installed.")
    exit()

def run_classification(X, y, algorithm, param):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    if algorithm == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=param)
    elif algorithm == 'SVM':
        clf = SVC(C=param, probability=True)
    
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    y_pred_proba = clf.predict_proba(X_test)[:, 1] # type: ignore
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    return accuracy, f1, roc_auc
