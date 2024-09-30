//WAP to implement Single inheritance on two classes. One in Father and another one is Son.

import java.util.Scanner;

class Father{
    String fnm;
    int age;

        void getData(String s , int a){
            fnm = s;
            age = a;
        }
        void display(){
            System.out.println("\nFathers name: "+ fnm + "\nFather's age: "+ age);
        }
}

class Son extends Father{
    String snm;
    int sage;
    void get(String fnm, int fage, String snm, int sage){
            this.fnm = fnm;
            this.age = fage;
            this.snm = snm;
            this.sage = sage;
        }
        void disp(){
            display();
            System.out.println("Son's name: " + snm + "\nSon's age: " + sage);
        }
}
public class SingleInheritance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Father's name: ");
        String Fnm = sc.nextLine();

        System.out.print("Enter Father's age: ");
        int fage = sc.nextInt();
        sc.nextLine();

        System.out.print("Enter Son's name: ");
        String snm = sc.nextLine();

        System.out.print("Enter Son's age: ");
        int sage = sc.nextInt();

        Son k = new Son();
        k.get(Fnm, fage, snm, sage);
        k.disp();

    }
}


// output
// Enter Father's name: fa
// Enter Father's age: 50
// Enter Son's name: sa
// Enter Son's age: 18

// Fathers name: fa
// Father's age: 50
// Son's name: sa
// Son's age: 18