########### Python Form Recognizer Train #############
from requests import post as http_post

# Endpoint URL
base_url = r"https://formrecognizersimen.cognitiveservices.azure.com/" + "/formrecognizer/v1.0-preview/custom"
source = r"https://simenstorageaccount.blob.core.windows.net/taxireceipts-training?st=2019-09-14T15%3A12%3A21Z&se=2019-09-15T15%3A12%3A21Z&sp=rl&sv=2018-03-28&sr=c&sig=QjOTS8NOxc961RZjD0%2FI%2F5zuHDUg5NxZdWc5L5iPJl0%3D"
headers = {
    # Request headers
    'Content-Type': 'image/jpeg',
    'Ocp-Apim-Subscription-Key': 'd9277a7e38cd469fa4988932489a8ed4',
}
url = base_url + "/train" 
body = {"source": source}
try:
    resp = http_post(url = url, json = body, headers = headers)
    print("Response status code: %d" % resp.status_code)
    print("Response body: %s" % resp.json())
except Exception as e:
    print(str(e))