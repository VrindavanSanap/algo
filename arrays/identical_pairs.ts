let nums :number[] = [1,2,3,1,1,3]
function numIdenticalPairs(nums : number[]) :number{
    // returns the number of idential pairs of ints are there in a array
    
    let n_pairs : number = 0
    for (let i = 0; i< nums.length;i++){
        for (let j = i + 1; j< nums.length;j++){
            if (nums[i] == nums[j]){
                n_pairs += 1;
            }
        }
    }
    return n_pairs;
};

console.log(numIdenticalPairs(nums))
