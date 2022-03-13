#Nama: Rifqi Hanief
#Nim: 081911633017
#Tanggal: 6 Januari 2021
#Proyek Game sederhana: Cloud Vs Sephiroth

import random
#random akan digunakan dalam men-generate angka acak
class Character():
	def __init__(self, name=None, Race=None, lifePoint=None):
	#Constructor Overloading dengan berbagai variabel
		if (name !=None and Race!=None and lifePoint!=None):
			self.name=name
			self.Race=Race
			self.lifePoint=lifePoint
		elif (name !=None and Race!=None):
			self.name=name
			self.Race=Race
			self.lifePoint=1000
		elif (name !=None):
			self.name=name
			self.Race="Human"
			self.lifePoint=1000
		else:
			self.name="Villager"
			self.Race="Human"
			self.lifePoint=1000
			
	def showStats(self):
		#method untuk menampilkan status character
		print("Name:",self.name)
		print("Race:",self.Race)
		print("Life point:",self.lifePoint)

	def showLifePoint(self, bos):
		#method untuk menampilkan lifepoint kedua character
		print("Life Point".center(50,"="))
		print(self.name,"Life point:",self.lifePoint)
		print(bos.name,"Life point:",bos.lifePoint)
		print("="*50)

	def Attack(self, bos):
		#method untuk character melakukan penyerangan
		self.charge += 10
		damage = (self.atkPoint - bos.defPoint)
		if (damage < 0):
			damage == 0
		print(self.name,"attacks",bos.name,"for",damage,"damage")
		bos.lifePoint = bos.lifePoint - damage

	def Guard(self, bos):
		#method untuk character melakukan pertahanan
		self.charge += 5
		if (bos.atkPoint - (self.defPoint * 1.5) < 0):
			damage = 0
		else:
			damage = (bos.atkPoint - (self.defPoint * 1.5))
		print(self.name,"Guard")
		self.lifePoint = self.lifePoint - damage