import java.util.ArrayList;

public class delete {
    

    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5};
        ArrayList<Integer> arr1 = new ArrayList<Integer>();
        for(int i = 0; i<=arr.length-1; i++){
            arr1.add(arr[i]);
        
        // int n = 2;
        // for(int i = 0; i<=arr.size(); i++){
        //     int temp = arr.remove(0);
        //     arr.add(temp);
        }
        for(Integer number: arr1)
        System.out.println(number);
        


    
    }}