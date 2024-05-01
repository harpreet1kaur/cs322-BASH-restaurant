#include "allData.hpp"
#include "test.hpp"

/*Todo:
* Make data file more compatable with data being inserted during operation (delete as entered, append when closed)
* 
*/

int main(void) {

	TestCases test;
	test.testTableFill();
	test.testDailyDisplay();
	test.testHourlyDisplay();

	Date dateTest(1, 3, 20);
	dateTest.subtractDay();
	
	
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