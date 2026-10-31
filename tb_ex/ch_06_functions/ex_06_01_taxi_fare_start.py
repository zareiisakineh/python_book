# file: ex_06_01_taxi_fare_start.py
import sys

# TODO: Write a function taxi_fare(distance_km: float) -> float
#       that calculates the total taxi fare.
#       Formula: base fare $4.00 + $0.25 per 140 meters
#       Add a docstring explaining what the function does.


    # TODO Part 1: Read distance in km from the user and display the fare
    #              Example: "Fare for 5.0 km: $13.93"
def taxi_fare(avstand_km: float) -> float:
        """ that calculates the total taxi fare."""
        avstand_meter = avstand_km * 1000
        pris = 4 + (avstand_meter / 140) * 0.25
        return pris
    
if __name__ == "__main__":
        if len(sys.argv) > 1:
            avstand_km = float(sys.argv[1])
        else:
            avstand_km = float(input("Gi antall km: "))
    
        fare = taxi_fare(avstand_km)
        
        print(f"Fare for {avstand_km} km: ${fare:.2f}")


    # TODO Part 2: If a command-line argument is provided, use it instead
    #              of prompting the user.
    #              Hint: check len(sys.argv) > 1
    #                    use float(sys.argv[1]) to get the distance
    #              Usage: python ex_06_01_taxi_fare.py 5.0
