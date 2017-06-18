import java.math.BigInteger;

public class FactorialDigitSum {
	
	public static void main(String[] args) {
		System.out.println(getFactorialDigitSum(100));
	}

	private static int getFactorialDigitSum(int number) {
		BigInteger factorial = getFactorial2(number);

		char[] result = factorial.toString().toCharArray();
		int sumOfDigits = 0;
		for (char c : result) {
			sumOfDigits+= Integer.valueOf(""+c);
		}
		return sumOfDigits;
	}

	private static BigInteger getFactorial(BigInteger i) {
		if (BigInteger.ONE.equals(i))
			return BigInteger.ONE;
		return i.multiply(getFactorial(i.subtract(BigInteger.ONE)));
	}
	
	private static BigInteger getFactorial2(int n) {
		BigInteger factorial = BigInteger.ONE;
		for (int i = 1; i <= n; i++) {
			factorial = factorial.multiply(BigInteger.valueOf(i));
		}
		return factorial;
	}
}
