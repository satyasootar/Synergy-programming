/*WAP to create a class PerformTask to perform the following task:
 * 1.To check the number is pallindrome or not.
 * 2.To check the number is prime or not
 * 3.Print n terms of fibonacci series.
 * 4.To print the factorial of a number
 */

import java.util.Scanner;

public class PerformTask {
    public void Pallindrome(int n){
        int rev = 0;
        int m = n;

        while(n>0){
            int r = n % 10;
            rev =(rev * 10) + r;
            n = n/10; 
        }
        if(rev == m){
            System.out.println("The number is pallindrome");

        }else{
            System.out.println("The number is not pallindrome");
        }
    }

    public void Prime(int n) {
        if (n <= 1) {
            System.out.println("Neither prime nor composite");
            return;
        }
    
        boolean isPrime = true;
    
        for (int i = 2; i <= n / 2; i++) {
            if (n % i == 0) {
                isPrime = false;
                break;
            }
        }
    
        if (isPrime) {
            System.out.println("prime");
        } else {
            System.out.println("composite");
        }
    }
    

    public void Fibo(int n){
        int a = 0 , c,  b = 1 , i =2;
        System.out.print("Fibonacci:");
        System.out.print(a);
        System.out.print(b);
        do {
            c = a+b;
            System.out.print(c);
            a=b;
            b = c;
            i++;
        } while (i < n);
        System.out.println();
    }

    public void Fact(int n){
        long f = 1;
        for (int i = 1; i <= n; i++) {
            f = f* i;
        }

        System.out.println("Factorial:"+ f);
    }


    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            sc = new Scanner(System.in);
            System.out.println("Enter a number:");
            int n = sc.nextInt();

            PerformTask p = new PerformTask();
            p.Pallindrome(n);
            p.Prime(n);
            p.Fibo(n);
            p.Fact(n);
        
    }
  }

/* Enter a number
  11
  The number is pallindrome
  prime
  Fibonacci:011235813213455
  Factorial:39916800
*/
