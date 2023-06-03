// Print the 4th letter of the given name using c++

#include <iostream> 
using namespace std;

int main() // Entry point of the program
{
    string name; // Declare a string variable to store the input value
    cin >> name; // Read the input value from the user

    if (name.size() < 4) { // Check if the size of the string is less than 4
        cout << 0; // If it is, print 0
    } else {
        cout << name[3]; // If it's not, print the character at index 3 of the string
    }

    return 0; // Return 0 to indicate successful program execution
}