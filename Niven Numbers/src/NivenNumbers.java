
public class NivenNumbers {

	public static void main(String[] args) {
		int N = 67;
		
		boolean isNiven = isNivenNumber(N / 10);
		System.out.println(isNiven);
		if (isNiven) {
			boolean srtnPrime = isPrime(N);
			System.out.println(srtnPrime);
		}

	}

	private static boolean isNivenNumber(int n) {
		if (n < 10)
			return true;
		int sumDigitOfDigits = getSumOfDigits(n);
		
		return n % sumDigitOfDigits == 0 && isNivenNumber(n/10);
	}

	private static int getSumOfDigits(int n) {
		int sum = 0;
		while (n > 9) {
			sum += n % 10;
			n /= 10;
		}
		sum += n;
		return sum;
	}

	private static boolean isPrime(int n) {
		
		double root = Math.sqrt(n);
		for (int i = 2; i < root; i++) {
			if (n % i == 0) {
				System.out.println(i);
				return false;
			}
		}
		return true;
	}

}
