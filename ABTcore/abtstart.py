#!/usr/bin/python
import os, sys, signal 
from time import sleep
import abtserver.rpc_main
import shutil


if __name__ == "__main__":
	
	try:
		if os.path.exists("/ABT/abt") == False: # check for abt directory , if false then 
			try:
				print "creating abt and db directory and copying places.db to abt"
				os.mkdir("/ABT/abt") # create abt directory and db to host all databases
				os.mkdir("/ABT/abt/db") # create abt directory and db to host all databases
				os.mkdir("/ABT/abt/export")
				
				if os.path.exists("/ABT/ABTcore/src/places.db") == True:
					print "coping palces.db"
					try:
						shutil.copy2("/ABT/ABTcore/src/places.db","/ABT/abt/places.db") # copy places.db from /src to abt
					except:
						print "could not copy places.db"
					try:
						os.system("mv /ABT/ABTcore/doc /ABT/abt/doc")
					except:
						print "can't move doc folder"
				
			except:
				if os.path.exists("/ABT/abt/doc") == False:
					print "cannot move doc"
					os.system("mv /ABT/ABTcore/doc /ABT/abt/doc")
				else:
					print "can't move directory somthing is wrong"

		else:
		 	if os.path.exists("/ABT/abt/db") == False: # check for abt/db directory , if false then
				try:
					#print "creating db directory and copying places.db esle "
					os.mkdir("/ABT/abt/db")
					os.mkdir("/ABT/abt/export")
					if os.path.exists("/ABT/ABTcore/src/places.db") == True:
                                                
						print "coping palces.db"
						try:
							shutil.copy2("/ABT/ABTcore/src/places.db","/ABT/abt/places.db") # copy places.db from /src to abt
						except:
							print "could not copy places.db"
						try:
							os.system("mv /ABT/ABTcore/doc /ABT/abt/doc")
						except:
							print "can't move doc folder"
					
				except:
					if os.path.exists("/ABT/abt/doc") == False:
						print "moving doc"
					
						os.system("mv /ABT/ABTcore/doc /ABT/abt/doc")
					else:
						print "can't move directory somthing is wrong"
			else:
				print "db already exist"
				
			print "abt already exist"
		
		abtserver.rpc_main.runabt()
		
	except:
		print "inside exception"
	
