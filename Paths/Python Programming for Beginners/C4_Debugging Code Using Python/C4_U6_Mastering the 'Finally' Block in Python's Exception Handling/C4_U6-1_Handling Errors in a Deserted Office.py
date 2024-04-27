try:
    office_chairs = 10
    employees = 0
    chairs_per_person = office_chairs / employees
except ZeroDivisionError:
    print("Office is empty, no division is possible.")
finally:
    print("Please remember to turn off the lights.")