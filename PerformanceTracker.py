class Student:
    students={}
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        
        Student.students[self.name]=self.scores
    def calculateAverage(self):
        if len(self.scores) == 0:
            return 0  # Default to 0 if no scores are provided
        return sum(self.scores) / len(self.scores)
    def isPassing(self):
        return self.calculateAverage()>=50
    
class PerformanceTracker:
    def __init__(self):
        # self.students=[]
        self.students={}
    def addStudent(self, name,grades):
        if name not in self.students:
            self.students[name] = Student(name, grades)
    def getStudent(self,name):
        return self.students.get(name, None)
    def getPassingStudents(self):
        return [student for student in self.students.values() if student.isPassing()]
    def getFailingStudents(self):
        return [student for student in self.students.values() if not student.isPassing()]
    def calculate_class_average(self):
        if not self.students:
            return 0.0
        total_score = sum(student.calculateAverage() for student in self.students.values())
        return total_score/len(self.students)
    
studentName=''
tracker=PerformanceTracker()
while True:
    studentName = input("Enter student name, if want to stop enter 'stop': ").strip()
    if studentName.lower() == "stop":
        break
    elif not studentName:
        print("Name cannot be empty. Please try again.")
        continue
    
    try:
        scores = []
        subjects = ["Mathematics", "English", "Science"]
        for subject in subjects:
            while True:
                try:
                    score = int(input(f"Enter score for {subject}: "))
                    if 0 <= score <= 100:  
                        scores.append(score)
                        break
                    else:
                        print("Score must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numeric score.")
            
        tracker.addStudent(studentName,scores)
        student = tracker.getStudent(studentName)
        print(f"Student {studentName} added successfully.")
        print(f"Average Score: {student.calculateAverage():.1f}")
        if student.isPassing():
            print("\n Student is Passed")
        else:
            print("\n Student is Failed")
    except ValueError:
        print("Invalid input. Please enter a valid number for the score.")
            
print("Student Performance:")
failing_students = tracker.getFailingStudents()
if failing_students:
    print("\nFailing Students:")
    for student in failing_students:
        print(f"{student.name} - Average Score: {student.calculateAverage():.1f}")
else:
    print("No failing students.")
passing_students = tracker.getPassingStudents()
if passing_students:
    print("\nPassing Students:")
    for student in passing_students:
        print(f"{student.name} - Average Score: {student.calculateAverage():.1f}")
else:
    print("No passing students.")

class_average = tracker.calculate_class_average()
print(f"Class Average Score: {class_average:.1f}")
            
            
            
        