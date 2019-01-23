"""
An animal shelter, which holds only dogs and cats, operates on a strictly
"first in, first out" basis. People must adopt either the "oldest" (based on arrival time)
of all animals in the shelter, or they can select whether they would prefer a dog or a cat
(and will receive the oldest animal of that type). They cannot select which specific animal they would like.
Create the data structure to maintain this system and implement operations such as enqueue, dequeueAny,
dequeueDog, and dequeueCat. You may use the built-in LinkedList Data Structure
"""
class Animal:
  def __init__(self, name, kind):
    self.name = name
    self.kind = kind
class Dog(Animal):
  def __init__(self, name):
    Animal.__init__(self, name, 'dog')
class Cat(Animal):
  def __init__(self, name):
    Animal.__init__(self, name, 'cat')

class AnimalShelter:
  def __init__(self):
    self.arr = []

  def enqueue(self,animal):
    self.arr.append(animal)

  def dequeueAny(self):
    if len(self.arr) > 0:
      return self.arr.pop(0)
    return None

  def dequeueCat(self):
    for i in range(len(self.arr)):
      if self.arr[i].kind == 'cat':
        return self.arr.pop(i)
    return None

  def dequeueDog(self):
    for i in range(len(self.arr)):
      if self.arr[i].kind == 'dog':
        return self.arr.pop(i)
    return None

if __name__ == '__main__':
  animalShelter = AnimalShelter()
  animalShelter.enqueue(Dog('buddy'))
  animalShelter.enqueue(Dog('obed'))
  animalShelter.enqueue(Cat('mark'))
  animalShelter.enqueue(Dog('hansel'))

  print(animalShelter.dequeueCat().name)
  print(animalShelter.dequeueDog().name)
  print(animalShelter.dequeueAny().name)

      
  








