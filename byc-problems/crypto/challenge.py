from hacksport.problem import Challenge
from hacksport.operations import execute
import string
import os

class Problem(Challenge):
	#comment
	def setup(self):
		x = 1 + 1

	def generate_flag(self,random):
		return "encryptception"
