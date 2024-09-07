try:
    from streamlit import error
    from pandas import read_csv, read_excel
except ImportError:
    print("Error in load data function make sure the libraries (pandas and streamlit) is installed.")
    exit()
def load_data(file):
    file_extension = file.name.split('.')[-1]
    if file_extension == 'csv':
        data = read_csv(file)
    elif file_extension == 'xlsx':
        data = read_excel(file)
    elif file_extension == 'tsv':
        data = read_csv(file, sep='\t')
    else:
        error("Unsupported file format. Please upload a CSV, Excel, or TSV file.")
        return None
    return data

