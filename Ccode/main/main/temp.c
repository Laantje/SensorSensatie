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

uint16_t getTemp()
	char buffer [10];
	sendInfo(buffer);
}