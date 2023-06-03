// print 1/0 based on the integer input using C++

#include <iostream> 
using namespace std; 

int main() 
{
    int x; // Declare an integer variable to store the input value
    cin >> x; // Read the input value from the user

    cout << bool(x > 100); // Print the result of the expression x > 100, which is either true or false, as a boolean value

    return 0; // Return 0 to indicate successful program execution
}
