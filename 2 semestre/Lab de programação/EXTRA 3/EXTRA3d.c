#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    double tamanho, mbps, tempo;
    int horas, minutos, segundos;
    
    printf("=== CALCULADORA DE DOWNLOAD ===\n\n");
    
    // Validação do tamanho
    printf("Digite o tamanho do arquivo em Mb: ");
while (scanf("%lf", &tamanho) != 1 || tamanho <= 0) {
    if (tamanho <= 0) {
        printf("Erro! O tamanho deve ser positivo: ");
    } else {
        printf("Erro! Digite um valor numérico válido: ");
    }
    while (getchar() != '\n');
}
    
    // Validação da velocidade
    printf("\nDigite a velocidade da sua internet em Mbps: ");
    while (scanf("%lf", &mbps) != 1) {
        printf("Erro! Digite um valor numérico válido: ");
        while (getchar() != '\n'); // Limpa o buffer
    }
    
    // Previne divisão por zero
    if (mbps <= 0) {
        printf("\nVelocidade inválida! Usando 1 Mbps como padrão.\n");
        mbps = 1;
    }
    
    // Cálculo do tempo em segundos
    tempo = (tamanho / mbps) * 60; // Converte para segundos
    
    // Converte para horas, minutos e segundos
    horas = (int)(tempo / 3600);
    minutos = (int)((tempo - (horas * 3600)) / 60);
    segundos = (int)(tempo - (horas * 3600) - (minutos * 60));
    
    // Exibição dos resultados
    printf("\n=== RESULTADOS ===\n\n");
    printf("Tamanho do arquivo: %.2lf Mb\n", tamanho);
    printf("Velocidade de download: %.2lf Mbps\n\n", mbps);
    printf("Tempo estimado de download:\n");
    printf("%02d:%02d:%02d (h:m:s)\n", horas, minutos, segundos);
    
    // Versão em minutos (mais útil pra arquivos pequenos)
    if (horas == 0 && minutos < 60) {
        printf("Ou aproximadamente %.1f minutos\n", tempo / 60);
    }
    
    return 0;
}