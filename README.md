Student Performance Predictor

A machine learning web app built with Streamlit that predicts a student's final exam grade (G3) based on academic and behavioral features such as past grades, study time, absences, and more.

---

## Project Overview

This project uses the `student-mat.csv` dataset to train a **Random Forest Regressor** and deploy it using **Streamlit**. The goal is to help estimate student outcomes through quick, data-driven predictions.

---

##  Tech Stack

- Python 
- Scikit-learn 
- pandas 
- joblib 
- Streamlit 

---
Dataset Source

This project uses the **Student Performance Data Set** from the UCI Machine Learning Repository:

🔗 [https://archive.ics.uci.edu/ml/datasets/student+performance](https://archive.ics.uci.edu/ml/datasets/student+performance)

The dataset includes demographic, social, and academic features for predicting student outcomes.

## 🚀 How to Run Locally

## 🌐 Live Demo

[Click here to use the app](https://student-performance-app-hhqq3v4hspei4ygflarh8t.streamlit.app)

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://student-performance-app-hhqq3v4hspei4ygflarh8t.streamlit.app)

  
```bash
git clone https://github.com/Prasannanandeti/student-performance-app.git
cd student-performance-app
pip install -r requirements.txt
streamlit run app.py

