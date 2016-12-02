from hacksport.problem import FlaskApp, File, files_from_directory
from hacksport.operations import execute
import string
import os

class Problem(FlaskApp):
	files = [File("templates/index.html"), File("templates/cat.jpg")]
#	files.append([File("templates/cat.jpg")])
	#files = [File("index.html",0o660)] 
	files.extend(files_from_directory("templates/"))
	def generate_flag(self,random):
		return "svchost.exe"
