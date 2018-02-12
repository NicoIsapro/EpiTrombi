# EpiTrombi
# Développé par Nico Isapro
# Je suis pas responsable si vous vous faites ban par le serveur Epitech

# ----------------------------------------------------#
#                      IMPORTATION                    #
# ----------------------------------------------------#

import sys
import os
import requests
import os.path
import re

# ----------------------------------------------------#
#                      EN TETE DOS                    #
# ----------------------------------------------------#

print ("")
print ("  _   _   _                    ___                                      ")
print (" | \ | | (_)   ___    ___     |_ _|  ___    __ _   _ __    _ __    ___  ")
print (" |  \| | | |  / __|  / _ \     | |  / __|  / _` | | '_ \  | '__|  / _ \ ")
print (" | |\  | | | | (__  | (_) |    | |  \__ \ | (_| | | |_) | | |    | (_) |")
print (" |_| \_| |_|  \___|  \___/    |___| |___/  \__,_| | .__/  |_|     \___/")
print ("                                                  |_|                  ")
print ("")
print ("                           EpiTrombi V1                ")
print ("")

# ----------------------------------------------------#
#                      INITIALISATION                 #
# ----------------------------------------------------#

hdmode = input("Try HD Mode ? (.bmp pictures) Y/N: ")

if hdmode == "y" or hdmode == "Y" or hdmode == "yes" or hdmode == "YA":
	extension = ".bmp"
else:
	extension = ".jpg"

print ("\nAn example of normal username:\nMy last name is nao and my first name is marvin\nMy username is -> marvin.nao\n")
username = input("Type the username to search in trombi: ").lower()

if username.find('.') == -1:
	print ("\nMarvin: You miss the '.', I give you a second try...")
	username = input("Type the username to search in trombi: ").lower()
	if username.find('.') == -1:
		print ("\nMarvin: Go fuck yourself!")
		exit()

# ----------------------------------------------------#
#                      CHECKS                         #
# ----------------------------------------------------#
headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
	'Upgrade-Insecure-Requests': '1',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7'
}

if extension == ".bmp":
	print ("Marvin: I will check if HD is available for your m8, It can take a minute\n")
	url = "https://cdn.local.epitech.eu/userprofil/" + username + extension
	response = requests.get(url, headers=headers)
	if response.status_code != 200:
		print ("Marvin: 404 not found lol --> I try with standard mode\n ")
		extension = ".jpg"
	else:
		print ("HD is available, start download in current folder...\n")
		filename = username + extension
		with open(filename, 'wb') as f:
			f.write(response.content)
		del response
		print ("Download Complete\n")
		exit()

print ("Marvin: I will check if your m8 exists\n")
url = "https://cdn.local.epitech.eu/userprofil/profilview/" + username + extension
response = requests.get(url, headers=headers)
if response.status_code != 200:
	print ("Marvin: 404 not found lol\n")
	exit()
else:
	print ("Marvin: Hey I found " + username.split('.')[0] + " in the universe\n")
	print ("I start the download in the current folder...\n")

# ----------------------------------------------------#
#                     DOWNLOAD                        #
# ----------------------------------------------------#

filename = username + extension
with open(filename, 'wb') as f:
	f.write(response.content)
del response
print ("Download Complete\n")
exit()