# The reason you shouldn't use mutable types as default values in Python
def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

addGrade(chrisley, 90)
addGrade(dallas, 100)

print(chrisley)
print(dallas)
# in the above example code, chrisley and dallas both end up with 2 grades each.
# this is obviously unintended but is due to the fact that the empty list only gets
# instantiated the first time and since we're appending it, it keeps growing every time because....

print(id(chrisley['grades']))
print(id(dallas['grades']))
# as the built-in id method shows, they are the same list for two (intended) instances of this list

# if we need to do this for whatever reason it should look like this
def correctCreateStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    "name": name,
    "age": age,
    "grades": grades
  }
  
