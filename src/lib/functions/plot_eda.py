try:
    from plotly.express import box, scatter_matrix
except ImportError:
    print("Error in run plot eda make sure the librarie plotly is installed.")
    exit()

def plot_eda(data):
    """
    Perform Exploratory Data Analysis (EDA) and display summary statistics.

    Parameters:
        data (array-like): The input data to be analyzed.

    Returns:
        tuple: A tuple containing two plots: a box plot and a scatter matrix.
    """
    fig1 = box(data)
    fig2 = scatter_matrix(data)
    return fig1, fig2