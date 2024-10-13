from widget2.tools2 import MyClass

while True:
    try:
        name=str(input("please enter your name"))
        height=float(input('please enter your height'))
        weight=float(input('please enter your weight'))
        bmi=weight/(height**2)
        grade = MyClass.get_status_message(bmi)
        print(f"{name}  bmi is {bmi},is {grade}")
    except ValueError:
        print("format error")
        continue
    stuff = input("please enter next data ('q':quit)")

    if stuff == 'q':
        break
print("app is end")