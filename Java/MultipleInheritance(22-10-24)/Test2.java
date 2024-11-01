// Write a program using inheritance to determine a student's eligibility for different fields (Engineering, Medical, Agriculture) based on their percentage. 

import java.util.Scanner;

class Profile {
    String name;
    int roll, age, per;

    void get(String nm, int roll, int age, int per) {
        this.name = nm;
        this.roll = roll;
        this.age = age;
        this.per = per;
    }

    void display() {
        System.out.println("Name = " + name + "\nRoll = " + roll + "\nAge = " + age + "\nPercentage = " + per);
    }
}

class Medical extends Profile {
    public void display() {
        System.out.println("You are eligible to be a Doctor");
        super.display();
    }
}

class Engineering extends Profile {
    public void display() {
        System.out.println("You are eligible to be an Engineer");
        super.display();
    }
}

class Agriculture extends Profile {
    public void display() {
        System.out.println("You are eligible to be a Farmer");
        super.display();
    }
}

public class Test2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter Your Name:");
        String name = sc.nextLine();

        System.out.println("Enter your Roll:");
        int roll = sc.nextInt();

        System.out.println("Enter your Age:");
        int age = sc.nextInt();

        System.out.println("Enter your Percentage:");
        int per = sc.nextInt();

        Profile p;

        if (per > 90) {
            p = new Engineering();
        } else if (per > 80) {
            p = new Medical();
        } else {
            p = new Agriculture();
        }

        p.get(name, roll, age, per);
        p.display();
    }
}



// Enter Your Name:
// satya
// Enter your Roll:
// 21
// Enter your Age:
// 21
// Enter your Percentage:
// 21
// You are eligible to be a Farmer
// Name = satya
// Roll = 21
// Age = 21
// Percentage = 21