# Student Attendance Analysis Project

## Overview
This project performs data mining on student attendance datasets to identify patterns and trends. It includes a synthetic data generator to create realistic attendance records and an analysis script to derive insights and visualizations.

## Project Structure
- `data/`: Contains the dataset (`student_attendance.csv`).
- `src/`: Source code for data generation and analysis.
    - `data_generator.py`: Generates synthetic attendance data.
    - `analysis.py`: Performs data cleaning, analysis, and visualization.
- `outputs/`: Generated plots and visualizations.

## Requirements
- Python 
- pandas
- numpy
- matplotlib
- seaborn

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. **Generate Data**:
   If you don't have a dataset, generate one using:
   ```bash
   cd src
   python data_generator.py
   ```
   This will create `data/student_attendance.csv` containing realistic attendance records.

2. **Run Analysis**:
   Perform analysis and generate visualizations:
   ```bash
   cd src
   python analysis.py
   ```
   
## key Insights & Features
- **Data Generation**: Simulates realistic patterns like lower attendance on Fridays or before holidays.
- **Data Cleaning**: Handles missing values and correct data types.
- **Analysis**:
    - Calculates overall attendance rates.
    - Identifies best and worst days for attendance.
    - Tracks individual student performance.
- **Visualization**: Generates bar charts and heatmaps to visualize trends (saved in `outputs/`).

## Sample Outputs
The analysis script generates:
- **Attendance Distribution**: Histogram of Present/Absent/Late statuses.
- **Day-wise Trends**: Bar chart showing attendance percentage by day of week.
- **Heatmap**: Visual representation of student attendance over time.



