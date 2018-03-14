import facebook as fb
from urllib.parse import urlparse


## Get page token to post as the page. You can skip
## the following if you want to post as yourself.
#cfg = {
#    "page_id"      : "teamprojectfacialrecognition",
#    "access_token" : "EAACJpJpzExkBANa4YyvOpwbB4xZAnpubgZBA25TFdelZByqNMrwnP1a7Keuxl2BKfOYSb6JCchGZCyGUqZAwCBPBjmOgi8DkDfe9XJqP0wtLZB6jYZAZAuDKDRyO5uDVQmVzNZC5xz1y40kZB7qn1LKMEuZALDT9ARsIWtA6AZCzfudJ9f6HcKHs4AQ9z1IX0HeD1Bg3YIQCqHDJP4kSEfSBBrr4"
#    }




#def get_api(cfg):
#    graph = fb.GraphAPI(cfg['access_token'], version='2.2')
#    xd=fb.GraphAPI.get_app_access_token(graph,'151340058874649', 'aa3404db06b8cbc000a463cee1da93d2')
#    resp = graph.get_object('me/accounts')
#    page_access_token = None
#    for page in resp['data']:
#        if page['id'] == cfg['page_id']:
#            page_access_token = page['access_token']
#    graph = fb.GraphAPI(page_access_token)
#    #return graph
#    msg = "Hello world!"
#    status = graph.put_wall_post(msg) 
#    return graph

#api = get_api(cfg)

#import facebook

#def main():
#  # Fill in the values noted in previous steps here
#  cfg = {
#    "page_id"      : "127898134710376", #100024705713078",  # Step 1
#    "access_token" : "EAACJpJpzExkBAHZCF5ZAgCxaF2hTV3B3DmCoyMhTiCPfZBCFMLVsCYDS5OHE66ZCt5ZAbzTeESNxhqNHaxYvH40F8jtUi0x1imOCvDLNtm2uTHdM6OtDOwaTM4uzxEO5u6R0uDH0U4ZB55swovGakS4OYFssISah6zn19ZAVOiXGem46aySWDaqV4AO8KZCtXeyPyISQ8MiEiyRFWZC5qPAiaNQIDdQpwkswZD"
#    }

#  api = get_api(cfg)
#  msg = "Hello, world!"
#  status = api.put_wall_post(msg)

#def get_api(cfg):
#  graph = facebook.GraphAPI(cfg['access_token'])
#  # Get page token to post as the page. You can skip 
#  # the following if you want to post as yourself. 
#  resp = graph.get_object('me/accounts')
#  page_access_token = None
#  for page in resp['data']:
#    if page['id'] == cfg['page_id']:
#      page_access_token = page['access_token']
#  graph = facebook.GraphAPI(page_access_token)
#  return graph
#  # You can also skip the above if you get a page token:
#  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
#  # and make that long-lived token as in Step 3

#if __name__ == "__main__":
#  main()




#!/usr/bin/python
# coding: utf-8

import facebook
import urllib
import urllib.parse
import subprocess
import warnings

# Hide deprecation warnings. The facebook module isn't that up-to-date (facebook.GraphAPIError).
warnings.filterwarnings('ignore', category=DeprecationWarning)


# Parameters of your app and the id of the profile you want to mess with.
FACEBOOK_APP_ID     = '151340058874649'
FACEBOOK_APP_SECRET = 'aa3404db06b8cbc000a463cee1da93d2'
FACEBOOK_PROFILE_ID = '100024705713078'


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
oauth_curl_cmd = ['curl',
                  'https://graph.facebook.com/oauth/access_token?' + urllib.parse.urlencode(oauth_args)]
oauth_response = subprocess.Popen(oauth_curl_cmd,
                                  stdout = subprocess.PIPE,
                                  stderr = subprocess.PIPE).communicate()[0]

try:
    oauth_access_token = urllib.parse.parse_qs(str(oauth_response))['access_token'][0]
except KeyError:
    print('Unable to grab an access token!')
    exit()

facebook_graph = facebook.GraphAPI(oauth_access_token)

## Try to post something on the wall.
#try:
#    fb_response = facebook_graph.put_wall_post('Hello from Python', \
#                                               profile_id = FACEBOOK_PROFILE_ID)
#    print fb_response
#except facebook.GraphAPIError as e:
#    print 'Something went wrong:', e.type, e.message
