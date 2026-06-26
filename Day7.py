#Stack Implementation Using a List
stack = []           # Create an empty stack

stack.append(5)      # Push
stack.append(5)      # Push
print(stack)

stack.pop()          # Pop
print(stack)

stack.append(7)      # Push
stack.append(4)      # Push
print("stack", stack)

print(stack[-1])     # Peek (Top element)

print(len(stack) == 0)   # isEmpty


#Linear Search using Stack (Pop Operation)
stack = [5, 7, 6, 4, 3]
l = len(stack)
T = 7

for i in range(l):
    if stack.pop() == T:
        print("Found")
        break


#Code Name: Class and Object using Constructor
class student:
    def __init__(self,name,age):
         self.name = name 
         self.age = age
    def display(self,name,age):
        print("Name:",self.name)
        print("Age:",age)
student1 = student("pavi",20)
student1.display("mahee",22)



#Python Class and Object using Constructor and Instance Methods
class Dog:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("playing")

    def study(self):
        print("eating")

    def sleep(self):
        print("sleeping")

Dog1 = Dog("lucky")

print(Dog1.name)
Dog1.sleep()
