class Student():
    def __init__(self,name,age):
        self.name=name
        self.age=age


print(Student('johnw',20).__dict__) #{'name': 'johnw', 'age': 20} 

import json
# t = json.dumps(Student()) TypeError: Object of type 'Student' is not JSON serializable

s = Student('johnw',20)
t = json.dumps(s,default=lambda obj:obj.__dict__) # {"name": "johnw", "age": 20}
print(t)




f = open('test.json','r')
def dict2Obj(d):
    return Student(d["name"],d["age"])
t1 = json.load(f,object_hook=dict2Obj)
print(t1) # <__main__.Student object at 0x0000000003453F98>

