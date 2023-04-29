from typing import Final

TT_NUM: Final = 'N' # number token type
TT_STR: Final = 'S' # string token type
TT_IDFR: Final = 'I' # identifier token type

KW_OUTSIDE_MAIN: Final = {
    'takemetourheart', 'gonna', "weknowthe"
}

DELIMITERS: Final = {
     '\n', ' ', '%','\'', '(', ')', '*',
    '+', ',', '-', '.', '/', ':',
    '<', '>', '[', ']'
}

OPERATORS: Final =  {
    '%', '(', ')', '*',
    '+', '-', '.', '/', ':',
    '<', '>', '[', ']'
}