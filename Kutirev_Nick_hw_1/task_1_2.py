new_list = []
sum = 0
result = 0
for i in range(1, 1001, 2):
    new_list.append(i ** 3)

for i in new_list:
    sum = i
    while i > 0:
        sum = sum + i % 10
        i = i // 10
    if sum % 7 == 0:
        result += sum
print(result)

new_list[:] = [i + 17 for i in new_list]

for i in new_list:
    sum = i
    while i > 0:
        sum = sum + i % 10
        i = i // 10
    if sum % 7 == 0:
        result += sum

print(result)
