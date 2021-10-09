#ifndef COURSE_H
#define COURSE_H

#include <string>

//this class is to give details regarding information about the course

class Course
{
public:
    Course();  //constructor
    ~Course(); //destructor

private:
    int courseNumber;
    std ::string courseTitle;
    int courseUnits;
    std ::string coursePrereq;
};

#endif
