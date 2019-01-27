import json

with open('keys.json') as k:
    content = k.read()
    keys = json.loads(content)

folder_id = keys['ya_cloud_folder_id']
iam_token = keys['ya_iam_token']
key = keys['google_maps']
