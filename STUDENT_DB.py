student_db = {
    "names": ["Kamal", "Vimal", "Anil", "Sita", "Ravi", "Neha", "Raj", "Aarti", "Mohan", "Pooja"],
    "rollno": [102, 105, 110, 115, 120, 125, 130, 135, 140, 145],
    "marks": {
        "m1": [12, 80, 55, 70, 85, 95, 60, 78, 88, 77],
        "m2": [60, 80, 70, 85, 65, 75, 80, 90, 85, 80],
        "m3": [90, 100, 80, 75, 60, 85, 90, 95, 100, 70]
    }
}
cutoff = 150

total_marks = [m1 + (m2 + m3) / 2 for m1, m2, m3 in zip(*student_db["marks"].values())]

# Combine student info and total marks
students = list(zip(student_db["names"], student_db["rollno"], total_marks))

# Separate passing and failing students
passing_students = [student for student in students if student[2] > cutoff]
failing_students = [student for student in students if student[2] <= cutoff]

# Sort passing students by total marks
passing_students.sort(key=lambda x: x[2], reverse=True)

# Print ranked passing students
print("Ranked Students (Total Marks Greater than Cutoff):")
for i, (name, rollno, marks) in enumerate(passing_students, start=1):
    print(f"Rank {i}: {name} (Roll Number: {rollno}) - Total Marks: {marks:.2f}")

# Print failing students
print("\nStudents Not Passing the Cutoff:")
for name, _, _ in failing_students:
    print(f"  {name}")
