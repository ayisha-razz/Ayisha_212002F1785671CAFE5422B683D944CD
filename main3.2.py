class Student:
   def __init__(self, name, roll_number, cgpa):
       self.name=name
       self.roll_number=roll_number
       self.cgpa=cgpa
def sort_students(student_list):
    return sorted(student_list, key=lambda x: x.cgpa, reverse=True)

# Test the function
if __name__ == "__main__":
     # Example usage
     students=[Student("Ishu","003",3.8),Student("Priya","004",3.6),Student("Varsha","005",3.5),Student("Keerthy","006",3.7)]

   
     sorted_student = sort_students(students)


     # Print sorted students
     for student in sorted_student:
      print(f"\nName:{student.name}\nRoll Number :{student.roll_number}\nCGPA :{student.cgpa}")