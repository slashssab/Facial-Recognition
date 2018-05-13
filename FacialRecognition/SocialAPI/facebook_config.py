import facebook as fb
from urllib.parse import urlparse


#1

import facebook
import urllib
import urllib.parse
import subprocess
import warnings
import pycurl
import io
import certifi

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = '151340058874649'
FACEBOOK_APP_SECRET = 'aa3404db06b8cbc000a463cee1da93d2'
FACEBOOK_PROFILE_ID = '127898134710376'


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
#oauth_curl_cmd = ['curl',
#                  'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]


buffer=io.BytesIO()
c = pycurl.Curl()
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.URL, 'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args))
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
print(body)
#input()
#2
body1=str(body)
oauth_access_token = body1.split('"')[3]
print(oauth_access_token)

#3

facebook_graph = facebook.GraphAPI(oauth_access_token)
#facebook_graph = facebook.GraphAPI('EAACJpJpzExkBANxE2BTPH8WuuYEAMp3IQv4zq6E7sZBJ1zQj7hUD3opj5U9UwCts14BG7hwtI3i3eBrfZBvYINneOZBZCtEdNhmCrgMdr7D4ByM8BfMGt5kUnZCJTJV74ZB9ugwyJ792SmIuMZBDr14fuEPxAVGZAjuH4U66b0LKC97y3ESqZAjBIErSlTKYaTLEfp58D6lX7BsOblfLlbFHu0ZCMClcvzSdcZD')

# Try to post something on the wall.
#try:
fb_response = facebook_graph.put_wall_post('test posta m8.1', \
                                               profile_id = FACEBOOK_PROFILE_ID)
#4
