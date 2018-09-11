![pepipostlogo](https://pepipost.com/assets/img/pepipost-footLogo.png)

[![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE.txt)
[![Twitter Follow](https://img.shields.io/twitter/follow/pepi_post.svg?style=social&label=Follow)](https://twitter.com/pepi_post)

# Official Python library :snake: for [Pepipost](https://pepipost.com)

   This SDK contain methods for easily interacting with the Pepipost Email Sending API to send emails within few seconds.

We are trying to make our libraries a Community Driven. To help us building right things in proper order we would request you to help us by sharing comments, creating new issues or pull request.

   We welcome any sort of contribution to this library.

   The latest 2.5.0 version of this library provides is fully compatible with the latest Pepipost v2.0 API.

   For any update of this library check [Releases]

## Table of Content
* [Installation](#installation)
* [Quick Start](#quickstart)
* [Announcements](#announcements)
* [Roadmap](#roadmap)
* [About](#about)
* [License](#license)


<a name="installation"></a>
## Installation 
   
   There are two ways of installing the library for Pepipost either you can use 
   
   ```pip install pepipost``` 
   
   **OR**
   
   ```git clone https://github.com/pepipost/pepipost-python.git``` 
   
   Below are the steps inorder to install the library
   
### Prerequisites
   * Python (2 >=2.7.9 or 3 >= 3.4)
   * Python IDE (we are using [Pycharm](https://www.jetbrains.com/pycharm/download/) )
   * Python packages  
     * nose
     * jsonpickle
   
   **OR**
   
   * [Pepipost package]() (includes all dependencies)
   
   Installation of PIP can be done from [here](https://pip.pypa.io/en/stable/installing/).
   
   We recommend using PIP Dependency manager in order to install all the dependencies which we had mentioned in ```requirements.txt``` files that comes in SDK.
   
   
### Defining Enviroment variable.   
   
   * Python and PIP Should be defined in your PATH.
   * Check using 
     ```pip --version```   --> Will display the version of PIP dependency manager installed.
     ![image]()
     
     ```python --version```  --> Will Display the Version of Python installed which should be >=2.7.1 if you are using 2 else it can be >=3.4 if you are using python 3.
     ![image2]()
     
   * Use Command line to navigate to directory containing the generated files which has ```requirements.txt```.  

<a name="quickstart"></a>
### Quickstart

   1. Using SDK from Github repository, Run the below command to download the requirements
         
      ```pip install -r requirement.txt```
      
      ![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=pepipost-Python)
      
      **OR**

      Using PIP dependency manager download our official library directly from PIP 
      
      Run below Command inorder to download Pepipost library.
      
      ```pip install pepipost```

   2. Open Project in an IDE
   
      Open up a Python IDE like PyCharm. 
      The basic workflow presented here is also applicable if you prefer using a different editor or IDE.
      
      ![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)
      
      Click on ```Open``` in PyCharm to browse to your generated SDK directory and then
      
      click ```OK```
      
    

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=pepipost-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=pepipost-Python&projectName=pepipost)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=pepipost-Python&projectName=pepipost)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=pepipost-Python&projectName=pepipost)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from pepipost.pepipost_client import PepipostClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=pepipost-Python&libraryName=pepipost.pepipost_client&projectName=pepipost&className=PepipostClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=pepipost-Python&libraryName=pepipost.pepipost_client&projectName=pepipost&className=PepipostClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### 

API client can be initialized as following.

```python

client = PepipostClient()
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [EmailController](#email_controller)

## <a name="email_controller"></a>![Class: ](https://apidocs.io/img/class.png ".EmailController") EmailController

### Get controller instance

An instance of the ``` EmailController ``` class can be accessed from the API Client.

```python
 email_controller = client.email
```

### <a name="create_send_email"></a>![Method: ](https://apidocs.io/img/method.png ".EmailController.create_send_email") create_send_email

> *Tags:*  ``` Skips Authentication ``` 

> This Endpoint sends emails with the credentials passed.

```python
def create_send_email(self,
                          api_key=None,
                          body=None)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| apiKey |  ``` Optional ```  | Generated header parameter. Example value ='5ce7096ed4bf2b39dfa932ff5fa84ed9ed8' |
| body |  ``` Optional ```  | The body passed will be json format. |



#### Example Usage

```python
api_key = 'api_key'
body = EmailBody()

result = email_controller.create_send_email(api_key, body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 405 | Method not allowed |




[Back to List of Controllers](#list_of_controllers)



