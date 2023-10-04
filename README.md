# Data Science Project: Working with CSVs, PDFs, Dates, and More

This project covers a range of data manipulation and analysis tasks using Python. It's designed to help you sharpen your skills in data handling, web scraping, date manipulation, regular expressions, and data visualization.

## Table of Contents

- [Working with CSV and PDFs](#working-with-csv-and-pdfs)
- [Skill Set: Dates, Times, and Regular Expressions](#skill-set-dates-times-and-regular-expressions)
- [Web Scraping and Exception Handling](#web-scraping-and-exception-handling)
- [Skill Set: Data Visualization with Matplotlib](#skill-set-data-visualization-with-matplotlib)

## Working with CSV and PDFs

### Reading, Writing CSV

- **Assignment**: Read a CSV file named "people.csv" containing user details like Name, Age, Email and write this data to a new CSV file named "output.csv" but in reverse order of rows.

### Handling Headers, Custom Delimiters

- **Assignment**: Given a CSV file "cars_data.txt" with a custom delimiter "|", read the file and write its contents to a new file "formatted.csv" with a comma as the delimiter. Ensure that the headers remain intact.

### Reading PDFs: Extract Info and Text

- **Assignment**: Extract text from a given PDF named "part_1.pdf" and save the extracted text to a text file named "extracted.txt".

### Writing and Combining PDFs

- **Assignment**: Combine two given PDFs "part_1.pdf" and "part_2.pdf" into a single PDF named "combined.pdf".

## Skill Set: Dates, Times, and Regular Expressions

### Working with Dates and Times

- **Assignment**: Given a date string "2023-04-15", write a program to add 45 days to it and return the new date.

### Formatting and Parsing

- **Assignment**: Parse the date string "15th April, 2023" into a date object and then format it as "2023-04-15".

### Intro to Regular Expressions

- **Assignment**: Write a regular expression to validate email addresses. Test it on a list of sample emails and filter out the invalid ones from the file ‘emails.txt’.

### Basic Patterns: Metacharacters, Literals, Quantifiers, Groups

- **Assignment**: Given a text, extract all the dates using regular expressions. Get the text from the file ‘pattern.txt’.

## Web Scraping and Exception Handling

### Intro to Scraping

- **Assignment**: Write a basic script to scrape the title of a given webpage.

### Making HTTP Requests with `requests`

- **Assignment**: Use the `requests` library to fetch the content of a webpage and print its status code.

### Parsing HTML with BeautifulSoup4

- **Assignment**: Parse the content of a webpage to extract all the hyperlinks (a tags) using BeautifulSoup4.

### Effective Web Scraping

- **Assignment**: Scrape product names and prices from a mock e-commerce webpage and save them as a CSV.

### Basic Exceptions: SyntaxError, NameError, ValueError

- **Assignment**: Write a script that intentionally causes each of the mentioned exceptions and handle them with appropriate error messages.

### Handling Exception Using `try`, `except`, `finally`

- **Assignment**: Write a function to divide two numbers. Handle the ZeroDivisionError using `try`, `except`, and `finally` blocks. In the `finally` block, print "Operation complete."

### Raise Exception with `raise`

- **Assignment**: Write a function that checks the length of a username. If the username is less than 5 characters or more than 15 characters, raise a custom exception.

## Skill Set: Data Visualization with Matplotlib

### Intro to Matplotlib

- **Assignment**: Install Matplotlib and create a basic plot showing a linear relationship between two lists of numbers.

### Basic Plots: Line Plots, Scatter Plots, Bar Plots

- **Assignment**: Given a dataset of monthly sales data for a year, create a line plot for sales, a scatter plot for profit, and a bar plot for the number of products sold.

### Advanced Plots: Histograms, Box Plots, Pie Charts

- **Assignment**: Given a dataset of student marks, create a histogram showing the distribution of marks, a box plot to show the quartiles, and a pie chart to show the percentage of students in each grade category (A, B, C, D, F).

### Styling and Saving Plots

- **Assignment**: Style the plots from the previous assignment using a theme of your choice and save each plot as a PNG image.

Feel free to dive into each assignment and enhance your data science skills. Happy coding!
