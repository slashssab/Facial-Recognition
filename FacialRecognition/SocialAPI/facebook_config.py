import facebook as fb
import facebook
import json
import requests


URL = 'https://facebook.com/100024705713078'
oauth_access_token = requests.get(URL, auth = ('100024705713078', 'team_project'))
#graph = facebook.GraphAPI(access_token="your_token", version="2.12")


graph = facebook.GraphAPI('EAACJpJpzExkBAGzXUcCuKDyMzCEJmhFbMOlWjfeUX7J2LQ6I53caX9IR2ewO23nK53ZCuz0n8BP5NVZC0u8FuozojTVQuZCxZCBwv2Cc4ZCIwOOaF4WZC9eK8NmV25WTZBcuaQgpTyaDL2q6DmvjBztaDbUotcfcJV5GvVhFlteeZCEfBZAKr9jj5HTiZB0gjc1vQUtpZANvtjwKZCWHfrBBwT4S')
photo = open("Tiger.jpg", "rb")
#graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
#graph.put_object(parent_object='me', connection_name='feed', message='Fuck U Python')
graph.put_photo(image=open("./zdj.jpg",'rb').read(), message='Last update')
photo.close()

