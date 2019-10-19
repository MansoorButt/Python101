#Object Oriented Programming using python
#Polymorphism,Inheritence,Abstraction,Encapsulation
#Instance cannot be created from Abstract class

class Man():
    def __init__(self,name,fname,qualification): #constructor
        self.name = name
        self.fname = fname
        self.qualification = qualification

        def speak(self , words="hello"):
            print(words)


obj = Man("Mansoor","Ilyas","BSCS")

print(obj.name) #"Mansoor" will be printed


class Car():
    def __init__(self,car_name,color,max_speed):
        self.car_name= car_name
        self.color = color
        self.max_speed = max_speed

    def turn_lightsOn(self , lights="ON"):
        print(lights)


newCar = Car("civic","green",220)

print(newCar.car_name)

newCar.turn_lightsOn()

#Inheritence
class CarMods(Car):
    def startCar(self , start="ON"):
        print(start)

car2 = CarMods("corolla","blue",300)

print(car2.car_name)
car2.startCar()

class Woman():
    def __init__(self,name,fname,gender): #constructor
        self.name = name
        self.fname = fname
        self.gender = gender

class Male(Woman):
    def __init__(self,language):
        self.language = language


        def noise(self , makingNoise="Yes"):
            print(makingNoise)


class Female(Woman):
    def __init__(self,eyeColor):
        self.eyeColor = eyeColor


        def scream(self , screaming="Yes"):
            print(screaming)

newMan = Male("Urdu")

print(newMan.language)


#Encapsulation

#Abstraction
class Human:

    def __init__(self):
        self.name=None
        self.age=None

    @abstractmethod
    def display(self,name,age):
        self.name = name
        self.age=age
