import java.util.Scanner;

class Addition12{
    double a,b;

    void getData(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number");
        a = sc.nextDouble();
        System.out.println("Enter the second number");
        b = sc.nextDouble();
    }

    double process(){
        return(a+b);
    }

    void display(){
        System.out.println("sum ="+ process());
    }

    public static void main(String[] args) {
        Addition12 obj= new Addition12();
        obj.getData();
        obj.display();
    }

}