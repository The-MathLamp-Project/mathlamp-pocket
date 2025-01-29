import lark

from mathlamp_pocket.base import calc, out_results

class CodeRunner:
    def runCodeLines(self,code:str) -> list:
        code_list = code.splitlines()
        for line in code_list:
            line_clean = line.rstrip()
            if not line_clean:
                continue
            try:
                calc(line_clean)
            except (lark.UnexpectedCharacters, lark.UnexpectedEOF) as e:
                raise Exception(e)
        return out_results