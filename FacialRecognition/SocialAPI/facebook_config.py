import facebook as fb


# Get page token to post as the page. You can skip
# the following if you want to post as yourself.
def get_api(cfg):
    resp = graph.get_object('me/accounts')
    page_access_token = None
    for page in resp['data']:
        if page['id'] == cfg['page_id']:
            page_access_token = page['access_token']
    graph = fb.GraphAPI(page_access_token)
    return graph

cfg = {
    "page_id"      : "my_page_id",
    "access_token" : "my_access_token"
    }

api = get_api(cfg)
msg = "Hello world!"
status = api.put_wall_post(msg) 