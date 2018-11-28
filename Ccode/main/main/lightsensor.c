/*
 * lightsensor.c
 *
 * Created: 11/6/2018 12:03:20 PM
 *  Author: Laantje
 */ 


#include <avr/io.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>
#include "serial.h"

uint16_t get_lightpercent(){								// Get % light	uint16_t percent = read_adc(3);							//0 - 1024 light	return percent;}void sendLight(void){	char buffer [10];	sprintf(buffer, "%u", get_lightpercent());	sendInfo(buffer);}