try:
	import streamlit as st
	import pandas as pd
	import numpy as np
	import matplotlib.pyplot as plt
	from umap import UMAP
	import seaborn as sns
	from sklearn.decomposition import PCA
	from sklearn.preprocessing import StandardScaler, LabelEncoder
	from sklearn.feature_selection import SelectKBest, f_classif
	from sklearn.neighbors import KNeighborsClassifier
	from sklearn.svm import SVC
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

from lib.functions import load_data, perform_pca, perform_umap, plot_3d, perform_feature_selection, train_and_evaluate

def main():
    st.title("Data Mining and Analysis Application")

    # Load Data
    st.header("1. Load Data")
    uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx', 'xls', 'tsv'])
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        if df is not None:
            st.write(df.head())
            st.write(f"Shape: {df.shape}")

            # 3D Visualizations
            st.header("2. 3D Visualizations")
            X = df.iloc[:, :-1]  # All columns except the last one
            y = df.iloc[:, -1]   # Last column

            pca_result = perform_pca(X)
            umap_result = perform_umap(X)

            st.subheader("PCA 3D Visualization")
            st.plotly_chart(plot_3d(pca_result, y, "PCA 3D Visualization"))

            st.subheader("UMAP 3D Visualization")
            st.plotly_chart(plot_3d(umap_result, y, "UMAP 3D Visualization"))

            # Exploratory Data Analysis
            st.header("3. Exploratory Data Analysis")
            st.subheader("Feature Correlation Heatmap")
            corr = X.corr()
            fig = px.imshow(corr, title="Feature Correlation Heatmap")
            st.plotly_chart(fig)

            st.subheader("Feature Distribution")
            feature = st.selectbox("Select a feature", X.columns)
            fig = px.histogram(df, x=feature, color=y, title=f"Distribution of {feature}")
            st.plotly_chart(fig)

            # Machine Learning Tabs
            st.header("4. Machine Learning")
            tab1, tab2 = st.tabs(["Feature Selection", "Classification"])

            with tab1:
                st.subheader("Feature Selection")
                k = st.slider("Select number of features to keep", 1, len(X.columns), len(X.columns) // 2)
                X_new, selected_features = perform_feature_selection(X, y, k)
                st.write("Selected features:", selected_features)

            with tab2:
                st.subheader("Classification")
                k_neighbors = st.slider("Select k for KNN", 1, 20, 5)
                c_param = st.slider("Select C for SVM", 0.1, 10.0, 1.0)

                knn = KNeighborsClassifier(n_neighbors=k_neighbors)
                svm = SVC(C=c_param, probability=True)

                results = []
                for model, name in [(knn, "KNN"), (svm, "SVM")]:
                    results.append(train_and_evaluate(X, y, model, f"{name} (Original)"))
                    results.append(train_and_evaluate(pd.DataFrame(X_new), y, model, f"{name} (Feature Selected)"))

                results_df = pd.DataFrame(results)
                st.write(results_df)

    # About
    st.header("5. About")
    st.write("""
    This application was developed for data mining and analysis using Streamlit.
    It supports loading tabular data, 3D visualizations, exploratory data analysis,
    feature selection, and classification tasks.

    Development Team:
    - [Your Name]: Project Lead, Application Architecture
    - [Team Member 1]: Data Preprocessing, Visualization
    - [Team Member 2]: Machine Learning Algorithms
    - [Team Member 3]: UI/UX Design, Documentation

    For more information, please visit our GitHub repository: [Your GitHub Repo URL]
    """)

if __name__ == "__main__":
    main()
