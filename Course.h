#ifndef COURSE_H
#define COURSE_H

#include <string>

class Course
{
public:
    Course();

private:
    int courseNumber;
    std ::string courseTitle;
    int courseUnits;
    std ::string coursePrereq;
};

#endif