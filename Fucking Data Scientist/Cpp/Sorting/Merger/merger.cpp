#include <iostream>


template <class ArrayType, class SizeType>
void show_array(ArrayType* array, SizeType length)
{
    for (SizeType i = 0; i < length; i++)
        std::cout << array[i] << '\t';
    std::cout << '\n';
}


template <typename ArrayType, typename SizeType>
void merge_sort(ArrayType* array, SizeType length)
{
    if (length > 1)
    {    
        merge_sort(array, length / 2);
        merge_sort(array + length / 2, length - length / 2);

        SizeType middle = length / 2;
        ArrayType* l_a = array;
        ArrayType* r_a = array + middle;
        SizeType l_len = middle;
        SizeType r_len = length - middle;
        SizeType l_i = 0;
        SizeType r_i = 0;
        // временный массив, в который будем сливать
        ArrayType* tmp_a = new ArrayType[length];
        SizeType tmp_i = 0;

        while (l_i < l_len && r_i < r_len)
        {
            if (l_a[l_i] <= r_a[r_i]) {
                tmp_a[tmp_i] = l_a[l_i];
                l_i++;
            }
            else {
                tmp_a[tmp_i] = r_a[r_i];
                r_i++;
            }
            tmp_i++;
        }
        
        while (l_i < l_len) {
            tmp_a[tmp_i] = l_a[l_i];
            l_i++;
            tmp_i++;
        }

        while (r_i < r_len) {
            tmp_a[tmp_i] = r_a[r_i];
            r_i++;
            tmp_i++;
        }

        for (SizeType i = 0; i < length; i++)
            array[i] = tmp_a[i];

        delete[] tmp_a;
    }
}


int main()
{
    uint32_t n = 40000;
    int64_t a[n] = {777};

    merge_sort(a, n);
    show_array(a, n);

    return 0;
}
