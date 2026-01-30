import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_student_data(num_students=50, num_days=30):
    """
    Generates synthetic student attendance data.
    """
    students = [f"S{str(i).zfill(3)}" for i in range(1, num_students + 1)]
    start_date = datetime(2023, 9, 1)
    dates = [(start_date + timedelta(days=d)) for d in range(num_days)]
    # Filter out weekends
    dates = [d for d in dates if d.weekday() < 5]
    
    data = []

    for date in dates:
        day_of_week = date.strftime("%A")
        
        # Simulate different attendance probabilities based on day of week
        # Monday and Friday might have slightly lower attendance
        base_prob = 0.9
        if day_of_week in ["Monday", "Friday"]:
            base_prob = 0.8
            
        for student_id in students:
            # Individual student patterns
            # Some students are more likely to be absent
            student_prob = base_prob
            if int(student_id[1:]) % 10 == 0: # Every 10th student is a skipper
                student_prob -= 0.2
            
            status = np.random.choice(["Present", "Absent", "Late"], p=[student_prob, (1-student_prob)*0.7, (1-student_prob)*0.3])
            
            # Class type logic
            # Lab sessions might have strictly higher attendance? or maybe split
            class_type = "Lecture"
            if day_of_week in ["Tuesday", "Thursday"]:
                 # Randomly assign some to Lab
                 if random.random() < 0.3:
                     class_type = "Lab"
            
            data.append({
                "Student_ID": student_id,
                "Date": date.strftime("%Y-%m-%d"),
                "Day_of_Week": day_of_week,
                "Class_Type": class_type,
                "Status": status
            })
            
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("Generating student attendance data...")
    df = generate_student_data()
    output_path = "../data/student_attendance.csv"
    
    # Ensure data directory exists (handled by run_command in agent workflow, but good for robustness)
    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
    print(df.head())
    print("\nDataset Info:")
    print(df.info())
