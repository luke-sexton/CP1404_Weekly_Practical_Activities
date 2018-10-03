from Prac08.taxi import Taxi
from Prac08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_fare = 0
    menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's Drive \n" + menu)
    user_choice = input(">>> ").upper()
    while user_choice != 'Q':
        if user_choice == 'C':
            print("Taxi's available: ")
            display_taxis(taxis)
            chosen_taxi = int(input("Choose Taxi: "))
            current_taxi = taxis[chosen_taxi]
        elif user_choice == "D":
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            fare = current_taxi.get_fare()
            print("Your {} trip cost you {}".format(current_taxi.name, fare))
            total_fare += fare
        else:
            print("Invalid Option")
        print("Bill to date: ${:.2f}".format(total_fare))
        print(menu)
        user_choice = input(">>> ").upper()
    print("Total trip cost: ${:.2f}".format(total_fare))
    print("Taxis are now: ")
    display_taxis(taxis)

def display_taxis(taxis):

    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))


main()
