from direct.distributed import ClientRepository
import ssl

import file

import depress
from direct.distributed import PyDatagram
from direct.distributed import PyDatagramIlterator
import webbrowser

inject = sys.argv(1)

webbrowser.cache(ssl, "www.google.com") #add google to the webbrowser module cache list.... (ssl need)
find = webbrowser.find([0], "x01Clientx02Datagramx05CODEx06OTP") # make the webbrowser find the certain inject search on google... [0] is in the cache list...
webbrowser.cache(find) #add the datagram page to the cache..
datagrampage = webbrowser.getCache([1]) #get get the datagram page in the cache.....

import p3dDownload as downloader #import pandas downloader...

downloader.downloadAddCache(datagrampage) #download it with pandas downloader and add cahce once download...

datagram = downloader.getCache([0]) #get downloaded datagram cache with variable..
datagram.addUint02(depress.initdepress())
datagram.addUint03(file.getRegistry([726])) #726 is ttrs registry key with mirai engine exe...
datagram.addStage03(depress.depressoverflow([443])) #depress the buffer overflow bytes in the dumb ttr cfsworks stupid bytecode....
datagram.addString(inject) #what the user want to inject....
datagram.sendPOSTREQ(ssl, "gameserver.toontownrewritten.com") #send it to ttrs gameserver to be inject (ssl need)
