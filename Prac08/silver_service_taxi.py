from Prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Car that includes fare costs."""
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def calculate_fare(self):
        return self.flag_fall + super().get_fare()
