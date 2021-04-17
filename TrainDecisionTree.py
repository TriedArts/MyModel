from odata import ODataService # CONNECT TO PYRAMID USE THIS LIBRARY https://github.com/tuomur/python-odata
from requests.auth import HTTPBasicAuth # SUPPORT BASIC AUTHENTICATION
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn import tree
import joblib
import pandas as pd
from urllib.request import urlopen

my_auth = HTTPBasicAuth("USERNAME","PASSWORD") # APPLY CREDENTIALS FOR PRODUCTION GRADE USE, USE TECHNOLOGY TO ENCRYPT PASSWORDS
#PYRAMID ODATA FEED URL:
url = "https://PYRAMID_SERVER_ODATA_FEED_URL"
Service = ODataService(url,reflect_entities=True, auth=my_auth)
#DISCOVER REPORT ITEM ID
Entity = Service.entities['ITEM_ID']

result = Service.query(Entity)
target = []
data = []

observ_result = []
dataDict = {}
i = 0
j = 0
for Entity in result:
    target.append(Entity.CUSTOMER_CLASS)
    data.append([Entity.GENDER, Entity.FLAG_MOBIL, Entity.OWN_CAR, Entity.OWN_REALTY,\
                 Entity.FLAG_PHONE, Entity.FLAG_WORK_PHONE, Entity.EDUCATION_TYPE, Entity.FAMILY_STATUS,\
                 Entity.HOUSING_TYPE, Entity.INCOME_TYPE, Entity.OCCUPATION, Entity.AMT_INCOME_TOTAL,\
                 Entity.CNT_FAM_MEMBERS, Entity.DAYS_BIRTH, Entity.DAYS_EMPLOYED])

#START DATA SCIENCE HERE
decisionTree = DecisionTreeClassifier(random_state=0)
model = decisionTree.fit(data,target)

print(joblib.dump(model, "model.pkl"))
print("Done")

#gitModel = joblib.load(urlopen("https://raw.githubusercontent.com/TriedArts/MyModel/main/model.pkl"))
#k = 0
#prediction = {}
#for aObservation in df.values.tolist():
    #ID = aObservation.pop(0)
    #observation = []
    #observation.append(aObservation)
    #PreDictCustClass = gitModel.predict(observation)
    #prediction[k] = {"ID":ID,"PREDICTED_CUSTOMER_CLASS":PreDictCustClass[0]}
    #k += 1

#resDF = pd.DataFrame.from_dict(prediction, orient='index')
#print(resDF)
