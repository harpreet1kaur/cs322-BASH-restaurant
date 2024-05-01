#pragma once
#ifndef __TEST_H
#define __TEST_H

#include "allData.hpp"

class TestCases {
public:
	TestCases() {

	}

	~TestCases() {

	}

	bool testTableFill() {
		std::string testString = "23-4-24/13:11/13:55/13:17,13:30,Water|3|3.50,/13:25,13:40,Toast|5|1.75,Egg|6|.25,/", stringHolder;
		Table testTable;
		testTable.fillTable(testString);

		Date testDate(23, 4, 24);
		Time testTime(13, 11);
		Time testTime2(13, 30);
		std::vector<Order> testOrderList;
		std::vector<Item> testItemList;

		if (!(testTable.getDate() == testDate)) {
			std::cout << "Date is incorrect" << std::endl;
			return 0;
		}

		if (!(testTable.getStart() == testTime)) {
			std::cout << "Start time is incorrect" << std::endl;
			return 0;
		}

		testTime.setHour(13);
		testTime.setMinute(17);

		if (!(testTable.getFinish() == testTime)) {
			std::cout << "Finish time is incorrect" << std::endl;
			return 0;
		}


		testTime.setHour(13);
		testTime.setMinute(55);
		testOrderList = testTable.getOrderList();
		
		for (int i = 0; i < testOrderList.size(); i++) {
			if (!(testOrderList[i].getStart() == testTime)) {
				std::cout << "Order " << i << " start time is incorrect" << std::endl;
				return 0;
			}

			if (!(testOrderList[i].getFinish() == testTime2)) {
				std::cout << "Order " << i << " finish time is incorrect" << std::endl;
				return 0;
			}

			testItemList = testOrderList[i].getItemList();

			for (int j = 0; j < testItemList.size(); j++) {
				if (j == 0 && i == 0) {
					if (!(testItemList[j].getItemName().compare("Water") == 0 &&
						testItemList[j].getQuantity() == 3 &&
						testItemList[j].getPrice() == 3.50)) {

						std::cout << "Order 1 Item 1 is incorrect" << std::endl;
						return 0;
					}
				}

				if (j == 0 && i == 1) {
					if (!(testItemList[j].getItemName().compare("Toast") == 0 &&
						testItemList[j].getQuantity() == 5 &&
						testItemList[j].getPrice() == 1.75)) {
						std::cout << "Order 2 Item 1 is incorrect" << std::endl;
						return 0;
					}
				}

				if (j == 1 && i == 1) {
					if (!(testItemList[j].getItemName().compare("Egg") == 0 &&
						testItemList[j].getQuantity() == 6 &&
						testItemList[j].getPrice() == .25)) {
						std::cout << "Order 2 Item 2 is incorrect" << std::endl;
						return 0;
					}
				}
			}


			testTime.setHour(13);
			testTime.setMinute(25);
			testTime2.setHour(13);
			testTime2.setMinute(40);
		}
		std::cout << "Table was filled properly" << std::endl;
		return 1;
	}

	void testDailyDisplay() {
		AllData testAllData;
		testAllData.showDailyData();
	}

	void testHourlyDisplay() {
		AllData testAllData;
		testAllData.showHourlyData();
	}

private:

};


#endif