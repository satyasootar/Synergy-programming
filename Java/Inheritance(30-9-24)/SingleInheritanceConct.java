//WAP to implement single inheritance on class initialise by constructor


import java.util.Scanner;

class Father{
    public String fnm;
    public int age;

        public Father(String s , int a){
            fnm = s;
            age = a;
        }
        void display(){
            System.out.println("\nFathers name: "+ fnm + "\nFather's age: "+ age);
        }
}

class Son extends Father{
    public String snm;
    public int sage;
    public Son(String fnm, int fage, String snm, int sage){
            super(fnm, fage);
            this.snm = snm;
            this.sage = sage;
        }
        void disp(){
            display();
            System.out.println("Son's name: " + snm + "\nSon's age: " + sage);
        }
}
public class SingleInheritanceConct {
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

        Son k = new Son(Fnm, fage, snm, sage);
        k.disp();

    }
}

// output
// Enter Father's name: Faa
// Enter Father's age: 51
// Enter Son's name: Saa
// Enter Son's age: 21

// Fathers name: Faa
// Father's age: 51
// Son's name: Saa
// Son's age: 21
