class Solution {
    public boolean validateStackSequences(int[] pushed, int[] popped) {
        Stack<Integer> st= new Stack<>();
        int i=0;
        for (int j:pushed){
            st.push(j);
            while(!st.isEmpty() && popped[i]==st.peek()){
                i++;
                st.pop();                
           }
        }
        return st.isEmpty();
    }
}