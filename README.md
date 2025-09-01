# 🚦 Urban Mobility & Traffic Accident Insights Dashboard

An **interactive web dashboard** for analyzing traffic accident data from the **United Kingdom (2016)**.  
Built with **Python, Pandas, and Plotly/Dash**, this project visualizes **geospatial and temporal patterns** in accidents, helping uncover **hotspots and risk factors**.

---

## 🌐 Live Demo
🔗 *Coming Soon*

---

## ✨ Features
- 🗺️ **Interactive Geospatial Map**  
  Visualize accident hotspots across the UK, color-coded by severity (*Fatal, Serious, Slight*).

- ⏰ **Temporal Analysis**  
  Interactive bar chart of accidents by hour, revealing **daily peak times**.

- 🌦️ **Categorical Insights**  
  Explore accident distributions by **weather conditions** and **road types**.

- 🎨 **Clean & Responsive UI**  
  A modern, **user-friendly interface** designed for intuitive exploration.

---

## 🛠 Technology Stack
- **Backend & Data Processing**: Python, Pandas  
- **Dashboard & Visualization**: Plotly, Dash  
- **Deployment**: Gunicorn, Render  

---

## 📂 Project Structure
```bash
urban-mobility-dashboard/
│
├── .gitignore                     # Specifies files for Git to ignore
├── data/
│   └── processed/
│       └── uk_accidents_2016.csv  # Final, clean dataset
│
├── src/
│   ├── app.py                     # Main Dash application script
│   └── data_preprocessing_clean.py# Script to process raw data
│
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

---

## ⚙️ Setup & Installation

Follow these steps to run the project locally:

### 1. 📥 Download the Raw Data
This project uses the **UK Road Safety: Accidents and Vehicles** dataset.  
Download from [Kaggle](https://www.kaggle.com/datasets).

### 2. 📂 Prepare Project Directory
Create a folder for raw data:
```bash
mkdir -p data/raw/
```
Place the following files inside `data/raw/`:
- `Accident_Information.csv`
- `Vehicle_Information.csv`

### 3. 🧹 Process the Data
Run the preprocessing script to generate the cleaned dataset:
```bash
cd src
python data_preprocessing_clean.py
```

### 4. 🚀 Install Dependencies & Run App
From the project’s root directory:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
python src/app.py
```
The app will be available at: 👉 [http://127.0.0.1:8050/](http://127.0.0.1:8050/)

---

## 📜 License
This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.
