# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """Main function for user interaction."""
    try:
        temperature = float(input("Enter the temperature to convert: "))  # Get temperature input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Get unit input

        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)  # Convert to Fahrenheit
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)  # Convert to Celsius
            print(f"{temperature}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # Handle invalid unit
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Handle invalid temperature input

if __name__ == "__main__":
    main()  # Run the main function
