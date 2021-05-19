######## 곱하기 혹은 더하기 ########
numbers_str = input()
numbers = []
for number_str in numbers_str:
    numbers.append(int(number_str))

result = 0
for number in numbers:
    if result <= 0 or number <= 0:
        result += number
    else:
        result *= number

print(result)