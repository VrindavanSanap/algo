#include <iostream>
#include <vector>
using namespace std;

template<typename T, size_t N>
void print_arr(const T (&arr)[N]) {
    std::cout << "Array elements: ";
    for (size_t i = 0; i < N; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int third_max(vector<int>& nums){
  int buffer[3] = {0};
  int writer = 0;
  for (int i = 0; i < nums.size(); i++){
    cout << nums[i]<< endl;
    if (nums[i] > buffer[(writer)%3]){
      if(buffer[(writer-1)%3] != nums[i]){
        buffer[writer%3] = nums[i];
        writer++;
      }
    }
    print_arr(buffer);
 }
 return 0;
  return buffer[(writer-1)%3];
}

int main(){

  vector<int> nums1{3,2,1};
  vector<int> nums2{1,2};
  vector<int> nums3{2,2,3,1};
  cout<<third_max(nums1)<<endl;
  cout<<"---"<<endl;
  cout<<third_max(nums2)<<endl;
  cout<<"---"<<endl;
  cout<<third_max(nums3)<<endl;
  cout<<"---"<<endl;


}
