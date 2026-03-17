result=True
def smart_input():
    thing=input()
    if thing == "end":
        global result
        result = False
        return None
    if thing.isnumeric():
        number = int(thing)
        return number
    else:
        print("输入错误，请输入数字")
        return smart_input()
class Student:
    def __init__(self, name,roll1,roll2,roll3):
        self.name = name
        self.roll1= roll1
        self.roll2 = roll2
        self.roll3 = roll3
    def request_marks(self):
        print(f"{self.name}:",self.roll1,self.roll2,self.roll3)
    def request_average(self):
        print(f"{self.name} average:",self.roll1+self.roll2+self.roll3/3)
    def insert_marks(self):
        result=True
        while result:
            i = 0
            name = input("请输入姓名\n")
            students.append(name)
            print(f"{name}的三次成绩")
            r = ["", "", ""]
            while result and i < 3:
                r[i] = smart_input()
                i = i + 1
            print("循环结束 原因：")
            if result:
                print("录入成功\n", f"{name}的数据：")
                students.append(Student(name, r[0], r[1], r[2]))
                Student.request_marks(students[-1])
            else:
                print("程序结束，error:end")
                break
    def show_all_students(self):
        i=0
        while i<len(students):
            Student.request_marks(students[i])
            i=i+1


students = []
students.append(Student('Alice', 1,2,5))
students.append(Student('Bob', 2,6,8))
students.append(Student('Charlie', 3,19,3))
# print(students[0].roll3)
# Student.request_marks(students[0])
# Student.request_average(students[0])
# Student.insert_marks(students)
# Student.show_all_students(students)

print(students[0].roll1, students[0].roll2, students[0].roll3)




