#!/usr/bin/python3

from random import choice
from os import system

members = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '0',
'1', '2', '3', '4', '5', '6', '7', '8', '9']

def create(tab):
	url = "https://prnt.sc/"
	image = ""
	global links
	links = "" # Default 5 url
	for i in range(tab): #random 6 characters for random image
		image = choice(members)+choice(members)+choice(members)+choice(members)+choice(members)+choice(members)
		links += " "+url+image



def save(links): #History file of links
	history = open("history.txt", "a")
	history.write(links+'\n')
	history.close()



banner = '\033[32m'+'''

               _.------.
           _.-`    ('>.-`"""-.
 '.__.---'`       _'`   _ .--.)		RANDOM LİGHTSHOOT İMAGES
        -'         '-.-';`   `
        ' -      _.'  ``'--. 
            '---`    .-'""`
    @Hamza Bora     /`

'''+'\033[0m'+'\033[1m'+"""

1 -
	How many tabs do you want in Firefox ?
	For example:

		Enter>>> 2

	[Default 5 tab]

2 - 
	For Exit

		Enter>>> exit

"""+'\033[0m'

print(banner)


while True:
	
	tabs = input("\nEnter>>> ")

	if tabs == "exit" or tabs == "EXIT":
		print('\033[1m'+"Goodbye Friend."+'\033[0m')
		break

	elif bool(tabs) == 0: #Default option
		create(5) #tabs
		save(links)
		print(links)
		system(f"firefox{links}")

	else:
		tabs = int(tabs)
		create(tabs)
		save(links)
		print(links)
		system(f"firefox{links}")