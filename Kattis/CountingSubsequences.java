package CountingSubsequences;

import java.util.Scanner;
import java.util.HashMap; 

public class CountingSubsequences_260728949 {

    public static void main(String []args){
	   	Scanner s = new Scanner(System.in);
	   	
	   	//number of test cases
	   	int test_cases_length = s.nextInt(); 
	   	
	   	//loop the function by number of test cases times
	   	for(int i=0; i<test_cases_length; i++) {
	   		//skip the blank line
	   		s.nextLine();
	   		
	   		//collect the input data
	   		int num_length = s.nextInt();
	   		int [] input = new int[num_length];	
	   		for (int j=0; j<num_length; j++) {
	   			input[j] = s.nextInt();
	   		}
	   		
	   		//count the result
	   		int count = 0;
	   		
	   		//add up the following total sum
	   		int addUp = 0;
	   		
	   		//Map all of the sum created in the hashmap
	   		HashMap<Integer, Integer> prevSum = new HashMap<>();
	   		
	   		for (int k=0; k<num_length; k++) {
	   			
	   			addUp += input[k];
	   			if (addUp == 47) { count++; }
	   			
	   			//if the hashmap contains the sum that is needed to get 47 from the current sum add the number
	   			if (prevSum.containsKey(addUp - 47)) {
	   				count += prevSum.get(addUp - 47);
	   			}
	   			
	   			prevSum.put(addUp, prevSum.getOrDefault(addUp, 0) + 1);
	   		}
	   		
	   		//print the count
	   		System.out.println(count);
	   	}
	   	s.close();
       
    }
}
