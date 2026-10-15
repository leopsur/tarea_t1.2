import requests

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "d3f4bab0-c8ab-11f1-9523-87088f88f86cd7a2e203-1bea-44d4-a335-628b049885a0"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify("11,5")

label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))
