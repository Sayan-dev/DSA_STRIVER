package Strings;

import java.util.*;

public class ParenthesisCheck {
    static boolean ispar(String x)
    {
        Map<Character, Character> pr = new HashMap<>();
        pr.put('[',']');
        pr.put('{','}');
        pr.put('(',')');
        // add your code here
        Stack<Character> st = new Stack();
        for(char c: x.toCharArray()){
            if(c == '[' || c=='{' || c=='(')
            {st.push(c);}
            else if(c=='}' || c==']' || c==')')
            {
                if(st.size()>0){
                    char ch = st.peek();
                    if(pr.get(ch) == c){
                        st.pop();
                    } else {
                        return false;
                    }
                }else {
                    return false;
                }


            }

        }
        if(st.size()==0){
            return true;
        }
        return false;

    }
}
