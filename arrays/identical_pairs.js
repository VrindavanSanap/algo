let nums = [1,2,3,1,1,3]
var numIdenticalPairs = function(nums) {
    let n_pairs = 0
    for (let i = 0; i< nums.length;i++){
        for (let j = i + 1; j< nums.length;j++){
            if (nums[i] == nums[j]){
                n_pairs += 1;
              console.log(i, j, n_pairs);
            }
        }
    }
    return n_pairs;
    
};
console.log(numIdenticalPairs(nums))
