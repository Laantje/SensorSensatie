/*
 * temp.c
 *
 * Created: 11/6/2018 12:25:21 PM
 *  Author: Laantje
 */ 

#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>
#include "serial.h"

char sendBuffer[20];

uint16_t getTemp(){	uint16_t degreesC = read_adc(0);	float voltage = degreesC * 5.0;	voltage /= 1024.0;	float celsius = (voltage - 0.5) * 100;	celsius *= 100;	return (uint16_t)celsius;}void sendTemp() {
	char buffer [10];	sprintf(buffer, "%u", getTemp());
	sendInfo(buffer);
}