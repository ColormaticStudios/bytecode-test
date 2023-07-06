import sys
from codes import codes

variables = {}

mode = ""
mode_data = b""


def interpret(bytecode):
	bytecode = bytecode.split(codes.next.to_bytes(1, "big")) #we have to convert the integer to bytes in order for python to be happy

	if bytecode[0] != b"archkobra": #make sure this is an archkobra file
		print("this is not an archkobra file")
		sys.exit()

	for itr in bytecode:
		if itr == b"archkobra":
			continue

		if itr[0] == codes.define_variable:
			variable = itr.split(codes.equals.to_bytes(1, "big"))
			variable_name = variable[0][1:]
			variable_contents = variable[1]
			variables[variable_name] = variable_contents


		elif itr[0] == codes.run:
			if itr[1] == codes.print:
				to_print = variables[itr[2:]]
				if to_print[0] == codes.string:
					to_print = to_print[1:].decode("utf-8")
				print(to_print)

	print(variables)

#interpret(open("bytecode.ac", "rb").read())
