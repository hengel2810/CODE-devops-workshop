# encoding=utf-8


class ValueTooLowException(Exception):
    print(Exception)

class ValueTooHighException(Exception):
    print(Exception)

class Calculator(object):
    def __init__(self, min_value=-1000, max_value=1000):
        self.min_value = min_value
        self.max_value = max_value

    def mul(self, a, b):
        if(a < self.min_value || b < self.min_value) 
            raise ValueTooLowException("Value to low");
        elif (a > self.max_value || b > self.max_value):
            raise ValueTooHighException("Value to high");
        else:
            return a * b

    def div(self, a, b):
        pass
