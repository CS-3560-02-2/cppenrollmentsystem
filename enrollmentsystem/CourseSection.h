#pragma once
#include "Course.h"

using namespace std;

class CourseSection
{
private:
	int studentCapacity;			// Holds capacity of the class
	bool courseAvailability;		// Holds true or false if the class is open or full
	std::string courseTime;				// Holds the time the course is held at
	std::string professorName;			// Holds the professor name

public:
	CourseSection();			// Constructor
};

