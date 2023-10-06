from random import randint

def captcha_challenge():
    x = [randint(0, 9) for i in range(3)]
    
    problema = f"{x[0]} {x[1]} {x[2]}"
    
    return problema, problema