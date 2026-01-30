import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set plotting style
sns.set(style="whitegrid")

def load_data(filepath):
    """
    Loads the attendance dataset.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found at {filepath}")
        return None
    return pd.read_csv(filepath)

def preprocess_data(df):
    """
    Performs basic preprocessing.
    """
    # Convert Date to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Check for missing values
    print("Missing Values:\n", df.isnull().sum())
    
    return df

def analyze_attendance(df):
    """
    Performs data mining and analysis on the dataset.
    """
    print("\n--- Analysis Report ---")
    
    # 1. Overall Attendance Rate
    total_records = len(df)
    present_count = df[df['Status'] == 'Present'].shape[0]
    attendance_rate = (present_count / total_records) * 100
    print(f"Overall Attendance Rate: {attendance_rate:.2f}%")
    
    # 2. Attendance by Status Distribution
    status_counts = df['Status'].value_counts()
    print("\nAttendance Status Distribution:\n", status_counts)
    
    # 3. Attendance by Day of Week
    day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    # Filter only for 'Present' to see which days have best attendance
    present_df = df[df['Status'] == 'Present']
    day_counts = df['Day_of_Week'].value_counts()
    day_present_counts = present_df['Day_of_Week'].value_counts()
    
    # Calculate percentage present per day
    day_analysis = pd.DataFrame({'Total': day_counts, 'Present': day_present_counts})
    day_analysis['Attendance_Rate'] = (day_analysis['Present'] / day_analysis['Total']) * 100
    day_analysis = day_analysis.reindex(day_order)
    print("\nDay-wise Attendance Rate:\n", day_analysis)
    
    return day_analysis

def visualize_results(df, day_analysis, output_dir="../outputs"):
    """
    Generates and saves visualizations.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Plot 1: Attendance Status Distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df, x='Status', palette='viridis')
    plt.title('Distribution of Attendance Status')
    plt.savefig(f"{output_dir}/status_distribution.png")
    plt.close()
    
    # Plot 2: Day-wise Attendance Rate
    plt.figure(figsize=(10, 6))
    sns.barplot(x=day_analysis.index, y=day_analysis['Attendance_Rate'], palette='magma')
    plt.title('Attendance Rate by Day of Week')
    plt.ylabel('Attendance Rate (%)')
    plt.ylim(0, 100)
    plt.savefig(f"{output_dir}/day_wise_attendance.png")
    plt.close()
    
    # Plot 3: Heatmap of Attendance (Student vs Day) - Sample of 20 students
    sample_students = df['Student_ID'].unique()[:20]
    subset = df[df['Student_ID'].isin(sample_students)]
    
    # Pivot for heatmap: 1 for Present, 0 for Absent/Late (Simplified for viz)
    subset['numeric_status'] = subset['Status'].apply(lambda x: 1 if x == 'Present' else 0)
    pivot_table = subset.pivot_table(index='Student_ID', columns='Date', values='numeric_status', fill_value=0)
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap="coolwarm", cbar_kws={'label': 'Present (1) / Absent/Late (0)'})
    plt.title('Attendance Heatmap (First 20 Students)')
    plt.savefig(f"{output_dir}/attendance_heatmap.png")
    plt.close()
    
    print(f"\nVisualizations saved to {output_dir}")

if __name__ == "__main__":
    data_path = "../data/student_attendance.csv"
    print(f"Loading data from {data_path}...")
    
    df = load_data(data_path)
    
    if df is not None:
        df = preprocess_data(df)
        day_analysis = analyze_attendance(df)
        visualize_results(df, day_analysis)
