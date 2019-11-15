def divide(dividend, divisor):
    if len(grades) == 0:
        raise ZeroDivisionError("divisor can not be zero")
    return dividend / divisor
grades = []
print("welcome to average grade program")

try:
    average = divide(sum(grades), len(grades))
    print(f"the average grade is {average}")
except ZeroDivisionError as e:
    print(e)
