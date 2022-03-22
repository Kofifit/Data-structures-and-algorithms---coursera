#include <iostream>

int get_change(int m) {
	// We have the following coins 1,5,10
	int n, coin10, coin5, coin1;
	coin10 = m / 10;
	m = m % 10;
	coin5 = m / 5;
	m = m % 5;
	coin1 = m / 1;
	n = coin10 + coin5 + coin1;
	return n;
}

int main() {
	int m;
	std::cin >> m;
	std::cout << get_change(m) << '\n';
}
