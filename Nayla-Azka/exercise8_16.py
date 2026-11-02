# Exercise 8-16: Imports
import carModule
car = carModule.makeCar('subaru', 'outback')
print(car)



from carModule import makecar

car = makeCar('subaru', 'outback')
print(car)



from carModule import makeCar as mc

car = mc('subaru', 'outback')
print(car)



import carModule as cm

car = cm.makeCar('subaru', 'outcack')
print(car)



from carModule import *

car = makeCar('subaru', 'outback')
print(car)