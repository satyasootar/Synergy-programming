//WAP to overload a constructor complex to add two complex number by 0 argument, 1 argument & 2 argument constructor


class Overload {
    int real;
    int imgr;

    public Overload(){
        real = 1;
        imgr =1;
    }

    public Overload(int r){
        real = r;
        imgr = 10;
    }

    public Overload(int r, int i){
        real = r;
        imgr = i;
    }

    public void display(){
        System.out.println(real+"+ i"+ imgr);
    }

    public void add(Overload t){
        System.out.println((real+ t.real)+"+ i"+(imgr + t.imgr));
    }

    public Overload add1(Overload t){
        Overload result = new Overload();
        result.real = real + t.real;
        result.imgr = imgr + t.imgr;
        return result;
    }

    public static void main(String[] args) {
        Overload obj1 = new Overload();
        obj1.display();
        Overload obj2 = new Overload(5);
        obj2.display();
        Overload obj3 = new Overload(5, 7);
        obj3.display();

        obj1.add(obj2);
        Overload r = obj2.add1(obj3);
        r.display();
    }
}

// OUTPUT
// 1+ i1
// 5+ i10
// 5+ i7
// 6+ i11
// 10+ i17