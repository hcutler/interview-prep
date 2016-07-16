import java.util.Arrays;

public class Anagram {


  // sort letters in input string and return sorted string
  public static String sort(String s) {
    char[] letters = s.toCharArray();
    Arrays.sort(letters);
    return new String(letters);
  }

  // returns True if s permutation of t, False otherwise
  public static boolean permutation(String s, String t) {
    return sort(s).equals(sort(t));

  }

  public static boolean anagram(String s, String t) {
    boolean status;
    if (s.length() != t.length()) {
      status = false;
    }
    char[] s_arr = s.toCharArray();
    char[] t_arr = t.toCharArray();

    for (char i : s_arr) {
      for (char j : t_arr) {
        if (i == j) {
          status = true;
        } else {
          status = false;
        }
      }
    }
    return status;
  }


  public static void main(String[] args) {
    String [][] pairs = {{"apple", "papel"}, {"carrot", "tarroc"}, {"hello", "llloh"}};
    for (String[] pair : pairs) {
      String s1 = pair[0];
      String s2 = pair[1];

      //first check: are the strings permutations of one another?
      boolean isAnagram = permutation(s1, s2);
      System.out.println(s1 + ", " + s2 + ": " + isAnagram);

      //second check: are the strings anagrams of one another?
      System.out.println(anagram(s1, s2));

    }

  }

}