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

private:
	int day;
	int month;
	int year;
};

#endif