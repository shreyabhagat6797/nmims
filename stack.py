#Stack Queue

'''1)	Given a stack of integers, write a python program that updates the input stack such that all occurrences of the smallest values are at the bottom of the stack, while the order of the other elements remains the same.

For example:
Input stack (top-bottom) :   5 66  5  8  7
Output:  66  8  7  5  5
'''

class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

def change_smallest_value(number_stack):
    l=[]
    while(not number_stack.is_empty()):
        l.append(number_stack.pop())
    mini = min(l)
    counter = l.count(min(l))
    for i in range(counter):
        number_stack.push(mini)
    for element in l[::-1]:
        if element!=mini:
            number_stack.push(element)
    return number_stack 
#Add different values to the stack and test your program
number_stack=Stack(8)
number_stack.push(9)
number_stack.push(3)
number_stack.push(4)
number_stack.push(87)
number_stack.push(6)
print("Initial Stack:")
number_stack.display()
change_smallest_value(number_stack)
print("After the change:")
number_stack.display()

'''2.) Modify the Stack program to include pop(), is_empty() and display() methods to implement the pop operation based on the algorithm discussed and display the element(s) of the stack from top to bottom.
Once done, pop five times from the stack and display the removed elements. Try to pop sixth time and observe the results.
'''
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data

    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False

    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:                         
            data = self.__elements[self.__top]
            self.__top-=1
            return data

    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1

stack1=Stack(5)
#Push all the required element(s).
#stack1.push("6")
stack1.push("1")
stack1.push("2")
stack1.push("3")
stack1.push("4")
stack1.push("5")
print("Stck :")
stack1.display()
print("popped elements:")
#Pop an element
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
#stack1.display()
