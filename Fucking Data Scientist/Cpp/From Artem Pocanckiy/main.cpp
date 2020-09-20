//
//  main.cpp
//  Deque
//
//  Created by Артём Lazemir on 20.04.2020.
//  Copyright © 2020 MIPT DGAP. All rights reserved.
//

#include <iostream>
#include "deque.h"

int main(int argc, const char * argv[]) {
    Deque<int> d;
    for (int i = 0; i < 20000000; ++i) {
        d.PushFront(i);
        d.PushBack(i);
    }
    
    std::cout << d.Back() << ' ' << d.Front() << ' ' << d.Size() << std::endl;
    
    for (int i = 0; i < 40000000; ++i) {
        std::cout << d[i] << std::endl;
    }
    
    return 0;
}
