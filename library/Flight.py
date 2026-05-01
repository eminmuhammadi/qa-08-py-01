class Flight():
    def __init__ (self, flight_namber, destination, departure_time):
        self.flight_namber = flight_namber
        self.destination = destination
        self.departure_time = departure_time
        self.__is_delay= False
   

    def is_flight_delayed(self):
        return self.__is_delay