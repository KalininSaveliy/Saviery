#include <cmath>
#include <iostream>
#include <ostream>



// класс комплексных чисел в алгебраическом виде: a + i*b
class Complex  
{
    private:
        double re;  // действительная часть
        double im;  // мнимая часть
    public:
        explicit Complex(double real = 1.0, double image = 0.0)
        {
            re = real;
            im = image;
        }
        double Re()
        {
            return re;
        }
        double Im()
        {
            return im;
        }
        double abs()
        {
            return sqrt(re*re + im*im);  // а здесь точно видно sqrt ?
        }
        Complex conjugate()  // сопряженное
        {
            Complex z(re, -im);
            return z;
        }
        Complex reverse()  // обратно число  
        {
            Complex rev(re / (re*re + im*im), -im / ((re*re + im*im)));
            return rev;
        }
        // Complex operator++();     // pre incriment
        // Complex operator++(int);  // post incriment
        bool operator == (Complex z)  // or use Complex &z ?
        {
            return ((re == z.Re()) && (im == z.Im())) ? true : false;
        }
        bool operator != (const Complex z)
        {
            return (*this == z) ? false : true;
        }
        void operator += (Complex z)
        {
            re += z.Re();  // or {  *this = z + *this; } ?
            im += z.Im();
        }
        void operator += (double x)
        {
            re += x; 
            im += x;
        }
        void operator -= (Complex z)
        {
            re -= z.Re();
            im -= z.Im();
        }
        void operator -= (double x)
        {
            re -= x; 
            im -= x;
        }
        void operator *= (Complex z)
        {
            re -= re * z.Re() - im * z.Im();
            im -= re * z.Im() + im * z.Re();
        }
        void operator *= (double x)
        {
            re *= x; 
            im *= x;
        }
        template <typename T>
        void operator /= (T z)
        {
            Complex tmp = *this / z;
            *this = tmp;
        }
        Complex operator + (Complex z)
        {
            Complex res(re + z.Re(), im + z.Im());  // не хочет жить с const
            return res;
        }
        Complex operator + (const double x)  // а если будет не double? мне шаблон писать, или пусть компилятор типы приводит?
        {
            Complex res(re + x, im);  // or {  Complex tmp(x,0);  return *this * tmp;} ?
            return res;
        }
        Complex operator - (Complex z)
        {
            Complex res(re - z.Re(), im - z.Im());
            return res;
        }
        Complex operator - (const double x)
        {
            Complex res(re - x, im);
            return res;
        }
        Complex operator * (Complex z)
        {
            Complex res(re * z.Re() - im * z.Im(), re * z.Im() + im * z.Re());
            return res;
        }
        Complex operator * (const double x)
        {
            Complex res(re * x, im * x);
            return res;
        }
        Complex operator / (Complex z)
        {
            if (z.Re() == 0 && z.Im() == 0)  // write normal exception
                std::cout << "Heeeeeelp, 0 divison" << '\n';
            else
            {
                Complex res = *this * z.reverse();  // надеюсь, это скромное равно ничего не скрывает
                return res;
            }
        }
        Complex operator / (const double x)
        {
            if (x == 0)
                std::cout << "Heeeeeelp, 0 divison" << '\n';
            else
            {
                Complex res(re / x, im / x);
                return res;
            }
        }
        // ~Complex();  // и что тут писать ?
};


// А зачем вставлять это в класс ( friend Complex operator+ (double lval, Complex rval); ) ?
// Чтобы заменит z.Re() на z.re ?
std::ostream& operator << (std::ostream out, Complex z)
{
    return out << "(" << z.Re() << ", " << z.Im() << ")";
}
Complex operator+ (const double lval, Complex rval)
{
    return rval + lval;
}
Complex operator- (const double lval, Complex rval)
{
    return rval - lval;
}
Complex operator- (Complex z)
{
    return 0 - z;
}
Complex operator* (const double lval, Complex rval)
{
    return rval * lval;
}
Complex operator/ (const double lval, Complex rval)
{
    return rval / lval;
}



int main()
{
    Complex a(3, 4);
    std::cout << "Expected: 3 -4 5" << a.conjugate().Re() << a.conjugate().Im() << a.conjugate().abs() << '\n';
    
    std::cout << "Expected: (6,8) (6,8) (-1,24) (1.5,2) (0.6,-0.8) (6,-8) (1,0): \n" << a*2 ;//<< 2*a << a*a << a/2 << a.reverse() << 10/a << a/a << '\n';
    Complex b = a;
    if (a == b)
        std::cout << "Ok" << '\n';
    else
        std::cout << "Probelms with ==" << '\n';
    if (-a != b)
        std::cout << "Ok" << '\n';
    else
        std::cout << "Probelms with !=" << '\n';

    return 0;
}
