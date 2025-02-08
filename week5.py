bicycles = ["trek", "allcity","cannondale"]
print (bicycles[2])
bicycles[1] = "lotus"
print (bicycles)
bicycles.insert(1,"raleigh")
print (bicycles)
bicycles.append("marin")
print (bicycles)
print(bicycles.pop())
print(bicycles)
print(len(bicycles))
for bicycleBrand in bicycles:
    print("do you like " + bicycleBrand)
    print("I do too!")

print("finished")

numbers = list(range(1,10))
print(numbers)

for number in numbers:
    square = number**2
    print(square)

ns1 = numbers[3:7]
ns2 = numbers[0:9:3]
print(ns1)
print(ns2)

numbers2 = numbers[0:9]
numbers2.append(10)
print(numbers2)
print(numbers)

# bicycles = ("trek", "raleigh", "cannondale")
# print (bicycles)