#include "allData.hpp"

int main(void) {

	std::string testString = "23-4-24/13:11/13:55/13:17,13:30,Water|3|3.99,/13:25,13:40,Toast|5|1.99,Egg|6|.99,/", stringHolder;
	Table testTable;
	std::vector<Table> dataList;
	testTable.fillTable(testString);
	std::ifstream infile;
	infile.open("data.dat");

	while (!getline(infile, stringHolder).eof()) {
		dataList.resize(dataList.size() + 1);
		dataList[dataList.size() - 1].fillTable(stringHolder);
	}

	AllData testCase;

	return 0;
}