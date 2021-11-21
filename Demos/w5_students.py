''' 
Program that imitates a small Database in the sense that it enables me to:
insert new students and their marks
keep continually adding students
print out student's name and marks
calculate avarage marks of all students 

'''

def generate_students():
  name = input("Enter the name: ")
  grade = float(input("Enter the mark: "))

  return name, grade #return a Tuple

def add_students():
  all_students = []

  while True:
    all_students.append(generate_students())
    
    x = int(input("To stop enter 99: "))

    if x == 99:
      break
  
  return all_students

def print_students(all_students):
  for student in all_students:
    print(f"{student[0]} earned {student[1]} marks on their exam")

def average_mark(lista):
  total = 0
  
  for person in lista:
    total += person[1]
  
  return total/len(lista)

def run():
  listb = add_students()
  print(listb)
  print(f"The average mark is {average_mark(listb)}")

run()