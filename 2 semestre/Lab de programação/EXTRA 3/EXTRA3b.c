#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double tempo, hh, mm, ss;

    printf("===CONVERSOR DE TEMPO DECIMAL===\n\n");
    printf("Digite um valor de tempo decimal. (Ex.: 10.87): " );
    scanf("%lf", &tempo);

    hh = floor(tempo);
    mm = (tempo - floor(tempo)) * 60;
    ss = (mm - floor(mm)) * 60;

    printf("\n\n===RESULTADOS===\n\n");
    printf("Tempo digitado: %lf\n", tempo);
    printf("Tempo convertido:\n\n");
    printf("%.0lf:%.0lf:%.0lf\n", hh, mm, ss);

    return 0;

}
