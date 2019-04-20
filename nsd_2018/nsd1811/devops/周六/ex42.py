## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal 
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name call name
        self.name = name

## 
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name call name
        self.name = name

## Person is-a object 
class Person(object):
    
    def __init__(self, name):
        ## Person has-a name call name
        self.name = name

        ##  Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name
        super(Employee, self).__init__(name)
        ##  
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog has-a name rover
rover = Dog("rover")

## satam is-a Cat has-a name satan
satan = Cat("Satan")

## mary is-a Person has-a name mary
mary = Person("mary")

## mary has-a pet of satan
mary.pet = satan

##  frank is-a Employee ,salary has-a 120000
frank = Employee("Frank", 120000)

## frank has-a pet of rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()