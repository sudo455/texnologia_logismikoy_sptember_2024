
try:
    from streamlit import selectbox, session_state, slider, write, table, plotly_chart, header, button, warning
    from plotly.graph_objects import Bar, Figure
    from pandas import DataFrame
    from lib.functions.run_classification import run_classification
except ImportError:
    print("Error in Classification page make sure all the libraries (lib.functions.run_classification, pandas, plotly and streamlit) is installed and in the correct place.")
    exit()

def classification():
    """
    Renders the Classification page.

    This page allows users to choose a classification algorithm, tune its parameters,
    and compare its performance on the original and reduced datasets.
    """

    header("Classification")

    # Check if data has been loaded and feature selection has been run
    if 'data' in session_state and 'X_reduced' in session_state:
        X_original = session_state['data'].iloc[:, :-1]
        X_reduced = session_state['X_reduced']
        y = session_state['y']

        # Choose classification algorithm using a selectbox
        algorithm = selectbox("Choose algorithm", ["KNN", "SVM"])

        if algorithm == "KNN":
            param = slider("Choose k for KNN", 1, 20, 5)
        else:
            param = slider("Choose C for SVM", 0.1, 10.0, 1.0, 0.1)

        # Run classification and display results if button is clicked
        if button("Run Classification"):
            accuracy_original, f1_original, roc_auc_original = run_classification(X_original, y, algorithm, param)
            accuracy_reduced, f1_reduced, roc_auc_reduced = run_classification(X_reduced, y, algorithm, param)

            # Create a table to display classification results
            results = DataFrame({
                'Metric': ['Accuracy', 'F1-Score', 'ROC-AUC'],
                'Original Dataset': [accuracy_original, f1_original, roc_auc_original],
                'Reduced Dataset': [accuracy_reduced, f1_reduced, roc_auc_reduced]
            })

            # Display table and plot a bar chart for performance comparison
            write("Classification Results:")
            table(results)

            fig = Figure(data=[
                Bar(name='Original Dataset', x=results['Metric'], y=results['Original Dataset']),
                Bar(name='Reduced Dataset', x=results['Metric'], y=results['Reduced Dataset'])
            ])
            fig.update_layout(barmode='group', title='Performance Comparison')
            plotly_chart(fig)

    else:
        warning("Please load data and run feature selection first.")
