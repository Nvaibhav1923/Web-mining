def calc_centered_average(numbers):
    for j in range(len(numbers)):
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]
            else:
                continue
    numbers = numbers[1:len(numbers) - 1]
    min_num = min(numbers)
    max_num = max(numbers)
    new = []
    for i in numbers:
        if i != min_num and i != max_num:
            new.append(i)
    new.append(min_num)
    new.append(max_num)
    for j in range(len(new)):
        for i in range(len(new) - 1):
            if new[i] > new[i + 1]:
                new[i + 1], new[i] = new[i], new[i + 1]
            else:
                continue
    avg = sum(new) / len(new)
    return avg
numbers = [4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 100]
print(f"The centered average of {numbers} is {calc_centered_average(numbers)}")