try:
    from streamlit import header, session_state, subheader, plotly_chart, warning
    from lib.functions.run_pca import run_pca
    from lib.functions.plot_3d_scatter import plot_3d_scatter
    from lib.functions.plot_eda import plot_eda
    from lib.functions.run_umap import run_umap
except ImportError:
    print("Error in Data Visualization page make sure all the libraries (streamlit, lib.functions.run_pca, lib.functions.plot_3d_scatter, lib.functions.plot_eda, lib.functions.run_umap) is installed and in the correct place.")
    exit()
def visualization_page():
    header("Data Visualization")
    if 'data' in session_state:
        data = session_state['data']
        X = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        subheader("PCA Visualization")
        pca_result = run_pca(X)
        fig_pca = plot_3d_scatter(pca_result, y, "PCA Visualization")
        plotly_chart(fig_pca)

        subheader("UMAP Visualization")
        umap_result = run_umap(X)
        fig_umap = plot_3d_scatter(umap_result, y, "UMAP Visualization")
        plotly_chart(fig_umap)

        subheader("Exploratory Data Analysis")
        fig_box, fig_scatter = plot_eda(X)
        plotly_chart(fig_box)
        plotly_chart(fig_scatter)
    else:
        warning("Please load data first.")