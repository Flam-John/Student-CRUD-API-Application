import requests

if __name__ == '__main__':
    
    # Initialize variables
    best_student = None
    worst_student = None
    total_grade = 0
    total_students = 0
    
    response = requests.get("http://localhost:8080/api/students")
    data = response.json()
    
    if not data:
        print("No students found.")
    else:
        # Loop through each student to find best and worst grades, and calculate total
        for student in data:
            if 'grade' in student and student['grade'] is not None:  # Ensure grade exists and is not None
                total_grade += student['grade']
                total_students += 1
                
                # Find the student with the best grade
                if best_student is None or student['grade'] > best_student['grade']:
                    best_student = student
                
                # Find the student with the worst grade
                if worst_student is None or student['grade'] < worst_student['grade']:
                    worst_student = student

        # Calculate the average grade
        if total_students > 0:
            average_grade = total_grade / total_students
        else:
            average_grade = 0
    
        # Print results
        if best_student:
            print("Best Grade:")
            print(f"Name: {best_student['firstName']} {best_student['lastName']}")
            print(f"Email: {best_student['email']}")
            print(f"Grade: {best_student['grade']}")
        
        if worst_student:
            print("\nLowest Grade:")
            print(f"Name: {worst_student['firstName']} {worst_student['lastName']}")
            print(f"Email: {worst_student['email']}")
            print(f"Grade: {worst_student['grade']}")
        
        print(f"\nAverage Grade of all students: {average_grade:.2f}")