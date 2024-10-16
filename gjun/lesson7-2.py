import random
import pyinputplus as pyip

while True:
    min = int(input("please enter min number:"))
    max = int(input("please enter max number:"))
    count = 0
    target = random.randint(min,max)

    while True:
        count += 1
        keyin = pyip.inputInt(f"guess range {min}~{max}:",min=min,max=max)
        if keyin == target:
            print(f"congraguration,answer is {keyin}")
            print(f"guess {count} time")
            break
        elif keyin > target:
            print("smaller")
            max = keyin - 1
        elif keyin < target:
            print("biggerr")
            min = keyin + 1
        print(f"guess {count} time")
    is_play = pyip.inputYesNo("continue? ")
    if is_play == 'no':
        break
    
print("app is end")