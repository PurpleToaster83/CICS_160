package week6.lab4;

import java.util.Scanner;

public class TemperatureChecker {

    public static double averageAboveFreezing(int numTemps, Scanner input) {
        double[] temps = new double[numTemps];
        for (int i = 0; i < numTemps; i++) {
            temps[i] = input.nextDouble();
        }

        int daysAbove = 0;
        double sum = 0;
        for (int i = 0; i < temps.length; i++) {
            if (temps[i] > 32) {
                daysAbove++;
                sum += temps[i];
            }
        }

        System.out.println("Days above freezing: " + daysAbove);
        return sum / daysAbove;
    }

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int numTemps = input.nextInt();
        System.out.println("Average: " + averageAboveFreezing(numTemps, input));
        input.close();
    }
}
