# This script takes a ipython notebbok, converts it as html  and post it as a draft post on tumlr
import nose
import unittest
import mock
import json
import io
import sys, getopt
from httpretty import HTTPretty, httprettified
import pytumblr
from urlparse import parse_qs

# Here need to parse the parameter ipython notebpok name and the post title

def main(argv):
	''' Posts the content of an html file as blog post on Tumblr'''
	inputfile = ''
	blogtitle = ''
	# TO DO
	# Check the args
	if len(argv)<3:
		print 'post_ipnb -i <inputfile> -t <blogtitle>'
		sys.exit(2)
	try:
		opts, args = getopt.getopt(argv,"hi:t:",["ifile=","title="])
	except getopt.GetoptError:
		print 'post_ipnb -i <inputfile> -t <blogtitle>'
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print 'test.py -i <inputfile> -t <blogtitle>'
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-t", "--title"):
			blogtitle = arg
	print 'Input file is "', inputfile
	print 'Blog Title is file is "', blogtitle

	credentials = json.loads(open('tumblr_credentials.json', 'r').read())
	blog_url='carto71.tumblr.com'
	# Define the client
	client = pytumblr.TumblrRestClient(
    credentials['consumer_key'],
    credentials['consumer_secret'],
    credentials['oauth_token'],
    credentials['oauth_token_secret'],
    )
	print client.info() 
	# Actually post the draft
	print "Creating the post"
	string_html  = linestring = open(inputfile, 'r').read()
	print string_html
	print client.create_text(blog_url, body=string_html, title=blogtitle, format='html')

if __name__ == "__main__":
	main(sys.argv[1:])
