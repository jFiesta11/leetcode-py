strings = ["flower", "flow", "floght"]

result =""

for i in range(len(strings[0])):

    currentChar = strings[0][i]
    if all(i < len(x) and x[i] == currentChar for x in strings):
        result+=currentChar
    else:
        break

print(result)

