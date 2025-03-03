import streamlit as st
import pandas as pd
from src.data_handling.data_import import DataImporter
from src.visualization.dashboards import Dashboard

def main():
    st.set_page_config(page_title="Data Analysis Platform", layout="wide")
    
    # Initialize components
    importer = DataImporter()
    dashboard = Dashboard()
    
    # File upload
    st.sidebar.title("Data Import")
    uploaded_file = st.sidebar.file_uploader("Upload your data", 
                                           type=['csv', 'xlsx'])
    
    if uploaded_file is not None:
        # Load data
        try:
            df = importer.read_file(uploaded_file)
            
            # Get numeric columns
            numeric_columns = df.select_dtypes(
                include=['int64', 'float64']
            ).columns.tolist()
            
            # Create tabs
            tab1, tab2 = st.tabs(["Overview", "Analysis"])
            
            with tab1:
                dashboard.create_data_overview(df)
                
            with tab2:
                dashboard.create_analysis_dashboard(df, numeric_columns)
                
        except Exception as e:
            st.error(f"Error loading file: {str(e)}")

if __name__ == "__main__":
    main()