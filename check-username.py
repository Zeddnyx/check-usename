#source https://t.me/API_J
import requests as req
import json
import os

def check():
	user = input('Input Name : ')
	print('')
	url = 'https://tufaah.herokuapp.com/username/?user={}'.format(user)
	res = req.get(url)
	cek = res.json()

	i   = cek['available']
	for x in i :
		url = x['Url']
		web = x['Website']

		print('[!] Available')
		print('url :',url)
		print('web :',web,'\n')

	a   = cek['taken']
	for z in a :
		url = z['Url']
		web = z['Website']

		print('\n[!] Taken!')
		print('url :',url)
		print('web :',web,'\n')
os.system('clear')
check()
