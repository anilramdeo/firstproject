
#imports
import json, os, sys

#current directory
root_dir = os.path.dirname(os.path.realpath(__file__))
#file directory
data_path = os.path.join(root_dir,'files')


# this function load the data into a dictionary
def loadData(filename):
	_file = os.path.join(data_path,filename)
	with open(_file) as f:
		data = json.load(f)
		return data

# this funcation parses the data and displays it in a readable format
def readData(data):
	for item in data['transactions']['transaction']:
		print item

transactions = loadData('transactions.json')

readData(transactions)