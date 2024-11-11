//WAP to check if the person is eligible to vote or not using throws

import java.io.IOException;
import java.util.Scanner;

public class Vote {
    public void check(String n, int age)throws IOException{
            if (age >= 18) {
                System.out.println("Eligible to vote");
            } else {
                throw new IOException("Age is less then 18");
            }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your name");
        String nm = sc.nextLine();
        System.out.println("Enter your age");
        int age = sc.nextInt();

        Vote obj = new Vote();
        try{
            obj.check(nm, age);
        }catch(Exception e){
            System.out.println("Error: "+e);
        }finally{
            System.out.println("Give age greater then 18");
        }
    }
}


// OUTPUT
// Enter your name
// satya
// Enter your age
// 10
// Error: java.io.IOException: Age is less then 18
// Give age greater then 18