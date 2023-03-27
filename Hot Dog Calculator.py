#Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers.

#The program should ask the user for the number of people attending the cookout and Hot dogs each person will be given.

#Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8.

#The program should display the following details:

# Number of packages of hot dogs required
# Number of packages of hot dog buns required
# Hot dogs that will be left over
# Hot dog buns that will be left over

import math

print('Welcome to the Hot Dog Calculator, hotshot! Here to assist you in your glizzy endeavors.')

SAUSAGES = 10
BUNS = 8

people = int(input("\nHow many people will eat hotdogs at the cookout? "))
hdpp = int(input("\nHow many hot dogs will each of them eat? "))


sausagePacks = (people * hdpp)/SAUSAGES
sausagePacks = math.ceil(sausagePacks)

bunPacks = (people * hdpp)/BUNS
bunPacks = math.ceil(bunPacks)

bunsLeft = (bunPacks * BUNS) - (people * hdpp)

sausagesLeft = (sausagePacks * SAUSAGES) - (people * hdpp)

print("\nNumber of packages of hot dogs required: ", sausagePacks)

print("\nNumber of packages of hot dog buns required:", bunPacks)

print("\nHot dogs that will be left over: ", sausagesLeft)

print("\nHot dogs buns that will be left over: ", bunsLeft)

