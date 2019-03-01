import requests
from requests.auth import HTTPDigestAuth
import json
import Config
from win10toast import ToastNotifier

config = Config.Config()
toaster = ToastNotifier()

response = requests.get(config.GET_PUBLIC_STASH_TABS)
print(response.json()['next_change_id'])
#stashResponses = StashResponses.StashResponses(response.json())
toaster.show_toast("Next change ID:" ,response.json()['next_change_id'])
for stash in response.json()['stashes']:
    for item in stash['items']:
        if item['category'] is not None:
            categories = item['category']
            #print(categories)
            if 'weapons' in categories and categories['weapons'] is not None:
                for weapon in categories['weapons']:
                    if weapon == 'bow':
                        if 'note' in item and item['note'] is not None:
                            print(item['name'] + " - " + item['note'])
