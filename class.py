class Students:
    def __init__(self,name,age,course,grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade

    def display_details(self):
        print("----Student Details----")
        print(f"Name :{self.name}")
        print(f"Age :{self.age}")
        print(f"Course :{self.course}")
        print(f"Grade :{self.grade}")

student1=Students("Ambadi",21,"Computer science","A")
student1.display_details()
