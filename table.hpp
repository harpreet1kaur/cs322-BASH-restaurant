#pragma once
#ifndef __TABLE_H
#define __TABLE_H

#include "order.hpp"
#include "date.hpp"

class Table {
public:
	Table() {
		orderList.resize(0);
	}

	~Table() {
		orderList.clear();
	}

	void setDate(Date newDate) {
		tableDate = newDate;
	}

	Date getDate() {
		return tableDate;
	}

	void setStart(Time newTime) {
		startTime = newTime;
	}

	Time getStart() {
		return startTime;
	}

	void setFinish(Time newTime) {
		finishTime = newTime;
	}

	Time getFinish() {
		return finishTime;
	}

	void setOrderList(std::vector<Order> newList) {
		orderList = newList;
	}

	std::vector<Order> getOrderList() {
		return orderList;
	}

	//class functions

	void fillTable(std::string rawString) {
		std::stringstream stringSplitter(rawString);
		std::string stringHolder;

		getline(stringSplitter, stringHolder, '/');
		tableDate.fill(stringHolder);
		getline(stringSplitter, stringHolder, '/');
		startTime.fill(stringHolder);
		getline(stringSplitter, stringHolder, '/');
		finishTime.fill(stringHolder);
		while (true) {
			getline(stringSplitter, stringHolder, '/');
			if (stringHolder.compare("") == 0) {
				return;
			}
			orderList.resize(orderList.size() + 1);
			orderList[orderList.size() - 1].fillOrder(stringHolder);
		}
	}

private:
	Date tableDate;
	Time startTime;
	Time finishTime;
	std::vector<Order> orderList;
};

#endif