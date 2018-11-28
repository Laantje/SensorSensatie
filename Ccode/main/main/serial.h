/*
 * serial.h
 *
 * Created: 11/6/2018 12:07:42 PM
 *  Author: Laantje
 */ 


#ifndef SERIAL_H_
#define SERIAL_H_

void send(uint8_t data);
char receive();
void send_char(char c);
void send_string(char s[]);
void transmitln(const char* line);
void sendInfo(const char* buff);
void setPoep(int val);


#endif /* SERIAL_H_ */