package Array;

public class RepeatedNumber {
    // https://leetcode.com/problems/find-the-duplicate-number/
    // Use Auxillary array to store if previously seen value
    public int findDuplicate(int[] nums) {
        int n = nums.length;
        boolean[] temp = new boolean[n + 1];
        for (int i = 0; i < n; i++) {
            if (temp[nums[i]] == true) {
                return nums[i];
            }
            temp[nums[i]] = true;
        }
        return 0;
    }

    // Using Floydd's Cycle Detection Algorithm
//    public int findDuplicate(int[] nums) {
//        int slow = nums[0]
//        int fast = nums[0]
//        // Phase 1: Find the intersection point in the cycle
//        do {
//            slow = nums[slow];
//            fast = nums[nums[fast]];
//        } while (slow != fast);
//
//        // Phase 2: Find the entrance to the cycle
//        slow = nums[0];
//        while (slow != fast) {
//            slow = nums[slow];
//            fast = nums[fast];
//        }
//        return slow;
//    }
}