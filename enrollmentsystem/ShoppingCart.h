#pragma once
#include "CourseSection.h"
#include <vector>

class ShoppingCart
{
private:
	int cartUnits;				// Total units 
	double cartTotal;			// Total price of the cart
	vector<CourseSection> cartList;			// A vector to hold the list of CourseSections

public:
	ShoppingCart();
	void outputCart();			// Will output the list of courses in the shopping cart, and the total units/price.
	void addSection();			// Adds a section to the shopping cart.
	void dropSection();			// Drops a section from the shopping cart.
};
