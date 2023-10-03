#Urubu do Pix
##Financial Transactions API

Project Description
This project is a backend API for handling financial transactions. It can be used to process payments using a system called Urubu do Pix. The API is designed to be scalable, handling multiple requests at once.

Table of Contents
Installation
Usage
Credits
License
Installation

To install the API, you will need to have Python 3, Pip and Django installed on your machine. Once you have installed the prerequisites, you can install the API using the following command:

```
pip install financial-transactions-api
```

Usage
Once the API is installed, you can start it using the following command:

```
python manage.py runserver
```


The API will then be running on port 8000. You can access the API from your browser by visiting http://127.0.0.1:8000/urubu/.

The API provides a number of endpoints for performing different financial operations. The following is a list of some of the endpoints:

```
/deposit: This endpoint can be used to make a deposit into your urubu-wallet.
/balance: This endpoint can be used to check your current balance.
/withdraw: This endpoint can be used to retrieve money from your urubu-wallet.

*/transactions: This endpoint can be used to view and manage financial transactions.

/add-profit <- internal endpoint
/profit <- internal endpoint
```
For more information on how to use the API, please see the postman collection.**


Credits
This project was developed by Narciso and Rafael.

Additional Information
In addition to the above information, you may also want to include the following in your README:

A description of the API's architecture and how it works.
A list of the API's features and functionality.
Examples of how to use the API.
Links to relevant documentation and resources.
You can also use your README to provide information about the project's development process, such as the following:

Versioning information
Release schedule
Contribution guidelines
Bug reporting instructions
By including all of this information in your README, you can create a comprehensive and informative resource for your users.