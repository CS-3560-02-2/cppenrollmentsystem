import sqlite3
from db import DB_PATH


conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


def insert_courses():
    try:
        cursor.execute("""DROP TABLE courses""")
        conn.commit()
        db.create_courses_table()
        cursor.execute(
            """INSERT INTO courses (subject,course_num,course_title,course_description,course_units) VALUES
            ("CS", "1400", "Intro to Computer Science", "Problem-solving methods. Object-oriented concepts including classes, inheritance, and polymorphism. Basic control structures and data types. Files. Input/Output. Exception handling. Program documentation and testing.", "4"),
            ("CS", "2400", "Data Structures and Advanced Programming", "Abstract data types and their implementation using linear and non-linear data structures. Interfaces and generics. Recursive structures and operations. Big-O notation and introduction to algorithm analysis.","4"),
            ("CS", "2560", "C++ Programming", "C++ fundamentals. Recursion, structures, class encapsulation, inheritance, polymorphism, and exception handling. Memory management using pointers. Template functions and template classes. Software reuse and object-oriented programming.", "3"),
            ("CS", "4350", "Database Systems", "Database and transaction systems. Database components. Database design and constraints. Normalization theory. Data modeling. Relational and object data models. Relational algebra and calculus. SQL programming paradigms. Concurrency control, crush recovery, and security.", "3"),
            ("MAT", "1050", "College Algebra", "The theory and applications of real-valued functions, domain and range, compositions, inverses, transformations, equations and inequalities, and absolute value. Emphasis on polynomials, rational functions, power and root functions, piecewise functions, logarithms and exponential functions. Both symbolic and graphical representations of functions. Use of graphing devices to support reasoning about functions.", "3"),
            ("MAT", "1060", "Trigonometry", "Right triangle trigonometry, the unit circle, trigonometric and inverse trigonometric functions, trigonometric identities, equations, graphs, Law of Sines and Law of Cosines, applications of trigonometry, complex numbers and DeMoivre’s Formula. Applications of trigonometry to solve problems.", "3"),
            ("MAT", "1070", "Precalculus", "Basic concepts of trigonometry and algebra including the theory of real-valued functions, the unit circle, equations and inequalities, absolute value, and graphing. Emphasis on power functions, polynomials, rational functions, exponential functions, trigonometric functions, piecewise functions, and their inverses. Applications of trigonometry and algebra.", "5"),
            ("MAT", "1140", "Calculus", "Functions, limits, continuity, derivatives of all functions including trigonometric, exponential, logarithmic, inverse trigonometric, and implicit functions. Applications of derivatives, including max/min problems and L’Hopitals rule. Definite and Indefinite Integrals, The Fundamental Theorem of Calculus, substitution rule and applications.", "4"),
            ("MAT", "1150", "Calculus II", "Integration techniques including integration by parts, integrals of trigonometric products, partial fractions, substitution and trigonometric substitution. Hyperbolic functions. Improper Integrals, sequences and series, polar coordinates, parametric equations and conic sections.", "4"),
            ("MAT", "2140", "Calculus III", "Introduction to vectors, dot product, cross product, equations of lines and planes, calculus of vector valued functions, introduction to multivariable functions, differential calculus of multivariable functions, the chain rule, applications including extreme problems and Lagrange multipliers, integral calculus of multivariable functions, double and triple integrals, applications of double and triple integrals, line and surface integrals of vector fields, Green’s Theorem, the Divergence Theorem, Stokes’ Theorem.", "3"),
            ("MAT", "2240", "Elementary Linear Algebra and Differential Equations", "Separable and linear ordinary differential equations; numerical and analytical solutions. Linear algebra: vectors in n-space, matrices, linear transformations, eigenvalues, eigenvectors, diagonalization; applications to the study of systems of linear differential equations.", "3"),
            ("MAT", "2250", "Linear Algebra with Applications to Differential Equations", "Systems of linear equations, Gaussian elimination, matrices and determinants, vector spaces, basis, dimension, linear transformations, rank-nullity, matrix representation and change of basis, eigenvalues and eigenvectors, diagonalization, first order DE’s, constant coefficient linear DE’s, harmonic oscillations, systems of linear 1st order DE, series solutions.", "4"),
            ("PHY", "1020", "Fundamentals of Physics", "The basic principles that govern the behavior of matter and energy. These principles will be explored in both fundamental contexts (e.g. the nature of measurement, space, time) and applied contexts (e.g. energy issues, the scientific basis of modern electronic technology).", "3"),
            ("PHY", "1510", "Introduction to Newtonian Mechanics", "Introduction to mechanics, including Newton’s laws, vectors, statics, kinematics, conservation laws, rotational motion, Newtonian gravity, fluids, and simple harmonic motion.", "3")"""
        )
        conn.commit()
        # Set the course prerequisite of PHY 1510 to PHY 1020
        cursor.execute(
            """UPDATE courses
            SET course_prereq = (SELECT course_id FROM courses WHERE (subject = 'PHY' AND course_num = 1020))
            WHERE (subject = 'PHY' AND course_num = 1510)"""
        )
        conn.commit()
    except sqlite3.Error as error:
        print(CONN_ERROR, error)
    finally:
        if conn:
            conn.close()
            print(CONN_CLOSED)


def insert_sections():
    try:
        cursor.execute("""DROP TABLE course_sections""")
        conn.commit()
        create_course_sections_table()
        cursor.execute(
            """INSERT INTO course_sections (course_section_id, course_id, room, schedule_days, start_time, end_time) VALUES
            ("01", "1", "40", "MW", "1:00", "2:15"),
            ("02", "1", "40", "TTh", "1:00", "2:15"),
            ("03", "1", "40", "MW", "10:00", "11:15"),
            ("01", "2", "20", "MW", "10:00", "11:15"),
            ("02", "2", "20", "MW", "1:00", "2:15"),
            ("03", "2", "20", "TTh", "1:00", "2:15"),
            ("01", "3", "10", "MWF", "10:00", "10:50"),
            ("02", "3", "10", "MW", "12:00", "1:15"),
            ("03", "3", "10", "TTh", "12:00", "1:15")
            """
        )
        conn.commit()

        # Set enrollment and waitlist
        cursor.execute(
            """UPDATE course_sections
            SET students_enrolled = 0,
                waitlist_enrolled = 0,
                waitlist_capacity = 10
            """
        )
        conn.commit()
        # Set capacities
        cursor.execute(
            """UPDATE course_sections 
            SET class_capacity = 35
            WHERE room = '40'
            """
        )
        conn.commit()
        cursor.execute(
            """UPDATE course_sections 
            SET class_capacity = 40
            WHERE room = '20'
            """
        )
        conn.commit()
        cursor.execute(
            """UPDATE course_sections 
            SET class_capacity = 30
            WHERE room = '10'
            """
        )
        conn.commit()
    except sqlite3.Error as error:
        print(CONN_ERROR, error)
    finally:
        if conn:
            conn.close()
            print(CONN_CLOSED)
