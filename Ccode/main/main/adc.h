/*
 * adc.h
 *
 * Created: 11/6/2018 12:13:22 PM
 *  Author: Laantje
 */ 


#ifndef ADC_H_
#define ADC_H_

void init_adc();
uint16_t read_adc(uint8_t channel);

#endif /* ADC_H_ */