#include <iostream>


struct node_t
{
    int data;
    node_t* next;
};


void print_node_array(node_t* begin)
{
    node_t* p = begin;
    while (p != nullptr)
    {
        std::cout << p->data << " ";
        p = p->next;
    }
    std::cout << std::endl;
}


int main()
{
    int n = 5;
    node_t* p_begin = new node_t;
    node_t* p = p_begin;
    std::cout << p;
    for (int i = 0; i < n; ++i)
    {
        p->data = i+1;  // p->data <=> (*p).data
        p->next = new node_t;
        p = p->next;
    }
    p->next = nullptr;
    p->data = 777;

    print_node_array(p_begin);


    return 0;
}
