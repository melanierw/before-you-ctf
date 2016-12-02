#from hacksport.problem import Challenge, File, files_from_directory
#from hacksport.operations import execute
#import string
#import os

#class Problem(Challenge):
#	#comment
#	def setup(self):
#		x = 1 + 1
#		files = [File("word_search.jpg")]	
#
#	def generate_flag(self,random):
#		return "matrixed"




from hacksport.problem import PHPApp, File, files_from_directory

class Problem(PHPApp):

#  files = [File("login.php")]
#  files.extend(files_from_directory("other/"))
#  files.extend(files_from_directory("."))
  files = (files_from_directory("."))
  def generate_flag(self,random):
    return "there_is_a_cookie"
