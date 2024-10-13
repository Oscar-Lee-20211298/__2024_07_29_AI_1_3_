class MyClass:
    @classmethod
    def get_status_message(cls,bmi: float) -> str:
        '''
        caculate bmi

        '''
        if bmi<18.5:
            return "too thin"
        elif bmi<24:
            return "normal"
        elif bmi<27:
            return "heavy"
        elif bmi<30:
            return "simple heavy"
        elif bmi<35:
            return "normal heavy"
        else:
            return "seriously heavy"


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