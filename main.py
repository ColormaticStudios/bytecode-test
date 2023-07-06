import bytecode_interpreter as bc
import parser

bytecode = parser.parse(open("source.ac", "rt").read())
#bc.interpret(open("bytecode.acc", "rb").read())
bc.interpret(bytecode)
