class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = {}


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

class CFGStudent(Student):

    def __init__(self, stream, name, age, id):
        self.stream = stream
        super(CFGStudent, self).__init__(name, age, id)

    def add_subject(self, subject_grade: dict):
        self.subjects.update(subject_grade)
        for subj, grade in subject_grade.items():
            print(f"The subject {subj.capitalize()} with the grade of {grade} has been added to the list of subjects.")

    def remove_subject(self, subject_name):
        self.subjects.pop(subject_name)

    def view_subjects(self):
        print(f"Here are the subjects and the grades of {self.name} of the {self.stream} specialization:")
        print("Subjects\tGrades")
        for subj, grade in self.subjects.items():
            print(f"{subj.capitalize():15s} {grade}")

    def average_grade(self):
        average = round(sum(self.subjects.values()) / len(self.subjects))
        print(f"{self.name}'s average marks is {average}.")


student_1 = CFGStudent("Software", "Ruth", 27, 1234)

# check if every function works
student_1.add_subject({"Python": 80})
student_1.add_subject({"Mathematics": 75})
student_1.add_subject({"English": 65})
student_1.add_subject({"Chemistry": 95})
student_1.remove_subject("Chemistry")
student_1.view_subjects()
student_1.average_grade()
