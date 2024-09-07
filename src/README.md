# Data Mining and Analysis Application - Source Code

This directory contains the source code for the Data Mining and Analysis Application.

## Directory Structure

```
.
├── lib/
│   ├── functions/
│   │   ├── load_data.py
│   │   ├── plot_3d_scatter.py
│   │   ├── run_classification.py
│   │   ├── run_feature_selection.py
│   │   ├── run_pca.py
│   │   └── run_umap.py
│   └── pages/
│       ├── home.py
│       ├── data_loading.py
│       ├── visualization.py
│       ├── feature_selection.py
│       ├── classification.py
│       └── about.py
├── .dockerignore
├── Dockerfile
├── main.py
├── requirements.txt
└── README.md
```

## Files and Directories

- `lib/functions/`: Contains modular functions for core functionalities.
- `lib/pages/`: Contains individual Streamlit pages for the application.
- `Dockerfile`: Used to build the Docker image for the application.
- `main.py`: The main entry point for the Streamlit application.
- `requirements.txt`: Lists all Python dependencies for the project.

## Running the Application

### Bare Metal

1. Ensure you're in the `src` directory.
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run main.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

### Docker

1. Build the Docker image:

   ```bash
   sudo docker build -t texnologia_logismikoy:latest .
   ```

2. Run the Docker container:

   ```bash
   sudo docker run -d -p 8501:8501 --name texnologia_logismikoy texnologia_logismikoy:latest
   ```

3. Open your browser and navigate to `http://localhost:8501`

## Docker Hub

The application is also available as a pre-built Docker image on Docker Hub. To use it:

```bash
sudo docker run -d -p 8501:8501 --name texnologia_logismikoy UserName/texnologia_logismikoy:latest
```

Then open your browser and navigate to `http://localhost:8501`
