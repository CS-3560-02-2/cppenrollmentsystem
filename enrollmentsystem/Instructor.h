#pragma once
#include "User.h"

// Inherits from User class
// 
class Instructor:User
{
public:
	// Constructor
	Instructor:User();
	// Destructor
	~Instructor:User();

private:
	std::string instructorID;
};
