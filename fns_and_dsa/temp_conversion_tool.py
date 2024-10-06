# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Conversion functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    """Main function for user interaction."""
    try:
        # Prompt user for temperature input
        temperature = float(input("Enter the temperature to convert: "))  # Check for numeric input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Normalize input

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)  # Convert Celsius to Fahrenheit
            print(f"{temperature}°C is {converted_temp}°F")  # Display result
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)  # Convert Fahrenheit to Celsius
            print(f"{temperature}°F is {converted_temp}°C")  # Display result
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # Handle invalid unit input
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Handle non-numeric input

if __name__ == "__main__":
    main()  # Execute the main function


