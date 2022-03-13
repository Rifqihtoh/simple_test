#Nama: Rifqi Hanief
#Nim: 081911633017
#Tanggal: 6 Januari 2021
#Proyek Game sederhana: Cloud Vs Sephiroth

from Char import Character

class Hero(Character):
	#Inheritance dimana class Hero merupakan child dari class Character
	#Constructor Overloading dengan berbagai variabel
	def __init__(self, name=None, Race=None, lifePoint=None, atkPoint=None, defPoint=None,mana=None):
		super().__init__(name,Race,lifePoint)
		if(atkPoint!=None and defPoint!=None and mana!=None):
			self.atkPoint=atkPoint
			self.defPoint=defPoint
			self.mana=mana
		elif(atkPoint!=None and defPoint!=None):
			self.atkPoint=atkPoint
			self.defPoint=defPoint
			self.mana=75
		elif(atkPoint!=None):
			self.atkPoint=atkPoint
			self.defPoint=1000
			self.mana=75
		else:
			self.atkPoint=1000
			self.defPoint=1000
			self.mana=75
		self.maxlp = self.lifePoint
		self.maxmp = self.mana
		self.charge = 0
		self.mpot = 5
		self.hpot = 5

	def itemUse(self,num):
		#membuat method untuk penggunaan item
		self.charge += 5
		if(num == 1):
			self.hpot -=1
			healing = 5000
			if(self.lifePoint + healing >= self.maxlp):
				self.lifePoint = self.maxlp
			else:
				self.lifePoint += 5000
			print(self.name,"heals for 5000 life point")
		elif(num == 2):
			self.mpot -=1
			manarec = 100
			if(self.mana + manarec >= self.maxmp):
				self.mana = self.maxmp
			else:
				self.mana += 100
			print(self.name,"recovers 100 mana")

	def skillCrossSlash(self, bos):
		bos.lifePoint = bos.lifePoint - 3000
		self.mana -= 50
		self.charge += 20
		print(self.name,"attacks",bos.name,"for",3000,"damage using Cross slash")

	def skillOmniSlash(self, bos):
		if(self.lifePoint >= self.maxlp * 0.3):
			self.charge = 0
		damage = self.atkPoint * 4
		bos.lifePoint = bos.lifePoint - damage
		print(self.name,"attacks",bos.name,"for",damage,"damage using Omni slash")

	def Heal(self):
		#method untuk menambah life point saat pertarungan
		healing = 3500
		self.mana -= 30
		self.charge += 10
		if (self.lifePoint + healing >= self.maxlp):
			self.lifePoint == self.maxlp
		else:
			self.lifePoint += 3500
		print(self.name,"heals for 3500 life point")

	def showStats(self):
		#polymorphism overriding, dimana showStats pada class child Hero meng override showStats
		#pada parent Character
		print()													
		print("Cloud Stats".center(26,"="))
		super().showStats()
		print("Attack point:",self.atkPoint)
		print("Defend point:",self.defPoint)
		print("Mana:",self.mana)
		print("="*26)

	def skillMenu(self,bos,num):
		#membuat method untuk menampilkan menu skill
		print("Cloud".center(26,"="))
		print("Life point:", self.lifePoint)
		print("Mana:", self.mana)
		print("="*26)
		print("  =======Skill Menu======")
		print("==1. Heal        -30 mana==")
		print("==2. Cross Slash -50 mana==")
		if(self.charge >= 100 or self.lifePoint <= self.maxlp * 0.3):
			print("==3. Omni Slash    LIMIT!==")
		print("==0. Back                ==")
		print("   ======================")
		choice = int(input())
		if(choice == 1):
			if(self.mana < 30):
				print("Not Enough Mana!")
				choice = int(self.skillMenu(bos,num))
			else:
				self.Heal()
		elif(choice == 2):
			if(num == 1):
				self.mana -= 50
			else:
				if(self.mana < 50):
					print("Not Enough Mana!")
					choice = int(self.skillMenu(bos,num))
				else:
					self.skillCrossSlash(bos)
		elif(choice == 3):
			if(self.charge >= 100 or self.lifePoint <= self.maxlp * 0.3):
				self.skillOmniSlash(bos)
		elif(choice == 0):
			pass
		else:
			if(self.charge != 100 and self.lifePoint >= self.maxlp * 0.3):
				print("Please, choose the numbers from 0 to 2")
				choice = int(self.skillMenu(bos,num))
			else:
				print("Please, choose the numbers from 0 to 3")
				choice = int(self.skillMenu(bos,num))
		return choice

	def itemMenu(self):
		#membuat method untuk menampilkan menu item
		print("Cloud".center(26,"="))
		print("Life point:", self.lifePoint)
		print("Mana:", self.mana)
		print("="*26)
		print("  ====Item Menu====")
		print("==1. Life Potion",self.hpot,"==")
		print("==2. Mana Potion",self.mpot,"==")
		print("==0. Back          ==")
		print("   ==============")
		choice = int(input())
		if(choice == 1):
			if(self.hpot <= 0):
				print("Life Potion is empty!")
				choice = int(self.itemMenu())
			else:
				self.itemUse(choice)
		elif(choice == 2):
			if(self.mpot <= 0):
				print("Mana Potion is empty!")
				choice = int(self.itemMenu())
			else:
				self.itemUse(choice)
		elif(choice == 0):
			pass
		else:
			print("Please, choose the numbers from 0 to 2")
			choice = int(self.itemMenu())
		return choice