import urllib.request
from bs4 import BeautifulSoup
import subprocess
import ssl
import re
ssl._create_default_https_context = ssl._create_unverified_context


cmd = "sudo /usr/local/bin/arp-scan -l --interface en0 | grep -i '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}' | tr '\t' '|' | cut -d '|' -f2 | cut -d '|' -f1"
macadd = (str(subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)).split("\n"))[0:-1]
macaddress=[]
for n in macadd:
    macaddress.append(n)

dareiru=[]
url = "URL"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
div_list=[]
flattenList=[]
count =0

for div in soup.find_all("div"):
    div_str=str(div.string)
    if(re.match("\$",div_str))!=None:
        div_str=div_str.strip("\$ ")
        div_str=div_str.split(" ")
        div_list.append(div_str)

for s in div_list:
    flattenList.extend(s)

for n in flattenList:
    if count<=len(flattenList):
        if n in macaddress:
            dareiru.append(flattenList[count+1])
    count+=1

for m in dareiru:
    print(m,end=" ")
