public class PalindromeChecker {
    public static void main(String[] args) {
        String str = "довод"; // текст для проверки палиндрома

        if (isPalindrome(str)) {
            System.out.println("Строка является палиндромом.");
        } else {
            System.out.println("Строка не является палиндромом.");
        }
    }

    public static boolean isPalindrome(String str) {
        str = str.replaceAll("[^a-zA-Zа-яА-Я0-9]", "").toLowerCase();
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}