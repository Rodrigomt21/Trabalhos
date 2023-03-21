import java.util.Scanner;
public class CalculandoEConformeFormula{
    public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int numero;
        int e;
        //entrada de dados
        do{
            System.out.println("Me de um numero inteiro positivo");
            numero = sc.nextInt();
        }while(numero <= 0);
        //System.out.println("OK, você digitou: " + numero);
        //processamento
        double E = 1;
        int denominador = 1;
        while(denominador <= numero){
            int fatorial = 1;
        for(int cont = denominador; cont > 1; cont--){
            fatorial = fatorial * cont;
        }
         E = E + 1.0 / fatorial;
            denominador++;
        }
        System.out.println(E);
        //ideia da conta= 1- 1+ 1/1!
        //2 -> 1 + 1/1! + 1/2!
    }
}