try:
    from plotly.express import box, scatter_matrix
except ImportError:
    print("Error in run plot eda make sure the librarie plotly is installed.")
    exit()

def plot_eda(data):
    fig1 = box(data)
    fig2 = scatter_matrix(data)
    return fig1, fig2