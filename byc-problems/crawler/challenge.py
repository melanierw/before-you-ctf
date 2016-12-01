from hacksport.problem import FlaskApp, File, files_from_directory
from hacksport.operations import execute
import string
import os

class Problem(FlaskApp):
	files = [File("index.html")] 
	#files = [File("index.html",0o660)] 
	files.extend(files_from_directory("templates/"))
	def generate_flag(self,random):
		return "svchost.exe"
