def get_status_message( bmi: float) -> str:

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
        
class MyClass():
    @classmethod
    def get_status_message(cls,bmi: float) -> str:
        '''
        #param bmi:這是要傳入bmi傳
        #return:傳出bmi的狀態
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
