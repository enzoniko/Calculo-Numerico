clc
clear
format long
x = 2;

%digitos_precisos = 16;
for i = 1:16
  termos = 1;
  soma = 1;
  num = 1;
  fat = 1;
  anterior = 0;
  diferenca = abs(soma - anterior);
  digitos_precisos = i;
  while (diferenca > 10^-digitos_precisos)
    num = num*x;
    fat = fat*termos;
    anterior = soma;
    soma = soma + (num/fat);
    diferenca = abs(soma - anterior);
    % pause
    termos = termos + 1;
  endwhile
  soma
  digitos_precisos
  termos
  termos - digitos_precisos
endfor
