
import csv

my_file = 'my_file.txt'

friuts = [
	['Banana', 10],
	['Orange', 3],
	['Apple', 5]
]


with open(my_file, 'w', newline='') as file:
	writers = csv.writer(file)
	writers.writerows(friuts)


with open(my_file, 'a', newline='') as file:
	friut = ['Pineapple', 12]
	writers = csv.writer(file)
	writers.writerow(friut)


with open(my_file, 'r', newline='') as file:
	reader = csv.reader(file)
	for line in reader:
		print(line[0] + ' - ' + str(line[1]))


#Работа со словарями

filename = 'users.txt'

users = [
	{'name' : 'Tom', 'age': 15},
	{'name':'Marina', 'age':20},
	{'name':'Jery', 'age':10}
]

with open(filename, 'w', newline='') as file:
	read = ['name', 'age']
	writer = csv.DictWriter(file, fieldnames=read)
	writer.writeheader()

    # запись нескольких строк
	writer.writerows(users)
     
	user = {"name" : "Sam", "age": 41}
    # запись одной строки
	writer.writerow(user)
 

with open(filename, 'a', newline='') as file:
	men = {'name':'Raf', 'age':14}
	writer = csv.DictWriter(file, fieldnames=men)
	writer.writeheader()
	writer.writerow(men)


with open(filename, 'r', newline='') as file:
	reader = csv.DictReader(file)
	for line in reader:
		if line['name'] == 'name':
			continue
		print(line['name'], '-', str(line['age']))