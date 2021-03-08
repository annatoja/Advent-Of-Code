numbers = []
with open("1.in", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        numbers.append(int(data[i].strip("\n")))


def fuel_counter(num):
    fuel = num // 3 - 2
    return fuel


result = 0

for i in range(len(numbers)):
    part_fuel = fuel_counter(numbers[i])
    if part_fuel < 9:
        result += part_fuel
    else:
        while part_fuel >= 0:
            result += part_fuel
            part_fuel = fuel_counter(part_fuel)
print(result)
