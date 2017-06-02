
public class TriangleWords {

	public static void main(String[] args) {
		
		System.out.println(isTriangleWords("SKY"));

	}

	private static boolean isTriangleWords(String string) {
		int wordSum = getWordSum(string);
		
		double discriminant = Math.sqrt(1 + 8 * wordSum);
		double plusN = (-1 + discriminant) / 2;
		
		System.out.println("Triangle root is " + plusN);
		
		return Math.abs(plusN - Math.round(plusN)) < 0.001;
		
	}

	private static int getWordSum(String string) {
		char[] word = string.toCharArray();
		
		int wordSum = 0;
		for (char c : word) {
			wordSum += c - 'A' + 1;
		}
		
		System.out.println("Word sum is " + wordSum);
		return wordSum;
	}

}
