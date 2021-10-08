class Solution {
  
    public static void secondLargest(int arr[], int size) {
        int i, first, second;
      
        if (size < 2) {
            System.out.print("Invalid Input");
            return;
        }
 
        first = second = Integer.MIN_VALUE;
        for (i = 0; i < size; i++) {
            if (arr[i] > first) {
                second = first;
                first = arr[i];
            }
            else if (arr[i] > second && arr[i] != first)
                second = arr[i];
        }
 
        if (second == Integer.MIN_VALUE)
            System.out.print("There is no second largest" + " element\n");
        else
            System.out.print("The second largest element" + " is " + second);
    }
  
    public static void main(String[] args) {
        int arr[] = { 12, 35, 1, 10, 34, 1 };
        int n = arr.length;
        secondLargest(arr, n);
    }
}
