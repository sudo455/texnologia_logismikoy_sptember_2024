try:
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
except ImportError:
    print("Error in run pca function make sure the sklearn librarie is installed.")
    exit()

def run_pca(data):
    """
    Run PCA dimensionality reduction on the input data.

    Parameters:
        data (array-like): The input data to be reduced.

    Returns:
        array-like: The reduced data in 3D space.
    """
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    # Set n_components to the number of columns in the original data
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(scaled_data)

    return pca_result