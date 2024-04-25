#pragma once
#ifndef __ITEM_H
#define __ITEM_H

#include "dataManagement.hpp"

class Item {
public:
	Item() {
		itemName = "";
		quantity = -1;
		price = -1;
	}

	Item(std::string name, int num, float knownPrice) {
		itemName = name;
		quantity = num;
		price = knownPrice;
	}

	~Item() {

	}

	void setItemName(std::string newName) {
		itemName = newName;
	}

	std::string getItemName() {
		return itemName;
	}

	void setQuantity(int newQuantity) {
		quantity = newQuantity;
	}

	int getQuantity() {
		return quantity;
	}

	void setPrice(float newPrice) {
		price = newPrice;
	}

	float getPrice() {
		return price;
	}

	//class functions

	void fillItem(std::string rawString) {
		std::stringstream stringSplitter(rawString);
		std::string stringHolder;
		int toInt;
		float toFloat;

		getline(stringSplitter, stringHolder, '|');
		itemName = stringHolder;
		getline(stringSplitter, stringHolder, '|');
		toInt = stoi(stringHolder);
		quantity = toInt;
		getline(stringSplitter, stringHolder, '|');
		toFloat = stof(stringHolder);
		price = toFloat;
	}
private:
	std::string itemName;
	int quantity;
	float price;
};

#endif