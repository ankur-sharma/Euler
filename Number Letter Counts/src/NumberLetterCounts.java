
public class NumberLetterCounts {

	public static void main(String[] args) {
		
		int[] ones = new int[] {3, //one
				3, //two
				5, //three
				4, //four
				4, //five
				3, //six
				5, //seven
				5, //eight
				4};  //nine
		
		int[] teens = new int[] {6, //eleven
				6, //twelve
				8, //thirteen
				8, //fourteen
				7, //fifteen
				7, //sixteen
				9, //seventeen
				8, //eighteen
				8}; //nineteen
				
		
		int[] tens = new int[] {3, //ten
				6, //twenty
				6, //thirty
				5, //forty
				5, //fifty
				5, //sixty
				7, //seventy
				6, //eighty
				6, //ninety
				10}; //one hundred
		
		int hundredAnd = 10; //hundred and
		int thousand = 11; //one thousand

		
		int sumOf1to10 = 0;
		int sumOf11to20 = 0;
		int sumOf21to100 = 0;
		int sumOf1to1000 = 0;
		
		for (int i : ones) {
			sumOf1to10 += i;
		}
		sumOf1to10 += tens[0];
		
		System.out.println("sumOf1to10 is " + sumOf1to10);
		
		for (int i : teens) {
			sumOf11to20 += i;
		}
		sumOf11to20 += tens[1];
		
		int sumOf1to9 = sumOf1to10 - 3;
		for (int i = 1; i < tens.length - 1; i++) {
			sumOf21to100 += tens[i] * 9 + sumOf1to9 + tens[i+1];
		}
		
		int sumOf1to100 = sumOf1to10 + sumOf11to20 + sumOf21to100;
		System.out.println("sumOf1to100 is " + sumOf1to100);
		
		int sumOf1to99 = sumOf1to100 - 10;
		
		sumOf1to1000 = (hundredAnd * 9 + sumOf1to9) * 99 + sumOf1to99*10 + (sumOf1to9 + 7*9) + thousand;
		System.out.println("sumOf1to1000 is " + sumOf1to1000);
		
	}

}
