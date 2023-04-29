from Keywords import *
import RickLexer
import RickParser

variables: Final[list[str]] = []
functions: Final[list[str]] = []

class Transpiler:
     def __init__(self, lexer):
          self.lexer = lexer
          self.is_main = False
          self.is_function = False
          self.indent_count = 0
          self.py_code = ""    # Python code, translated from RickRoll code

     def write(self, stmt: str):
          self.py_code += f"{'  ' * self.indent_count + stmt}\n"

     def convert(self, kw):
          if kw.tvalue in functions:
               pass
          elif kw.tvalue =='takemetourheart':
               self.write('if __name__ == "__main__":')

               self.is_main = True
               self.indent_count += 1

          elif self.indent_count == 0:
               self.is_main = False
               self.is_function = False

          elif kw.tvalue == 'ijustwannatelluhowimfeeling':
               """
                    print expr
               """

               expr = join_list(self.values[1:])
               self.write(f'print({expr}, end="")')

          elif kw.tvalue == 'give':
               """
                    let id up xpr
               """

               id = join_list(self.values[self.values.index(KW.LET.value) + 1 : self.values.index(KW.ASSIGN.value)])
               xpr = join_list(self.values[self.values.index(KW.ASSIGN.value) + 1:])
               self.write(f'{id} = {xpr}')

          elif kw.tvalue == 'andifuaskmehowimfeeling':
               """
                    if `cond`
               """

               cond = join_list(self.values[1:])
               self.write(f'if {cond}:')
               self.indent_count += 1

          elif kw.tvalue == 'thereaintnomistaking':
               self.write('try:')
               self.indent_count += 1

          elif kw.tvalue == 'iftheyevergetudown':
               self.write('except:')
               self.indent_count += 1

          elif kw == 'togetherforeverandnevertopart':
               self.write('while True:')
               self.indent_count += 1

          elif kw.tvalue == 'togetherforeverwith':
               """
                    while1 `cond`
               """

               cond = join_list(self.values[1:])
               self.write(f'while {cond}:')
               self.indent_count += 1

          elif kw.tvalue == 'desertu':
               self.write('break')

          elif kw.tvalue == 'runaround':
               self.write('continue')

          elif kw.tvalue == 'gonna':
               """
                    def `id` ARGS
               """
               id = self.values[1]
               ARGS = join_list(self.values[2:])

               self.write(f'def {id}({ARGS}):')

               self.is_function = True
               self.indent_count += 1

          elif kw.tvalue == 'whenigivemy':
               """
                    return1 `xpr` return2
               """
               xpr = join_list(self.values[1:])
               self.write(f'return {xpr}')

          elif kw.tvalue == 'saygoodbye':
               self.write('pass')
               self.indent_count -= 1

          elif kw.tvalue == 'weknowthe':
               """
                    import1 lib_name import2
               """
               self.write(f'import {self.values[1]}')

          elif kw.tvalue == 'PY:':
               self.write(join_list(self.values[1:]))


     def to_py(self):
          tok = self.lexer.get_tok()
          if self.is_main or (self.is_main == False and self.values[0] in KW_OUTSIDE_MAIN) or self.is_function:
               self.convert(tok)

def py_run(src):
     lexer = RickLexer.Lexer(src)
     transpiler = Transpiler(lexer)
     transpiler.to_py()