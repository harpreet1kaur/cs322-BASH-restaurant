#pragma once
#ifndef __ORDER_H
#define __ORDER_H

#include "item.hpp"
#include "time.hpp"

class Order {
public:
	Order() {
		itemList.resize(0);
	}

	~Order() {
		itemList.clear();
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

	void setItemList(std::vector<Item> newList) {
		itemList = newList;
	}

	std::vector<Item> getItemList() {
		return itemList;
	}

	//class functions

	void fillOrder(std::string rawString) {
		std::stringstream stringSplitter(rawString);
		std::string stringHolder;
		getline(stringSplitter, stringHolder, ',');
		startTime.fill(stringHolder);
		getline(stringSplitter, stringHolder, ',');
		finishTime.fill(stringHolder);
		while (true) {
			getline(stringSplitter, stringHolder, ',');
			if (stringHolder.compare("") == 0) {
				return;
			}
			itemList.resize(itemList.size() + 1);
			itemList[itemList.size() - 1].fillItem(stringHolder);
		}
	}

private:
	Time startTime;
	Time finishTime;
	std::vector<Item> itemList;
};

#endif