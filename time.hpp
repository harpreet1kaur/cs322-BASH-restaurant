#pragma once
#ifndef __TIME_H
#define __TIME_H

#include "dataManagement.hpp"

class Time {
public:
	Time() {

	}

	Time(int newHour, int newMinute) {
		hour = newHour;
		minute = newMinute;
	}

	~Time() {

	}

	void setHour(int newHour) {
		hour = newHour;
	}

	int getHour() {
		return hour;
	}

	void setMinute(int newMinute) {
		minute = newMinute;
	}

	int getMinute() {
		return minute;
	}

	//class functions

	void fill(std::string timeString){
		std::stringstream stringSplitter(timeString);
		std::string stringHolder;
		getline(stringSplitter, stringHolder, ':');
		hour = stoi(stringHolder);
		getline(stringSplitter, stringHolder);
		minute = stoi(stringHolder);
	}

	std::string print() {
		std::stringstream stringBuilder;
		stringBuilder << hour << ':' << minute;
		return stringBuilder.str();
	}

private:
	int hour;
	int minute;
};

#endif