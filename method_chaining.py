class Car:

    def turn_on(self):
        print("Start")

    def drive(self):
        print("Drive")
        return self

    def brake(self):
        print("Brakes")
        return self

    def turn_off(self):
        print("Turn off")
        return self

car = Car()


<<<<<<< HEAD
(car.drive()
 .turn_off()
 .brake()
 .turn_on())
=======
car.drive().turn_off().brake().turn_on()
>>>>>>> origin/master
