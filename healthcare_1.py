# importing all the important libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import mysql.connector
import streamlit as st

# Connection to Database

connection =  mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "healthcare_db"
    )

# Run query with function

def run_query(query):
    return pd.read_sql(query, connection)


# Home Page UI

st.set_page_config(page_title= "HEALTHCARE DESHBORD", layout= "wide")
st.title("🏥 Healthcare Insights Dashboard")

# Creating Selectbox

analysis = st.selectbox("Select Question Analysis",[
    "Q1 - Admission over time",
    "Q2 - Top Diagnoses",
    "Q3 - Bed Occupancy",
    "Q4 - Length of Stay",
    "Q5 - Seasonal Admissions",

    "Q6 - Doctor Workload",
    "Q7 - Total Revenue",
    "Q8 - Insurance vs Patient",
    "Q9 - Avg Billing per Diagnosis",
    "Q10 - Most Common Tests",

    "Q11 - Patient Feedback",
    "Q12 - Stay by Diagnosis",
    "Q13 - Monthly Revenue",
    "Q14 - Bed Distribution",
    "Q15 - Follow-up Rate",

    "Q16 - Revenue by Doctor",
    "Q17 - Patients per Test",
    "Q18 - Max Billing Diagnosis",
    "Q19 - Min Billing Diagnosis",
    "Q20 - Avg Insurance Coverage"
])

# Querys for the questions

# Q-1

if analysis == "Q1 - Admission over time":
    query = """
            SELECT DATE_FORMAT(Admit_Date,'%Y-%m') AS Month,
            COUNT(*) AS Count
            FROM healthcare_data GROUP BY Month ORDER BY Month;
            """
    
    df = run_query(query)
    st.dataframe(df)

    # fig, ax = plt.subplots(figsize=(6,3))
    # sns.barplot(data=df, x="Month", y="Count", ax=ax)
    # st.pyplot(fig)SS
    col1, col2 = st.columns(2)
    with col1:
        fig2 = px.bar(df, x="Month", y="Count", height=500)
        st.plotly_chart(fig2)
    with col2:
        fig = px.line(df, x="Month", y='Count', height=500)
        st.plotly_chart(fig)
    
# Q-2
elif analysis == "Q2 - Top Diagnoses":
    query = """
            SELECT Diagnosis,
            COUNT(*) AS Count
            FROM healthcare_data GROUP BY Diagnosis
            ORDER BY Count DESC LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    # fig,ax = plt.subplots(figsize=(9,5))
    # sns.barplot(data=df, x="Count", y="Diagnosis", ax=ax)
    # st.pyplot(fig)
    col1, col2 = st.columns(2)
    with col1:
        fig_1=px.bar(df, x="Count", y="Diagnosis", title="Top Diagnoses", height=500)
        st.plotly_chart(fig_1)
    with col2:
        fig_2 = px.pie(df, names="Diagnosis", values="Count", height=500)
        st.plotly_chart(fig_2)

# Q-3
elif analysis == "Q3 - Bed Occupancy":
    query = """
            SELECT Bed_Occupancy,
            COUNT(*) AS Count
            FROM healthcare_data
            GROUP BY Bed_Occupancy;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(df, names="Bed_Occupancy", values="Count", title="Bed Occupancy", height=500)
        st.plotly_chart(fig)
    with col2:
        fig2 = px.bar(df, x="Count", y="Bed_Occupancy", height=500)
        st.plotly_chart(fig2)

# Q-4
elif analysis == "Q4 - Length of Stay":
    query = """
            SELECT Diagnosis,
            AVG(DATEDIFF(Discharge_Date, Admit_Date)) AS Avg_Stay
            FROM healthcare_data
            GROUP BY Diagnosis LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Diagnosis", y="Avg_Stay", title="Length of Stay", height=500)
        st.plotly_chart(fig)
    with col2:
        fig2 = px.treemap(df,path=["Diagnosis"],values="Avg_Stay",title="Length of Stay Contribution", height=500)
        st.plotly_chart(fig2)

# Q-5
elif analysis == "Q5 - Seasonal Admissions":
    query = """
            SELECT MONTH(Admit_Date) AS Month,
            COUNT(*) AS Count
            FROM healthcare_data
            GROUP BY Month;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Month", y="Count", title="Seasonal Admissions")
        st.plotly_chart(fig)
    with col2:
        fig2 = px.area(df,x="Month",y="Count",title="Seasonal Admissions (Area View)")
        st.plotly_chart(fig2, use_container_width=True, key="season_area")


# Q-6
elif analysis == "Q6 - Doctor Workload":
    query = """
            SELECT Doctor,
            COUNT(*) AS Patients
            FROM healthcare_data
            GROUP BY Doctor
            ORDER BY Patients DESC LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Doctor", y="Patients", title ="Doctor Workload", height=500)
        st.plotly_chart(fig)
    with col2:
        fig2 = px.pie(df, names="Doctor", values="Patients", height=500)
        st.plotly_chart(fig2)

# Q-7
elif analysis == "Q7 - Total Revenue":
    query = """
            SELECT SUM(Billing_Amount) AS Revenue
            FROM healthcare_data
            """
    df = run_query(query)
    st.dataframe(df)

# Q-8
elif analysis == "Q8 - Insurance vs Patient":
    query = """
            SELECT 
            SUM(Health_Insurance_Amount) AS Insurance,
            SUM(Billing_Amount - Health_Insurance_Amount) AS Patient
            FROM healthcare_data;
            """
    df = run_query(query)
    st.dataframe(df)

    pie_df = pd.DataFrame({
        "Category": ["Insurance", "Patient"],
        "Amount": [df["Insurance"][0], df["Patient"][0]]
    })
    col1, col2 = st.columns(2)
    with col1:
        fig = px.pie(pie_df, names="Category", values="Amount", title="Insurance vs Patient")
        st.plotly_chart(fig)
    with col2:
        fig2 = px.treemap(pie_df,path=["Category"],values="Amount",title="Contribution Breakdown", height=500)
        st.plotly_chart(fig2, key="treemap_compare")

# Q-9
elif analysis == "Q9 - Avg Billing per Diagnosis":
    query = """
            SELECT Diagnosis,
            AVG(Billing_Amount) AS Avg_Bill
            FROM healthcare_data
            GROUP BY Diagnosis LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Diagnosis", y="Avg_Bill", title="Avg Billing per Diagnosis", height=500)
        st.plotly_chart(fig)
    with col2:
        fig2 = px.treemap(df, path=["Diagnosis"], values="Avg_Bill", title="Avg Billing per Diagnosis", height=500)
        st.plotly_chart(fig2)

# Q-10
elif analysis == "Q10 - Most Common Tests":
    query = """
            SELECT Test, COUNT(*) AS Count
            FROM healthcare_data
            GROUP BY Test LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Test", y="Count", title="Most Common Tests", height=500)
        st.plotly_chart(fig)
    with col2:
        fig2 = px.pie(df, names="Test", values="Count", title="Most Common Tests", height=500)
        st.plotly_chart(fig2)

# Q-11
elif analysis == "Q11 - Patient Feedback":
    query = """
            SELECT Feedback, COUNT(*) AS Count
            FROM healthcare_data 
            GROUP BY Feedback;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(df, x="Feedback", y="Count", title="Patient Feedback", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Feedback", values="Count", height=500)
        st.plotly_chart(fig2)

# Q-12
elif analysis == "Q12 - Stay by Diagnosis":
    query = """
            SELECT Diagnosis,
            AVG(DATEDIFF(Discharge_Date, Admit_Date)) AS Stay
            FROM healthcare_data 
            GROUP BY Diagnosis LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Stay", y="Diagnosis", title="stay by Diagnosis", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Diagnosis", values="Stay", height=500)
        st.plotly_chart(fig2)

# Q-13
elif analysis == "Q13 - Monthly Revenue":
    query = """
            SELECT DATE_FORMAT(Admit_Date,'%Y-%m') AS Month,
            SUM(Billing_Amount) AS Revenue
            FROM healthcare_data 
            GROUP BY Month;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Month", y="Revenue", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.line(df, x="Month", y="Revenue", height=500)
        st.plotly_chart(fig2)

# Q-14
elif analysis == "Q14 - Bed Distribution":
    query = """
            SELECT Bed_Occupancy,
            COUNT(*) AS Count
            FROM healthcare_data 
            GROUP BY Bed_Occupancy;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Bed_Occupancy", y="Count", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Bed_Occupancy", values="Count", height=500)
        st.plotly_chart(fig2)

# Q-15
elif analysis == "Q15 - Follow-up Rate":
    query = """
            SELECT COUNT(Followup_Date) AS Followups,
            COUNT(*) AS Total
            FROM healthcare_data;
            """
    df = run_query(query)
    st.dataframe(df)

    followups = df["Followups"][0]
    total = df["Total"][0]

    percentage = (followups / total) * 100

    st.metric("Follow-up %", f"{percentage:.2f}%")

# Q-16
elif analysis == "Q16 - Revenue by Doctor":
    query = """
            SELECT Doctor,
            SUM(Billing_Amount) AS Revenue
            FROM healthcare_data 
            GROUP BY Doctor LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Revenue", y="Doctor", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Doctor", values="Revenue", height=500)
        st.plotly_chart(fig2)

# Q-17
elif analysis == "Q17 - Patients per Test":
    query = """
            SELECT Test,
            COUNT(*) AS Patients
            FROM healthcare_data 
            GROUP BY Test LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Patients", y="Test", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Test", values="Patients", height=500)
        st.plotly_chart(fig2)

# Q-18
elif analysis == "Q18 - Max Billing Diagnosis":
    query = """
            SELECT Diagnosis, 
            MAX(Billing_Amount) AS Max_Bill
            FROM healthcare_data 
            GROUP BY Diagnosis LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Max_Bill", y="Diagnosis", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Diagnosis", values="Max_Bill", height=500)
        st.plotly_chart(fig2)

# Q-19
elif analysis == "Q19 - Min Billing Diagnosis":
    query = """
            SELECT Diagnosis,
            MIN(Billing_Amount) AS Min_Bill
            FROM healthcare_data 
            GROUP BY Diagnosis LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x="Min_Bill", y="Diagnosis", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Diagnosis", values="Min_Bill", height=500)
        st.plotly_chart(fig2)

# Q-20
elif analysis == "Q20 - Avg Insurance Coverage":
    query = """
             SELECT Diagnosis, 
             AVG(Health_Insurance_Amount) AS Avg_Insurance
            FROM healthcare_data 
            GROUP BY Diagnosis LIMIT 10;
            """
    df = run_query(query)
    st.dataframe(df)

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(df, x ="Avg_Insurance", y="Diagnosis", height=500)
        st.plotly_chart(fig)

    with col2:
        fig2 = px.pie(df, names="Diagnosis", values="Avg_Insurance", height=500)
        st.plotly_chart(fig2)