#string manipulation
x = "     nobody in the planet is dumb       "
print(x.strip())
#letter uppercase / lowercase
x="nobody in the planet is dumb"
print(x.upper())
x="NOBODY IN THE PLANET IS DUMB"
print(x.lower())
#making sure the list works correctly
x=("nobody in the planet is very dumb")
print(x.split())


#string formating 
name = "Anvay"
age = "10"
print("{} is {} years old".format(name,age))

# another way to learn buy planelearn
print(name + " is " + str(age) + " years old")

#slicing apart a string as if it was a list
a = "apple , bannana , mango , cherry , framboose"
print(a[:])
print(a [0::2])

#random things always work
import random
print(random.randint(1,10))
a = ["sdbhcbsdhjbchjdsb","jdkchjdsbfhjdsbfhjbsdjfh","sdbhsdbwedhebfi"]
print(random.choice(a))


