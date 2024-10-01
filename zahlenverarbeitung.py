
'''
2.	Implementiere die Methode def isPrimeNumber(number)). Sie ermittelt,ob es
sich bei der übergebenen Zahl um eine Primzahl handelt. Primzahlen heißen Zahlen,
 die größer als 1, nur durch 1 und durch sich selbst ohne Rest teilbar sind.
  Handelt es sich um eine Primzahl, gibt die Methode `True`, andernfalls `False` zurück.
'''
def is_prime_number(number):  # number 21
    number_to_check=2
    upper_limit=number-1      # 4
    while number_to_check<=upper_limit:   # 2<=4 --> True
        if number%number_to_check==0:     # 5%2==0 --> False
            return False
        number_to_check+=1
    return True


# 41

def is_prime_number_more_efficient(number):  # number 4
    number_to_check=2
    upper_limit=number-1      # 3
    while number_to_check<=upper_limit//2 + 1:   # 2<=2 --> True
        if number%number_to_check==0:
            return False
        number_to_check+=1
    return True


def getPrimeNumbers(start, end):
    response=""
    while start <= end:
        if is_prime_number(start):
            response = response + " " + str(start)
        start=start+1
    return response

print(getPrimeNumbers(2, 15))

