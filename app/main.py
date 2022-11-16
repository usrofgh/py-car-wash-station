class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            if car.clean_mark < self.clean_power:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return income

    def calculate_washing_price(self, car: Car) -> float:
        # I don't know how to do here correctly
        return round(car.comfort_class * ((self.clean_power - car.clean_mark) * (self.average_rating
                                                             / self.distance_from_city_center)), 1)

    def wash_single_car(self, car: object) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rate: int) -> None:
        # and here
        self.average_rating = round((self.count_of_ratings * self.average_rating + rate)
                                    / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1


bmw = Car(comfort_class=3, clean_mark=3, brand="BMW")
audi = Car(comfort_class=4, clean_mark=2, brand="Audi")

wash_station = CarWashStation(
    distance_from_city_center=6,
    clean_power=8,
    average_rating=4.2,
    count_of_ratings=11
)

print(wash_station.average_rating)    # 3.9
print(wash_station.count_of_ratings)  # 11

wash_station.rate_service(1)

print(wash_station.average_rating)    # 4.0
print(wash_station.count_of_ratings)  # 12
