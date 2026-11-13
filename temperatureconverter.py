
"""
CIT-104 Assignment Chapter 9
Khem Kafley
11/13/2026

This program converts temperatures between Fahrenheit and Celsius and displays the converted temperature.
"""


from breezypythongui import EasyFrame   # Import the stuff from the breezypythongui that we need for this.

class TemperatureConverter(EasyFrame): # For converting temperatures.

    def __init__(self):
        EasyFrame.__init__(self, title="Temperature Converter") # Name of window.

        self.addLabel(text="Fahrenheit", row=0, column=0) # GUI row 1: Labels for Fahrenheit and Celsius.
        self.addLabel(text="Celsius", row=0, column=1)

        self.fahrenheitField = self.addFloatField( # GUI row 2: Entry fields that also have the starting numbers for Fahrenheit and Celsius.
            value=32.0, row=1, column=0
        )
        self.celsiusField = self.addFloatField(
            value=0.0, row=1, column=1
        )

        self.addButton(text=">>>>", row=2, column=0, # GUI row 3: Conversion buttons for Fahrenheit to Celsius and Celsius to Fahrenheit.
                       columnspan=1, command=self.convertToCelsius)

        self.addButton(text="<<<<", row=2, column=1,
                       columnspan=1, command=self.convertToFahrenheit)

    def convertToCelsius(self): # Convert Fahrenheit to Celsius and make it so absolute zero is the minimum.
        fahrenheit = self.fahrenheitField.getNumber()
        fahrenheit = max(fahrenheit, -459.67)
        celsius = (fahrenheit - 32) * 5 / 9
        self.celsiusField.setNumber(celsius)

    def convertToFahrenheit(self): # Convert Celsius to Fahrenheit and make it so absolute zero is the minimum.
        celsius = self.celsiusField.getNumber()
        celsius = max(celsius, -273.15)
        fahrenheit = celsius * 9 / 5 + 32
        self.fahrenheitField.setNumber(fahrenheit)


# Start the program and run the GUI.
TemperatureConverter().mainloop()
