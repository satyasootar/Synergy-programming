
class Addition{
    public static double Additions(double p, double q){
       return (p+q);
    }

    public static void main(String[] args) {
        Addition obj = new Addition();
        double r = Additions(5.3, 6.7);
        System.out.println(r);
    }
}
