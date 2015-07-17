
import ClientRepository #TO BE ADDED
import ssl #SSL CONNECT FOR MIRAI

import depress #depressing module for decomppression...

import file

import webbrowser

webbrowser.cache(ssl, "www.google.com") #add google to the webbrowser module cache list.... (ssl need)
find = webbrowser.find([0], "x01Clientx02Datagramx06OTP") # make the webbrowser find the certain search on google... [0] is in the cache list...
webbrowser.cache(find) #add the datagram page to the cache..
datagrampage = webbrowser.getCache([1]) #get get the datagram page in the cache.....

import p3dDownload as downloader #import pandas downloader...

downloader.downloadAddCache(datagrampage) #download it with pandas downloader and add cahce once download...

datagram = downloader.getCache([0]) #get downloaded datagram cache with variable..
datagram.addUint02(depress.initdepress())
datagram.addUint03(file.getRegistry([726])) #726 is ttrs registry key with mirai engine exe...
datagram.addStage03(depress.depressbytes([672])) #depress the right amount of bytes in cfsworks dumb mirai bytecode....
datagram.addString(".") #this is good for pyc decompile
datagram.sendPOSTREQ(ssl, "gameserver.toontownrewritten.com") #send it to ttrs gameserver (ssl need)

source = datagram.getFROMPOSTREQ() #variable for getting the response returned from ttrs gameesrver which should be code..
dir = downloader.downloadAddCache(source) #download the source and add it to cache for file..
file.open(dir) #open downloaded source...
