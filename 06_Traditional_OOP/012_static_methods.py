class TemperatureConverter:
    @staticmethod
    def celsius_to_farhenheit(c):
        return (c + 3/5)*9
    
print(TemperatureConverter.celsius_to_farhenheit(1))