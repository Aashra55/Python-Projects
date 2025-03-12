import streamlit as st
import pandas as pd 
import os 
from io import BytesIO
from sklearn.ensemble import IsolationForest  # (AI-Powered Anomaly Detection)
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")  
genai.configure(api_key=api_key)

st.set_page_config(page_title="💿 Data Refiner",layout="wide") 
st.title("💿 Data Refiner")
st.write("Transform your files between Excel and CSV formats with built-in data cleaning and visualization!")

uploaded_files = st.file_uploader("Upload your files (CSV or EXCEL)", type=["csv","xlsx"],accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()

        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Unsupported file format: {file_ext}")
            continue
        
        #Display file information
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size/1024} KB")

        #Display sample data
        st.write("Preview the head of data frame:")
        st.write(df.head())
        
        #Options for Data Cleaning
        st.subheader("🧹 Data Cleaning Options")
        if st.checkbox(f"Clean data from {file.name}"):
            col1,col2 = st.columns(2)

            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df = df.drop_duplicates()
                    st.success("Duplicates removed successfully!")
            
            with col2:
                if st.button(f"Fill Missing Values from {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values filled successfully!")

        #  AI-Powered Anomaly Detection
        if st.checkbox("🚀 Detect Anomalies in Numeric Data"):
            model = IsolationForest(contamination=0.05)
            df['Anomaly'] = model.fit_predict(df.select_dtypes(include=["number"]))
            st.write("**Anomaly Detection Applied**: -1 = Anomaly, 1 = Normal")
            st.write(df.head())

        # 🧠 AI-Powered Data Insights (Using Google Gemini AI)
        if st.button("🧠 Get AI-Powered Data Summary"):
            try:
                if df.empty:
                    st.warning("Dataset is empty! Upload a valid file.")
                else:
                    model = genai.GenerativeModel("gemini-pro")
                    
                    # Ensure numerical data for summary
                    numeric_df = df.select_dtypes(include=["number"])
                    if numeric_df.empty:
                        st.warning("No numeric columns found in the dataset. AI analysis may not be useful.")
                    else:
                        summary = numeric_df.describe().to_string()
                        prompt = f"Summarize the key insights about this dataset: {summary}"
                        
                        response = model.generate_content(prompt)
                        
                        if hasattr(response, "text"):
                            st.write("**AI Insights:**")
                            st.write(response.text)
                        else:
                            st.error("AI response did not return text. Check the API settings.")
            except Exception as e:
                st.error(f"Error with AI analysis: {e}")
                            

        # Choose specific columns to keep or convert
        st.subheader("🔍 Column Selection and Conversion")
        columns = st.multiselect(f"Select columns to keep or convert from {file.name}",df.columns,default=df.columns)
        df = df[columns]

        # Data Visualization
        st.subheader("📊 Data Visualization")
        if st.checkbox(f"Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include=["number"]).iloc[:,:2])

        # Convert the file CSV -> Excel
        st.subheader("🔁 Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:",("CSV","Excel"), key=file.name)
        if st.button(f"Convert {file.name} to {conversion_type}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer,index=False)
                file_name = file.name.replace(file_ext,".csv")
                mime_type = "text/csv"

            elif conversion_type == "Excel":
                df.to_excel(buffer,index=False)
                file_name = file.name.replace(file_ext,".xlsx")
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)

            # Download Button
            st.download_button(label=f"Download {file.name} as {conversion_type} file",
            data=buffer,file_name=file_name,mime=mime_type)

            st.success("🎉 All operations completed successfully!")
                    
