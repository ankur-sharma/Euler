public class LetterCount {
    
    /** Creates a new instance of LetterCount */
    public LetterCount() {
        int onetonine = "onetwothreefourfivesixseveneightnine".length();
        int tentonineteen = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen".length();
        int and = "and".length();
        int twentytoninety = "twentythirtyfortyfiftysixtyseventyeightyninety".length();
        int hundred = "hundred".length();
        int thousand = "thousand".length();
        count = "one".length() + thousand + 
          900*hundred + 100*onetonine + 
          100*twentytoninety + 891*and + 
          80*onetonine + 10*(onetonine + tentonineteen);
    }
 
    int count;
    
    int getCount(){return count;}
    
    public static void main(String[] args) {
        System.out.println(new LetterCount().getCount());
    }
}