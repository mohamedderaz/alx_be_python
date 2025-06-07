FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} F is {celsius} c")
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celsius} C is {fahrenheit} F")    
temp = int(input("Enter the temperature to convert: "))
type= str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
if type=="C":
    convert_to_fahrenheit(temp)
elif type=="F":
    convert_to_celsius(temp)



    

