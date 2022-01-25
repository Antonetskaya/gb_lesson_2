#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

#Список

winter = [12, 1, 2]
summer = [6, 7, 8]
autumn = [9, 10, 11]
spring = [3, 4, 5]

number_month = int(input("Введите номер месяца: "))

if number_month in winter:
  print("Зима")
elif number_month in summer:
  print("Лето")
elif number_month in autumn:
  print("Осень")
elif number_month in spring:
  print("Весна")
else:
  print("Такого месяца не существует")