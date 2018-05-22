import facebook as fb
import facebook
import json
import requests

def socialPost(frame):
    URL = 'https://facebook.com/100024705713078'
    oauth_access_token = requests.get(URL, auth = ('100024705713078', 'team_project'))
    #graph = facebook.GraphAPI(access_token="your_token", version="2.12")


    graph = facebook.GraphAPI('EAACJpJpzExkBANSjShz0GeHM5VcYtdsQsk1LmyGB2jdZAuKrRRdxlnftLowlgs2TDbkUXp0EIRXnxZB4UTQuP9QTZBDyJZAJbSKIZAPQMl5aEM7aoX7rZCZArHbZAZBwzL2TOQjfqZAC4JxajYTFSlpeyGV0nblJMn7CpckUnDGpsBOyr0YnYI9rth3IZBrBZA4BlIsIlUM3lXZBA8IGypPZBHlU7a')
    #photo = open("Tiger.jpg", "rb")
    #graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
    #graph.put_object(parent_object='me', connection_name='feed', message='Fuck U Python')
    graph.put_photo(image=frame, message="Intruder")
    #frame.close()


#socialPost(open("Tiger.jpg", "rb"))