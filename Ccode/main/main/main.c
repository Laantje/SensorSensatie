/*
 * main.c
 *
 * Created: 11/6/2018 11:54:27 AM
 *  Author: Laantje
 */ 


#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "serial.h"
#include "lightsensor.h"
#include "AVR_TTC_scheduler.h"
#include "adc.h"
#include "uart.h"
#include "distance.h"
#include "convert.h"
#include "mode.h"
#include "state.h"
#include "led.h"
#include "commands.h"
#include "ultrasoon.h"

#define F_CPU 16E6

char bufferLight[20];
char bufferTemp[20];
char bufferFinal;

int main(void)
{
	uart_init();
	initUltraSensor();
	init_adc();
	initLeds();
	
	setMode(1);

	SCH_Init_T1();
	
	SCH_Add_Task(ledHandler,0,1); // Add ledhandler task
	SCH_Add_Task(checkCommands,0,1); // Add commands task
	//SCH_Add_Task(sendPulse,0,1); // Add sendinfo task
	//SCH_Add_Task(sendDistInfo,0,5); // Add sendinfo task
	
	_delay_ms(1000);
	
	SCH_Start();
	
	//DDRD = 0b11101000;
	
    while(1)
    {
		SCH_Dispatch_Tasks(); 
	}    
	
	return 0;
}