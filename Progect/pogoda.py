#Узнаём погоду

print("Программа запущенна")


import pyowm
from colorama import Fore, Back, Style
from colorama import init
init()
print(Back.GREEN)
print(Fore.BLACK)



owm = pyowm.OWM('24ee316d05bdc2ba0488d888ac3546a5')
mgr = owm.weather_manager()

p = input("Где ты живёшь? ")

observation = mgr.weather_at_place(p)
w = observation.weather

t = w.temperature('celsius')["temp"]
t2 = w.temperature('celsius')["temp_max"]
t3 = w.temperature('celsius')["temp_min"]
we = w.wind()
ob = w.clouds
ti = w.heat_index
v = w.humidity
rain = w.rain

print(Back.MAGENTA)
if w.detailed_status == "clear sky":
	print("В городе " + p + " сейчас " + "чистое небо")
elif w.detailed_status == "clouds":
	print("В городе " + p + " сейчас " + "облачно")
elif w.detailed_status == "broken clouds":
	print("В городе " + p + " сейчас " + "тучи")
elif w.detailed_status == "few clouds":
	print("В городе " + p + " сейчас " + "небольшие облака")
elif w.detailed_status == "scattered clouds":
	print("В городе " + p + " сейчас " + "рассеянные облака")
elif w.detailed_status == "overcast clouds":
	print("В городе " + p + " небо " + "с небольшим количеством облаков")
else:
	print("Хз чё за погода")

#print("В городе " + p + " сейчас " + w.detailed_status)

print(Back.YELLOW)
print("Температура на данный момент - " + str(t))
print("Максимальная температура за день - " + str(t2))
print("Минимальная температура за день - " + str(t3))
print("Ветер = " + str(we))
print("Облака = " + str(ob))
print("Тепловой индекс = " + str(ti))
print("Влажность = " + str(v))
print("Дождь = " + str(rain))

print(Fore.BLUE)
print(Back.BLACK)

if t < 0: 
	print("Одевай все, что у тебя есть!\n")
elif t < 20:
	print("Одевайся по теплее\n")
else:
	print("На улице тепло, одевай что хочешь!\n")


print(Fore.WHITE)
print("Программа завершена (нажмите Enter для выхода)")

input()




