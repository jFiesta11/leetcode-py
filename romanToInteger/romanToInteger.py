
roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

result = 0

for i in range(len(userInput)):
    if(i+1 < len(userInput) and roman[userInput[i]] < roman[userInput[i+1]] ):
        result-=roman[userInput[i]]
    else: 
        result+=roman[userInput[i]]

print(result)