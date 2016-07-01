import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        BigInteger a = new BigInteger(s.nextLine());
        BigInteger power;
        int greatest = 0, sum;
        int n = a.intValue();
        char[] numchar;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
        {
            sum = 0;
            power = BigInteger.valueOf(i);
            power = power.pow(j);
            numchar = power.toString().toCharArray();
            for(int z = 0; z < numchar.length; z++)
            {
                sum += numchar[z] - '0';
            }
            if(sum > greatest)
                greatest = sum;
        }
        System.out.println(greatest);
    }
}