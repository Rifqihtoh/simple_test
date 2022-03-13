#Nama: Rifqi Hanief
#Nim: 081911633017
#Tanggal: 6 Januari 2021
#Proyek Game sederhana: Cloud Vs Sephiroth

from Char import Character

class Boss(Character):
	#Inheritance dimana class Boss merupakan child dari class Character
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
		self.charge = 0
		self.maxmana = self.mana
		self.recovmana = 1

	def bossAction(self,number,bos):
		#membuat method agar nantinya dalam pertarungan
		#boss memiliki aksi yang berbeda-beda
		if(self.mana <= 0):
			self.skillRecovMana()
		else:
			if(number == 1):
				self.Guard(bos)
			elif(number == 2):
				self.Attack(bos)
			elif(number == 3):
				self.Heal()
			elif(number == 4):
				self.skillGigaFlare(bos)

	def skillRecovMana(self):
		self.mana == self.maxmana
		print(self.name,"Fully restored their mana")

	def skillGigaFlare(self, bos):
		bos.lifePoint = bos.lifePoint - 4500
		self.mana -= 65
		print(self.name,"attacks",bos.name,"for",4500,"damage using Giga Flare")

	def skillSuperNova(self, bos):
		if bos.lifePoint <= 50:
			print(self.name,"attacks",bos.name,"for",bos.lifePoint - bos.lifePoint / 16,"damage using Super Nova")
			bos.lifePoint = 0
		else:
			print(self.name,"attacks",bos.name,"for",bos.lifePoint - bos.lifePoint / 16,"damage using Super Nova")
			bos.lifePoint = bos.lifePoint / 16

	def Heal(self):
		healing = 5000
		self.mana -= 50
		if (self.lifePoint + healing >= self.maxlp):
			self.lifePoint = self.maxlp
		else:
			self.lifePoint += 5000
		print(self.name,"heals for 5000 life point")

	def showStats(self):
		#polymorphism overriding, dimana showStats pada class child boss meng override showStats
		#pada parent Character
		print()													
		print("Sephiroth Stats".center(26,"="))
		super().showStats()
		print("Attack point:",self.atkPoint)
		print("Defend point:",self.defPoint)
		print("Mana:",self.mana)
		print("="*26)
