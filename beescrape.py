import urllib.request
import csv
import os
from pathlib import Path

species = []

with open('beespotter.csv') as csvDataFile:
	csvReader = csv.reader(csvDataFile)
	next(csvReader)
	for row in csvReader:
		#species: row[17]
		#url: row[27]
		#create species directory if there isn't one
		if not os.path.exists("beespotter/" + row[17].replace(" ","_")):
			os.makedirs("beespotter/" + row[17].replace(" ","_"))

		#get image name, create PATH to save to
		IMAGE = row[27].rsplit('/',1)[1]
		PATH = "beespotter/" + row[17].replace(" ","_") + "/" + IMAGE

		#download to proper directory, if it hasn't already been:
		if not (Path(PATH).exists() and Path(PATH).is_file()):
			print("downloading "+IMAGE)
			urllib.request.urlretrieve(row[27],PATH)
		else:
			print("already downloaded, skipping "+IMAGE)

print("downloaded all images!")