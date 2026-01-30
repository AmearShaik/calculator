import java.util.Scanner;

class Calculator {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(a + b); // addition
        System.out.println(a - b); // subtraction
        System.out.println(a * b); // multiplication
        System.out.println(a / b); // division
    }
}
