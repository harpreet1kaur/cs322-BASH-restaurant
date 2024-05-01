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

	int findDifference(Time secondTime) {

		if (hour > secondTime.getHour()) {
			return secondTime.getHour() * 60 + secondTime.getMinute() + (24 - hour) * 60 + (60 - minute);
		}

		return (secondTime.getHour() - hour) * 60 + (secondTime.getMinute() - minute);
	}

	void minutesToTime(int minutes) {
		hour = minutes / 60;
		minute = minutes % 60;
	}

	bool subtractHour() {
		if (hour == 0)
		{
			hour == 23;
			return 1;
		}
		else {
			hour--;
			return 0;
		}
	}

	bool operator == (Time& compareTime) {
		if (hour == compareTime.getHour() && minute == compareTime.getMinute());
		{
			return 1;
		}
		return 0;
	}

private:
	int hour;
	int minute;
};

#endif