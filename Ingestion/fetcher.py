import requests
import json
from storage.storagemanager import *

URL = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'

def getSession():
    session = requests.Session()
    session.headers.update({'User-Agent': USER_AGENT})
    session.headers.update({'Accept-Encoding': 'gzip, deflate, br'})
    return session

def getPageData(url):
    session = getSession()
    page = session.get(url).text    
    return page

def getListings():
      
    jsonResult = getPageData(URL)    
    
    if not len(jsonResult) > 0:
        raise Exception(f'Unable to fetch listings information from : {URL}')
    
    listings = json.loads(jsonResult)['data']['rows']    
    return listings
   