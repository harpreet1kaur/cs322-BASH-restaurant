#pragma once
#ifndef __DATE_H
#define __DATE_H

#include "dataManagement.hpp"

class Date {
public:
	Date() {

	}

	Date(int newDay, int newMonth, int newYear) {
		day = newDay;
		month = newMonth;
		year = newYear;
	}

	Date(std::string dateString) {

	}

	~Date(){
	
	}

	void setDay(int newDay) {
		day = newDay;
	}

	int getDay() {
		return day;
	}

	void setMonth(int newMonth) {
		month = newMonth;
	}

	int getMonth() {
		return month;
	}

	void setYear(int newYear) {
		year = newYear;
	}

	int getYear() {
		return year;
	}

	//class functions

	void fill(std::string dateString) {
		std::stringstream stringSplitter(dateString);
		std::string stringHolder;
		getline(stringSplitter, stringHolder, '-');
		day = stoi(stringHolder);
		getline(stringSplitter, stringHolder, '-');
		month = stoi(stringHolder);
		getline(stringSplitter, stringHolder);
		year = stoi(stringHolder);
	}

	std::string print() {
		std::stringstream stringBuilder;
		stringBuilder << day << '-' << month << '-' << year;
		return stringBuilder.str();
	}

	bool operator == (Date compareDate) {

		if (day == compareDate.getDay() && month == compareDate.getMonth() && year == compareDate.getYear())	{
			return 1;
		}
		return 0;
	}

	void subtractDay() {
		if (day == 1) {
			//previous month has 31 days
			if (month == 2 || month == 4 || month == 6 || month == 8 || month == 9 || month == 11) {
				day = 31;
				month--;
			}
			//previous month has 30 days
			if (month == 5 || month == 7 || month == 10 || month == 12) {
				day = 30;
				month--;
			}
			//previous month is Febuary
			if (month == 3) {
				//leap year
				if (year % 4 == 0) {
					day = 29;
				}
				else {
					day = 28;
				}
				month--;
			}
			//previous month is in last year
			if (month == 1) {
				month = 12;
				year--;
			}
		}
		else {
			day--;
		}
	}

private:
	int day;
	int month;
	int year;
};

#endif