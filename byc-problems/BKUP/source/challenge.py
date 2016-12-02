from hacksport.problem import Challenge, File
from hacksport.operations import execute
import string
import os

class Problem(Challenge):
	#comment
	def setup(self):
		x = 1 + 1
		files = [File("index.html")]
	def generate_flag(self,random):
		m = "svchost.exe"
		return m
