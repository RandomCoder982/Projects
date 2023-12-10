#include<iostream>
#include<time.h>


using namespace std;

float add(float x, float y) {
  cout << "Choose your first number: " << std::endl;
  cin >> x;
  cout << "Choose your second number: ";
  cin >> y;
  return x + y;
}

float subtract(float x, float y){
  cout << "Choose your first number: " << std::endl;
  cin >> x;
  cout << "Choose your second number: ";
  cin >> y;
  return x - y;
}

float divide(float x, float y){
  cout << "Choose your first number: " << std::endl;
  cin >> x;
  cout << "Choose your second number: ";
  cin >> y;
  return x/y;
}

float multiply(float x, float y){
  cout << "Choose your first number: " << std::endl;
  cin >> x;
  cout << "Choose your second number: ";
  cin >> y;
  return x * y;
}

int main(){
  int run = 0;
  int operation;

  while (run < 5)
  {
    cout << "\nChoose an operation. \n +(1) -(2) x(3) /(4) ";
    cin >> operation;
    switch (operation)
    {
    case 1:
      cout << "\nYour answer is: " <<  add(0, 0) << "\n";
      break;
    case 2:
      cout << "\nYour answer is: " << subtract(0, 0) << "\n";
      break;
    case 3:
      cout << "\nYour answer is: " << multiply(0, 0) << "\n";
      break;
    case 4:
      cout << "\nYour answer is: "<< divide(0, 0) << "\n";
      break;
    
    default:
      cout << "\nTbat is not a valid operation\n";
      break;
    }
    run++;
  } 
}
