 ------ University Management System -----

This is python based University Management System which is demonstrated OOP concepts like inheritance, Encapsulation, Polimorphism and others concepts like method overriding. 

This taks contains 5 seperate python files including the main file.and system can be run as whole or can be tested each file seperately. 

Project files:-

main.py - this is demo script which is merge everything together. this contains the sample data for the departments, faculty, courses, lectures, students and can run the sytsem based on given data. runing this file you can create department and course, assign faculty, enroll students in courses and get the GPA and academic status.

person.py - contains the base class and related class staff and SecureStudentRecord. SecureStudentRecord class used for GPA and course management with validations.

student.py - Define Student class and UndergraduateStudent and GraduateStudent inherited from the Student super class. This file includes course enrollment, GPA calculation, and academic status management. Undergraduate and Graduate students responsibilites also define here. 

faculty.py - defines faculty, professor, lecturer and teaching assitant (TA) including their workload and responsibilities. 

department.py - Defines the Department and Course classes for managing courses, faculty, and student enrollment with prerequisite checking.

Example:-

after running the main.py the output sould be looks like below,

Dr. Gayan assigned to teach Introduction to Programming
Dr. Gayan assigned to teach Advanced Programming techniques
Mr. Amila assigned to teach Computational Programming
Pinsara Dilsanka GPA: 3.8 - 1st Class
Sumudu Sanjaya GPA: 3.1 - Second Class Lower Division
Professor: Dr. Gayan (ID: 506) ----> Professors focus on teaching, mentoring, research and publishing
Lecturer: Mr. Amila (ID: 802) ----> Lecturers focus on delivering lectures, preparing course materials and grading assignments
TA: Ayodhya (ID: 1003) ----> Teaching assistent assist to students
UndergraduateStudent: Pinsara Dilsanka (ID: 6001) ----> Undergraduate student responsibilities
GraduateStudent: Sumudu Sanjaya (ID: 6002) ----> Graduate student responsibilities
Staff: Sumith (ID: 3001) ----> Staff Role: Admin

Note.
python 3.8 +
Each python file can be run individualy or whole system can be run through main.py file. 
Modify the sample data to explore and experience the system further more.


 ------ Web Scrapping and Data Analysis ------

Overview 

This project demonstrates how to scrape structured product data from demo websites (e.g., Books to Scrape, WebScraper.io test sites),
there are two data sets books_data.csv (books data) and demo_products_phones.csv (phones and their details). bus according to the no of raws df_books dataset is only taken to next steps.
perform data cleaning and preprocessing, and apply exploratory data analysis (EDA) and basic statistical modeling to extract meaningful business insights.

It covers the end-to-end workflow:

Web Scraping → Collect product details (books_data.csv → title, price, description, rating,), (demo_products_phones.csv → name, price,description)
Data Cleaning → Handle missing values, remove duplicates, normalize text, convert prices to numeric.
Exploratory Data Analysis (EDA) → Distribution analysis, outlier detection, frequency counts.
Visualization → Histograms, boxplots, scatter plots, pie charts, interactive plots.
Statistical Modeling → Correlation, hypothesis testing, regression, and simple recommendation system.

Tech Stack

Python 3.x

Libraries:

requests → Fetch HTML pages
BeautifulSoup (bs4) → Parse HTML content
pandas → Data wrangling & cleaning
numpy → Numerical analysis
matplotlib, seaborn → Data visualization
plotly → Interactive plots
scikit-learn / scipy → Statistical modeling, similarity-based recommendation.

Run the CourseWork_Question_02_Books_Dataset jupyter notboook file in jupter notebook envioronment to get the outputs. 
Also you can run the E_Commerce_demo_data file to get the idea about sample data set which is not much data compared to books data. 