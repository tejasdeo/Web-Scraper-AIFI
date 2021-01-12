# import library
from bs4 import BeautifulSoup
import requests
import json

# getting the html
url = "https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=16"
page = requests.get(url, verify = False)

#parsing the html
soup = BeautifulSoup(page.text, 'html.parser')

#html tree traversal and extracting required attributes
a = soup.find_all("div", attrs={"class": "fixed-table-body card-table"})
keys = []
values = []
for li_tag in a:
    for span_tag in li_tag.find_all("div", attrs={"class":"title"}):
        field = span_tag.find('span').text
        keys.append(field)
    for span_tag1 in li_tag.find_all("div", attrs={"class":"value"}):
        value = span_tag1.find('span').text
        values.append(value)

#creating json list 
jsonList = []
for i in range(0,len(keys)):
    jsonList.append({keys[i] : values[i]})

#storing the data
with open('data.json', 'w') as f:           # inplace of .json extension, we can use .txt extension to save data as text file 
    json.dump(jsonList, f, ensure_ascii=False)

print("Scraping Complete")