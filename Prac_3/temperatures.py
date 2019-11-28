"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

print(MENU)

choice = input(">>> ").upper()


def c_to_f(temperature):
    fahrenheit = temperature * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def f_to_c(temperature):
    celsius = 5 / 9 * (temperature - 32)
    print("Result: {:.2f} C".format(celsius))


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        c_to_f(celsius)
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        fahrenheit = float(input("Fahrenheit: "))
        f_to_c(fahrenheit)
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
