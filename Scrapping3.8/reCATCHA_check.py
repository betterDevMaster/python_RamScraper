# python -m pip install beautifulsoup4
# python -m pip install requests
# python -m pip install --upgrade lxml
# python -m pip install cssselect

from bs4 import BeautifulSoup
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask
import requests
import csv
import time
import os

# Change the url for checking the reCATCHA)
source = requests.get('https://www.georgiamls.com/real-estate/search-action.cfm?gtyp=loc&typ=sd&cnty=&city=&ln=&address=&sch=&zip=30075&subd=&lpl=&lph=&br=0&baf=0&button1id=', headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}).text

print(source)
