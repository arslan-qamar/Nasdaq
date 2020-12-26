from Notifier.notifier import *
from datetime import datetime
from mongohelper import *
from storage.storagemanager import *
import urllib.parse



new_listings = getNewListings(datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0))

for new_listing in new_listings:

    message =  f"""
    New Nasdaq Listing : <b>{new_listing['symbol']}</b>    
    Company : <b>{new_listing['name']}</b> 
    Last Price : <b>{new_listing['lastsale']}</b>    
    Market Cap : <b>{float(new_listing['marketCap'])/1000000} Million</b>
    Net Change : {new_listing['netchange']}
    Percentage Change : {new_listing['pctchange']}
    Industry : {new_listing['industry']} 
    Sector Name : {new_listing['sector']} 
    IPO Year : {new_listing['ipoyear']} 
    Discovered at : {new_listing['Discovered_At'].strftime('%d %b %Y %H:%M %p')}
    """
    msg_sent = telegram_bot_sendtext(message)
    print(msg_sent)