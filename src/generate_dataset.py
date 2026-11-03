
import pandas as pd
import numpy as np

# Generate 500 fictional student records
np.random.seed(42)

number_of_students = 500

student_data = {
    "student_id": range(1001, 1001 + number_of_students),
    "student_name": [f"Student_{i}" for i in range(1, number_of_students + 1)],
    "department": np.random.choice(
        ["CSE", "CSE-DS", "ECE", "IT", "EEE"],
        number_of_students
    ),
    "cgpa": np.round(np.random.uniform(5.0, 10.0, number_of_students), 2),
    "attendance": np.round(np.random.uniform(50, 100, number_of_students), 2),
    "aptitude_score": np.random.randint(30, 101, number_of_students),
    "technical_skills": np.random.randint(1, 11, number_of_students),
    "internship": np.random.choice(
        ["Yes", "No"], number_of_students
    ),
    "placement_status": np.random.choice(
        ["Placed", "Not Placed"],
        number_of_students,
        p=[0.65, 0.35]
    )
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(student_data)

# Save dataset as CSV
df.to_csv("data/student_placement_data.csv", index=False)

print("Student dataset created successfully!")
print("Total students:", len(df))
print("\nFirst 5 student records:")
print(df.head())
