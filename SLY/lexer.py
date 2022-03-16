from sly import Lexer

class LittleDuck2020Lexer(Lexer):
    # Set of token names.   This is always required
    tokens = {'PROGRAM', 'INT', 'FLOAT', 'IF', 'ELSE', 'PRINT', 'VAR',
          'VAR_CTE_ID', 'VAR_CTE_INT', 'VAR_CTE_FLOAT', 'VAR_CTE_STRING',
          'PLUS', 'MINUS', 'TIMES', 'DIV', 'LESS_THAN', 'GREATER_THAN',
          'EQUAL', 'NOT_EQUAL', 'LEFT_PAR', 'RIGHT_PAR', 'LEFT_KEY',
          'RIGHT_KEY', 'COMMA', 'COLON', 'SEMI_COLON'}

    # Ignored characters
    ignore = ' \t'

   # Reserved words 
    reserved = {
        'program': 'PROGRAM',
        'int': 'INT',
        'float': 'FLOAT',
        'if': 'IF',
        'else': 'ELSE',
        'print': 'PRINT',
        'var': 'VAR'
    }

    # Identifiers and keywords
    VAR_CTE_ID = r'[A-za-z]([A-za-z]|[0-9])*'
    VAR_CTE_ID['program'] = PROGRAM
    VAR_CTE_ID['if'] = IF
    VAR_CTE_ID['else'] = ELSE
    VAR_CTE_ID['print'] = PRINT
    VAR_CTE_ID['var'] = VAR
    VAR_CTE_ID['int'] = INT
    VAR_CTE_ID['float'] = FLOAT

    # Regular expressions
    VAR_CTE_STRING = r'"(.*?)"'
    PLUS = r'\+'
    MINUS = r'\-'
    TIMES = r'\*'
    DIV = r'\/'
    LESS_THAN = r'\<'
    GREATER_THAN = r'\>'
    EQUAL = r'\='
    NOT_EQUAL = r'\<\>'
    LEFT_PAR = r'\('
    RIGHT_PAR = r'\)'
    LEFT_KEY = r'\{'
    RIGHT_KEY = r'\}'
    COMMA = r'\,'
    COLON = r'\:'
    SEMI_COLON = r'\;'

    # @_(r'[A-za-z]([A-za-z]|[0-9])*')
    # def t_VAR_CTE_ID(self, t):
    #     if t.value in reserved:
    #         t.type = reserved[t.value]
    #     return t

    @_(r'\d+')
    def VAR_CTE_INT(self, t):
        t.value = int(t.value)
        return t

    @_(r'([0-9]*[.])?[0-9]+')
    def VAR_CTE_FLOAT(t):
        t.value = float(t.value)
        return t

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    # Error handling
    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1

lexer = LittleDuck2020Lexer()