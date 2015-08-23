TTR_DIRECTORY="/Users/USER/Library/Applicaion Support/Toontown Rewritten/Toontown“

cd $TTR_DIRECTORY

# This will take some time, so be patient
 rsync -rav rsync://denver-1.download.toontownrewritten.com/ttr_win32/ 
# Once its complete, add a # infront of this line ^

echo --------------------------------------------------------------------------------
echo Toontown Rewritten: Dev
echo Give me a second to start.    
echo --------------------------------------------------------------------------------

echo Setting Gameserver and cookie.
echo --------------------------------------------------------------------------------

export DYLD_LIBRARY_PATH=`pwd`/Libraries.bundle
export TTR_PLAYCOOKIE=Brian
export TTR_GAMESERVER=86.0.229.42

echo Game server and cookie set! Starting the game.
echo --------------------------------------------------------------------------------
