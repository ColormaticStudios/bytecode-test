from codes import codes

def parse(code):
    bytecode = b"archkobra"

    code = code.split("\n")
    for itr in code:
        itr = itr.split(" ")
        print(itr)
        if itr[0] == "var":
            variable_contents = ""
            if itr[3][0] == "\"" and itr[3][-1] == "\"":
                variable_contents = itr[3][1:][:-1]
                print("variable contents: ", varaible_contents)
            variable_statement = codes.define_variable.to_bytes(1, "big") + itr[1].encode("utf-8") + codes.equals.to_bytes(1, "big") + variable_contents.encode("utf-8")
            bytecode = bytecode + codes.next.to_bytes(1, "big") + variable_statement

    return bytecode
