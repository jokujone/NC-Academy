import time
import random

#AI GENERATED SLOP:

class RenaultTwingo:
    def __init__(self):
        self.speed = 0
        self.engine_on = False
        self.fuel = 50  # liters
        self.max_speed = 160  # km/h

    def start_engine(self):
        if self.fuel > 0:
            self.engine_on = True
            print("Engine started. Vroom vroom!")
        else:
            print("No fuel! Can't start engine.")

    def stop_engine(self):
        self.engine_on = False
        self.speed = 0
        print("Engine stopped.")

    def accelerate(self, amount):
        if not self.engine_on:
            print("Start the engine first!")
            return
        if self.fuel <= 0:
            print("Out of fuel!")
            self.stop_engine()
            return
        self.speed += amount
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        self.fuel -= amount * 0.05
        print(f"Accelerating... Speed: {self.speed:.1f} km/h, Fuel: {self.fuel:.1f} L")

    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0
        print(f"Braking... Speed: {self.speed:.1f} km/h")

    def honk(self):
        print("Beep beep! 🚗")

    def drive(self, duration):
        if not self.engine_on or self.speed == 0:
            print("You need to start the engine and accelerate first!")
            return
        distance = self.speed * (duration / 60)  # duration in minutes
        fuel_used = distance * 0.07
        if fuel_used > self.fuel:
            print("Not enough fuel for this trip!")
            return
        self.fuel -= fuel_used
        print(f"Drove {distance:.1f} km in {duration} minutes. Fuel left: {self.fuel:.1f} L")

def main():
    car = RenaultTwingo()
    print("Welcome to the Renault Twingo Simulator!")
    while True:
        print("\nOptions: start, stop, accelerate, brake, honk, drive, status, quit")
        cmd = input("What do you want to do? ").strip().lower()
        if cmd == "start":
            car.start_engine()
        elif cmd == "stop":
            car.stop_engine()
        elif cmd == "accelerate":
            amt = float(input("How much to accelerate (km/h)? "))
            car.accelerate(amt)
        elif cmd == "brake":
            amt = float(input("How much to brake (km/h)? "))
            car.brake(amt)
        elif cmd == "honk":
            car.honk()
        elif cmd == "drive":
            mins = float(input("How many minutes to drive? "))
            car.drive(mins)
        elif cmd == "status":
            print(f"Speed: {car.speed:.1f} km/h, Fuel: {car.fuel:.1f} L, Engine: {'On' if car.engine_on else 'Off'}")
        elif cmd == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()