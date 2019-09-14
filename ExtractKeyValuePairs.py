########### Python Form Recognizer Analyze #############
from requests import post as http_post
import json

# Endpoint URL
base_url = r"https://formrecognizersimen.cognitiveservices.azure.com/" + "/formrecognizer/v1.0-preview/custom"
file_path = r"C:\Temp\FormRecognizer\Taxi 561 26-10-2017.jpg"
model_id = "a3d57c4e-b813-4abc-ad06-f8608b56ec73"
headers = {
    # Request headers
    'Content-Type': 'image/jpeg',
    'Ocp-Apim-Subscription-Key': 'd9277a7e38cd469fa4988932489a8ed4',
}

try:
    url = base_url + "/models/" + model_id + "/analyze" 
    with open(file_path, "rb") as f:
        data_bytes = f.read()  
    resp = http_post(url = url, data = data_bytes, headers = headers)
    print("Response status code: %d" % resp.status_code)    
    print("Response body:\n%s" % resp.json())
  
  #writing the results to a json file
    with open('C:/Users/simen.aakhus/Documents/GitHub/FormRecognizer/Results/Response.json', 'w') as json_file:
        json.dump(resp.json(), json_file)

except Exception as e:
    print(str(e))