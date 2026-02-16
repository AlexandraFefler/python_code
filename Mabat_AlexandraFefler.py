from enum import IntEnum


class Omes(IntEnum):
    EVENING = 1
    NOON = 2
    MORNING = 3


class MaxSpeeds(IntEnum):
    TAXI = 180
    BUS = 150
    CAR = 160


dis = input("Enter the distance from your destination: ")
if (dis.isdecimal()):
    dis = int(dis)
    if (dis > 0):
        day_time = input("What time of the day it is? ")
        if (day_time == "Morning"):
            day_time = Omes.MORNING
        elif (day_time == "Noon"):
            day_time = int(Omes.NOON)
        elif (day_time == "Evening"):
            day_time = int(Omes.EVENING)
        else:
            print("Error")

        preference = input("Which traveling option do you prefer? ")
        if (preference == "Public"):
            price_per_hour = int(input("What is the price of an hour of traveling? "))
            num_passangers = int(input("How many passengers there are on the bus? "))
            if (num_passangers < 20):
                num_passangers = 20

            speed_bus = (MaxSpeeds.BUS - num_passangers) / day_time
            if (day_time == 1):
                speed_bus = MaxSpeeds.BUS
            time_bus = round(dis / speed_bus, 2)
            price_bus = round(time_bus * price_per_hour)

            speed_taxi = round(MaxSpeeds.TAXI / (day_time + 2), 2)
            time_taxi = round(dis / speed_taxi, 2)
            price_taxi = round(time_taxi * price_per_hour + 50)

            if (price_bus > price_taxi and time_bus > time_taxi):  # choices
                bestOption = "taxi"
                total_time = time_taxi
                total_price = price_taxi
            elif (price_bus < price_taxi and time_bus < time_taxi):
                bestOption = "bus"
                total_time = time_bus
                total_price = price_bus
            else:
                bestOption = "taxi"
                total_time = time_taxi
                total_price = price_taxi
            print("You chose to travel in public transport. \nThe best option is the " + str(
                bestOption) + ". It will take" + str(total_time) + " hours, and it will cost " + str(
                total_price) + " shekels.")

        if (preference == "Private"):
            price_per_hour = int(input("What is the price of an hour of traveling? "))
            speed_car = round(MaxSpeeds.CAR / day_time, 2)
            time_car = round(dis / speed_car, 2)
            price_car = round(time_car * price_per_hour)
            print("You chose to travel in the car. \nIt will take " + str(time_car) + " hours, and it will cost " + str(
                price_car) + " shekels.")
        else:
            print("Error")
    elif (dis == 0):
        print("No need for traveling - you are at your destination.")
    else:
        print("Error")
else:
    print("Error")
