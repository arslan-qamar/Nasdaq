import requests
import json
from storage.storagemanager import *

URL = 'https://www.nasdaq.com/api/v1/screener?page={page}&pageSize={pageSize}'
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
    pageIndex = 1
    pageSize = 300
    data = []

    jsonResult = getPageData(URL.format(page = pageIndex, pageSize = pageSize ))    
    
    if not len(jsonResult) > 0:
        raise Exception(f'Unable to fetch listings information from : {URL}')
    
    listings = json.loads(jsonResult)    
    total_Listings = listings['count']
    
    data.extend(listings['data'])
    listings_Fetched = 0
    listings_Fetched += len(listings['data'])
    
    while listings_Fetched < total_Listings and pageIndex < total_Listings / pageSize:
        pageIndex += 1
        jsonResult = getPageData(URL.format(page = pageIndex, pageSize = pageSize ))    
        listings = json.loads(jsonResult)    
        data.extend(listings['data'])
        listings_Fetched += len(listings['data'])
        print(f'{listings_Fetched} listings fetched. Current Page Index : {pageIndex}')
        

    return data


