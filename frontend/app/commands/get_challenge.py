'''
Author: Laggstar
'''

import requests

async def get_chall_from_db(ctx, url):
    #{ "id" : 1, "author: : "author", "title" : "title", "challenge" : "Some challenge description"}
    return requests.get(url).content()