package Strings;

public class GetRomanNumberFromString {

        public int getValue(char str) {
            switch (str) {
                case 'I':
                    return 1;
                case 'V':
                    return 5;
                case 'X':
                    return 10;
                case 'L':
                    return 50;
                case 'C':
                    return 100;
                case 'D':
                    return 500;
                case 'M':
                    return 1000;

            }
            return 0;
        }
        // Finds decimal value of a given roman numeral
        public int romanToDecimal(String str) {
            int answer = 0;
            int i=0;
            int n = str.length();

            while(i<n){
                if(i+1<n){
                    if(getValue(str.charAt(i))<getValue(str.charAt(i+1))){
                        answer+=getValue(str.charAt(i+1))-getValue(str.charAt(i));
                        i+=2;
                        continue;
                    }
                }
                answer += getValue(str.charAt(i));
                i++;
            }
            // code here

            return answer;

        }

}
