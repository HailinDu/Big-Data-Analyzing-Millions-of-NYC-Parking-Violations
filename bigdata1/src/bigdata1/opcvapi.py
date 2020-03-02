from sodapy import Socrata
from requests import get
import json

def call_opcv(APP_KEY, page_size, num_pages, output):
	client = Socrata("data.cityofnewyork.us", APP_KEY)
	results = open(output, 'w')
	for record in range(num_pages):
		page = client.get("nc67-uf89", limit = page_size, offset = record * page_size)
		results.write(json.dumps(page) + '\n')
	return results