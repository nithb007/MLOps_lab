import os

name = os.getenv("STUDENT_NAME", "Student")

print("="*40)
print("Message: Hello MLOps!")
print(f"Brought to you by: {name}")
print("="*40)