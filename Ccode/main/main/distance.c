/*
 * distance.c
 *
 * Created: 11/7/2018 10:17:10 AM
 *  Author: Laantje
 */

#define F_CPU 16E6
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h> 

#define TrigPin PIND3
#define EchoPin PIND2

uint8_t get_distance(){
	//send a pulse
	PORTD &= ~(1<<TrigPin);			// Set Trigger Pin To 0
	_delay_ms(40);					// Wait
	PORTD |= (1<<TrigPin);			// Set Trigger Pin To 1
	_delay_ms(40);					// Wait
	PORTD &= ~(1<<TrigPin);			// Set Trigger Pin To 0
	//Get distance
	TCNT0 = 0;
	while ((PIND & EchoPin)	== 0);
	TCCR0B |= (1 << CS02) | (1 << CS00);
	while ((PIND & EchoPin) > 0);
	TCCR0B = 0;
	uint8_t time = TCNT0;
	time *= 1.097;
	return time;
}