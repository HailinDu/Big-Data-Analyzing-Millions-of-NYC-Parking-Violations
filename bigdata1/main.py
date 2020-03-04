from sys import argv
from src.bigdata1.callapi import call_api
import os
import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--page_size', type = int)
	parser.add_argument('--num_pages', default = None, type = int)
	parser.add_argument('--output', default = None)
	args = parser.parse_args()

	APP_KEY = os.getenv('APP_KEY')
	call_api(args.page_size, args.num_pages, args.output, APP_KEY)