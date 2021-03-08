numbers = []
with open("1.in", "r") as f:
    data = f.readlines()
    for i in range(len(data)):
        numbers.append(int(data[i].strip("\n")))


def fuel_counter(num):
    fuel = num // 3 - 2
    return fuel


res = 0

for i in range(len(numbers)):
    a = fuel_counter(numbers[i])
    if a < 9:
        res += a
    else:
        while a >= 0:
            res += a
            a = fuel_counter(a)

print(res)
