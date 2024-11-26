total_days = int(input("Enter the total number of working days: "))
absent_days = int(input("Enter the total number of days absent: "))

attended_days = total_days - absent_days
attendance_percentage = (attended_days / total_days) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")
if attendance_percentage < 75:
    print("The student is not eligible to sit in the exam.")
else:
    print("The student is eligible to sit in the exam.")
