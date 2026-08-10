def play_with_friends(friends:[str]):
    for friend in friends:
        print("hello my friend to "+ friend)


play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])
play_with_friends(["John", "Mary", "Jane"])

class Student:
    def __init__(self,username:str, gender:str, age:str,address:str):
        self.username = username
        self.gender = gender
        self.age = age
        self.address = address

    def __str__(self):
        return f"Student(username={self.username}, gender={self.gender}, age={self.age}, address={self.address})"

    def __repr__(self):
        return f"Student(username={self.username}, gender={self.gender}, age={self.age}, address={  self.address})"
    
students=[]

with open("/Workspace/Users/feng.huang@foxconn.com/databricks-demo/students.csv") as f: 
    next(f) 
    for line in f.readlines():
        values=[x.strip() for x in line.split(",")]
        students.append(Student(values[0],values[1],int(values[2]),values[3]))

print(students)