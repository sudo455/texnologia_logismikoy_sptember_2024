try:
    from umap import UMAP
except ImportError:
    print("Error in run Umap function make sure the umap librarie is installed.")
    exit()

def run_umap(data):
    reducer = UMAP(n_jobs=1, n_components=3, random_state=42)
    umap_result = reducer.fit_transform(data)
    return umap_result