while True:
    try:
        name=str(input("please enter your name"))
        height=float(input('please enter your height'))
        weight=float(input('please enter your weight'))
        bmi=weight/(height**2)
        if bmi<18.5:
            grade="too thin"
        elif bmi<24:
            grade="normal"
        elif bmi<27:
            grade="heavy"
        elif bmi<30:
            grade="simple heavy"
        elif bmi<35:
            grade="normal heavy"
        else:
            grade="seriously heavy"
        print(f"{name}  bmi is {bmi},is {grade}")
    except ValueError:
        print("format error")
        continue
    stuff = input("please enter next data ('q':quit)")

    if stuff == 'q':
        break
print("app is end")