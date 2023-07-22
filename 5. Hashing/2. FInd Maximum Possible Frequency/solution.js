const maxFrequency = function(nums, k){
let maxFrq = 0;
let currFreq = 1;
let frequencyMap = {};
let remainingKey = k;
const arrayLength = nums.length
nums.sort();
for(const i=0;i<arrayLength;i++){
    if(i+1<arrayLength){
        const diff = nums[i+1]-nums[i];
        if(diff<remainingKey){
            currFreq++;
            remainingKey = remainingKey - diff;
        }
    }
}
}