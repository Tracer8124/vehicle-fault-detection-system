# vehicle-fault-detection-system
Python-based fault detection system using Pandas and NumPy to analyze time-series vehicle sensor data and identify anomalies like high speed, acceleration spikes, and sudden drops.
# 🚗 Vehicle Fault Detection System

## 📌 Overview

This project analyzes vehicle sensor data to detect faults such as:

* High Speed
* Acceleration Spikes
* Sudden Speed Drops

It uses **Pandas and NumPy** to process time-series data and identify continuous fault intervals.

---

## ⚙️ Features

* Data cleaning and preprocessing
* Time-series feature engineering using `.diff()`
* Detection of continuous fault intervals
* Export results to Excel
* Modular and scalable code structure

---

## 📂 Input Data

CSV file with columns:

* `MTS_TIME`
* `Velocity_VDY`
* `Acceleration`

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📊 Output

* `processed_data.csv` → cleaned + feature-added dataset
* `output.xlsx` → detected fault intervals

---

## 🧠 Key Concepts Used

* Pandas DataFrame operations
* NumPy / vectorized computation
* Time-series analysis
* State-based fault detection

---

## 🔥 Future Improvements

* Support multiple files
* Add visualization
* Convert to OOP structure
* Real-time data processing

---

## 👩‍💻 Author

Tanvi Ligade
