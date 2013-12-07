# Define some global constants
USAGE_STR = "usage: ./nectj yourFileName"
ERR_NOFILE = "nectj: no file was passed to the interpreter."
ERR_ARGS = "nectj: too many arguments."
ERR_IO = "nectj: cannot open the file"

def handle_error(errorMsg, usageMsg):
	print errorMsg + "\n" + usageMsg + "\n"
	exit()

class NECTJInterpreter:
	"""
	A class that represents an interpreter for the programming language NECTJ.
	
	"""
	
	fileLines = "initialize"
	
	def __init__(self, fileName):
		"""
		Initializes the file that contains NECTJ code.
		
		Keyword arguments:
		fileName -- the name of the NECTJ code file
		
		"""
		
		self.file = fileName
		
		try:
			file = open(fileName[:-1], 'r')
		except IOError:
			handle_error(ERR_IO + " " + fileName, USAGE_STR)
		else:
			fileLines = file.readlines()
			file.close();
			print fileLines
	
	def RunInterpreter():
		"""
		
		"""
		AnalyzeLexicon()
		AnalyzeSyntax()
		
	def AnalyzeLexicon():
		"""
		
		"""
		
	def AnalyzeSyntax():
		"""
		
		"""
	