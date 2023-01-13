#mohammad hossein farahani
#class: يکشنبه 7:45

tedad=int(input("enter the number : "))
counter = 0
for i in range(tedad):
    print(i*"*")
    counter+=1
for i in range(tedad):
    print(counter*"*")
    counter-=1
