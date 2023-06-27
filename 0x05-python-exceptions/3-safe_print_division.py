#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divd = a / b
    except (TypeError, ZeroDivisionError):
        divd = None
    finally:
        print("Inside result: {}".format(divd))
    return (divd)
