FAHRENHEIT_TO_CELSIUS_FACTOR= 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


def main():

    temp_value = int(input("Enter a temperature to convert:"))
    temp_type = input("Is this temperatute in Celsius or Fahrenheit? (C/F): ").strip().upper()


    if temp_type == 'C':
        converted_temp = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {converted_temp:.7f}°F")
    elif temp_type == 'F':
        converted_temp = convert_to_celsius(temp_value)
        print(f"{temp_value}°C is {converted_temp:.7f}°F")
    else:
        print("Invalid temperature type.6")    

if __name__ == "__main__":
    main()