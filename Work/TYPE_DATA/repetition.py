from art import tprint
tprint("STACK", font="Noto Sans")

text = input("Please, enter an example:")
stack = []
check = True

for i in text:
    if i in "([{":
        stack.append(i)
        continue
    if i in ")]}":
        if len(stack) == 0:
            check == False
            break

        meaning = stack.pop()

        if meaning == "(" and i == ")":
            continue
        elif meaning == "[" and i == "]":
            continue
        elif meaning == "{" and i == "}":
            continue

        check == False
        break
    

if check == True and len(stack) == 0:
    print("This test was successful!")
else:
    print("fooo")
