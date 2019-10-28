def main():
    class Car:
        def __init__(self, work, model, year, speed=0):
            self.__work = work
            self.__model = model
            self.__year = year
            self.__speed = speed


        @property
        def work(self):
            return self.__work

        @work.setter
        def work(self, work):
            self.__work = work


        @property
        def model(self):
            return self.__model

        @model.setter
        def model(self, model):
            self.__model = model

        @property
        def year(self):
            return self.__year

        @year.setter
        def year(self, year):
            self.__year = year

        @property
        def speed(self):
            return self.__speed

        @speed.setter
        def speed(self, speed):
            self.__speed = speed

        def speed_up(self):
            pass
            # speed += 5

        def speed_down(self):
            pass
            # speed -= 5

        def stop(self):
            pass
            # speed = 0

        def speed_display(self):
            pass
            # print(car.speed)

        def turn(self):
            pass
            # speed = -1 * speed

    car_1 = Car('toyota', 'corolla', 2010, 30)
    print(car_1.work)
    print(car_1.model)
    print(car_1.year)
    car_1.speed = 100
    print(car_1.speed)















if __name__ == '__main__':
    main()