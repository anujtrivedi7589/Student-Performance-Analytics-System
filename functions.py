import numpy as np

def calculate_total(marks_list):
    total = 0
    for m in marks_list:
        total += m
    return total

def calculate_average(marks_list):
    return np.mean(marks_list)

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"

def check_pass_fail(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"

def analyze_subject_performance(df, subjects):
    avg_dict = {}
    for sub in subjects:
        avg_dict[sub] = np.mean(df[sub])
    best = max(avg_dict, key=avg_dict.get)
    return best, avg_dict