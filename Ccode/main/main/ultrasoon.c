/*
 * ultrasoon.c
 *
 * Created: 11/13/2018 12:06:49 PM
 *  Author: Laantje
 */ 

#include <avr/io.h>
#include <util/delay.h>
#include <util/atomic.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "serial.h"

#define F_CPU 16E6

uint16_t numuS;
uint8_t oldSREG;
uint16_t sendValue;

void initUltraSensor() {
	DDRC |= (1<<DDC5) | (1<<DDC4);
	DDRC &= ~(1<<DDC5);						// Set Pin C5 as input to read Echo
	PORTC |= (1<<PORTC5);					// Enable pull up on C5
	PORTC &= ~(1<<PC4);						// Init C4 as low (trigger)

	PRR &= ~(1<<PRTIM1);					// To activate timer1 module
	TCNT1 = 0;								// Initial timer value
	TCCR1B |= (1<<CS10);					// Timer without prescaller. Since default clock for atmega328p is 1Mhz period is 1uS
	TCCR1B |= (1<<ICES1);					// First capture on rising edge

	PCICR = (1<<PCIE1);						// Enable PCINT[14:8] we use pin C5 which is PCINT13
	PCMSK1 = (1<<PCINT13);					// Enable C5 interrupt
	sei();									// Enable Global Interrupts
}

void Trigger_Pulse()
{
	PORTC |= (1<<PC4);						// Set trigger high
	_delay_us(10);							// for 10uS
	PORTC &= ~(1<<PC4);						// to trigger the ultrasonic module
}

ISR(PCINT1_vect) {
	if (bit_is_set(PINC,PC5)) {					// Checks if echo is high
		TCNT1 = 0;								// Reset Timer
	} else {
		numuS = TCNT1;							// Save Timer value
		uint8_t oldSREG = SREG;
		cli();									// Disable Global interrupts

		SREG = oldSREG;							// Enable interrupts
	}
}

uint16_t getDistance(void) {
	int i = numuS;
	
	while(i == numuS) {
		Trigger_Pulse();
	}
	
	sendValue = numuS / 58;
	
	return sendValue;
}

void sendDistance(void) {	
	int i = numuS;
	
	while(i == numuS) {
		Trigger_Pulse();
	}
	
	sendValue = numuS / 58;
	
	char buffer [20];	sprintf(buffer, "%u", sendValue);	sendInfo(buffer);
}