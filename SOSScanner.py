import re
from functools import reduce
from time import time
import argparse
import pdb
import sys
sys.path.append("../part2/")
from tokens import tokens,Token,Lexeme
from typing import Callable,List,Tuple,Optional


# No line number this time
class ScannerException(Exception):
    pass

class SOSScanner:
    def __init__(self, tokens: List[Tuple[Token,str,Callable[[Lexeme],Lexeme]]]) -> None:
        self.tokens = tokens

    def input_string(self, input_string:str) -> None:
        self.istring = input_string

    def token(self) -> Optional[Lexeme]:
        # Implement me!
        if self.istring == "":
            return None

        while self.istring and self.istring[0] in [' ','\n','\t']:
            self.istring = self.istring[1:]

        if self.istring == "":
            return None

        for token_type, regex, action in self.tokens:
            match = re.match(regex, self.istring)
            if match:
                matched_text = match.group(0)
                self.istring = self.istring[len(matched_text):]
                lexeme = Lexeme(token_type, matched_text)
                return action(lexeme)

        raise ScannerException(f"Unexpected char: {self.istring[0]}")



if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str)
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    
    f = open(args.file_name)    
    f_contents = f.read()
    f.close()

    verbose = args.verbose

    s = SOSScanner(tokens)
    s.input_string(f_contents)

    start = time()
    while True:
        t = s.token()
        if t is None:
            break
        if (verbose):
            print(t)
    end = time()
    print("time to parse (seconds): ",str(end-start))    
