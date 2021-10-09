#pragma once

// This class is an abstract class
// Base class for Instructor and Student
class User {
public:
	// Constructor
	User();
	// Desructor
	~User();
private:
	std::string name;				// name of user
	std::string emailAddress;		// emailAddress of user
	std::string phoneNumber;		// phoneNumber of user
	std::string address;			// address of user
};