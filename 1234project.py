import random

num = int(input("enter goal number:\n"))
if num >= 0:
    nums = [1, 2, 3, 4]
if num < 0:
    nums = [-1, -2, -3, -4]

operators = ["*", "/", "+", "-", "**"]

all_equations = []

while True:
    fin = ""
    for x in range(len(nums)):
        c = random.choice(nums)
        c1 = random.choice(operators)
        if x == 3:
            fin += f"{c}"
        elif x != 3:
            fin += f"{c} {c1} "
        nums.remove(c)

    try:
        fin1 = eval(fin)
    except:
        continue
    print(f"Tried: {fin} = {fin1}")
    all_equations.append(fin)
    

    nums = [1, 2, 3, 4]
    operators = ["*", "/", "+", "-"]

    if fin1 == num:
        print(f"CORRECT ANSWER: {fin} = {num}")
        break
    
