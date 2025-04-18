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

class NGScanner:
    def __init__(self, tokens: List[Tuple[Token,str,Callable[[Lexeme],Lexeme]]]) -> None:
        self.tokens = tokens
        self.actions = {tok.name: action for tok, _, action in self.tokens}
        named_groups = [f"(?P<{tok.name}>{regex})" for tok, regex, _ in self.tokens]
        self.master_pat = re.compile("|".join(named_groups))

    def input_string(self, input_string:str) -> None:
        self.istring = input_string
        self.pos = 0
        
    def token(self) -> Optional[Lexeme]:
        while self.pos < len(self.istring):
            match = self.master_pat.match(self.istring, self.pos)
            if not match:
                raise ScannerException(f"Unexpected char: {self.istring[self.pos]}")
            ttype = match.lastgroup
            mtext = match.group(ttype)
            self.pos = match.end()
            if ttype == "IGNORE":
                continue
            lexeme = Lexeme(Token[ttype], mtext)
            return self.actions[ttype](lexeme)
        return None

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str)
    parser.add_argument('--verbose', '-v', action='store_true')
    args = parser.parse_args()
    
    f = open(args.file_name)    
    f_contents = f.read()
    f.close()

    verbose = args.verbose

    s = NGScanner(tokens)
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
