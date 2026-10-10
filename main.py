import pandas as pd
import numpy as np
from functions import calculate_total, calculate_average, assign_grade, check_pass_fail, analyze_subject_performance

df = pd.read_csv('students.csv')
subjects = ['Python', 'SQL', 'HTML', 'CSS', 'JavaScript']

print("Objective -> Dataset -> Pandas -> NumPy -> Functions -> Loops/Conditions -> Analysis -> Output -> Final Outcome")
print("==============================================")
print(" STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("==============================================")
print()
print("========= STUDENT DATA =========")
print()
print(df.to_string(index=True))
print()
print("========= STUDENT PERFORMANCE =========")
print()

totals = []
averages = []
grades = []
results = []

for index, row in df.iterrows():
    marks = [row[sub] for sub in subjects]
    total = calculate_total(marks)
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    result = check_pass_fail(avg)

    totals.append(total)
    averages.append(round(avg, 2))
    grades.append(grade)
    results.append(result)

df['Total'] = totals
df['Average'] = averages
df['Grade'] = grades
df['Result'] = results

performance_df = df[['Student_ID', 'Name', 'Total', 'Average', 'Grade', 'Result']]
print(performance_df.to_string(index=True))
print()
print("========= FINAL OUTCOME =========")
print(f"Class Average: {np.mean(df['Average']):.2f}")
print(f"Highest Average: {np.max(df['Average'])} ({df.loc[df['Average'].idxmax(), 'Name']})")
print(f"Lowest Average: {np.min(df['Average'])} ({df.loc[df['Average'].idxmin(), 'Name']})")
best_subject, _ = analyze_subject_performance(df, subjects)
print(f"Best Performing Subject: {best_subject}")
top3 = df.sort_values(by='Average', ascending=False).head(3)
print("\nTop 3 Performers:")
print(top3[['Name','Average','Grade']].to_string(index=False))