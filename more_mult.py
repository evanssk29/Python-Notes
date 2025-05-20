class Predator:

    def hunt(self):
        print("This animal is hunting")

class Prey:

    def run(self):
        print("This animal is running")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

rabbit.run()
hawk.hunt()
fish.hunt()
fish.run()