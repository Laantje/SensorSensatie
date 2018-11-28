/*
 * serial.c
 *
 * Created: 11/6/2018 12:00:33 PM
 *  Author: Laantje
 */ 
#include <avr/io.h>
#include <string.h>
#include <stdlib.h>
#include <util/delay.h>
#include <stdio.h>
#include <avr/sfr_defs.h>

char sendBuffer[20];
int poep = 0;

void send(uint8_t data)
{
	loop_until_bit_is_set(UCSR0A, UDRE0);
	UDR0 = data;
}

char receive()
{
	if(poep == 0) {
		loop_until_bit_is_set(UCSR0A, RXC0);
		return UDR0;
	}	
	
	if(UCSR0A & _BV(RXC0) && poep == 1) {
		return UDR0;
	}	 
}

void setPoep(int val) {
	poep = val;
}
void transmitln(const char* line) {//const char* -> string in de functie definitie	for(size_t i=0; i<strlen(line); i++){		send(line[i]);	}	send('\n');}	

void send_char(char c)
{
	while ((UCSR0A & (1 << UDRE0)) == 0) {};
	UDR0 = c;
}

void send_string(char s[])
{
	int i =0;
	
	//Make sure its 4 bytes
	switch(strlen(s)) {
		case 5:
			for(int i; i<3; i++) {
				send_char(0x30);
			}
			break;
		case 6:
			for(int i; i<2; i++) {
				send_char(0x30);
			}
			break;
		case 7:
			send_char(0x30);
			break;
	}
	
	//Send the value
	while (s[i] != 0x00)
	{
		send_char(s[i]);
		i++;
	}
}

void sendInfo(const char* buff) {	transmitln(buff); // verstuur variabele "woord"
	_delay_ms(100); // wacht een seconde}