import urllib.request
import json
import requests
from modules import auth_keys


def recognize(input_file):
    with open(input_file, "rb") as f:
        data = f.read()

    params = "&".join([
        "topic=general",
        "folderId=%s" % auth_keys.folder_id,
        "lang=ru-RU",
        "format=lpcm",
        "sampleRateHertz=16000",
        "format=lpcm"
    ])

    url = urllib.request.Request("https://stt.api.cloud.yandex.net/speech/v1/stt:recognize/?%s" % params, data=data)
    url.add_header("Authorization", "Bearer %s" % auth_keys.iam_token)
    # url.add_header("Transfer-Encoding", "chunked")

    response_data = urllib.request.urlopen(url).read()#.decode('UTF-8')
    decoded_data = json.loads(response_data)

    if decoded_data.get("error_code") is None and decoded_data.get("result") != '':
        return decoded_data.get("result").lower()
    else:
        return None


def synthesize(text, filename):
    url = 'https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize'
    headers = {
        'Authorization': 'Bearer ' + auth_keys.iam_token,
    }

    data = {
        'text': text,
        'voice': 'zahar',
        'emotion': 'good',
        'folderId': auth_keys.folder_id,
        'format': 'lpcm',
        'sampleRateHertz': 16000,
    }

    resp = requests.post(url, headers=headers, data=data)
    if resp.status_code == 200:
        with open(filename, "wb") as f:
            f.write(resp.content)
        # raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

    return resp.status_code
