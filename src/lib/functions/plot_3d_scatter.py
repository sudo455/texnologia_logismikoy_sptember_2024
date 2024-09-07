try:
    import plotly.express as px
except ImportError:
    print("Error in run plot 3d scatter function make sure the librarie plotly is installed.")
    exit()

def plot_3d_scatter(data, labels, title):
    fig = px.scatter_3d(
        data, x=0, y=1, z=2, color=labels,
        title=title,
        labels={'0': 'Component 1', '1': 'Component 2', '2': 'Component 3'}
    )
    return fig