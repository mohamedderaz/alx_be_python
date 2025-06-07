FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit} F is {celsius} c")
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32
    print(f"{celsius} C is {fahrenheit} F")    

def is_valid_temperature(value):
    try:
        float(value)  # نحاول نحول القيمة إلى رقم عشري
        return True
    except ValueError:
        return False

def is_valid_unit(unit):
    return unit.upper() in ["C", "F"]

temp = int(input("Enter the temperature to convert: "))
type= str(input("Is this temperature in Celsius or Fahrenheit? (C/F):"))
# مدخلات من المستخد

# التحقق من المدخلات
if is_valid_temperature(temp) and is_valid_unit(type):
    temperature = float(temp)
    unit = type.upper()
    if type=="C":
        convert_to_fahrenheit(temp)
    elif type=="F":
        convert_to_celsius(temp)
    else:print("enter a valid temp and unit")
else:
    print("Invalid input. Please enter a valid number and unit (C or F).")

    

