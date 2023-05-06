#include <stdio.h>

int main() {
	int a = 8;
	int *p = &a + 1;
	int *q = &a;
	int r = *q + 1;
	printf("a = %d\n", a);
	printf("a = %p\n", &a);
	printf("*p = %d\n", *p);
	printf("p = %p\n", p);
	printf("r = %d\n", r);
	printf("r = %p\n", &r);
	return (0);
}
