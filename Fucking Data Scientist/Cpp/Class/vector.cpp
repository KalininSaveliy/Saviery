#include <iostream>


// Массив с дополнительными функциями
template <typename T>
class MyVector
{
    private:
        T* data;
        int length;
        int fullness;
    public:
        MyVector()  // как сделать инициализацию в виде a = {3,2,1} ?
        {
            data = new T[1];
            fullness = 0;   // from 0 to n
            length = 1;  // from 0 to n
        }
        T* begin()
        {
            return data;
        }
        int size()
        {
            return fullness;
        }
        int capacity()
        {
            return length;
        }
        void pop_back()
        {
            if (fullness == 0)  // write normal exception
                std::cout << "You pop_back an empty vector. Bad idea" << '\n';
            fullness--;
        }
        void push_back(const T x)
        {
            if (fullness == length)
            {
                length *= 2;
                T* tmp = new T[length];
                for (int i = 0; i < fullness; ++i)
                    tmp[i] = data[i];
                delete[] data;
                data = tmp;
            }
            data[fullness] = x;
            fullness++;
        }
        T operator [] (const int i)
        {
            if (i >= fullness)
                std::cout << "It's not your memory" << '\n';
            return data[i];
        }
        void operator = (MyVector right_vec) // вот эту идею скатал у друга
        {
            delete[] data;
            data = right_vec.begin();
            fullness = right_vec.size();
            length = right_vec.capacity();
        }
        // тут должна быть куча строк про итераторы, но в питоне оно проще
        ~MyVector()
        {
            delete[] data;
        }
};


int main()
{
    MyVector <int>a;
    a.push_back(7);
    a.pop_back();
    std::cout << a.size() << a.capacity() << *(a.begin()) << '\n';  // 0, 1, 7
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    MyVector <int>b = a;
    b.pop_back();
    b.pop_back();
    std::cout << b.size() << b.capacity() << *(b.begin()) << b[0] << '\n';  // 1, 4, 1, 1

    return 0;
}
