%{
   #include"y.tab.h"
   #include<string.h>
 
%}//?tokens was not copied..no no..i had copied..it came no?no..invalid it seems..
%%
if\([^\)]*\) {printf("IF_COND-> %s\n",yytext);return IF_COND;}
else {printf("ELSE-> %s\n",yytext);return ELSE;}
int {printf("INT-> %s\n",yytext);return INT;}
float {printf("FLOAT-> %s\n",yytext);return FLOAT;}
double {printf("DOUBLE-> %s\n",yytext);return DOUBLE;}
return/" "[a-z]; {printf("Return-> %s\n",yytext);return Return;}
[a-z]/[;,)=+\-*/] {printf("ID-> %s\n",yytext);int ch=*yytext;return ID;}
";" {printf("SC-> ;\n");return SC;}
"{"  {printf("OP-> %s\n",yytext);return OP;}
"}" {printf("CP-> %s\n",yytext);return CL;}
"(" {printf("OC-> (\n");return OC;}
")" {printf("CC-> )\n");return CC;}
"," {printf("comma-> ,\n");return comma;}

func[0-9a-z]*/\( {printf("FUNC-> %s\n",yytext);return FUNC;}

[0-9]+/[;+\-*/] {printf("NUM-> %s\n",yytext);return NUM;} 
[0-9]+"."[0-9]+f/[;+\-*/] {printf("FNUM-> %s\n",yytext);return FNUM;} 
[0-9]+"."[0-9]+/[;+\-*/] {printf("DNUM-> %s\n",yytext);return DNUM;}
[+\-*/] {printf("OPR-> %s\n",yytext);return OPR;} 
= {printf("EQ-> %s\n", yytext); return EQ;}
[^;{}\n=+*\-/ ]*/; {printf("statement-> %s\n",yytext);return statement;}
"\n" {}
. {}
%%
int yywrap(){
return 1;
}
