// https://leetcode.com/problems/two-sum/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function (nums, target) {
    var output = [];
    for (var i = 0; i < nums.length; i++) {
        for (var j = 0; j < nums.length; j++) {
            var sum = 0;
            if (i == j) {
                continue;
            } else {
                sum = nums[i] + nums[j];
                if (sum == target) {
                    output.push(i);
                    output.push(j);
                    return output;
                }
            }
        }
    }
};