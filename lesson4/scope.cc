#include<bits/stdc++.h>

int a = 5;

int main () {
  int a = 6;

  if (a == 6) {
    int a = 7;
    std::cout << a << std::endl; // 7
  }
  std::cout << a << std::endl; // 6
}
