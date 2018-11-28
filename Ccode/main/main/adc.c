/*
 * adc.c
 *
 * Created: 11/6/2018 11:58:42 AM
 *  Author: Laantje
 */ 

#include <avr/io.h>
#include <util/delay.h>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>

void init_adc()
{
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)
	ADMUX = (1<<REFS0);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}uint16_t read_adc(uint8_t channel){
	ADMUX &= 0xF0;                  //Clear the older channel that was read
	ADMUX |= channel;               //Defines the new ADC channel to be read
	_delay_ms(10);					// Start the AD conversion
	ADCSRA|=0x40;					// Wait for the AD conversion to complete
	while ((ADCSRA & 0x10)==0);
	ADCSRA|=0x10;
	return ADC;                    //Returns the ADC value of the chosen channel
}
