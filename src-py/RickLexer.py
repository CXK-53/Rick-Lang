from Keywords import *
import Helpers

ALL_KW = "ijustwannatelluhowimfeeling,andifuaskmehowimfeeling,\
give,up,weknowthe,andweregonnaplayit,gonna,whenigivemy,itwillbecompletely,\
thereaintnomistaking,iftheyevergetudown,takemetourheart,saygoodbye,desertu,\
runaround,togetherforeverandnevertopart,togetherforeverwith,isgreaterthan,\
islessthan,isgreaterthanorequalto,islessthanorequalto,aint,is,py:"

class Token:
     def __init__(self, ttype, tvalue):
          self.ttype = ttype
          self.tvalue = tvalue
     def __str__(self):
          return f"Token({self.ttype}: {self.tvalue})"


class Lexer:
     def __init__(self, src):
          self.src = src
          self.idx = 0 # index of which line is reading of self.src
          self.line_cnt = 0 # number of lines/line count
          self.last_idfr = ""

     def get_tok(self) -> Token:
          current_tok = ""
          
          while self.idx < len(self.src):
               ch = self.src[self.idx]
               if ch == '#': # skip comments
                    self.idx += 1
                    while self.src[self.idx] != '\n' and self.idx < self.src:
                         self.idx += 1
               elif ch == '\n':
                    self.line_cnt += 1
               elif ch >= '0' and ch <= '9':
                    while self.idx < len(self.src) and self.src[self.idx] >= '0' and self.src[self.idx] <= '9':
                         current_tok += self.src[self.idx]
                         self.idx += 1
                    self.idx += 1
                    return Token(TT_NUM, current_tok)
               elif ch == '"': # lexicalize string
                    self.idx += 1
                    while self.idx < len(self.src) and self.src[self.idx] != '"':
                         current_tok += self.src[self.idx]
                         self.idx += 1

                    # parse string
                    self.idx += 1
                    return Token(TT_STR, current_tok) # update buffer
               elif (ch >= 'A' and ch <= 'Z' or ch >= 'a' and ch<='z') or ch=='_':
                    """
                    TODO: while ... : if src[idx + 1] != ',': idx += 1, current_tok += src[idx]
                    """
                    while self.idx < len(self.src) and current_tok in ALL_KW:
                         if self.src[self.idx] not in DELIMITERS:
                              if current_tok + self.src[self.idx] not in ALL_KW:
                                   return Token(TT_IDFR, current_tok)
                              current_tok += self.src[self.idx]
                         # print(current_tok + f"[{self.idx}]")
                         self.idx += 1


                    return Token(TT_IDFR, current_tok)


               self.idx += 1