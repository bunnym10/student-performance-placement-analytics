
import pandas as pd

# Load the student dataset
df = pd.read_csv("data/student_placement_data.csv")

# 1. Total number of students
print("TOTAL STUDENTS:", len(df))

# 2. Department-wise student count
print("\nDEPARTMENT-WISE STUDENT COUNT:")
print(df["department"].value_counts())

# 3. Average CGPA
print("\nAVERAGE CGPA:")
print(round(df["cgpa"].mean(), 2))

# 4. Average attendance
print("\nAVERAGE ATTENDANCE:")
print(round(df["attendance"].mean(), 2), "%")

# 5. Placement count
placed_students = (df["placement_status"] == "Placed").sum()
not_placed_students = (df["placement_status"] == "Not Placed").sum()

print("\nPLACEMENT SUMMARY:")
print("Placed:", placed_students)
print("Not Placed:", not_placed_students)

# 6. Placement percentage
placement_percentage = (placed_students / len(df)) * 100

print("\nOVERALL PLACEMENT PERCENTAGE:")
print(round(placement_percentage, 2), "%")

# Department-wise placement analysis

print("\nDEPARTMENT-WISE PLACEMENT ANALYSIS:")

department_placement = df.groupby(
    "department"
)["placement_status"].value_counts().unstack(fill_value=0)

print(department_placement)

# Calculate placement percentage by department

department_placement["placement_percentage"] = (
    department_placement["Placed"] /
    (department_placement["Placed"] +
     department_placement["Not Placed"])
) * 100

print("\nDEPARTMENT-WISE PLACEMENT PERCENTAGE:")

print(
    department_placement[
        ["placement_percentage"]
    ].round(2)
)

import matplotlib.pyplot as plt

# Department-wise placement chart

placement_rates = department_placement[
    "placement_percentage"
]

plt.figure(figsize=(9, 5))

placement_rates.plot(
    kind="bar",
    title="Department-wise Placement Percentage"
)

plt.xlabel("Department")
plt.ylabel("Placement Percentage (%)")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("reports/department_placement.png")

plt.show()

# CGPA comparison between placed and not placed students

print("\nAVERAGE CGPA BY PLACEMENT STATUS:")

cgpa_comparison = df.groupby(
    "placement_status"
)["cgpa"].mean()

print(cgpa_comparison.round(2))

# Create a bar chart

plt.figure(figsize=(8, 5))

cgpa_comparison.plot(
    kind="bar",
    title="Average CGPA by Placement Status"
)

plt.xlabel("Placement Status")
plt.ylabel("Average CGPA")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("reports/cgpa_placement_comparison.png")

plt.show()

# Technical skills vs placement analysis

print("\nTECHNICAL SKILLS VS PLACEMENT:")

skills_analysis = df.groupby(
    "placement_status"
)["technical_skills"].mean()

print(skills_analysis.round(2))

# Create chart

plt.figure(figsize=(8, 5))

skills_analysis.plot(
    kind="bar",
    title="Average Technical Skills by Placement Status"
)

plt.xlabel("Placement Status")
plt.ylabel("Average Technical Skills (1-10)")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("reports/technical_skills_placement.png")

plt.show()

# Aptitude score vs placement analysis

print("\nAPTITUDE SCORE VS PLACEMENT:")

aptitude_analysis = df.groupby(
    "placement_status"
)["aptitude_score"].mean()

print(aptitude_analysis.round(2))

# Create aptitude comparison chart

plt.figure(figsize=(8, 5))

aptitude_analysis.plot(
    kind="bar",
    title="Average Aptitude Score by Placement Status"
)

plt.xlabel("Placement Status")
plt.ylabel("Average Aptitude Score")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig("reports/aptitude_placement.png")

plt.show()

# Internship vs placement analysis

print("\nINTERNSHIP VS PLACEMENT:")

internship_analysis = pd.crosstab(
    df["internship"],
    df["placement_status"]
)

print(internship_analysis)

# Calculate placement percentage

internship_analysis["placement_percentage"] = (
    internship_analysis["Placed"] /
    (internship_analysis["Placed"] +
     internship_analysis["Not Placed"])
) * 100

print("\nPLACEMENT PERCENTAGE BY INTERNSHIP:")

print(internship_analysis["placement_percentage"].round(2))

# Create chart

internship_analysis["placement_percentage"].plot(
    kind="bar",
    title="Placement Percentage by Internship Experience"
)

plt.xlabel("Internship Experience")
plt.ylabel("Placement Percentage (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("reports/internship_placement.png")
plt.show()
# Save analysis summary

summary = pd.DataFrame({
    "Metric": [
        "Total Students",
        "Average CGPA",
        "Average Attendance",
        "Placed Students",
        "Not Placed Students",
        "Overall Placement Percentage"
    ],
    "Value": [
        len(df),
        round(df["cgpa"].mean(), 2),
        round(df["attendance"].mean(), 2),
        placed_students,
        not_placed_students,
        round(placement_percentage, 2)
    ]
})

summary.to_csv("reports/analysis_summary.csv", index=False)

print("\nAnalysis summary saved successfully!")