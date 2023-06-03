// Extract 2nd last digit (using C++)

#include <iostream>
using namespace std;
int main() 
{
    // Declare an integer variable num
    int num;
    // Take input for num
    cin>>num;
    // Check if num is less than 10
    if (num<10)
        // If num is less than 10, print an error message
        cout<<"Invalid number";
    else
        // If num is 10 or greater, extract the tens digit of num and print it
        cout <<(int((num/10)%10));
    // End the program
    return 0;
}
