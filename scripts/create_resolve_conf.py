import io
import argparse

def create_configuration_string(listLinesOfConfiguration) :
	document =""
	
	for attributeValuePair in listLinesOfConfiguration :
		document += attributeValuePair[0] + " " + attributeValuePair[1] + "\n"
		
	return (document)

# test doesn't notice if close is called before write!
def write_file(stream_to_write_to, configuration_as_string_to_write) :
	stream_to_write_to.write(configuration_as_string_to_write)
	stream_to_write_to.close()
	return()

# if __name__ == "__main__" :
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument("remote_destination", action="store")
# 	parser.add_argument("pair", action="append", destination="collection")


def parse_commandline(arguments) :

	parser = argparse.ArgumentParser()

	parser.add_argument("destination")
	parser.add_argument("-pair", action="append", nargs=2)
	return parser.parse_args(arguments)