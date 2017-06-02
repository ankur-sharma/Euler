
public class CountingSundays {

	public static void main(String[] args) {
		
		long start = System.nanoTime();
		int lastDayOfPreviousMonth = 6; //31 Dec 1899 is Sunday as 1 Jan 1900 is Monday
		
		int countOfSundayOnFirstOfMonth = 0;
		
		for (int year = 1900; year <= 2000; year++) {
			for (int month = 1; month <= 12; month++) {
				int dayOnFirstOfThisMonth = (lastDayOfPreviousMonth + 1) % 7;
				if (year > 1900 && dayOnFirstOfThisMonth == 6)
					countOfSundayOnFirstOfMonth++;
				switch (month) {
				case 1: // Jan
				case 3: // Mar
				case 5: // May
				case 7: // Jul
				case 8: // Aug
				case 10: // Oct
				case 12: // Dec
					lastDayOfPreviousMonth = (lastDayOfPreviousMonth + 3) % 7;
					break;
				case 4: // Apr
				case 6: // Jun
				case 9: // Sep
				case 11: // Nov
					lastDayOfPreviousMonth = (lastDayOfPreviousMonth + 2) % 7;
					break;
				case 2: // Feb
					if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0))
						lastDayOfPreviousMonth = (lastDayOfPreviousMonth + 1) % 7;
				}
			}
		}
		long stop = System.nanoTime();
		
		System.out.println(countOfSundayOnFirstOfMonth);
		System.out.println(stop - start);
		
	}

}
