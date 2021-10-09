#ifndef PREIVOUSCOURSE_H
#define PREIVOUSCOURSE_H
#include "Course.h"

#include <string>

//this class is to list the previous courses taken by the student
//it Inherits from the Course.h file from it related the title, units, and number

class previousCourse : Course
{
public:
    previousCourse();  //constructor
    ~previousCourse(); //destructor

private:
    int courseGrade;
    std ::string courseDate;
};

#endif