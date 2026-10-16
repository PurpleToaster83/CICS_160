package week6.lab4;

public class PasswordChecker {

    public static boolean isValidPassword(String username, String password) {
        if (password.length() < 8) {
            return false;
        }
        if (password.equals(username)) {
            return false;
        }
        if (!password.contains("!")) {
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(isValidPassword("student", "password!"));
    }
}
