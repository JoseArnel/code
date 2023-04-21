

// Given a string, return a string where for every char in the original, there are two chars.
public String doubleChar(String str) {
	String result = "";
	for (int i = 0; i < str.length(); i ++){
	  result = result + str.charAt(i) + str.charAt(i);
	}
	return result;
  }

// Return the number of times that the string "hi" appears anywhere in the given string.
public int countHi(String str) {
	int count = 0;
	for (int i = 0; i < str.length()-1; i ++ ){
		if (str.substring(i,i+2).equals("hi")){
		count ++;
		}
	}
	return count;
}

// Return true if the string "cat" and "dog" appear the same number of times in the given string.
public boolean catDog(String str) {
	int c1 = 0;
	int c2 = 0;
	for (int i = 0; i < str.length()-2; i++){
	  if(str.substring(i, i+3).equals("cat")){
		c1 ++;
	  }
	  else if(str.substring(i, i+3).equals("dog")){
		c2 ++;
	  }
	}
	if (c1 == c2)
	  return true;
	return false;
  }

// Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
public int countCode(String str) {
int count = 0;
	for (int i = 0; i < str.length()-3; i ++){
		if (str.substring(i, i+2).equals("co")){
			if (str.charAt(i+3) == 'e')
				count ++;
			}
	}
	return count;
}
  
// Given two strings, return true if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: str.toLowerCase() returns the lowercase version of a string.
public boolean endOther(String a, String b) {
	a = a.toLowerCase();
	b = b.toLowerCase();
	return a.endsWith(b) || b.endsWith(a);
  }

// Return true if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
public boolean xyzThere(String str) {
	Boolean flag = false;
	
	if (str.length() >= 3 && str.substring(0,3).equals("xyz"))
	  flag = true;
	
	for (int i = 1; i < str.length()-2; i ++){
	  if (str.charAt(i-1) != '.' && str.substring(i, i +3).equals("xyz"))
		flag = true;
	}
	return flag;
  }

// Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.
public boolean bobThere(String str) {
	boolean flag = false;
	for(int i = 0; i<str.length()-2; i ++){
	  if (str.charAt(i) == 'b' && str.charAt(i+2) == 'b')
		flag = true;
	}
	return flag;
  }

// We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. Return true if the given string is xy-balanced.
public boolean xyBalance(String str) {
	Boolean flag = false;
	for(int i = str.length()-1; i >= 0; i --){
	  if (str.charAt(i) == 'y'){
		flag = true;
	  }
	  if (str.charAt(i) == 'x' && flag == false){
		return false;
	  }
	}
	return true;
  }

// Given two strings, a and b, create a bigger string made of the first char of a, the first char of b, the second char of a, the second char of b, and so on. Any leftover chars go at the end of the result.
public String mixString(String a, String b) {
	String x = "";
	int y = Math.min(a.length(),b.length());
	for (int i = 0; i < y; i ++){
	  x = x + a.charAt(i) + b.charAt(i);
	}
	return x = x + a.substring(y) + b.substring(y);
  }

// Given a string and an int n, return a string made of n repetitions of the last n characters of the string. You may assume that n is between 0 and the length of the string, inclusive.
public String repeatEnd(String str, int n) {
	String x = "";
	for (int i = 0; i < n ; i ++ ){
	  x = x + str.substring(str.length()-n, str.length());
	}
	return x;
  }

// Given a string and an int n, return a string made of the first n characters of the string, followed by the first n-1 characters of the string, and so on. You may assume that n is between 0 and the length of the string, inclusive (i.e. n >= 0 and n <= str.length()).
public String repeatFront(String str, int n) {
	String x = "";
	int y = n;
	for (int i = 0; i < n; i ++){
	  x = x + str.substring(0,y);
	  y --;
	}
	return x;
  }

// Given a string, consider the prefix string made of the first N chars of the string. Does that prefix string appear somewhere else in the string? Assume that the string is not empty and that N is in the range 1..str.length().
public boolean prefixAgain(String str, int n) {
	String x = str.substring(0,n);
	for (int i = n; i <= str.length()-n; i ++){
	  if(str.substring(i, i + n).equals(x))
		return true;
	}
	return false;
  }
  