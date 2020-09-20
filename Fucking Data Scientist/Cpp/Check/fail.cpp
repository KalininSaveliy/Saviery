#include<iostream>
int* mergesort(int* a, int a_size)
{
    int* newa = new int[a_size];
    int middle = a_size/2;
    int* a_left = a;
    int a_left_size = middle;
    int* a_right = a + middle;
    int a_right_size = a_size - middle;
    int* b = new int[a_left_size];
    int* c = new int[a_right_size];
    if (a_size>1)
    {
        b = mergesort(a_left, a_left_size);
        c = mergesort(a_right, a_right_size);
        int y;//equals 0 if its b and 1 if its c
        int k = 0;
        int i1 = 0;
        int i2 = 0;
        // if (b[0]>c[0])
        // {
        //     newa[0] =c[0];
        //     k = 1; //number of elements in a new array
        //     y = 1;
        //     i2 = 1;
        // }
        // else
        // {
        //     newa[0] = b[0];
        //     k = 1;
        //     y = 0;
        //     i1 = 1;
        // }
        y = 0;
        while (k <a_size)
        {
            if (y == 1)
            {
                while (c[i2]<=b[i1] && i2<a_right_size)//problems when i2 == a_right_size
                {
                    newa[i2+i1] = c[i2];
                    i2++;
                    k++;
                }
                if (i2 == a_right_size)
                {
                    for (int i = i1; i <a_left_size ; i++)
                    {
                        newa[i2+i1] = b[i];
                        k++;
                    }
                }
                y = 0;
            }
            else
            {
                while (c[i2]>=b[i1] && i1< a_left_size)
                {
                    newa[i2+i1] = b[i1];
                    i1++;
                    k++;
                }
                if (i1 == a_left_size)
                {
                    for (int i = i2; i <a_right_size ; i++)
                    {
                        newa[i2+i1] = c[i];
                        k++;
                    }
                }
                y = 1;
            }
        }
    }
    else {newa[0] = a[0];}
    return newa;
    int k = 0;
    int i1 = 0;
    int i2 = 0;
}
int main()
{
    //choose a sort
    int n;
    std::cin>>n;
    int* a = new int[n];
    int* b = new int[n];
    for (int i = 0; i < n; i++)
    {
        std::cin>>a[i];
    }
    b = mergesort(a, n);
    for (int i = 0; i < n; i++)
    {
        std::cout<<b[i]<<' ';
    }
    
}