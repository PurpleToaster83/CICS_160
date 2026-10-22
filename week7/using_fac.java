public class using_fac {
    public static void main(String[] args) {
        System.out.println(fac_while(10));
        System.out.println(fac_for(10));
        System.out.println(fac_rec(10));
    }

    public static int fac_while(int n) {
        int prod = 1;

        while(n > 1) {
            prod *= n;
            n--;
        }

        return prod;
    }

    public static int fac_for(int n) {
        int prod = 1;

        for(int i = n; i > 1; i--) {
            prod *= i;
        }

        return prod;
    }

    public static int fac_rec(int n) {
        if (n <= 1) {
            return 1;
        }
        else {
            return n * fac_rec(n - 1);
        }
    }
}
