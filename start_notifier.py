from Notifier.notifier import *
from datetime import datetime
from mongohelper import *
from storage.storagemanager import *
import urllib.parse



new_listings = getNewListings(datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0))

for new_listing in new_listings:

    message =  f"""
    New Nasdaq Listing : <b>{new_listing['ticker']}</b>    
    Company : <b>{new_listing['company']}</b> 
    Analyst Consensus : <b>{new_listing['analystConsensus']}</b> 
    Market Cap : <b>{new_listing['marketCap']/1000000} Million</b> 
    Market Cap Group : {new_listing['marketCapGroup']} 
    Sector Name : {new_listing['sectorName']} 
    Discovered at : {new_listing['Discovered_At'].strftime('%d %b %Y %H:%M %p')}      
    Price 7 Days : 
    {new_listing['priceChartSevenDay']}
    """
    msg_sent = telegram_bot_sendtext(message)
    print(msg_sent)