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
    result += fuel_counter(numbers[i])
print(result)
