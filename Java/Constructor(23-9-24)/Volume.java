//WAP to overload a constructor volume to calculate the volume of a sphere, cube, cuboid.

import java.util.Scanner;

public class Volume {
    double l, b, h, r, pi;
    double value;

    // Default constructor
    public Volume() {}

    // Constructor to calculate the volume of a sphere
    public Volume(double r, double pi) {
        this.r = r;
        this.pi = pi;
        double value = (4.0 / 3.0) * pi * r * r * r;
        System.out.println("The volume of sphere: " + value);
    }

    // Constructor to calculate the volume of a cube
    public Volume(double l) {
        this.l = l;
        System.out.println("The volume of cube: " + l * l * l);
    }

    // Constructor to calculate the volume of a cuboid
    public Volume(double l, double b, double h) {
        this.l = l;
        this.b = b;
        this.h = h;
        System.out.println("The volume of cuboid: " + l * b * h);
    }

    public static void main(String[] args) {
        double pi = 3.14;    
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the Radius: ");
        int r = sc.nextInt();
        System.out.print("Enter the length: ");
        int l = sc.nextInt();
        System.out.print("Enter the Breadth: ");
        int b = sc.nextInt();
        System.out.print("Enter the height: ");
        int h = sc.nextInt();
        // Create object to calculate the volume of a sphere
        Volume sphere = new Volume(r, pi);
        Volume cube = new Volume(l);
        Volume cuboid = new Volume(l, b, h);
    }
}

// Output
// Enter the Radius: 5
// Enter the length: 4
// Enter the Breadth: 3
// Enter the height: 6
// The volume of sphere: 523.3333333333334
// The volume of cube: 64.0
// The volume of cuboid: 72.0
