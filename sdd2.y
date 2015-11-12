%{
  #include<stdlib.h>
  #include<stdio.h> 
extern char* yytext;
%}
%token IF_COND OP CL OC CC statement ELSE ID FUNC INT FLOAT DOUBLE Return comma SC EQ NUM FNUM DNUM OPR
%left statement
%left Return
%left OPR

%%
Start:Type FUNC param OP S CL    {printf("Start-> Type FUNC param OP S CP\n");}
     ;

S:if_block S       	{printf("S-> if_block S\n");}
 |statement SC S           {printf("S-> statement SC S\n");}
 |Block S		{printf("S-> Block S\n");}
 |Return ID SC      	{printf("S-> Return ID SC\n");}
 |Decl SC S               {printf("S-> Decl SC S\n");}
 |EX SC S                  {printf("S-> EX SC S\n");}
 |          		{printf("S-> lambda\n");}                                 
 ;
param: OC L CC          {printf("param-> OC L CC\n");}                                 
     ;
L: Decl L1	{printf("L-> Decl L1\n");}
 |		{printf("L-> lambda\n");}                                 
 ;
L1 : comma Decl L1		{printf("L1-> comma Decl L1\n");}
   |	{printf("L1-> lambda\n");}
   ;
Block:OP S CL  {printf("Block-> OP S CP \n");}
     ;
if_block: IF_COND Block temp_if  {printf("if_block-> IF_COND Block temp_if\n");}
        ;
temp_if: ELSE Block			{printf("temp_if-> ELSE Block \n");}
       |                       {printf("temp_if-> lambda\n");}
       ;
Decl:Type ID    {printf("Decl-> Type ID \n");}
    ;
Type:INT    {printf("Type-> INT\n");} 
    |FLOAT  {printf("Type-> FLOAT\n");}
    |DOUBLE {printf("Type-> DOUBLE\n");}
    ;
EX:ID EQ EXPR  {printf("EX-> ID EQ EXPR\n");}
  ;
EXPR:EXPR OPR EXPR  {printf("EXPR-> EXPR OPR EXPR\n");}
    |ID     {printf("EXPR-> ID\n");}
    |NUM    {printf("EXPR-> NUM\n");}
    |FNUM   {printf("EXPR-> FNUM\n");}
    |DNUM {printf("EXPR-> DNUM\n");}
    ;    
%%
int yyerror(char* x){
	printf("INVALID\n");
        exit(0);
}
int main(){
        int i=yyparse();
}
