//Print 1/0 based on the character input using c++

#include <iostream>
using namespace std; 

int main() // Entry point of the program
{
    char x; // Declare a character variable to store the input value
    cin >> x; // Read the input value from the user

    if (x == 'a' || x == 'e' || x == 'i' || x == 'o' || x == 'u') { // Check if the character is 'a', 'e', 'i', 'o', or 'u'
        cout << 1; // If it is, print 1
    } else {
        cout << 0; // If it's not, print 0
    }

    return 0; // Return 0 to indicate successful program execution
}
