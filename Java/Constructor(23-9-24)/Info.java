//WAP to accept name, age, roll no of a student. Initialise it using a constructor and explictly using a getData() method & display it.

import java.util.Scanner;

public class Info {
    String nm;
    int age,roll;

    public Info(){}

    public Info(String nm, int age, int roll){
        this.nm = nm;
        this.age = age;
        this.roll = roll;
    }

    public void getData(String nm, int age, int roll){
        this.nm = nm;
        this.age = age;
        this.roll = roll;
    }

    public void display(){
        System.out.println();
        System.out.println("Name: "+ nm + "\nRoll: "+ roll +"\nAge: "+age);
    }


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = sc.nextLine();

        System.out.print("Enter your Roll number: ");
        int roll = sc.nextInt();

        System.out.print("Enter your age: ");
        int age = sc.nextInt();

        Info obj = new Info(name, age , roll);
        Info k = new Info();
        
        k.getData(name, age, roll);
        obj.display();
        k.display();
    }
}


// Output
// Enter your name: satya
// Enter your Roll number: 51
// Enter your age: 19

// Name: satya
// Roll: 51
// Age: 19

// Name: satya
// Roll: 51
// Age: 19