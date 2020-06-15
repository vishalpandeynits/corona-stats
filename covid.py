import requests
import time
from datetime import date
from bs4 import BeautifulSoup

#requesting data from url
url="https://www.mohfw.gov.in/"
r=requests.get(url)
content = r.content

#parsing it by html5lib and beautifulSoup
soup = BeautifulSoup(content,'html5lib')

while True:
#title of the page
    print("Data of "+soup.title.string+"\n\n\n")

    #colecting data
    k=soup.find("section",id="state-data")
    state=[]
    for data in k.find_all("tr"):
        for k in data.find_all("td"):
            if k.string:
                state.append(k.string)
    cc=discharged=deaths=0
    print(state)
    for i in range(1,len(state)//6):
        print("State: "+state[6*i-5])
        print("      Confirmed Cases: "+state[6*i-4])
        cc += int(state[6*i-4])
        print("      Cured/Discharged/Migrated:  "+state[6*i-3])
        discharged += int(state[6*i-2])
        print("      Deaths:  "+state[6*i-2])
        deaths  += int(state[6*i-3])
        print("-------------------------------------------------------")
    print("\n\n Total No. Of Confirmed Cases:  "+str(cc))
    print("Total No. Of Discharged Cases: "+str(discharged))
    print("Total no. of deaths: "+str(deaths))
    today = date.today()
    print("As per Today's date:", today)
    time.sleep(300)
