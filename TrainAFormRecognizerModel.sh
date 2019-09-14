#Train a Form Recognizer model:
curl -X POST "https://formrecognizersimen.cognitiveservices.azure.com/formrecognizer/v1.0-preview/custom/train" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key: d9277a7e38cd469fa4988932489a8ed4" --data-ascii "{ \"source\"": \"https://simenstorageaccount.blob.core.windows.net/taxireceipts?st=2019-09-13T13%3A44%3A43Z&se=2019-09-14T13%3A44%3A43Z&sp=rl&sv=2018-03-28&sr=c&sig=YwvbR2mA8T1omewRf924uAEYf9%2Fh7eNPtEimQYZkH0s%3D"\"}"

endpoint = "formrecognizersimen.cognitiveservices.azure.com/"
subscription_key = "d9277a7e38cd469fa4988932489a8ed4"
SAS_URL = "\https://simenstorageaccount.blob.core.windows.net/taxireceipts?st=2019-09-13T13%3A44%3A43Z&se=2019-09-14T13%3A44%3A43Z&sp=rl&sv=2018-03-28&sr=c&sig=YwvbR2mA8T1omewRf924uAEYf9%2Fh7eNPtEimQYZkH0s%3D"

curl -X POST "https://{$endpoint}formrecognizer/v1.0-preview/custom/train" -H "Content-Type: application/json" -H "Ocp-Apim-Subscription-Key:{$subscription_key}"  --data-ascii "{ \"source\"": \"{$SAS_URL}\"}"
