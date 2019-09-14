########### Python Form Recognizer Train #############
from requests import post as http_post

# Endpoint URL
base_url = r"https://formrecognizersimen.cognitiveservices.azure.com/" + "/formrecognizer/v1.0-preview/custom"
source = r"https://simenstorageaccount.blob.core.windows.net/taxireceipts?st=2019-09-13T13%3A44%3A43Z&se=2019-09-14T13%3A44%3A43Z&sp=rl&sv=2018-03-28&sr=c&sig=YwvbR2mA8T1omewRf924uAEYf9%2Fh7eNPtEimQYZkH0s%3D"
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