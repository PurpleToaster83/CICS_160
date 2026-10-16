package week6.lab4;

public class SplitBill {

    public static double splitBill(double bill, int people, double tipPercent) {
        double total = bill + bill * (tipPercent / 100.0);
        double share = total / people;
        return Math.round(share * 100) / 100.0;
    }

    public static void main(String[] args) {
        System.out.printf("%.2f%n", splitBill(50.75, 3, 25.0));
    }
}
