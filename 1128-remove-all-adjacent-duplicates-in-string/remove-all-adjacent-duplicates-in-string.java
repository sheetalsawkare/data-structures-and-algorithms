import java.util.*;
class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> myStack = new Stack<>();
        StringBuilder sb = new StringBuilder();

        for(int i=0; i<s.length(); i++){
            char ch = s.charAt(i);
            if(myStack.empty()){
                myStack.push(ch);
                continue;
            }
            if(ch == myStack.peek()){
                myStack.pop();
                continue;
            }
            myStack.push(ch);
        }

        while(!myStack.empty()){
            sb.append(myStack.pop());
        }

        return sb.reverse().toString();
    }
}