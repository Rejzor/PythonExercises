import requests
from bs4 import BeautifulSoup

source_code = requests.get('https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/').text
soup = BeautifulSoup(source_code, "html.parser")

elements = open('symbols.txt', 'r+')
ele = elements.readlines()
ele = ele[0][:].split(',')
for count, world in enumerate(ele,4):
	if count % 5 == 0:
		elements.write(world)
elements.close        