#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int x;
	x = 10;
	int y =20;
	
	printf("Hola mundo de programacion en C\n");
	printf("Introduce un numero entero:");
	scanf("%d",&y);
	
	printf("\tX vale: %d y Y vale : %d \a",x,y);
	if (y > 10){
		printf("\n%d es mayor que 10",y);
	}
	if (y < 10){
		printf("\n%d es menor que 10",y);
	}
	printf("\nCon if - else");
	if(y > 10){
		printf("\n%d es mayor que 10",y);
	}
	else{
		printf("\n%d e menor que 10",y);
	}
	
	printf("Intruduce un valor entero entre 1 y 5:");
	scanf("%d",&x);
	switch (x){
		case 1:
			printf("Hola\n");
				break;
		case 2:
			printf("Adios\n");
				break;
		case 3:
			printf("Hello\n");
				break;
		case 4:
			printf("Bye\n");
				break;
		case 5:
			printf("Gusten tag\n");
				break;
		case 6:
			printf("Gusten tag\n");
				break;
		default:
			printf("Opcion no valida\n");
			
	}
}
