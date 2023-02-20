MORSEdic= { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-',' ':''}
def string_to_code(input):
    txt = str(input).upper()
    code = ""
    for s in txt:
        code += MORSEdic[s]+"_"
    code = code[:-1]
    return code
def code_to_string(input):
    MORSEdic2 = {v: k for k, v in MORSEdic.items()}
    code = str(input).split("_")
    txt = ""
    for s in code:
        txt += MORSEdic2[s]
    return txt
if __name__ == '__main__':
    print(string_to_code("Hello world"))
    print(code_to_string("...._._.-.._.-.._---_,_.--_---_.-._.-.._-.."))
