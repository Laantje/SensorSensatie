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

uint16_t get_lightpercent(){								// Get % light