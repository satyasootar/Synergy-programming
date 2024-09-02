public class AccessBio {
    String name;
    int age;
    String branch;

    public AccessBio(){}

    public AccessBio(String name , int age , String branch){
        this.name = name;
        this.age = age;
        this.branch = branch;
    }
    public void display(){
        System.out.println("Name:"+ name);
        System.out.println("Branch:" + branch);
        System.out.println("Age:"+ age);
    }

    public static void main(String[] args) {
        AccessBio a = new AccessBio("Satya", 19, "CSE");
        AccessBio b = new AccessBio("Soumya", 19, "Electrical");
        a.display();
        b.display();
    }
}
