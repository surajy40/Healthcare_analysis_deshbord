
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/surajy40/Healthcare_analysis_deshbord
cd healthcare-dashboard

# 🏥 Healthcare Insights Dashboard

An interactive **data analytics dashboard** built using **Streamlit, MySQL, and Plotly** to analyze healthcare data and generate meaningful insights.

---

## 🚀 Features

* 📊 20+ Healthcare Analysis Questions
* 📈 Interactive Visualizations (Plotly)
* 🗄️ MySQL Database Integration
* 📉 Real-time Data Query Execution
* 🎯 User-friendly Dashboard Interface

---

## 📌 Key Insights Covered

### 📍 Patient & Admission Analysis

* Admission trends over time
* Seasonal admission patterns
* Follow-up rates

### 🩺 Diagnosis & Treatment

* Top diagnoses
* Length of stay by diagnosis
* Most common medical tests

### 🛏️ Hospital Operations

* Bed occupancy & distribution
* Doctor workload
* Patient engagement

### 💰 Financial Analysis

* Total revenue
* Insurance vs patient payments
* Revenue by doctor
* Billing trends

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend**: Python
* **Database**: MySQL
* **Visualization**: Plotly, Seaborn, Matplotlib
* **Data Handling**: Pandas, NumPy

---

## 📂 Project Structure

```
📁 healthcare_dashboard/
│
├── healthcare_1.py     # Main Streamlit App
├── README.md           # Project Documentation
└── requirements.txt    # Dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/healthcare-dashboard.git
cd healthcare-dashboard
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Setup MySQL Database

Make sure MySQL is running and create database:

```sql
CREATE DATABASE healthcare_db;
```

Update credentials in the code if needed:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="abc",
    password="abc",
    database="healthcare_db"
)
```

---

### 4️⃣ Run the Streamlit App

```bash
streamlit run healthcare_1.py
```

---

## 📊 Dashboard Preview

* Interactive charts (bar, pie, line, treemap)
* Side-by-side comparisons using columns
* KPI metrics (e.g., Follow-up rate)

---

## 🔥 Example Visualizations

* 📈 Line Chart → Admission trends
* 📊 Bar Chart → Doctor workload
* 🥧 Pie Chart → Insurance vs Patient
* 🌳 Treemap → Revenue contribution

---

## ⚠️ Common Issues & Fixes

### ❌ Charts not showing

✔ Run using:

```bash
streamlit run healthcare_1.py
```

---

### ❌ Duplicate Plotly Chart Error

✔ Add unique key:

```python
st.plotly_chart(fig, key="unique_key")
```

---

### ❌ Database Connection Error

✔ Ensure:

* MySQL is running
* Database exists
* Credentials are correct

---

## 📌 Future Enhancements

* 🌍 Geo-visualization (Map view)
* 🎛️ Filters (Date, Diagnosis, Doctor)
* 📱 Mobile-responsive UI
* ☁️ Cloud deployment (Streamlit Cloud)

---

## 👨‍💻 Author

**Suraj**
📊 Data Analyst | Python Developer

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!

---
