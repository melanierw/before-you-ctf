from hacksport.problem import PHPApp, File, files_from_directory

class Problem(PHPApp):

  files = (files_from_directory("."))
  def generate_flag(self,random):
    return "i_will_take_the_code_pill"
