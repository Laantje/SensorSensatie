/*
 * state.c
 *
 * Created: 11/9/2018 10:23:52 AM
 *  Author: Laantje
 */ 
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#include <stdlib.h>
#include "led.h"
#include "ultrasoon.h"

int state = 0; // 0 = idle, 1 = open, 2 = close
int progression = 0; //0 = fully closed
int interrupt = 0;
int maxUitrol = 10;
int isWorking = 0;

char uitrolBuffer[20];

void openScreen() {
	setGreenLed(1);
	setRedLed(0);
	
	state = 1;
	
	interrupt = 0;
}

void closeScreen() {
	setGreenLed(0);
	setRedLed(1);
	
	state = 2;
	
	interrupt = 0;
}

void setMaxUitrol(char val[]) {
	int i;
	
	if(strlen(val) == 4) {
		i = i + (val[1] * 100);
		i = i + (val[2] * 10);
		i = i + val[3];
	}
	else if(strlen(val) == 3) {
		i = i + (val[1] * 10);
		i = i + val[2];
	}
	else if(strlen(val) == 2) {
		i = i + val[1];
	}		
	
	maxUitrol = i;
}

int getStatus() {
	return state;
}

void ledHandler() {
	if(state == 0) {
		setYellowLed(0);
	}
	
	if(state == 1 && progression < maxUitrol && isWorking == 0) {
		isWorking = 1;
		_delay_ms(5000);
		setYellowLed(1);
		_delay_ms(5000);
		setYellowLed(0);
		progression++;
		isWorking = 0;
	}
	else if(state == 2 && progression > 0 && isWorking == 0) {
		isWorking = 1;
		_delay_ms(5000);
		setYellowLed(1);
		_delay_ms(5000);
		setYellowLed(0);
		progression--;
		isWorking = 0;
	}
	
	//set to idle when done
	if(state == 2 && progression <= 0 || state == 1 && progression >= maxUitrol) {
		state = 0;
		interrupt = 0;
		isWorking == 0;
	}
	
	/*if(isWorking == 0) {
		isWorking == 1;
		//State handler
		if(state == 0) {
			setYellowLed(0);
			isWorking == 0;
		}
		else if(state == 1) {
			interrupt = 1;

			if(progression < maxUitrol && interrupt == 1) {
				_delay_ms(5000);
				setYellowLed(1);
				_delay_ms(5000);
				setYellowLed(0);
				progression++;
				if(getDistance() < 250) {
					interrupt = 0;
					progression = maxUitrol;
				}
				isWorking = 0;
			}
		
		/*do
		{
			progression++;
			_delay_ms(5000);
			setYellowLed(1);
			_delay_ms(5000);
			setYellowLed(0);
			if(getDistance() < 250) {
				interrupt = 0;
				progression = maxUitrol;
			}
		}
		while (progression < maxUitrol && interrupt == 1 && state == 1);		
		}
		else if(state == 2) {		
			interrupt = 1;

			if(progression > 0 && interrupt == 1 && isWorking == 0) {
				_delay_ms(5000);
				setYellowLed(1);
				_delay_ms(5000);
				setYellowLed(0);
				progression--;
				if(getDistance() < 250) {
					interrupt = 0;
					progression = 0;
				}
				isWorking = 0;
			}
		
			do
			{
				progression--;
				_delay_ms(5000);
				setYellowLed(1);
			_delay_ms(5000);
			setYellowLed(0);
			if(getDistance() < 250) {
				interrupt = 0;
				progression = 0;
			}
			
		}
		while (progression > 0 && interrupt == 1 && state == 2);
		}
	
		
	}*/
}

void sendMsg(int val) {
	char buffer [10];	sprintf(buffer, "%u", val);
	transmitln(buffer);
}