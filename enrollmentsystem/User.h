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
	std::string name;
	std::string emailAddress;
	std::string phoneNumber;
	std::string address;
};