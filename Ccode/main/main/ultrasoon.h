/*
 * ultrasoon.h
 *
 * Created: 11/13/2018 12:06:59 PM
 *  Author: Laantje
 */ 


#ifndef ULTRASOON_H_
#define ULTRASOON_H_

void Trigger_Pulse(void);
void initUltraSensor(void);
void sendDistance(void);
uint16_t getDistance(void);

#endif /* ULTRASOON_H_ */