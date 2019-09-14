#Extract Key-Value Pairs
#curl -X POST "https://formrecognizersimen.cognitiveservices.azure.com/formrecognizer/v1.0-preview/custom/models/a3d57c4e-b813-4abc-ad06-f8608b56ec73/analyze" -H "Content-Type: multipart/form-data" -F "form=@C:\Temp\FormRecognizer\Taxi 561 26-10-2017.jpg;type=image/jpeg" -H "Ocp-Apim-Subscription-Key: d9277a7e38cd469fa4988932489a8ed4"


endpoint = "https://formrecognizersimen.cognitiveservices.azure.com/formrecognizer/"
subscription_key = d9277a7e38cd469fa4988932489a8ed4
modelID = a3d57c4e-b813-4abc-ad06-f8608b56ec73
path = C:\Temp\FormRecognizer\Taxi 561 26-10-2017.jpg
fileType = image/jpeg

curl -X POST "{$endpoint}formrecognizer/v1.0-preview/custom/models/{$modelID}/analyze" -H "Content-Type: multipart/form-data" -F "form=@{$path};type={$fileType}" -H "Ocp-Apim-Subscription-Key: {$subscription_key}"

