class BMI():
    def __init__(self, name:str, height:float, weight:float):
        self.name = name
        self.height = height
        self.weight = weight

    def getName(self) -> str:
        return self.name

    def getBMI(self) -> float:
        return self.weight / (self.height ** 2)

    def get_status_message(self, bmi: float) -> str:

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
        
    def result(self) -> str:
        bmi = self.getBMI()
        return f"{self.getName()} 's BMI is {bmi}, is {self.get_status_message(bmi)}"

while True:
    try:
        name=str(input("please enter your name"))
        height=float(input('please enter your height'))
        weight=float(input('please enter your weight'))

        Mybmi = BMI(name=name, height=height, weight=weight)
        print(Mybmi.result())

    except ValueError:
        print("format error")
        continue
    stuff = input("please enter next data ('q':quit)")

    if stuff == 'q':
        break
print("app is end")