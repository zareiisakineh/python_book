# file: ex_05_13_slice_and_comp_start.py

temps = [18, 21, 19, 24, 27, 22, 20, 16, 23, 25, 28, 17, 19, 21]

# TODO: 1. Print the first week (first 7 days) and the second week (last 7 days)
print(f"First week: {temps[:7]}")
print(f"Second week: {temps[7:]}")

# TODO: 2. Print every other day, starting from the first
print(f"Every other day: {temps[::2]}")
# TODO: 3. Print the list reversed, and separately the last three days
print(f"Reversed: {temps[::-1]}")
print(f"Last three: {temps[-3:]}")
# TODO: 4. Print every temperature converted to Fahrenheit, as whole degrees
fahrenheit = [round(temp * 9 / 5 + 32) for temp in temps]
print(f"Farenheit: {fahrenheit}")
# TODO: 5. Print the warm days (22 or higher) from the second week only
varme_dager2 = [temp for temp in temps[7:] if temp >= 22]
print(f"Warm second-week days: {varme_dager2}")
# TODO: 6. Print a label for each day: "warm" if 22 or higher, otherwise "cool"
label = []
for temp in temps:
    if temp >= 22:
        label.append("Warm")
    else:
        label.append("Cool")
print(label)
# Stuck? See the Hints section in ex_05_13_slice_and_comp.md
