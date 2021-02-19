# Пункты от a до c
#
user_answ = int(input('Введите кол-во секунд: '))

hours = user_answ // 3600
minutes = (user_answ % 3600) // 60
seconds = user_answ % 60
print(f'{hours} часов {minutes} мин {seconds} сек')
