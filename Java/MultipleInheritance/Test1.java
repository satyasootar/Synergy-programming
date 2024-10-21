import java.util.*;

class Shape{
    float xco, yco, rad, side;
}

class Rectangle extends Shape{

   public void get(float x, float y){
    xco = x;
    yco = y;
   }
   public void area(){
    System.out.println("Area of the Rectangle: "+ (xco*yco));
   }
  
}

class Circle extends Shape{
    public void get(float r){
        rad = r;
    }
    public void area(){
        System.out.println("Area of the Circle: "+ Math.PI * Math.pow(rad, 2));
       }
}

class Square extends Shape{
    public void get(float s){
        side = s;
    }
    public void area(){
        System.out.println("Area of the Square: "+ (side*side));
       }
}


public class Test1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Rectangle r = new Rectangle();
        System.out.println("Enter length & Breadth");
        float l =  sc.nextFloat();
        float b = sc.nextFloat();
        r.get(l, b);
        r.area();
        

        Circle c = new Circle();
        System.out.println("Enter the radius");
        float rad = sc.nextFloat();
        c.get(rad);
        c.area();

        Square s = new Square();
        System.out.println("Enter the Side");
        float side = sc.nextFloat();
        s.get(side);
        s.area();
    }
}

// Output
// Enter length & Breadth
// 2
// 3
// Area of the Rectangle: 6.0
// Enter the radius
// 4
// Area of the Circle: 50.26548245743669
// Enter the Side
// 5
// Area of the Square: 25.0