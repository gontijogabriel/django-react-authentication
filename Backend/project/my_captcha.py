from random import randint

def captcha_challenge():
    x = [randint(0, 9)]
    
    problema = str(x[0])
    resultado = str(sum(x))
    
    return problema, resultado