def convert_to_celsius(temp):
    celsius = int(temp - 32) * 5 / 9
    return celsius

fahrenheit = int(input())

print(convert_to_celsius(fahrenheit))