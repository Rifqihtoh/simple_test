#Nama: Rifqi Hanief
#Nim: 081911633017
#Tanggal: 6 Januari 2021
#Proyek Game sederhana: Cloud Vs Sephiroth

import random
from Char import Character
from Player import Hero
from Enemy import Boss
#random akan digunakan dalam men-generate angka acak

def credit():
	#untuk mengeprint pembuat pada akhir game
	print()
	print("Project Created by:".center(50,"="))
	print("Nama: Rifqi Hanief")
	print("Nim: 081911633017")
	print("Tanggal: 6 Januari 2021")
	print("Thank you for playing!")
	print("="*50)

def menu():
	#membuat method untuk menampilkan menu utama
	print("Cloud Vs Sephiroth".center(50,"="))
	print("1. Start fight")
	print("2. Show Cloud stats")
	print("3. Show Sephiroth stats")
	print("4. Exit")
	print("="*50)
	choice = input()
	return choice

def fightmenu():
	#membuat method untuk menampilkan menu saat pertarungan
	print("  ==Fight Menu===")
	print("==1. Attack      ==")
	print("==2. Guard       ==")
	print("==3. Item        ==")
	print("==4. Skill       ==")
	print("   ==============")
	choice = input()
	return choice

class Main():
	#membuat objek hero dan boss untuk permainan
	hero1 = Hero("Cloud","Human",9999,3500,2750,250)
	boss1 = Boss("Sephiroth","Unknown",30000,4000,1800,350)
	n = 0
	#pendeklarasian variable n = 0 untuk penggunaan infinite while loop
	while n == 0:
		print()
		choice = int(menu())
		#menampilkan pilihan pada menu utama untuk user
		if(choice == 1):
			print("="*50)
			print("Cloud: S...Sephiroth!")
			print("Sephiroth: Cloud...i will give you ultimate despair!")
			while (hero1.lifePoint > 0 and boss1.lifePoint > 0):
				hero1.showLifePoint(boss1)
				choose = int(fightmenu())
				#menampilkan menu pilihan pada saat pertarungan untuk user
				num = random.randint(1,4)
				#men-generate angka random antara 1 hingga 4 untuk membuat musuh melakukan
				#aksi sesuai dengan angka yang disetting pada classs Boss
				if(choose == 1):
					if(num == 1):
						boss1.Guard(hero1)
					else:
						hero1.Attack(boss1)
						boss1.bossAction(num,hero1)
				elif(choose == 2):
					if(num == 4):
						boss1.bossAction(num,hero1)
					else:
						hero1.Guard(boss1)
				elif(choose == 3):
					itChoice = int(hero1.itemMenu())
					if(itChoice == 0 ):
						if(hero1.hpot <=0  or hero1.mpot <=0):
							pass
					else:
						if(num == 1):
							num = random.randint(2,4) 
						boss1.bossAction(num,hero1)
				elif(choose == 4):
					skillChoice = int(hero1.skillMenu(boss1,num))
					if(skillChoice == 0):
						pass
					else:
						if(skillChoice == 1):
							num = random.randint(2,4)
						elif(num == 1):
							boss1.Guard(hero1)
						elif(skillChoice == 3):
							boss1.skillSuperNova(hero1)
						else:
							boss1.bossAction(num,hero1)
				else:
					print("Please, choose the numbers from 1 to 5")
			else:
				if (hero1.lifePoint < boss1.lifePoint):
					#apabila nyawa hero 0 terlebih dahulu, anda kalah dalam pertarungan
					print()
					hero1.showLifePoint(boss1)
					print("Cloud: Everyone...i'm sorry...")
					print("Game Over".center(50,"="))
					credit()
					break
				elif (boss1.lifePoint < hero1.lifePoint):
					#apabila nyawa boss 0 terlebih dahulu, anda menang dalam pertarungan
					print()
					hero1.showLifePoint(boss1)
					print("Cloud: Stay where you belong...in my memories.")
					print("Sephiroth: I will...never be a memory.")
					print("The End".center(50,"="))
					credit()
					break
		elif(choice == 2):
			hero1.showStats()
		elif(choice == 3):
			boss1.showStats()
		elif(choice == 4):
			credit()
			break
		else:
			print("Please, choose the numbers from 1 to 4")
			
#Menjalankan program
Maintest = Main()