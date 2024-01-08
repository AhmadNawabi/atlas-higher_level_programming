#!/usr/bin/python3

def safe_print_division(a, b):
    result_div = None
    try:
        result_div = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(result_div))
    return result_div
