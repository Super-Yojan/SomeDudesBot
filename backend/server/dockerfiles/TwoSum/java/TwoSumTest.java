/**
 * On Mac/Linux:
 *  javac -cp .:junit-cs211.jar *.java         # compile everything
 *  java -cp .:junit-cs211.jar Solution        # run tests
 *
 * On windows replace colons with semicolons: (: with ;)
 *  javac -cp .;junit-cs211.jar *.java         # compile everything
 *  java -cp .;junit-cs211.jar Solution        # run tests
 */

import static org.junit.Assert.*;
import org.junit.Test;

public class Solution {
    public int[] correctTwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return null;
    }
    public static void main(String args[]) {
		org.junit.runner.JUnitCore.main("Solution");
	}

    int[] nums1 = {2, 7, 11, 15};
    int target1 = 9;
    int[] nums2 = {3, 2, 4};
    int target2 = 6;
    int[] nums3 = {3, 3};
    int target3 = 6;
    int[] nums4 = {2, 7, 11, 15};
    int target4 = 40;

    //Target 9
    @Test(timeout = 1000)
	public void test_sum_1() {
        boolean found = true;
        String total = "";
            for (int i : nums1) {
                total += i + " ";
            }
        int[] user = twoSum.sum(nums1, target1);
        int[] solve = this.correctTwoSum(nums1, target1);
        if (user.length != solve.length) {
            assertEquals("Incorrect array size for test 1 is wrong:\nnums = " + total + "target value = " + found, true);
        }

        for (int i = 0; i < solve.length; i++) {
            for (int j = i + 1; j < user.length; j++) {
                if (user[j] == solve[i]) {
                    continue;
                }
                else if (user[j] != solve[i] && i == solve.length - 1) {
                    found = false;
                    assertEquals("Test 1 is wrong:\nnums = " + total + "target value = " + target1, user, solve);
                }
            }
        }
    }

    //Target 6
    @Test(timeout = 1000)
	public void test_sum_2() {
        boolean found = true;
        String total = "";
            for (int i : nums2) {
                total += i + " ";
            }
        int[] user = twoSum.sum(nums2, target2);
        int[] solve = this.correctTwoSum(nums2, target2);
        if (user.length != solve.length) {
            assertEquals("Incorrect array size for test 2 is wrong:\nnums = " + total + "target value = " + found, true);
        }

        for (int i = 0; i < solve.length; i++) {
            for (int j = i + 1; j < user.length; j++) {
                if (user[j] == solve[i]) {
                    continue;
                }
                else if (user[j] != solve[i] && i == solve.length - 1) {
                    found = false;
                    assertEquals("Test 2 is wrong:\nnums = " + total + "target value = " + target2, user, solve);
                }
            }
        }
    }

    //Target 6
    @Test(timeout = 1000)
	public void test_sum_3() {
        boolean found = true;
        String total = "";
            for (int i : nums3) {
                total += i + " ";
            }
        int[] user = twoSum.sum(nums3, target3);
        int[] solve = this.correctTwoSum(nums3, target3);
        if (user.length != solve.length) {
            assertEquals("Incorrect array size for test 3 is wrong:\nnums = " + total + "target value = " + found, true);
        }

        for (int i = 0; i < solve.length; i++) {
            for (int j = i + 1; j < user.length; j++) {
                if (user[j] == solve[i]) {
                    continue;
                }
                else if (user[j] != solve[i] && i == solve.length - 1) {
                    found = false;
                    assertEquals("Test 3 is wrong:\nnums = " + total + "target value = " + target3, user, solve);
                }
            }
        }
    }

    //Null case
    @Test(timeout = 1000)
	public void test_sum_4() {
        boolean found = true;
        String total = "";
            for (int i : nums4) {
                total += i + " ";
            }
        int[] user = twoSum.sum(nums4, target4);
        int[] solve = this.correctTwoSum(nums4, target4);
        assertEquals("Test 3 is wrong:\nnums = " + total + "target value = " + found, user, solve);
    }
}