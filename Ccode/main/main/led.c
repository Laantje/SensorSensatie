/*
 * led.c
 *
 * Created: 11/8/2018 11:49:29 AM
 *  Author: Laantje
 */ 

#include <avr/io.h>
#include <stdio.h>

void initLeds() {
	DDRD |= _BV(PIND5); // Pin 5 output redLED
	DDRD |= _BV(PIND6); // Pin 6 output yellowLED
	DDRD |= _BV(PIND7); // Pin 7 output greenLED
}

void setRedLed(int val) {
	if(val == 0) {
		PORTD &= 0b11011111;
	}
	else {
		PORTD |= 0b00100000;
	}
}

void setGreenLed(int val) {
	if(val == 0) {
		PORTD &= 0b01111111;
	}
	else {
		PORTD |= 0b10000000;
	}
}

void setYellowLed(int val) {
	if(val == 0) {
		PORTD &= 0b10111111;
	}
	else {
		PORTD |= 0b01000000;
	}
}