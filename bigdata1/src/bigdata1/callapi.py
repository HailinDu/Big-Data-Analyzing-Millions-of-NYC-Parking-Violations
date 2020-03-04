import json
import pprint
from sodapy import Socrata
from requests import get

def call_api(page_size, num_pages, output, APP_KEY):
	client = Socrata("data.cityofnewyork.us", APP_KEY)

	if num_pages is None:
		count_total = int(client.get("nc67-uf89", select='COUNT(*)')[0]['COUNT'])
		num_pages = count_total // page_size + 1
	for n in range(num_pages):
		page = client.get("nc67-uf89", limit = page_size, offset = n*page_size)
		if output is not None:
			response = open(output, 'w')
			response.write(json.dumps(page) + '\n')
		else:
			pprint.pprint(page)
	if output is not None:
		response.close()
		print(response)