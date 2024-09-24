import java.util.Scanner;

public class Volume {
    double l,b,h,r, pi;
    double value;

    public Volume(){}

    public Volume(double n, double pi){
        this.r = n;
        this.pi = pi;
        double value = 4/3*pi*r*r*r;
        System.out.println("The volume of circle: "+ value);
    }

    public Volume(double l){
        this.l = l;
        System.out.println("The volume of Cube: "+l*l*l);
    }

    public Volume(double l, double b, double h){
        this.l = l;
        this.b=b;
        this.h=h;
        System.out.println("The volume of Cube: "+l*b*h);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double r = sc.nextInt();
        double pi= sc.nextInt();
        Volume circle = new Volume(r, pi);
    }
}
