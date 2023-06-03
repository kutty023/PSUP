// Sum of extracted digits (using C++)

#include <iostream>
using namespace std;
int main() {
    // Take input for n1 and n2
    int n1, n2;
    cin >> n1 >> n2;

    // Check if either number is less than 10
    if (n1 < 10 || n2 < 10) {
        // If either number is less than 10, print an error message
        cout << "Invalid number";
    } 
    else {
        // If both numbers are greater than or equal to 10, proceed with the calculation
        // Divide n1 and n2 by 10 to extract the tens digit
        int digit1 = n1 / 10;
        int digit2 = n2 / 10;

        // Take the modulo of the result with 10 to get the ones digit
        // and add the ones digits together to get the sum
        int sum = (digit1 % 10) + (digit2 % 10);

        // Print the sum as an integer
        cout << sum;
    }

    return 0;
}
