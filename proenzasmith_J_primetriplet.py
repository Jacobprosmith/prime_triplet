"""
Name: Jacob Proenza-Smith
Date: 9/4/2024
Due date: 9/4/2024
About this project: This project's goal was to provide a relatively simple
project that will find the smallest prime triplet above a given input. it 
will give the students a small introduction into python as well as showcase
their ability to deal with time complexity.
assumptions: The user will input a valid number about  +- 1000000000000
All work below was performed solely by Jacob Proenza-Smith
I used a small bit of code in my "isPrime" function from chatGPT. Starting
from 'while i*i' to 'return true' in the same function.
I ran my code with 1000000000000 and the time I got was: 27.18
""

def isPrime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def findSmallestTriplet(num):
    answer = []
    vNum = int(abs(num))
    validNum = max(2, vNum + 1)
    if validNum % 2 == 0:
        validNum += 1
    while True:
        if isPrime(validNum) and isPrime(validNum + 2) and isPrime(validNum + 6):
            answer.extend([validNum, validNum + 2, validNum + 6])
            return answer
        if isPrime(validNum) and isPrime(validNum + 4) and isPrime(validNum + 6):
            answer.extend([validNum, validNum + 4, validNum + 6])
            return answer
        validNum += 2
        

while True:
    negative = False
    num = input("\nEnter a number: ")
    #num = 999999999999
    try:
        validNum = int(num)
    except ValueError:
        continue
    if validNum < 0:
        quick = []
        quick.extend([5,7,11])
        print(quick)
        continue
    print("The Smallest triplet higher than", validNum, "is", findSmallestTriplet(validNum))
    break
    
