#include <vector>

// C++ heap functionality is intentionally not used
// in order to try implementing a heap
template<class T>
class BinaryHeap {
private:
    std::vector<T> data;

    static inline size_t get_parent_index(size_t index) { return index >> 1; }
    static inline size_t get_left_child_index(size_t parent_index) { return parent_index << 1; }

    void sift_up(size_t index);
    void sift_down(size_t index);

    T& get(size_t index) { return this->data[index - 1]; }

public:
    BinaryHeap() = default;
    
    inline size_t size() const { return this->data.size(); }
    void add(const T elem);
    T pop_min();
};


template<class T>
void BinaryHeap<T>::add(const T elem) {
    this->data.push_back(elem);
    this->sift_up(data.size());
}


template<class T>
T BinaryHeap<T>::pop_min() {
    T result = this->data.front();
    this->data.front() = this->data.back();
    this->data.pop_back();
    this->sift_down(1);

    return result;
}


template<class T>
void BinaryHeap<T>::sift_up(size_t index) {
    if (index == 1)  // already a root
        return;

    size_t parent_index = this->get_parent_index(index);
    if (this->get(parent_index) <= this->get(index))  // heap property is fine
        return;
    
    // swap current elem with its parent
    std::swap(this->get(parent_index), this->get(index));

    // recursively call in parent
    this->sift_up(parent_index);
}


template<class T>
void BinaryHeap<T>::sift_down(size_t index) {
    size_t left_child_index = this->get_left_child_index(index);
    size_t right_child_index = left_child_index + 1;
    if (left_child_index > this->data.size())  // already a leaf
        return;

    size_t min_index = index;

    if (this->get(left_child_index) < this->get(min_index))
        min_index = left_child_index;

    if (this->get(right_child_index) < this->get(min_index))
        min_index = right_child_index;

    if (min_index == index)  // heap property is fine
        return;

    std::swap(this->get(index), this->get(min_index));
    this->sift_down(min_index);
}

