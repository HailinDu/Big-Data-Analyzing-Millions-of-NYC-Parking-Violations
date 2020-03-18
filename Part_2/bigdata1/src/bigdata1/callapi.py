import json
import pprint
from sodapy import Socrata
from requests import get
from datetime import datetime, date
from elasticsearch import Elasticsearch

def create_update_index(index_name):
	es = Elasticsearch()
	try:
		es.indices.create(index=index_name)
	except:
		pass
	return es

def format_push_data(record, es, index_name):
	for key, value in record.items():
		if '_amount' in key:
			record[key] = float(value)
		elif '_date' in key:
			record[key] = datetime.strptime(record[key], '%m/%d/%Y').date()
	es.index(index=index_name, id=record['summons_number'], body=record)

def call_api(APP_KEY, page_size, num_pages, output, push_elastic):
	client = Socrata("data.cityofnewyork.us", APP_KEY)

	if num_pages is None:
		count_total = int(client.get("nc67-uf89", select='COUNT(*)')[0]['COUNT'])
		num_pages = count_total // page_size + 1
	if push_elastic:
		es = create_update_index('nyopcv')
	for n in range(num_pages):
		page = client.get("nc67-uf89", limit = page_size, offset = n*page_size)
		if output is not None:
			response = open(output, 'w')
			response.write(json.dumps(page) + '\n')
		else:
			pprint.pprint(page)
		if push_elastic:
			for record in page:
				format_push_data(record, es, 'nyopcv')
	if output is not None:
		response.close()
		print(response)