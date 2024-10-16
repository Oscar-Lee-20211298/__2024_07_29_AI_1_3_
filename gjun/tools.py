def get_status_message(bmi: float) -> str:
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
