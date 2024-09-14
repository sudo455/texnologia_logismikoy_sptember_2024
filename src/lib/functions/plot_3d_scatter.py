try:
    from plotly.express import scatter_3d
except ImportError:
    print("Error in run plot 3d scatter function make sure the librarie plotly is installed.")
    exit()

def plot_3d_scatter(data, labels, title):
    """
    Plot a 3D scatter plot using the first three components of the input data.

    Parameters:
        data (array-like): The input data to be plotted.
        labels (array-like): The corresponding labels for each data point.
        title (str): The title of the plot.

    Returns:
        figure: A Plotly Express figure representing the 3D scatter plot.
    """

    fig = scatter_3d(
        data, x=0, y=1, z=2, color=labels,
        title=title,
        labels={'0': 'Component 1', '1': 'Component 2', '2': 'Component 3'}
    )

    return fig