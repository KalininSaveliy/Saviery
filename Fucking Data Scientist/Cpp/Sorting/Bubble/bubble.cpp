#include <iostream>


void swap(int* a, int* b)
{
    int tmv = *a;
    *a = *b;
    *b = tmv;
}


void bubble(int* array, int len_array)
{
    for (int i = len_array - 2; i >= 0; --i)
    {
        if (array[i] > array[i+1])
        {
            swap(& array[i], & array[i+1]);

            for (int j = i+1; j < len_array - 1; ++j)
                if (array[j] > array[j+1])
                    swap(& array[j], & array[j+1]);
        }
    }
}


int main()
{
    int n = 9;
    // int a[] = {3, 2, 1};
    int a[] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    
    bubble(a, n);

    for (int i = 0; i < n; ++i)
        std::cout << a[i] << " ";

    std::cout << "\n";

    return 0;
}
