n = input("Напиши текст из 100 слов: ")
if len(n) >= 100:
	print("Молодец")
if len(n) <= 100:
	print("Зря ты так ):")
q = 1000
while q >= 1:
	print("я гуль " + str(q) +  " - 7" )
	q = q - 7
	if q <= 6:
		print("Я умер прости")
		break
input()