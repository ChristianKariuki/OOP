import StudentClass as sc

student = sc.Student()

print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"DOB: {student.dob.strftime('%Y-%m-%d')}")
print(f"Classification: {student.classification}")
print(f"Age: {student.get_age()} years")
print(f"Registration Dates: {student.get_registration_dates()}")
