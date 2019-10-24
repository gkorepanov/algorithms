#include "heap.hpp"
#include <vector>
#include <iostream>

int main() {
    std::vector<uint> numbers = {10, 5, 3, 4, 1, 2, 9, 7, 6};
    BinaryHeap<uint> heap;
    for (const auto& x: numbers)
        heap.add(x);

    while (heap.size())
        std::cout << heap.pop_min() << " ";

    std::cout << std::endl;
    return 0;
}
