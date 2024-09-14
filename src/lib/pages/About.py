try:
    from streamlit import header, write, subheader
except ImportError:
    print("Error in About page make sure the librarie streamlit is installed.")
    exit()
def About_page():
    """
    Renders the About page.

    This page provides information about the application, its development team,
    and how it works.
    """

    header("About")
    write("This application was developed as part of a data mining and analysis project.")
    write("Team members and their contributions:")
    write("- Angelos Moraitis: Data loading, preprocessing, Feature selection and classification algorithms")
    write("- Theocharis Parisis: Visualization dimensionality reduction, UI design and integration")

    subheader("How it works")
    write("1. Load your dataset (CSV, Excel, or TSV format)")
    write("2. Explore the data through PCA, UMAP, and EDA visualizations")
    write("3. Perform feature selection to reduce the dimensionality of your data")
    write("4. Run classification algorithms (KNN or SVM) on both original and reduced datasets")
    write("5. Compare the performance of the algorithms before and after feature selection")