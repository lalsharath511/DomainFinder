
# Domain Info Finder

This project is a domain and other information finder tool developed in Python. The tool helps users find information about a domain or company by performing a search on various sources on the internet.

The tool works by taking a domain or company name as input and then performing a search on various sources such as WHOIS and Google. The tool then compiles all the information found on these sources and presents it in a user-friendly format.

The information that can be found using this tool includes the domain registrar, domain expiration date, company size, location, key personnel, and more. This tool can be useful for businesses that want to gather information about their competitors or for individuals who are interested in learning more about a particular domain or company.

The tool is developed in Python, making use of popular libraries such as requests, whois, googlesearch. The user interface of the tool is designed to be simple and easy to use, with clear instructions on how to perform a search.

Overall, this tool can be a useful resource for anyone looking to gather information about a domain or company quickly and easily. With its user-friendly interface and comprehensive search capabilities, it provides a valuable service to users looking to gain insight into the world of business and domains.


## Installation

Clone the repository to your local machine using the following command:

```bash
  git clone https://github.com/lalsharath511/DomainFinder.git
```

Change into the project directory:

```bash
  cd DomainFinder
```

Create a virtual environment for the project:

```bash
 virtualenv venv

```
Activate the virtual environment:

```bash
source venv/bin/activate

```

Install the required dependencies:
```bash
pip install -r requirements.txt

```




    
## Usage/Examples
To use this Python project, follow the steps below:



1.Install the required dependencies by running the following command in the terminal:
```python
pip install -r requirements.txt

```
2.Create a .txt file that contains a list of company names, with each company name on a separate line. For example:
```python
ABC Corporation
XYZ Inc.
123 Industries
```
3.Place the .txt file in the same directory as the main.py file.

4.Run the following command in the terminal:
```python
python3 main.py
```
5.The program will then ask for the file name. For example:
```python
Enter the file Relative path : <file name>.txt
```

6.The program will then read the .txt file and perform a search for each company name, displaying the results in the terminal.


7.Once the program has finished running, it will generate a CSV file named Data Set.csv that contains all the search results.

## Running Tests

To run tests, run the following command

```bash
  python3 main.py
```
Enter Input has test.txt

```bash
  Enter the file Relative path : test.txt
```