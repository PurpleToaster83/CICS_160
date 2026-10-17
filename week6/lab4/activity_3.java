package week6.lab4;

import java.util.Scanner;

public class activity_3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //get inputs
        System.out.print("Bill amount: ");
        double bill = scanner.nextDouble();
        
        System.out.print("Tip percentage (Out of 100): ");
        int tip = scanner.nextInt();

        System.out.print("People to split between: ");
        int people = scanner.nextInt();

        System.out.println(splitTheBill(people, tip, bill));        
    }
    public static double splitTheBill(int people, int tip, double bill){
        double total = bill * (1.00 + tip/100.0);
        System.out.println(String.valueOf(total));
        double per_person = Math.round(total * 100.0/ people) / 100.0;
        return per_person;
    }
}

