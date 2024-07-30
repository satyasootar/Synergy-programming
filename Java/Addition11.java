import java.util.Scanner;

class Addition11{
    public static double Additions(double p, double q){
       return (p+q);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter the numbers");
        double a = sc.nextDouble();
        double b = sc.nextDouble();   
        double r = Additions(a, b);
        System.out.println(r);
    }
}
