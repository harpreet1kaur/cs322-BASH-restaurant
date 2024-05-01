#pragma once
#ifndef __ALLDATA_H
#define __ALLDATA_H

#include "table.hpp"

class AllData {
public:
	AllData() {

		std::string stringHolder;

		std::time_t now = time(0);
		char timeCharArr[26];
		ctime_s(timeCharArr, sizeof timeCharArr, &now);
		std::string timeString(timeCharArr);

		infile.open("data.dat");
		while (!getline(infile, stringHolder).eof()) {
			completeData.resize(completeData.size() + 1);
			completeData[completeData.size() - 1].fillTable(stringHolder);
		}
	}

	~AllData() {
		infile.close();
		writeToFile();
	}

	//Class functions

	void mainLoop() {
		calculate(completeData);
	}

	void showHourlyData() {
		//Start at the last and work your way up. List should be sorted with the oldest being the first.
		Time checkTime = completeData[completeData.size() - 1].getFinish();
		Date checkDate = completeData[completeData.size() - 1].getDate();
		int listNav = completeData.size() - 1;
		std::vector<Table> calculationList;

		while (listNav >= 0)
		{
			if (completeData[listNav].getFinish().getHour() == checkTime.getHour() &&
				completeData[listNav].getDate() == checkDate) {
				calculationList.push_back(completeData[listNav]);
			}
			else {
				dataDisplayHour(calculationList, checkTime, checkDate);
				calculationList.clear();
				checkDate = completeData[listNav].getDate();
				checkTime = completeData[listNav].getFinish();
				calculationList.push_back(completeData[listNav]);
			}
			listNav--;
		}

		dataDisplayHour(calculationList, checkTime, checkDate);
	}

	void dataDisplayHour(std::vector<Table> calculationList, Time forTime, Date forDay ) {
		std::cout << forTime.getHour() << ":00 - " << forDay.getMonth() << '/' << forDay.getDay() << '/' << forDay.getYear() << std::endl;
		calculate(calculationList);
	}


	void showDailyData() {
		//Start at the last and work your way up. List should be sorted with the oldest being the first.
		Date checkDate = completeData[completeData.size() - 1].getDate();
		int listNav = completeData.size() - 1;
		std::vector<Table> calculationList;

		while (listNav >= 0)
		{
			if (completeData[listNav].getDate() == checkDate) {
				calculationList.push_back(completeData[listNav]);
			}
			else {
				dataDisplayDay(calculationList, checkDate);
				calculationList.clear();
				checkDate = completeData[listNav].getDate();
				calculationList.push_back(completeData[listNav]);
			}
			listNav--;
		}
		dataDisplayDay(calculationList, checkDate);
	}

	void dataDisplayDay(std::vector<Table> calculationList, Date forDay) {
		std::cout << forDay.getMonth() << '/' << forDay.getDay() << '/' << forDay.getYear() << std::endl;
		calculate(calculationList);
	}

	void calculate(std::vector<Table> calculationList) {
		float revenue;
		Time timeDisplay;
		std::vector<Item> perItemDisplay;

		//revenue
		revenue = calculateRevenue(calculationList);

		std::cout << "Revenue: " << revenue << '$' << std::endl;

		//revenue precentage per item

		perItemDisplay = calculatePerItem(calculationList);

		displayRevenuePrecentage(perItemDisplay, revenue);

		//popularity per item

		displayItemPopularity(perItemDisplay);

		//Turnaround time

		timeDisplay = calculateTurnaround(calculationList);

		std::cout << "Average Turnaround Time: " << timeDisplay.getHour() << ':' << timeDisplay.getMinute() << std::endl;

		//Order completion time.

		timeDisplay = calculateOrderTime(calculationList);

		std::cout << "Average Time To Complete Order: " << timeDisplay.getHour() << ':' << timeDisplay.getMinute() << "\n" << std::endl;


	}

	float calculateRevenue(std::vector<Table> calculationList) {
		float returnable = 0;
		std::vector<Order> currentOrderList;
		std::vector<Item> currentItemList;

		for (int i = 0; i < calculationList.size(); i++) {
			currentOrderList = calculationList[i].getOrderList();
			for (int j = 0; j < currentOrderList.size(); j++) {
				currentItemList = currentOrderList[j].getItemList();
				for (int k = 0; k < currentItemList.size(); k++) {
					returnable += currentItemList[k].getQuantity() * currentItemList[k].getPrice();
				}
			}
		}

		return returnable;
	}

	Time calculateTurnaround(std::vector<Table> calculationList) {
		Time returnable;
		int average = 0;
		for (int i = 0; i < calculationList.size(); i++) {
			average += calculationList[i].getStart().findDifference(calculationList[i].getFinish());
		}
		
		average = average / calculationList.size();

		returnable.minutesToTime(average);

		return returnable;
	}

	Time calculateOrderTime(std::vector<Table> calculationList) {
		Time returnable;
		int average = 0;
		std::vector<Order> currentOrderList;
		for (int i = 0; i < calculationList.size(); i++) {
			currentOrderList = calculationList[i].getOrderList();
			for (int j = 0; j < currentOrderList.size(); j++) {
				average += currentOrderList[j].getStart().findDifference(currentOrderList[j].getFinish());
			}
		}

		average = average / calculationList.size();

		returnable.minutesToTime(average);

		return returnable;

	}

	std::vector<Item>calculatePerItem(std::vector<Table> calculationList) {
		std::vector<Item> returnable;
		std::vector<Order> currentOrderList;
		std::vector<Item> currentItemList;
		bool sharedItem = false;

		for (int i = 0; i < calculationList.size(); i++) {
			currentOrderList = calculationList[i].getOrderList();
			for (int j = 0; j < currentOrderList.size(); j++) {
				currentItemList = currentOrderList[j].getItemList();
				for (int k = 0; k < currentItemList.size(); k++) {
					
					for (int n = 0; n < returnable.size(); n++) {
						if (returnable[n].getItemName().compare(currentItemList[k].getItemName()) == 0) {
							returnable[n].addQuantity(currentItemList[k]);
							sharedItem = true;
						}
					}
					if (!sharedItem) {
						returnable.push_back(currentItemList[k]);
					}
					sharedItem = false;
				}
			}
		}

		return returnable;
	}

	void displayRevenuePrecentage(std::vector<Item>perItemDisplay, float revenue) {
		float precentage = 0;
		std::cout << "Revenue Precentage per item:" << std::endl;
		for (int i = 0; i < perItemDisplay.size(); i++) {
			precentage = (perItemDisplay[i].getPrice() * perItemDisplay[i].getQuantity()) / revenue * 100;
			std::cout << perItemDisplay[i].getItemName() << ": " << precentage << '%' << std::endl;
		}
	}

	void displayItemPopularity(std::vector<Item>perItemDisplay) {
		std::cout << "Popularity per item:" << std::endl;
		for (int i = 0; i < perItemDisplay.size(); i++) {
			std::cout << perItemDisplay[i].getItemName() << ": " << perItemDisplay[i].getQuantity() << std::endl;
		}
	}

	void modifyData() {

	}

	void writeToFile() {
		std::ofstream outfile;
		std::stringstream dataBuilder;
		Table tableCopy;
		std::vector<Order> orderListCopy;
		std::vector<Item> itemListCopy;

		outfile.open("data.dat", std::ios::out);
		for (int i = 0; i < completeData.size(); i++) {
			tableCopy = completeData[i];
			dataBuilder.str(std::string());
			dataBuilder << tableCopy.getDate().print() << '/'
				<< tableCopy.getStart().print() << '/'
				<< tableCopy.getFinish().print() << '/';

			orderListCopy = tableCopy.getOrderList();
			for (int j = 0; j < orderListCopy.size(); j++) {
				dataBuilder << orderListCopy[j].getStart().print() << ','
					<< orderListCopy[j].getFinish().print() << ',';

				itemListCopy = orderListCopy[j].getItemList();
				for (int k = 0; k < itemListCopy.size(); k++) {
					dataBuilder << itemListCopy[k].getItemName() << '|'
						<< itemListCopy[k].getQuantity() << '|'
						<< itemListCopy[k].getPrice() << ',';

					}
				dataBuilder << '/';
			}
			outfile << dataBuilder.str() << '\n';
		}
		outfile.close();
	}

	void clearData() {
		
	}

private:
	std::vector<Table> completeData;
	std::ifstream infile;
	std::ofstream outfile;
	Date currentDate;
	Time currentTime;
};



#endif