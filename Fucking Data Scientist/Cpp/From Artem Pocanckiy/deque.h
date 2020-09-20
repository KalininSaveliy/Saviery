//
//  deque.h
//  Deque
//
//  Created by Артём Lazemir on 20.04.2020.
//  Copyright © 2020 MIPT DGAP. All rights reserved.
//

#ifndef deque_h
#define deque_h

template <class T>
class Deque {
public:
    Deque() {
        this->resize(2);
        front_block = 0;
        back_block = 1;
        buf[front_block] = new T[size];
        buf[back_block] = new T[size];
        size_block = 2;
    }

    void PushBack(const T& t) {
        if (num_back) {
            if (back == size - 1) {
                back_block = (cap_block + (back_block + 1)) % cap_block;
                buf[back_block] = new T[size];
                ++size_block;
                back = -1;
            }
            if (size_block == cap_block) {
                this->resize(2 * cap_block);
            }
            
            ++back;
        } else {
            back = 0;
            back_block = 1;
            if (!num_front) {
                front = back;
                front_block = back_block;
            }
        }
        buf[back_block][back] = t;
        ++num_back;
    }
    void PopBack() {

    }

    T& Back() {
        return buf[back_block][back];
    }
//    const T& Back() const {
//        return buf[back];
//    }

    void PushFront(const T& t) {
        if (num_front) {
            if (front == 0) {
                front_block = (cap_block + (front_block - 1)) % cap_block;
                buf[front_block] = new T[size];
                ++size_block;
                front = size;
            }
            if (size_block == cap_block) {
                this->resize(2 * cap_block);
            }
            
            --front;
        } else {
            front = size - 1;
            front_block = 0;
            if (!num_back) {
                back = front;
                back_block = front_block;
            }
        }
        buf[front_block][front] = t;
        ++num_front;
    }
    void PopFront() {

    }

    T& Front() {
        return buf[front_block][front];
    }
//    const T& Front() const {
//
//    }

    size_t Size() const {
        return num_front + num_back;
    }

    T& operator[](size_t index) {
        return buf[(front_block + index / size) % cap_block][(front + index) % size];
    }
//    const T& operator[](size_t index) const {
//        // ...
//    }

    ~Deque() {
        // ...
    }
private:
    T** buf = nullptr;
    int num_back, num_front, size = 10, size_block, front = size - 1, back = 0, front_block, back_block, cap_block;
    
    void resize(const unsigned int new_cap) {
        T** tmp = new T*[new_cap];
        
        if (buf) {
            for (int i(0), j(front_block); i < cap_block && j != back_block; ++i, j = (j + 1) % cap_block) {
                tmp[i] = buf[j];
            }
            tmp[size_block - 1] = buf[back_block];
        
            delete[] buf;
        }
        buf = tmp;
        cap_block = new_cap;
        front_block = 0;
        back_block = size_block - 1;
    }
};

#endif /* deque_h */
