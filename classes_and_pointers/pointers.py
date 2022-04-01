"""pointers
    """

# ? Not using pointers
num1 = 11
num2 = num1

print('Before value is updated:')
print(f'num1 is {num1} and num2 is {num2}')

num1 = 22

print('After value is updated:')
print(f'num1 is {num1} and num2 is {num2}')

# ? using pointers
dic1 = {'value': 11}
dic2 = dic1

print('Before value is updated:')
print(f'dic is {dic1} and dic2 is {dic2}')

dic1['value'] = 22
print('After value is updated:')
print(f'dic1 is {dic1} and dic2 is {dic2}')
