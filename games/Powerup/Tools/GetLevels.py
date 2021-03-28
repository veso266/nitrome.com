import os #to be able to create directory and work with files

def Py2():
	import hashlib #To create out MD5
	import urllib2 #import URLlib library for python2
	import time #we need to sleep :)
	class Python2():
		
		global Directory #make this accessible from everywhere
		global Game_ID #make this accessible from everywhere
		global Level_ID #make this accessible from everywhere
		global NumberOfLevels #make this accessible from everywhere
		Directory = "levels" #our DIR name
		Game_ID = "powerup" # Name of the Game
		Level_ID = "rumble" #LevelID
		NumberOfLevels = 32 #LevelID
		
		if not os.path.isdir(Directory): #os.pazh.isdir because it will only return true if Directory exists while os.path.exists will also do it on a file
			os.makedirs(Directory)
		
		def GenerateLevelName(main, LevelNumber):
			leading_zero = False #I don't know what this is for if it is true maybe timelapse levels??
			leading_zeroNum = "" #I don't know what this is for if it is true maybe timelapse levels??
			if leading_zero:
				if LevelNumber < 10:
					leading_zeroNum = "0"
		
			level_id = Level_ID; #Its the same for all levels (15 levels there is)
			hash = hashlib.md5() #Select MD5 as hashing algorithm
			hash.update(level_id + leading_zeroNum + str(LevelNumber)) #we update the hash with our own string otherwise hash would just be (d41d8cd98f00b204e9800998ecf8427e)
			return hash.hexdigest()
		def Download(main, url, file_name):
			try:
				data = urllib2.urlopen(url + file_name) #open request with filename
				file = open(Directory + '/' + file_name, "wb") #open file for write and tell it the file is in binary
				file.write(data.read()) #we read the data out
				file.close() #write that
		
			except urllib2.HTTPError, e:
				print "HTTP Error:",e.code , url
			except urllib2.URLError, e:
				print "URL Error:",e.reason , url
		
	#Initiate Python class
	_Python2 = Python2()
	
	print("Downloading Block Definitions")
	_Python2.Download('http://cdn.nitrome.com/games/' + Game_ID + '/levels/','blockdefs.xml') #Download(url, file_name)
	
	print("Downloading Title Screen")
	_Python2.Download('http://cdn.nitrome.com/games/' + Game_ID + '/levels/','title_screen.xml') #Download(url, file_name)
	
	for i in range (1,NumberOfLevels):
		_Python2.Download('http://cdn.nitrome.com/games/' + Game_ID + '/levels/', _Python2.GenerateLevelName(i) + '.xml') #Download(url, file_name)
		time.sleep(1) #Sleep for 1 second just in case
		print "Level " + str(i) + " Downloaded" 
	

def Py3():
	print("NotImplemented")
	#class Python3():
		#def __init__():
		#	import urllib2
		
		#print ("Python3")
		#urllib2.urlretrieve ("http://www.example.com/songs/mp3.mp3", "mp3.mp3")


# RUNTIME VERSION CHECK #
import sys

if sys.version_info <= (3, 0):
	Py2()
else:
	Py3()

# RUNTIME VERSION CHECK #	