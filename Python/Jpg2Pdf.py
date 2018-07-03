# Utilizes smallpdf api to convert a jpg file to a pdf file and downloads the converted file

import urllib
import json
import requests
import hashlib
import time
import warnings
import os


# suppress warnings
warnings.filterwarnings("ignore")

dir = "./JPG" # Give your path to jpf files here
print("Searcing for files in " + dir)
for root, dirs, files in os.walk(dir):
    for file in files:
        if file.endswith('.jpg'):
		        ts = time.time()
		        print("Getting url for upload for " + file)                
		        print("\n")                
		        filename = hashlib.md5(str(ts)).hexdigest() + ".jpg"
		        response = requests.get("https://files.smallpdf.com/upload-url/"+ filename, verify=False).json()
		        url = response['url']
		        print("Preparing to upload " + file)
		        print("\n")
		        with open(os.path.join(dir, file), 'rb') as fp:
		            r = requests.Request('PUT', url, data=fp.read())
		        prepped = r.prepare()
		        s = requests.Session()
		        s.verify = False
		        resp = s.send(prepped)
		        if resp.reason != 'OK':
		                print("Error in uploading file. Please try again later.")
		                quit()
		        print("Uploaded file. Preparing for download...")
		        print("\n")
		        ts = time.time()
		        taskid = hashlib.md5(str(ts)).hexdigest()
		        print 'Getting data for task id ' + taskid
		        taskUrl = 'https://task.smallpdf.com/v1/tasks/'
		        taskData = json.dumps({
		        "tool":"jpg-to-pdf",
		        "version":0,
		        "task_id":taskid,
		        "input_tokens":[filename],
		        "options":{"format":"a4","margin":"small","orientation":"auto"}})
		        t = requests.post(taskUrl, data=taskData, verify=False)
		        if t.reason != 'Created':
		                print("Error in converting file. Please try again later.")
		                quit()
		        print("\n")
		        print('Downloading the pdf file')
		        response = requests.get(taskUrl+taskid, verify=False)
		        output_file = response.json()['data']['result']['output_files'][0]
		        d_url = 'https://files.smallpdf.com/files/' + output_file
		        urllib.urlretrieve(d_url, file +".pdf")
		        print("\n")
		        print("Converted and downloaded " + file )
		        print("\n")





