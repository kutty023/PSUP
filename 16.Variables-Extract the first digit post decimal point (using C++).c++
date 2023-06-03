// Extract the first digit post decimal point using c++

#include <iostream> // Include the iostream library for input/output operations

using namespace std; // Use the standard namespace

int main() // Entry point of the program
{
    float n; // Declare a float variable to store the input number
    cin >> n; // Read the input number from the user

    if (n < 10) // Check if the number is less than 10
        cout << ((-int(n * 10)) % 10); // Multiply n by 10, convert it to an integer, negate it, and take modulo 10. Print the result.
    else
        cout << ((int(n * 10)) % 10); // Multiply n by 10, convert it to an integer, and take modulo 10. Print the result.

    return 0; // Return 0 to indicate successful program execution
}
