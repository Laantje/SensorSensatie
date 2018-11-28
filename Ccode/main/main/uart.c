/*
 * init.c
 *
 * Created: 11/6/2018 12:11:45 PM
 *  Author: Laantje
 */ 

#include <avr/io.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>
#include "serial.h"

#define F_CPU 16E6
#define UBBRVAL 51

void uart_init()
{
	// Set baudrate 19200
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
	//Effe handshaken
	handshake();
}