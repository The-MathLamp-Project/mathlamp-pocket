import lark

from mathlamp_pocket.base import calc

class REPL:
    def runLine(self,code:str) -> str:
        try:
            return calc(code)
        except (lark.UnexpectedCharacters, lark.UnexpectedEOF) as e:
            raise Exception(e)

    def runCodeLines(self,code:str) -> list:
        output = []
        code_list = code.splitlines()
        for line in code_list:
            line_clean = line.rstrip()
            if not line_clean:
                continue
            try:
                output.append(calc(line_clean))
            except (lark.UnexpectedCharacters, lark.UnexpectedEOF) as e:
                raise Exception(e)
        return output