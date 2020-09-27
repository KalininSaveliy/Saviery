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
        Complex();
        explicit Complex(double r)
        {
            re = r;
            im = 0.0;
        }
        Complex(double real = 1.0, double image = 0.0)
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
        Complex reverse()  // обратное число  
        {
            double abs = this->abs();
            if (abs == 0)
                std::cout << "Error: 0 division" << '\n';
            Complex rev(re / abs, -im / abs);
            return rev;
        }
        friend bool operator==(const Complex& lhs, const Complex& rhs)
        {
            return ((lhs.re == rhs.re) && (lhs.im == rhs.im)) ? true : false;
        }
        friend bool operator!=(const Complex& lhs, const Complex& rhs)
        {
            return (lhs == rhs) ? false : true;
        }
        friend Complex operator+(const Complex& lhs, const Complex& rhs)
        {
            Complex res(lhs.re + rhs.re, lhs.im + rhs.im);
            return res;
        }
        void operator+=(const Complex& rhs)
        {
            *this = *this + rhs;
        }
        friend Complex operator-(const Complex& lhs, const Complex& rhs)
        {
            Complex res(lhs.re - rhs.re, lhs.im - rhs.im);
            return res;
        }
        void operator-=(const Complex& rhs)
        {
            *this = *this - rhs;
        }
        Complex operator-()
        {
            return (0.0, 0.0) - *this;
        }
        friend Complex operator*(const Complex& lhs, const Complex& rhs)
        {
            Complex res(lhs.re * rhs.re - lhs.im * rhs.im,
                        lhs.re * rhs.re + lhs.im * rhs.re);
            return res;
        }
        void operator*=(const Complex& rhs)
        {
            *this = *this * rhs;
        }
        friend Complex operator/(const Complex& lhs, Complex& rhs)  // я хочу cooooonst
        {
            Complex res = lhs * rhs.reverse();
            return res;
        }
        void operator/=(Complex& rhs)
        {
            *this = *this / rhs;
        }
        friend std::ostream& operator<<(std::ostream os, const Complex& rhs)
        {
            return os << rhs.re << " + i * " << rhs.im;
        }
};



int main()
{
    Complex a(3, 4);
    std::cout << "Expected: 3 -4 5: " << a.conjugate().Re() << a.conjugate().Im() << a.conjugate().abs() << '\n';
    
    std::cout << "Expected: (6,8) (6,8) (-1,24) (1.5,2) (0.6,-0.8) (6,-8) (1,0): \n" << a*2 << 2*a << a*a << a/2 << a.reverse() << 10/a << a/a << '\n';
    Complex b = a;
    if (a == b)
        std::cout << " \"==\" Ok" << '\n';
    else
        std::cout << "Probelms with ==" << '\n';
    if (-a != b)
        std::cout << " \"!=\" Ok" << '\n';
    else
        std::cout << "Probelms with !=" << '\n';

    return 0;
}
