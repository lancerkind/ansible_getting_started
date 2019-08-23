import unittest
import create_resolve_conf
import io
import argparse

class TestCreateResolveConf(unittest.TestCase) :

	def test_add_single_entry(self) :
		attribute = "nameserver"
		value ="127.0.0.1"
		self.assertEqual(attribute + " " + value +"\n", create_resolve_conf.create_configuration_string([(attribute, value)]))

	def test_add_another_entry(self) :
		attribute1 = "nameserver"
		value1 = "1.0.0.5"

		self.assertEqual(attribute1 + " " + value1 + "\n", create_resolve_conf.create_configuration_string([(attribute1, value1)]))

	def test_add_two_entry(self) :
		attribute1 = "nameserver"
		value1 = "1.0.0.5"
		attribute2 = "search"
		value2 = "arbitrary.foo"

		self.assertEqual(attribute1 + " " + value1 + "\n" 
			+ attribute2 + " " + value2 + "\n", create_resolve_conf.create_configuration_string([(attribute1, value1),(attribute2, value2)]))


	def test_write(self) :
		class ClosableStringIO(io.StringIO) :
			closed=False

			def close(self, paramater=None) :
				self.closed=True
		
		stringio = ClosableStringIO("","\n")
		configuration_as_string = "something arbitrary"

		create_resolve_conf.write_file(stringio, configuration_as_string)

		self.assertTrue(stringio.closed)
		self.assertEqual(configuration_as_string, stringio.getvalue())

	def test_experiment_with_member_overloading(self) :
		class Super :
			member = True

		class Sub(Super) :
			member = False
		
		super = Super()
		sub = Sub()

		self.assertTrue(super.member)
		self.assertTrue(not sub.member)

	def test_arguments_of_only_destination(self) :
		arguments = ["/path/to/destation"]
		
		result = create_resolve_conf.parse_commandline(arguments)
		self.assertEqual(argparse.Namespace(destination=arguments[0], pair=None), result)

	def test_arguments_of_destination_and_one_pair(self) :
		arguments = ["/path/to/destination", "-pair", "arbitrary.com", "10.0.0.1"]
		
		result = create_resolve_conf.parse_commandline(arguments)
		self.assertEqual(argparse.Namespace(destination=arguments[0], pair=[["arbitrary.com", "10.0.0.1"]]), result)

	def test_arguments_of_destination_and_two_pairs(self) :
		arguments = ["/path/to/destination", "-pair", "arbitrary.com", "10.0.0.1", "-pair", "another.arbitrary.com", "6.6.0.1"]
		
		result = create_resolve_conf.parse_commandline(arguments)
		self.assertEqual(argparse.Namespace(destination=arguments[0], pair=[["arbitrary.com", "10.0.0.1"], ["another.arbitrary.com", "6.6.0.1"]]), result)

	def xtest_experiment_with_overloading(self) :
		# can't do the below
		def method() :
			return "no argument"

		def method(name) :
			return name

		def method(name1, name2):
			return name1 + name2

		self.assertEqual("no argument", method())
		serf.assertEqual("bob", method("bob"))

	def xtest_expirementWithStream(self) :
		stringio = io.StringIO("","\n")
		stringio.write("test")
		self.assertEqual("test", stringio.getvalue())

	def xtest_expirementWithIterateTuple(self) :
		tuple = [("hi", "there"), ("you", "guys")]

		def printTuple(tuple) :
			print("iterate")
			buffer = ""
			
			for item in tuple :
				buffer += "time: " + item[0] + " " + item[1]
			print(buffer)

		printTuple(tuple)
		var1 ="my"
		var2 = "dog"
		printTuple( [(var1, var2)] )


if __name__ == '__main__': unittest.main()
