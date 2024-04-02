#include <iostream>
#include <vector>

int main() {
    // Initializing using initializer list
    std::vector<char> chars = {'A', 'B', 'C'};
    
    // Initializing using brace-enclosed initializer list
    std::vector<char> chars2 {'D', 'E', 'F'};
    
    // Access elements using index or iterator
    std::cout << chars[0] << std::endl; // Output: A
    std::cout << chars2[0] << std::endl; // Output: D
    
    return 0;
}
