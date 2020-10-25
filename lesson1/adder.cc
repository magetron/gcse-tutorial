#include <iostream>

int add (int a, int b) {
  return a + b;
}

int main () {
  int a, b;
  std::cout << "a:"; // print a:
  std::cin >> a;     // read a
  std::cout << "b:"; // print b:
  std::cin >> b;     // read b
  std::cout << a << " + " << b << " = " << add(a, b) << std::endl; // print formula
  return 0;
}
