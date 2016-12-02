from hacksport.problem import Challenge, File
from hacksport.operations import execute
import string
import os

class Problem(Challenge):
	#comment
	def setup(self):
		x = 1 + 1
		files = [File("word_search.jpg")]	

	def generate_flag(self,random):
		return "matrixed"
