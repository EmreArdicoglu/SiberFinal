import os
from xml.dom.minidom import Element
import xmltodict
import json
import requests
parsedData=[]
port = input("Port girin : ")
url= input("URL girin: ")
script = input("Script girin :  ")
XMLoutput= "D:\\result.xml"
nmap_final = "nmap " + "-p " + port + " -oX " + XMLoutput + " --script " + script + " " + url
os.system(nmap_final)
dosya = open("D:\\result.xml")
xml_content = dosya.read()
dosya.close()
nmap_results = xmltodict.parse(xml_content)
urls = nmap_results["nmaprun"]["host"]["ports"]["port"]["script"]["@output"].replace("/n","").replace("\n","")
parsedData.append(nmap_final)
parsedData.append(urls[urls.index("http")::].split("    "))
jsonData = json.dumps(parsedData)
newLineJson=json.loads(jsonData)

print(json.dumps(newLineJson,indent=4,sort_keys=True))
breakpoint()
os.system("pause")