import os
import shutil
class File_manager:
	start=os.chdir("C:\\")
	def expression(self):
		for x in os.listdir(os.getcwd()):
			print(x)
		while True:
			giris=input("\nselect file name: ")
			print("-------------------------------------------------")
			if giris in os.listdir():		
				os.chdir(giris)
				for x in os.listdir(os.getcwd()):
					print(x)
			else:
				break
			print("-------------------------------------------------")
	def delete(self):
		cvb=input("sil: ")
		if cvb in os.listdir(os.getcwd()):
			result=os.getcwd()+"/"+cvb
			shutil.rmtree(r"{}".format(result))
			print("file has deleted....")
			print("-------------------------------------------------")
	def onetimebfr(self):
		os.chdir(os.path.dirname(os.getcwd()))
		for x in os.listdir(os.getcwd()):
			print(x)
		print("-------------------------------------------------")
	def search(self):
		cvb=input("file name:  ")
		for x,y,z in os.walk(os.getcwd()):
			if x.endswith(cvb):
				print(x)
				break
while True:
	fm=File_manager()
	ans=input("1-Express\n2-Delete\n3-One walk back\n4-Search\nAnswer:  ")
	if ans=="1":
		fm.expression()
	elif ans=="2":
		fm.delete()
	elif ans=="3":
		fm.onetimebfr()
	elif ans=="4":
		fm.search()
		