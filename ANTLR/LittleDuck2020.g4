grammar  LittleDuck2020;

/* Parser */
programa_1: PROGRAM VAR_CTE_ID SEMI_COLON programa_2 bloque_1;

programa_2: vars_1
          | 
          ;

vars_1: VAR vars_2;

vars_2: vars_3 COLON tipo SEMI_COLON vars_4;

vars_3: VAR_CTE_ID vars_5;

vars_4: vars_2
      | 
      ;

vars_5: COMMA vars_3
      | 
      ;

tipo: INT
    | FLOAT
    ;

bloque_1: LEFT_KEY bloque_2 RIGHT_KEY;

bloque_2: estatuto bloque_2
        | 
        ;

estatuto: asignacion
        | condicion_1
        | escritura_1
        ;

asignacion: VAR_CTE_ID EQUAL expresion_1 SEMI_COLON;

escritura_1: PRINT LEFT_PAR escritura_2 RIGHT_PAR SEMI_COLON;

escritura_2: expresion_1 escritura_3
           | VAR_CTE_STRING escritura_3
           ;

escritura_3: COMMA escritura_2
           | 
           ;

expresion_1: exp_1 expresion_2;

expresion_2: GREATER_THAN exp_1
           | LESS_THAN exp_1
           | NOT_EQUAL exp_1
           | 
           ;

exp_1: termino_1 exp_2;

exp_2: PLUS exp_1
     | MINUS exp_1
     | 
     ;

termino_1: factor_1 termino_2;

termino_2: TIMES termino_1
         | DIV termino_1
         | 
         ;

factor_1: LEFT_PAR expresion_1 RIGHT_PAR
        | factor_2 var_cte
        ;

factor_2: PLUS
        | MINUS
        | 
        ;
    
condicion_1: IF LEFT_PAR expresion_1 RIGHT_PAR bloque_1 condicion_2 SEMI_COLON;

condicion_2: ELSE bloque_1
           | 
           ;

var_cte: VAR_CTE_ID
       | VAR_CTE_INT
       | VAR_CTE_FLOAT
       ;

/* Lexer */
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
LESS_THAN: '<';
GREATER_THAN: '>';
NOT_EQUAL: '<>';
EQUAL: '=';
LEFT_PAR: '(';
RIGHT_PAR: ')';
LEFT_KEY: '{';
RIGHT_KEY: '}';
COMMA: ',';
COLON: ':';
SEMI_COLON    : ';';
INT: 'int';
FLOAT: 'float';
IF: 'if';
ELSE: 'else';
VAR: 'var';
PRINT: 'print';
PROGRAM: 'program';
VAR_CTE_ID: [A-za-z]([A-za-z]|[0-9])* ;
VAR_CTE_INT: '\d+';
VAR_CTE_FLOAT: ([0-9]*[.])?[0-9]+;
VAR_CTE_STRING: '"(.*?)"';
WHITESPACE: [ \t\r\n]+ -> skip ;