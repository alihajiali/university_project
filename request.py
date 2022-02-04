from bs4 import BeautifulSoup
import requests
import time
company = {
    "khodro":"65883838195688438", 
    "khsapa":"44891482026867833", 
    "shasta":"2400322364771558", 
    "tamellat":"11129387075131725", 
    "vatejarat":"63917421733088077", 
}
def last_sell(company_name):
    name = company[company_name]
    url = "http://www.tsetmc.com/Loader.aspx?ParTree=151311&i="+name
    result = requests.get(url)
    content = BeautifulSoup(result.text, 'html.parser')
    r = content.select('script')
    first = str(r[5]).find('TradeHistory=')+16
    last = str(r[5]).find(']')-1
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()), f" --{company_name}--> ", str(r[5])[first:last].split("','")[1])

while True:
    for i in company:
        last_sell(i)
    time.sleep(3)