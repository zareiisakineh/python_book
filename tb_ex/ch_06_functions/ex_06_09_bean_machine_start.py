# file: ex_06_09_bean_machine_start.py
import random

# TODO: Write drop_ball(num_rows: int) -> int
#       Simulates one ball dropping through num_rows pegs.
#       At each row the ball moves left or right with equal chance.
#       Hint: start at slot 0. Which random call gives you either 0 or 1?
#             Add that choice once per row; the final slot is the total.
#       Returns the final slot number (0 to num_rows).
def drop_ball(num_rows: int) -> int:
    slot = 0
    høyre = 1 
    venstre = 0
# alle baller som faller, legges i slot 0 til num_rows. 
    for i in range(num_rows):
# hvis kulen faller til høyre økes slot-index. baller som faller til venstre, legges i samme slot-index
        if random.randint(0, 1) == 1:
            slot += 1
    return slot

print(drop_ball(8))
# TODO: Write run_simulation(num_balls: int, num_rows: int) -> list
#       Drops num_balls balls through num_rows rows.
#       Returns a list of length num_rows + 1 with the count for each slot.
#       Hint: create a list of zeros, then for each ball call drop_ball()
#             and increment the corresponding slot counter.
def run_simulation(num_balls: int, num_rows: int) -> list:
#Lager en liste av nuller:
    counts = [0] * (num_rows + 1)
#  adderer hvert ball-fall til lista ved hjelp av funksjonen drop_ball(num_rows)
    for i in range(num_balls):
        slot = drop_ball(num_rows)
        counts[slot] += 1
# reurnerer lista. Nå har vi en liste av slotene med antall baller i hver index
    return counts

# TODO: Write display_histogram(counts: list)
#       Prints one row per slot showing the count and a bar of asterisks.
#       Example: "Slot 3 (107):  *****..."
#       Hint: use one asterisk per ball for simplicity.
def display_histogram(counts: list):
    for slot_nr, count in enumerate(counts):
# legger stjerner for antall baller i hver slot
        print (f"slot: {slot_nr} {'*' * count}")


# TODO (extension): Write display_histogram_vertical(counts: list)
#       Show the histogram vertically: bars grow upward, **with the slot
#       counts and slot numbers along the bottom**. Best viewed with a small
#       number of balls, since the height equals the largest count.
#       See the Extension section in the book for the approach.
def display_histogram_vertical(counts: list):
# finner maksimum antall baller
    maks_ant_baller = max(counts)
    print(f"maksimum antall baller: {maks_ant_baller}")
    print()
   
    for row in range(maks_ant_baller, 0, -1):
        for count in counts:
            if count >= row:
                print("*", end=" ")
            else:
                print(" ", end= " ")
        print()
# **with the slot counts and slot numbers along the bottom**
    for count in counts:
        print(count, end="  ")
    print()

    for slot in range(len(counts)):
        print(slot, end="   ")
    print()


if __name__ == "__main__":
    NUM_BALLS = 500
    NUM_ROWS = 8

    print(f"Bean Machine - {NUM_BALLS} balls, {NUM_ROWS} rows\n")

    # TODO: Call run_simulation() and then display_histogram()
    counts = run_simulation(NUM_BALLS, NUM_ROWS)
    print("----------------------------------------------------Horisontalt histogram----------------------------------------------------")
    display_histogram(counts)
    print("----------------------------------------------------Vertikalt histogram----------------------------------------------------")
    display_histogram_vertical(counts)
    
    
   