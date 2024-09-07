try:
    import streamlit as st
    import pandas as pd
    import numpy as np
    from umap import UMAP
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.feature_selection import SelectKBest, f_classif
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
    import plotly.express as px
except ImportError:
    print("""Error: Some or one library is not installed.
Make sure you are in an activated python virtual environment using the command:
    python -m venv venv
to activate a python virtual environment look at: 
https://python.land/virtual-environments/virtualenv#Python_venv_activation

Lastly install the libraries using pip inside the virtual python environment:
    pip install -r requirements.txt""")
    exit()

def load_data(file):
    if file.name.endswith('.csv'):
        df = pd.read_csv(file)
    elif file.name.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(file)
    elif file.name.endswith('.tsv'):
        df = pd.read_csv(file, sep='\t')
    else:
        st.error("Unsupported file format. Please upload a CSV, Excel, or TSV file.")
        return None
    return df

def perform_pca(df):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.iloc[:, :-1])
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(scaled_data)
    return pca_result

def perform_umap(df):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df.iloc[:, :-1])
    umap = UMAP(n_components=3, random_state=42)
    umap_result = umap.fit_transform(scaled_data)
    return umap_result

def plot_3d(data, labels, title):
    fig = px.scatter_3d(x=data[:, 0], y=data[:, 1], z=data[:, 2], color=labels,
                        title=title)
    return fig

def perform_feature_selection(X, y, k):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_new = selector.fit_transform(X, y)
    selected_features = X.columns[selector.get_support()].tolist()
    return X_new, selected_features

def train_and_evaluate(X, y, model, model_name):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Encode labels if they're not already numeric
    le = LabelEncoder()
    y_train = le.fit_transform(y_train)
    y_test = le.transform(y_test)
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    # Handle ROC AUC for binary and multi-class cases
    if len(np.unique(y)) == 2:
        roc_auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    else:
        try:
            roc_auc = roc_auc_score(y_test, model.predict_proba(X_test), multi_class='ovr', average='weighted')
        except ValueError:
            roc_auc = np.nan  # Set to NaN if ROC AUC can't be computed
    
    return {
        'Model': model_name,
        'Accuracy': accuracy,
        'F1-Score': f1,
        'ROC-AUC': roc_auc
    }