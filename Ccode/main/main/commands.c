/*
 * commands.c
 *
 * Created: 11/9/2018 2:12:34 PM
 *  Author: Laantje
 */ 
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <stdlib.h>
#include "led.h"
#include "serial.h"
#include "temp.h"
#include "lightsensor.h"
#include "ultrasoon.h"

#define F_CPU 16E6

uint8_t command;
char receiveBuffer[200];
char handshakeBuffer[200];

int screenRequest = 0;

void ser_readln(char *line, uint8_t bufsize) {
	uint8_t p=0;
	char c;
	do {
		c=receive();
		if (c!='\n') {
			line[p++]=c;
		}
		line[p]='\0';
	} while ((c!='\n') && (p<bufsize-1));
}

void handshake(){
	ser_readln(handshakeBuffer, 20);
	
	if (!strcmp(handshakeBuffer, "handshake"))
	{
		transmitln("Hand shaked!");
		setPoep(1);
	}
}

int getScreenRequest() {
	if(screenRequest == 1) {
		screenRequest = 0;
		return 1;
	} 
	else if(screenRequest == 2) {
		screenRequest = 0;
		return 2;
	}
	else {
		return 0;
	}
}

void checkCommands()
{
	ser_readln(receiveBuffer, 200); //lees een regel, doe het in "buffer" met grootte 200	int command = receiveBuffer[0];
	switch(command)
	{
		// Command 1: Update the manual status
		case '1': //Request temp
			sendTemp();
			return;
		case '2': //Request light
			sendLight();
			return;
		case '3': //Request Ultrasoon
			sendDistance();
			return;
		case '4': //Open window
			sendStatus(4444);
			openScreen();
			return;
		case '5': //Close window
			sendStatus(5555);
			closeScreen();
			return;
		case '6': //set uitrolstand
			setMaxUitrol(receiveBuffer);
			sendStatus(6666);
			return;

		default:
			return;
	}
}

void sendStatus(int val) {
	char buffer [10];	sprintf(buffer, "%u", val);
	transmitln(buffer);
}