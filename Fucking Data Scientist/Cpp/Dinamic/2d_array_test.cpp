#include <iostream>


void func(int* a, int n, int m)
{
    std::cout << a[(n-1)*m + (m-1)] << std::endl;
}


int main()
{
    int n = 3, m = 4;
    int a[n][m];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j)
        {
            a[i][j] = 10 * (i*m + j);
            std::cout << a[i][j] << " ";
        }
        std::cout << std::endl;

    func(reinterpret_cast<int*> (a), n, m);
    

    return 0;
}
