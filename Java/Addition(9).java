
class Addition{
    public double Additions(double p, double q){
       return (p+q);
    }

    public static void main(String[] args) {
        Addition obj = new Addition();
        double r = obj.Additions(3.5, 6.7);
        System.out.println(r);
    }
}
//10.2