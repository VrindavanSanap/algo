var nums = [1, 2, 3, 1, 1, 3];
function numIdenticalPairs(nums) {
    // returns the number of idential pairs of ints are there in a array
    var n_pairs = 0;
    for (var i = 0; i < nums.length; i++) {
        for (var j = i + 1; j < nums.length; j++) {
            if (nums[i] == nums[j]) {
                n_pairs += 1;
            }
        }
    }
    return n_pairs;
}
;
console.log(numIdenticalPairs(nums));
