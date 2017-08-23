#include <wiringPi.h>

void udelay(int n)
{
	volatile int i;
	for (i=0; i<n; ++i);
}

int main (void)
{
	int i;
	wiringPiSetup () ;
	pinMode (6, OUTPUT) ;
//	for (i = 0; i < 10000; ++i)
	for (;;)
	{
		digitalWrite (6, HIGH) ; 
		udelay (5000) ;
		digitalWrite (6,  LOW) ; 
		udelay (15000) ;
	}
	return 0 ;
}
