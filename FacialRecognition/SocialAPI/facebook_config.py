import facebook as fb
import facebook
import json
import requests

#def get_fb_token(app_id, app_secret):           
#    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
#    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
#    #print file.text #to test what the FB api responded with    
#    result = file.text.split("=")[1]
#    #print file.text #to test the TOKEN
#    return result

URL = 'https://facebook.com/100024705713078'
oauth_access_token = requests.get(URL, auth = ('100024705713078', 'team_project'))
#graph = facebook.GraphAPI(access_token="your_token", version="2.12")


graph = facebook.GraphAPI('EAACEdEose0cBALZCNmHuVWMZB2RSEiSWGRzl6v8BtZCYH2tmDWU7ZCZB99gyZCSJ5R0ZBtpn8TeZCbCHhG982vqO9QByPrCGaCbjxNOLP70i3yG0wCUdWAQ6QFFarUyNwZAT7UbdlhGFLbEgCZBV5WUQ5ZAwpYCJsiaJP6iKG2CEdyTWZBZAZAUoZAZBqI3xrrWZBx2ERoaZBvZAnHc2N1bX01BP2hDDlvo')
photo = open("Tiger.jpg", "rb")
#graph.put_object("me", "photos", message="You can put a caption here", source=photo.read())
graph.put_object(parent_object='me', connection_name='feed', message='Fuck U Python')
photo.close()

