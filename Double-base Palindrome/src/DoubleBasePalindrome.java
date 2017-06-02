
public class DoubleBasePalindrome {
	
	

	public static void main(String[] args) {
		
		for (int index = 0; index < 10000; index++) {
			boolean doubleBasePalindrome = isDoubleBasePalindrome(index);
			if (doubleBasePalindrome)
				System.out.println(index + " : " + doubleBasePalindrome);			
		}

	}

	private static boolean isDoubleBasePalindrome(int number) {
		
		String string = String.valueOf(number);
		StringBuilder numberString = new StringBuilder(string);
		
		boolean base10Palindrome = numberString.reverse().toString().equals(string);

//		System.out.println("base10Palindrome is " + base10Palindrome);
		if (!base10Palindrome)
			return false;
		String base2NumberString = getBase2Number(number);
		numberString = new StringBuilder(base2NumberString);
		
		boolean doubleBase = numberString.reverse().toString().equals(base2NumberString);
		if (doubleBase)
			System.out.println(base2NumberString);
		return doubleBase;
	}

	private static String getBase2Number(int number) {
		
		String base2 = "";
		while (number > 1) {
			base2 += number % 2;
			number /=2;
		}
		base2 += number;
		return base2;
	}

}
