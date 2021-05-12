# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
'''
Task 1

A Person class

Make a class called Person. Make the __init__() method take firstname, lastname, and age as parameters and add them as attributes. Make another method called talk() which makes prints a greeting from the person containing, for example like this: “Hello, my name is Carl Johnson and I’m 26 years old”.
'''
class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname =firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print(f'hi, my name is {self.firstname} {self.lastname} and I’m {self.age} years old' )
user=Person(input('What is your firstnme?'),input('What is your lastnme?'),input('What is your age?'))
user.talk()
'''
Task 2

Doggy age

Create a class Dog with class attribute `age_factor` equals to 7. Make __init__() which takes values for a dog’s age. Then create a method `human_age` which returns the dog’s age in human equivalent.
'''
class Doggy:

    def __init__(self, name, age='7'):
        self.name =name
        try:
            voz = float(age)
            if voz < 0:
                raise Exception
        except:
            voz = float(input('age can be only float and more than zero'))


        self.age=voz
    def human_age(self):
        if self.age<1:
            return self.age*31
        else:
            return (self.age-1)*11+31

dog=Doggy(input('What is name of your dog?'),input('How old is it ?'))
print('if your dog was human. It was ',dog.human_age(),' years old')
'''
Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.
 

The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

```

CHANNELS = ["BBC", "Discovery", "TV1000"]

 class TVController:

pass

 controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.is_exist(4) == "No"

controller.is_exist("BBC") == "Yes"


'''
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.now=0

    def first_channel(self):
        self.now = 0
        return self.channels[0]

    def last_channel(self):
        self.now = -len(self.channels)-1
        return self.channels[-1]

    def turn_channel(self,index):
        try:

            turn= self.channels[index-1]
            self.now=index-1
            return turn
        except:
            print('we cant do it')
            return self.channels[self.now]

    def next_channel(self):
        self.now+=1
        if self.now==len(self.channels):
            self.now=0
        return self.channels[self.now]
    def previous_channel(self):
        self.now-=1
        if self.now<0:
            self.now=len(self.channels)-1
        return self.channels[self.now]
    def current_channel(self):
        return self.channels[self.now]

    def is_exist(self,name):
        for i in self.channels:
            if i==name:
                return "Yes"
        return "No"
controller = TVController(CHANNELS)
print(controller.first_channel() == "BBC",

controller.last_channel() == "TV1000",

controller.turn_channel(1) == "BBC",

controller.next_channel() == "Discovery",

controller.previous_channel() == "BBC",

controller.current_channel() == "BBC",

controller.is_exist(4) == "No",

controller.is_exist("BBC") == "Yes")