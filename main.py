def Add(val):
    delimiters = [",","\n"]
    result = 0; exception = []
    if val == "":
        return 0
    if val[:2] == "//" and len(val) > 4:
        delimiters[0] = val[2:val.index("\n")]
        val = val[4:]
    for x in val.split(delimiters[0]):
        for y in x.split(delimiters[1]):
            if y and int(y) > -1:
                result += int(y)
            elif y and int(y) < 0:
                exception.append(y)
    if len(exception) > 0: raise Exception("negatives not allowed - {}".format(", ".join(exception)))
    return result


assert Add("") == 0, "Test case 1 failed"
assert Add("1") == 1, "Test case 2 failed"
assert Add("1,2") == 3, "Test case 3 failed"
assert Add("1,2,3,4,5") == 15, "Test case 4 failed"
assert Add("1 \n2,3") == 6, "Test case 5 failed"
assert Add("//;\n1;2") == 3, "Test case 6 failed"
