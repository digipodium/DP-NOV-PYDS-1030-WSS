class Dog:
    # init is used to initialize the object
    def __init__(self, breed, age, weight):
        self.breed = breed
        self.age = age
        self.weight = weight
        print("Dog object created")


panther = Dog(breed="German Shepherd", age=11, weight=30)
tiger = Dog(breed='Pug', age= 3, weight= 15)
blacky = Dog(breed='Labrador', age= 5, weight= 25)

print(panther.breed)
print(tiger.breed)
print(blacky.breed)
