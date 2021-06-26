#include <iostream>
using namespace std;

// array program

template <typename T>
void array_function()
{
    int size;

    T *p;

    cout << "Enter the size of array:\n";
    cin >> size;
    
    p = new T[size];

    cout << "Enter data into the array:" << endl;

    for (int i = 0; i < size; i ++)
    {
        cin >> p[i];
    }

    cout << "Printing the data: " << endl;
    for(int i = 0; i < size; i ++)
    {
        cout << p[i] << endl;
    }

}

int main()
{
    char choice;


    while(true)
    {

        cout << "Enter datatype which you want to store in the array" << endl;
        cout << "s for string, i for int, f for float" << endl;
        cin >> choice;

        if(choice == 's')
        {
            array_function<string>();
            break;
        }
        else if(choice == 'i')
        {
            array_function<int>();
            break;
        }
        else if(choice == 'f')
        {
            array_function<float>();
            break;
        }
        else
        {
            cout << "Sorry incorrect choice enter again!" << endl;
        } 
    }

}