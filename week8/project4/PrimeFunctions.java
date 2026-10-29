import java.util.Arrays;

public class PrimeFunctions {
    public static boolean IsPrime(int n) {
        // compute what to search up to
        int root = (int)(Math.sqrt(n) + 1);

        // check 2 and odd numbers for prime
        for(int i = 2; i < root; i++) {
            if (n % i == 0) {
                return false;
            }
        }

        return (n != 1);
    }

    public static int[] PrimesUpTo(int n) {
        // loop through once to determine array size
        int count = 0;
        for(int i = 2; i < n; i++) {
            if(IsPrime(i)) {
                count++;
            }
        }

        // loop throuhg a second time to fill primes
        int[] primes = new int[count];
        int idx = 0;
        for(int j = 2; j < n; j++) {
            if(IsPrime(j)) {
                primes[idx] = j;
                idx++;
            }
        }

        return primes;
    }

    public static int[] PrimeDecomposition(int n) {
        int[] posFactors = PrimesUpTo(n);

        int running = n;
        int count = 0;
        
        // loop through once to determine array size
        for(int i = 0; i < posFactors.length; i++) {
            int active = posFactors[i];
            
            while (running % active == 0) {
                running /= active;
                count++;
            }
        }

        if(count == 0 && n > 1) {
            return new int[]{n};
        }

        int[] factors = new int[count];
        
        running = n;
        int idx = 0;
        int f_idx = 0;

        // loop through once to determine array size
        while(idx < posFactors.length) {
            int active = posFactors[idx];
            
            while(running % active == 0) {
                running /= active;
                factors[f_idx] = active;
                f_idx++;
            }

            idx++;
        }


        return factors;
        
    }
}
