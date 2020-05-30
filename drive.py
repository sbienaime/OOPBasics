import cars


mycar = cars.Cars(4,'blue','Honda','Civic')

print("mycar is an instance aka  an object  of the Cars class defined in cars.py.  \n \n " )
print("I can access the attributes and methods/functions of this object using dot notation as seen below. \n \n  ")


print("My car is a " + mycar.color+ " "+mycar.make+" "+mycar.model )

mycar.move()
mycar.accelerate()
mycar.Break()



print("Once again, a class is a definition of a type of a object, you can have many instances or versions of a class which have different attributes ( these are versions or instances are objects of that class.\n \n ")

print("Below is another instance/object of this same class.\n \n ")

ans = 'N'
while (ans !="y" ) :
    ans = input("Are you ready to see an other instance of the same class, type the letter (y) when youre ready  ")

#this is another instance or object of the Cars class
myOtherCar = cars.Cars(5,'green','Toyota','camry')


print(' \n ')
print(' \n ')
print(' \n ')



print("My other car ( another object of the same class)  is a " + myOtherCar.color+ " "+myOtherCar.make+" "+myOtherCar.model )


print(' \n ')

myOtherCar.move()
myOtherCar.accelerate()
myOtherCar.Break()

print("This other object has a different color and make  and model etc but it could have had the same attribues of the previous object but they would have still been two different objects, "
      "just like if you had two cars with the same make model color etc in real life")
