## Functional Prompt
    # Implement a function that will flatten and sort an array of integers in ascending order, and which 
    # adheres to a functional programming paradigm.
    # Remember, when writing in a functional style:
    # Keep variables immutable
    # Write only pure functions
    # Remember, functions may be higher order
import time

def my_flatten_func(ar_1,ar_2):
    new_list = []
    for item in ar_1:
        new_list.append(item)
    for item in ar_2:
        new_list.append(item)
    
    new_list.sort()
    return(new_list)

# def my_flatten_func_bad(ar_1,ar_2):
#     for item in ar_2:
# #         ar_1.append(item)
    
#     ar_1.sort()
#     return(ar_1)

# def add_time(v):
#     v['t'] = 10 + v['t']
#     return v


x=[1,3,4,5]
y=[6,8,20]

z=my_flatten_func(x,y)
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

z=my_flatten_func(x,y)
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')
print(f'--------')

# Example of pure function 
# k = {'t': 5}
# p = add_time(k)
# print(f'k = {k}')
# print(f'p = {p}')

# p = add_time(k)
# print(f'k = {k}')
# print(f'p = {p}')


a=[2,6,10,30]
b=[4,3,7,40]
r=my_flatten_func(a,b)
print(a)
print(b)
print(r)



    # Once a functional solution to this problem has been implemented, answer the following questions.
    # How does this solution ensure data immutability?
        # When printing x, y, and z mutliple times, the values do not change and are immutable.
    # Is this solution a pure function? Why or why not?
        # When printing x, y, and z mutliple times, the values do not change and is a pure function. When run multiple times
        # given the same input, the return values do not change and is a pure function.  There are no side effects.
    # Is this solution a higher order function? Why or why not?
        # It is not a higher order function because it doesn't take in a function as a parameter and it doesent return a function as a result.
    # Would it have been easier to solve this problem using a different programming style?
        # Probably would have been the same using a different programming style.
    # Why in particular is functional programming a helpful paradigm when solving this problem?
        # I can't think of any reasons.



## Object Oriented Prompt
    # Watto needs a new system for organizing his inventory of podracers. Help him do this by implementing an Object Oriented solution according to the following criteria.

    # First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes.
    # Define a repair() method that will update the condition of the podracer to "repaired".
    # Define a new class, AnakinsPod that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
    # Define another class that inherits Podracer and call this one SebulbasPod. This class should have a special method called flame_jet that will update the condition of another podracer to "trashed".

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(x):
        x.condition = 'Repaired'

class AnakinsPod(Podracer):
    def __init__(self,max_speed,condition,price):
        super().__init__(max_speed,condition,price)

    def boost(self):
        self.max_speed = self.max_speed*2

class SebulbasPod(Podracer):
    def __init__(max_speed,condition,price):
        super().__init__(max_speed,condition,price)

    def flame_jet(self,other):
        other.condition = 'Trashed'
    
    
    
    
    # Once an Object Oriented solution has been implemented, answer the following questions:
    # How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    # Encapsulation
        # We are bundling information inside of a class.
    # Abstraction
        # We are hiding unnecessary information inside of class
    # Inheritance
        # With classes you resuse code
    # Polymorphism
        # this solution demonstrates polymorphism with the subclass of AnakinsPod and SebulbasPod
    # Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
        # this probably would have been harder with functional programming.
    # How in particular did Object Oriented Programming assist in the solving of this problem?
        # It helped by allow us to resue some code, and package the code better.


## Reflection

    # Take some time now to think about the lessons we've just covered. Prompting questions have been 
    # provided, but reflections do not need to be limited to only their answers.
    # Is one of these coding paradigms "better" than the other? Why or why not?
        # It seems to depend on what code one is trying to write.
    # Given the opportunity to work predominantly using either of these coding paradigms, which seems more 
    # appealing? Why?
        # OOP seems very useful in certain situations like when trying to code around well defined objects
    # Now being more familiar with these coding paradigms, what tasks/features/pieces of logic would be best 
    # handled using functional programming? Object Oriented Programming?
        # More simple functions work well with functional programming and programs with multiple objects would do better
        # with object oriented programming.
    # Personally, which of these styles takes more work to understand? What should be done in order to 
    # deepen understanding related to this paradigm?
        # It's harder for me to define functional programming but object oriented programming makes a lot of sense.