from hacksport.problem import FlaskApp, File, files_from_directory
from hacksport.operations import execute
import string
import os

class Problem(FlaskApp):
	files = [File("templates/index.html")]
	files.extend(files_from_directory("templates/"))
	def generate_flag(self,random):
		return "i_wish_my_name_was_neo"
