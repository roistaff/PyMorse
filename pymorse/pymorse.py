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
                    '(':'-.--.', ')':'-.--.-',' ':','}
class MORSE:
    @classmethod
    def string_to_code(self,input):
        txt = str(input).upper()
        code = ""
        for s in txt:
            code += MORSEdic[s]+"_"
        code = code[:-1]
        return code
    @classmethod
    def code_to_string(self,input):
        MORSEdic2 = {v: k for k, v in MORSEdic.items()}
        code = str(input).split("_")
        txt = ""
        for s in code:
            txt += MORSEdic2[s]
        return txt
if __name__ == '__main__':
    print(MORSE.string_to_code("Hello world"))
    print(MORSE.code_to_string("...._._.-.._.-.._---_,_.--_---_.-._.-.._-.."))
