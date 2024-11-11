//WAP to show NumberFormatException

class NumberFormatException {
    public static void main(String[] args) {
        String a = "satya";
        try {
            int p = Integer.parseInt(a);
        } catch(Exception e){
             System.out.println("Error: "+ e);
        }
    }
}


// OUTPUT
// Error: java.lang.NumberFormatException: For input string: "satya"