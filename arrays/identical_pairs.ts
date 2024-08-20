function count_identical_pairs(nums: number[]): number {
    let identical_pairs_count: number = 0;

    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            if (nums[i] === nums[j]) {
                identical_pairs_count++;
            }
        }
    }

    return identical_pairs_count;
}

const nums: number[] = [1, 2, 3, 1, 1, 3];
console.log(count_identical_pairs(nums));
