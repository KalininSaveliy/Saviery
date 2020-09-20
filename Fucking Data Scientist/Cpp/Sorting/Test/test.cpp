#include <iostream>


template <class ArrayType, class SizeType>
void sort(ArrayType* array, SizeType length)
{;}


int main()
{
    bool ok = true;
    int test_number = 1;
    int len = 100;

    int* input_array = new int[len];
    int* array = new int[len];
    for (int i = 0; i < len; i++) {
        input_array[i] = len - i;
        array[i] = len-i;
    }

    int* target_array = new int[len];
    for (int i = 0; i < len; i++)
        target_array[i] = i + 1;

    sort(array, len);
    for (int i = 0; i < len && ok; i++)
        if (array[i] != i+1)
        {
            ok = false;
            std::cout << "Wrong sort in test " << test_number << " !\n";
            std::cout << " Input array: ";
            for (int i = 0; i < len; i++)
                std::cout << input_array[i] << " ";
            std::cout << std::endl << "Output array: ";
            for (int i = 0; i < len; i++)
                std::cout <<array[i] << " ";
            std::cout << std::endl;
        }
}
