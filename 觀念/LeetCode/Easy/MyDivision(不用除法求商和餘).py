"""
不使用除法計算商數和餘數
"""
import math


def myDivision(Dividend , Divisor):
    return mylog(Dividend, Divisor, 0)


def mylog(Dividend, Divisor, quotient):
    power = math.log(Dividend, Divisor)
    quotient += Divisor ** int(power - 1)
    remainder = Dividend - Divisor * (Divisor ** int(power - 1))
    print(quotient, remainder)
    if remainder >= Divisor:
        return mylog(remainder, Divisor, quotient)
    else:
        return quotient, remainder


print(myDivision(100, 6))
