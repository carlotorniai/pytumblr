import json
import oauth2
from urlparse import parse_qsl

# from this nice post on stack overflow
credentials = json.loads(open('../tests/tumblr_credentials.json', 'r').read())

REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
CONSUMER_KEY = credentials['consumer_key']
CONSUMER_SECRET = credentials['consumer_secret']

consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth2.Client(consumer)


resp, content = client.request(REQUEST_TOKEN_URL, "GET")

request_token = dict(parse_qsl(content))
print "Request Token:"
print "    - oauth_token        = %s" % request_token['oauth_token']
print "    - oauth_token_secret = %s" % request_token['oauth_token_secret']


print "Go to the following link in your browser:"
print "%s?oauth_token=%s" % (AUTHORIZATION_URL, request_token['oauth_token'])

# After the user has granted access to you, the consumer, the provider will
# redirect you to whatever URL you have told them to redirect to. You can 
# usually define this in the oauth_callback argument as well.
oauth_verifier = raw_input('What is the PIN? ')
# Now below I had to compy manually form the redirect URL the oauth_verifier parameter
# Embedded in the URL.. i knwo not nice but it works..
token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
token.set_verifier(oauth_verifier)
client = oauth2.Client(consumer, token)

resp, content = client.request(ACCESS_TOKEN_URL, "POST")
print content
access_token = dict(parse_qsl(content))

print "Access Token:"
print "    - oauth_token        = %s" % access_token['oauth_token']
print "    - oauth_token_secret = %s" % access_token['oauth_token_secret']
print