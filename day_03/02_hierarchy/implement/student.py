class Student:
    #pass
    class Person:
        def __init__(self, first_name, last_name):
            self.first_name = first_name
            self.last_name = last_name

        def introduce(self):
            # print(self.first_name, self.last_name)
            print f"I am {self.first_name} {self.last_name}"

    class Student(Person:
        def introduce(self)
        print
        f"I am a student"

    student = Person.student("Jeff", "Castro")
    print(student.introduce())
    #person1 = Person("Richard", "Smith")
    #person1.introduce()
