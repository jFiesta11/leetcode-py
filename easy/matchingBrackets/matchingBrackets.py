s = "]"

valid = False
pair = {")": "(", "]": "[", "}": "{"}
stack = []
for i in range(len(s)):
    if s[i] in "([{":
        stack.append(s[i])
    elif s[i] in ")]}":
        if len(stack) == 0 or stack[-1] != pair[s[i]]:
            break
        elif stack[-1] == pair[s[i]]:
            stack.pop()

if len(stack) == 0:
    valid = True
else:
    valid = False

print(valid)
