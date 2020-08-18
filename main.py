import time
import random

class Yaris:
	def __init__(self,model,hiz):
		self.model = model
		self.hiz = hiz
	def myspeed(self):
		return self.hiz

i = 0
while i = 0:
	secenek = input("Oyun modunu seçin. (1P/2P): ")
	if secenek == "1P":
		k1 = print("Adını gir: ")
		rhiz1 = random.randint(1,3)
		rhiz2 = random.randint(1,3)
		a1 = Yaris(k1,rhiz1)
		a2 = Yaris("Bot",rhiz2)
		i += 1 
	elif secenek == "2P":
		k1 = input("Oyuncu-1 adını gir: ")
		k2 = input("Oyuncu-2 adını gir: ")
		rhiz1 = random.randint(1,3)
		rhiz2 = random.randint(1,3)
		a1 = Yaris(k1,rhiz1)
		a2 = Yaris(k2,rhiz2)
		i += 1
	else:
		continue	


while True:
	print("Yarış başladı!")
	time.sleep(2)
	if a1.myspeed() > a2.myspeed():
		print(k1 + " yarışı kazandı, tebrikler!")
	elif a2.myspeed() > a1.myspeed():
		print(k2 + " yarışı kazandı, tebrikler!")
	elif a2.myspeed() == a1.myspeed():
		print("Yarış berabere!")
	break
