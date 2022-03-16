import sys
from sly import Parser
from lexer import LittleDuck2020Lexer

class LittleDuck2020Parser(Parser):
    debugfile = 'parser.out'
    
    # Get the token list from the lexer (required)
    tokens = LittleDuck2020Lexer.tokens

    # Grammar rules

    # PROGRAM
    @_('PROGRAM VAR_CTE_ID SEMI_COLON programa_2 bloque_1')
    def programa_1(self, p):
        return

    # VARS
    @_('vars_1',
       'empty')
    def programa_2(self, p):
        return

    @_('VAR vars_2')
    def vars_1(self, p):
        return

    @_('vars_3 COLON tipo SEMI_COLON vars_4')
    def vars_2(self, p):
        return

    @_('VAR_CTE_ID vars_5')
    def vars_3(self, p):
        return

    @_('vars_3',
       'empty')
    def vars_4(self, p):
        return

    @_('COMMA vars_3',
       'empty')
    def vars_5(self, p):
        return

    # TIPO
    @_('INT',
       'FLOAT')
    def tipo(self, p):
        return
    
    # BLOQUE
    @_('LEFT_KEY bloque_2 RIGHT_KEY')
    def bloque_1(self, p):
        return

    @_('estatuto bloque_2',
       'empty')
    def bloque_2(self, p):
        return

    # ESTATUTO
    @_('asignacion',
       'condicion_1',
       'escritura_1')
    def estatuto(self, p):
        return

    # ASIGNACION
    @_('VAR_CTE_ID EQUAL expresion_1 SEMI_COLON')
    def asignacion(self, p):
        return

    # ESCRITURA
    @_('PRINT LEFT_PAR escritura_2 RIGHT_PAR SEMI_COLON')
    def escritura_1(self, p):
        return

    @_('expresion_1 escritura_3',
       'VAR_CTE_STRING escritura_3')
    def escritura_2(self, p):
        return

    @_('COMMA escritura_2',
       'empty')
    def escritura_3(self, p):
        return

    # EXPRESION
    @_('exp_1 expresion_2')
    def expresion_1(self, p):
        return

    @_('GREATER_THAN exp_1',
       'LESS_THAN exp_1',
       'NOT_EQUAL exp_1',
       'empty')
    def expresion_2(self, p):
        return

    # EXP
    @_('termino_1 exp_2')
    def exp_1(self, p):
        return

    @_('PLUS exp_1',
       'MINUS exp_1',
       'empty')
    def exp_2(self, p):
        return

    # TERMINO
    @_('factor_1 termino_2')
    def termino_1(self, p):
        return
    
    @_('TIMES termino_1',
       'DIV termino_1',
       'empty')
    def termino_2(self, p):
        return

    # FACTOR
    @_('LEFT_PAR expresion_1 RIGHT_PAR',
       'factor_2 var_cte')
    def factor_1(self, p):
        return

    @_('PLUS',
       'MINUS',
       'empty')
    def factor_2(self, p):
        return

    # CONDICION
    @_('IF LEFT_PAR expresion_1 RIGHT_PAR bloque_1 condicion_2 SEMI_COLON')
    def condicion_1(self, p):
        return

    @_('ELSE bloque_1',
       'empty')
    def condicion_2(self, p):
        return

    # VAR_CTE
    @_('VAR_CTE_ID',
       'VAR_CTE_INT',
       'VAR_CTE_FLOAT')
    def var_cte(self, p):
        return

    # EMPTY
    @_('')
    def empty(self, p):
        pass

if __name__ == '__main__':
    lexer = LittleDuck2020Lexer()
    parser = LittleDuck2020Parser()

    if len(sys.argv) == 2:
        file = sys.argv[1]

        try:
            ifFile = open(file, 'r')
            data = ifFile.read()
            ifFile.close()
            print(parser.parse(lexer.tokenize(data)))
        except:
            print("Error opening the file!")
    else:
        print("Try running the following command: python parser.py name_of_file.txt")