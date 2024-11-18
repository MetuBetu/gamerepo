# Import vars

import config.initvars as initvars

currentamount = initvars.startamount
walletmoney = initvars.walletmoney
currentcost = initvars.startcost

# Import / download required modules

import os
import time
import random
import threading
try:
	from colorama import init as colorama_init
except ImportError:
	try:
		os.system("pip install colorama")
		from colorama import init as colorama_init
	except:
		print("Unable to download required modules!")

try:
	from termcolor import cprint
except ImportError:
	try:
		os.system("pip install termcolor")
		from termcolor import cprint
	except:
		print("Unable to download required modules!")

# Init colorama for compat
colorama_init()

# Define functions
def mainmenu():
	print("-" * 20)
	cprint("MAIN MENU", "light_blue")
	print("-" * 20)
	mainmenuchoice = input("[S]ell or [B]uy or [C]heck:")
	return mainmenuchoice

def threadTenSeconds():
	while True:
		global currentcost
		time.sleep(10)
		coinflip = random.randrange(1, 100)
		if (coinflip >= 50 and currentcost < 20) or currentcost < 50:
			currentcost = currentcost * 1.2
			currentcost = round(currentcost, 2)
		elif coinflip < 50 or currentcost > 200:
			currentcost = currentcost * 0.8
			currentcost = round(currentcost, 2)

ThreadTenSeconds = threading.Thread(target=threadTenSeconds)
ThreadTenSeconds.start()

# Runtime loop

while True:
	mainmenuchoice = mainmenu()
	if mainmenuchoice == "S" or mainmenuchoice == "s" and currentamount != 0:
		amountosell = input("Enter amount: ")
		amountosell = int(amountosell)
		if amountosell <= currentamount:
			walletmoney += amountosell * currentcost
			currentamount -= amountosell
	if mainmenuchoice == "B" or mainmenuchoice == "b" and walletmoney >= currentcost:
		amountobuy = input("Enter amount: ")
		amountobuy = int(amountobuy)
		if amountobuy * currentcost <= walletmoney:
			walletmoney -= amountobuy * currentcost
			currentamount += amountobuy
	if mainmenuchoice == "C" or mainmenuchoice == "c":
		print("Cash: " + str(walletmoney))
		print("Amount of stock: " + str(currentamount))
		print("Price of stock: " + str(currentcost))

input()
ThreadTenSeconds.join()