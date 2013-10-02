# This script takes a ipython notebbok, converts it as html  and post it as a draft post on tumlr
import json
import sys, getopt
import pytumblr

# TO DO
# Make the blog URL a parameter

BLOG_URL='carto71.tumblr.com'

def main(argv):
	''' Posts the content of an html file as blog post on Tumblr'''

	inputfile = ''
	blogtitle = ''
	# TO DO
	# Check the args
	if len(argv)<3:
		print 'Usage; post_ipnb -i <inputfile> -t <blogtitle>'
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

	# Reads credentials
	credentials = json.loads(open('tumblr_credentials.json', 'r').read())
	

	# Define the client
	client = pytumblr.TumblrRestClient(
    credentials['consumer_key'],
    credentials['consumer_secret'],
    credentials['oauth_token'],
    credentials['oauth_token_secret'],
    )
	
	# Actually post the draft
	print "Creating the post..."
	
	# Serialize html into a string
	string_html  = linestring = open(inputfile, 'r').read()
	
	# Add status as parameter in case
	response =  client.create_text(BLOG_URL, body=string_html, title=blogtitle, format='html')
	
	# Parse the response to check if an id for the post is returned
	if  'id' not in response.keys():
		print "Error creating post!"
		meta = response['meta']
		status = meta['status']
		msg = meta['msg']
		print "Status:" , status
		print "Message:", msg
	else:
		print "Post created successfully. Post Id:" , response['id']

if __name__ == "__main__":
	main(sys.argv[1:])
