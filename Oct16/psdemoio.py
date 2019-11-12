"""demo for IO"""

try:
    name = input('enter the name:')
    city = input('enter the city:')
    zip_code = int(input('enter the postal code:'))

    print('name:', name)
    print('city:', city)
    print(zip_code)
    print(type(zip_code))
except ValueError as error:
    print(error)

print('the very next statement after the try catch block')
