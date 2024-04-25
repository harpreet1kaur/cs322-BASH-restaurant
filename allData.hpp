#pragma once
#ifndef __ALLDATA_H
#define __ALLDATA_H

#include "table.hpp"

class AllData {
public:
	AllData() {

		std::string stringHolder;

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

	void showHourlyData() {

	}

	void showDailyData() {

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
		//TRIPLE NESTED FOR LOOP LFGGGGGGGGG
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

private:
	std::vector<Table> completeData;
	std::ifstream infile;
	std::ofstream outfile;
};



#endif