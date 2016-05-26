import java.io.*;
import java.util.*;


public class Solution {
    
    public static boolean checkpalindrome(String a)
    {
        char[] c = a.toCharArray();
        int length = a.length();
        for(int i=0; i<=length/2; i++)
        {
            if(c[i] != c[length-1-i])
                return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int n = s.nextInt();
        int k = s.nextInt();
        int sum=0;
        for(int j=0; j<n; j++)
        {
            if(checkpalindrome(Integer.toString(j, k)) && checkpalindrome(Integer.toString(j)))
                sum += j;
        }
        System.out.println(sum);
    }
}