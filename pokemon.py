#!/usr/bin/python

# CLASSES

class Pokemon:
	def __init__(self, name, atk_type, level, xp=0, ko=False):
		self.name = name
		self.atk_type = atk_type
		self.level = level
		self.xp = xp
		self.max_xp = level * 10
		self.ko = ko
	
	def __repr__(self):
		return "{name} is a level {level} {type} Pokemon. Max health: {max_xp}".format(name=self.name, level=self.level, type=self.type, max_xp=self.max_xp)
		
	# Pokemon Attack
	def attack(self, other):
		damage = 1
		for x in self.atk_type:
			for y in other.atk_type:
				if (x == "fire" and y == "grass") \
				or (x == "water" and y == "fire") \
				or (x == "grass" and y == "water"):
					damage += 0.5
				elif (x == "fire" and y =="water")\
				or (x == "water" and y == "grass")\
				or (x == "grass" and y == "fire"):
					damage -= 0.5
		total_damage = self.level * damage
		other.xp = max(other.xp - total_damage, 0)
		print("{name} has dealt {damage} damage from {other}!".format(name=self.name, damage=total_damage, other=other.name))
		
		if other.xp == 0:
			other.ko == True
		
	# Pokemon Health
	def lose_health(self, damage):
		curr_xp = self.xp - damage
		if curr_xp > 0:
			self.xp = curr_xp
			print("{name} has lost {damage} health! Current health: {health}".format(name=self.name, damage=damage, health=self.xp))
		if curr_xp == 0:
			ko = True
			print(self.name + " is knocked out!")
	
	def gain_health(self):
		curr_xp = self.xp + gain_xp
		if self.xp < self.max_xp:
			self.xp = self.max_xp
			pring("{name} has gained {gain} health! Current health: {health}".format(name=self.name, gain=gain_xp, health=self.xp))
		elif self.xp == self.max_xp:
			self.xp = self.max_xp
			print(self.name + "has restored to full health!")	
	
	#Pokemon Level Up
	def levelUp(self):
		self.level += 1
		self.max_xp = self.level * 10


class Trainer:
	def __init__(self, name, pokemons, potions, curr_pokemon):
		self.name = name
		self.pokemons = pokemons
		self.potions = potions
		self.curr_pokemon = curr_pokemon
	
	def __repr__(self):
		return "The trainer {name} has {pokemons} pokemon, {potions} potions, and {curr} active pokemon".format(name=self.name, pokemons=self.pokemons, potions=self.potions, curr=self.curr_pokemon)
	
	#Attack Other Trainers
		def atk_other_trainers(self, other_trainer):
			their_pokemon = other_trainer.pokemons[other_trainer.curr_pokemon]
			self.curr_pokemon.atk_other_trainers(their_pokemon)
			print(self.name + " has attacked " + other_trainer.name + "!")		
				
	#Using Potion
	def potion(self):
		if self.potions == 0:
			print("No potions left")
		elif self.curr_pokemon.xp == self.curr_pokemon.max_xp:
			print("{name} is at full health".format(name=self.curr_pokemon))
		else:
			while pokemon.curr_xp <= pokemon.max_xp:
				self.potions -= 1
				self.curr_pokemon.gain_health(10)
				print("{name} has used one potion".format(name=self.name))
	
		