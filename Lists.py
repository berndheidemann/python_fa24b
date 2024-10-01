


sample_list=[5.1, 8, "Hallo", 3, 8, 12, 1, 2, 7]


y=[]

for x in range(100):
    y.append(x**2+2*x+26)    #x^2+2x+26

print(y)

print(y[:5])
print(y[17:20])
print(y[17:30:5])


filtered_list=[number for number in y if number%2==0]
print(filtered_list)


filtered_list=[]
for number in y:
    if number%2==0:
        filtered_list.append(number)
print(filtered_list)

import random

random_numbers=[random.randint(0, 9) for i in range(100)]

print(random_numbers)

def evaluate_list(random_list, digit):
    count=0
    # schleife, über alle Werte von random_list
    # wenn die Zahl gleich digit --> count um eins erhöhen
    # count zurückgeben

evaluate_list(random_numbers, 3)












