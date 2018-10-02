from Prac08.unreliable_car import UnreliableCar

reliable_car = UnreliableCar("Reliable Car 1", 100, 60)
unreliable_car = UnreliableCar("Unreliable Car 1", 100, 0)
reliable_car.drive(40)
unreliable_car.drive(40)
print(reliable_car)
print(unreliable_car)
