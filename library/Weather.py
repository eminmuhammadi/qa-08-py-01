class Weather():
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature # public attribute
        self.humidity = humidity
        self.pressure = pressure
        self.__is_rainy_day = False # private attribute

    def display_forecast(self):
        forecast = ""

        if self.__is_rainy_day:
            forecast += "[Yagisli Hava]"

        if self.humidity < 50:
            forecast += "[Nemli Hava]"
        else:
            forecast += "[Normal Hava]"

        if self.pressure < 1000:
            forecast += "[Asagi Tezyiq]"
        else:
            forecast += "[Yuxari Tezyiq]"

        if self.temperature < 30:
            forecast += "[Soyuq Hava]"
        else:
            forecast += "[Isti Hava]"
        
        return forecast
            

    def check_rain(self):
        return self.__is_rainy_day
    
    def update_weather(self, is_rainy_day):
        self.__is_rainy_day = is_rainy_day