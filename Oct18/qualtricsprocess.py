"""Qualtrics data import and load"""
import requests
import zipfile
import json
import io, os
import sys
import csv
import mysql.connector

# Setting user Parameters
apiToken = '0eWoZUIdV3Vgud8FOhmezFLUirsBeiMYasgOxi6E'
surveyId = "SV_2nRw1ySwgxCHkfX"
fileFormat = "csv"
dataCenter = 'co1'

# Setting static parameters
requestCheckProgress = 0.0
progressStatus = "inProgress"
baseUrl = "https://{0}.qualtrics.com/API/v3/surveys/{1}/export-responses/".format(dataCenter, surveyId)
headers = {
    "content-type": "application/json",
    "x-api-token": apiToken,
}

# Step 1: Creating Data Export
downloadRequestUrl = baseUrl
downloadRequestPayload = '{"format":"' + fileFormat + '"}'
downloadRequestResponse = requests.request("POST", downloadRequestUrl, data=downloadRequestPayload, headers=headers)
progressId = downloadRequestResponse.json()["result"]["progressId"]
print(downloadRequestResponse.text)

# Step 2: Checking on Data Export Progress and waiting until export is ready
while progressStatus != "complete" and progressStatus != "failed":
    print("progressStatus=", progressStatus)
    requestCheckUrl = baseUrl + progressId
    requestCheckResponse = requests.request("GET", requestCheckUrl, headers=headers)
    requestCheckProgress = requestCheckResponse.json()["result"]["percentComplete"]
    print("Download is " + str(requestCheckProgress) + " complete")
    progressStatus = requestCheckResponse.json()["result"]["status"]

# step 2.1: Check for error
if progressStatus is "failed":
    raise Exception("export failed")

fileId = requestCheckResponse.json()["result"]["fileId"]

# Step 3: Downloading file
requestDownloadUrl = baseUrl + fileId + '/file'
requestDownload = requests.request("GET", requestDownloadUrl, headers=headers, stream=True)

# Step 4: Unzipping the file
zipfile.ZipFile(io.BytesIO(requestDownload.content)).extractall("MyQualtricsDownload")

# Step 5: Insert into mysql
conn = mysql.connector.connect(host='localhost', user='ravikumarchundi', passwd='Bangalore@3', database='test')
cursor = conn.cursor()
sql_stmt = "INSERT INTO SV_2nRw1ySwgxCHkfX (RecordedDate, ResponseId, Q1Response, Q2Response, Q3Response) \
                VALUES (%s, %s, %s, %s, %s);"
with open('MyQualtricsDownload/Customer Service APAC.csv') as f:
    reader = csv.reader(f)
    fulllist = list(reader)
    for row in range(3, len(fulllist) - 2370):
        sql_data = (fulllist[row][7], fulllist[row][8], fulllist[row][17], fulllist[row][18], fulllist[row][19])
        result = cursor.execute(sql_stmt, sql_data)
        conn.commit()
cursor.close()
conn.close()

print('Complete')
