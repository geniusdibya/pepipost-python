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
* [Sample Example](#sample)
* [Announcements](#announcements)
* [Roadmap](#roadmap)
* [About](#about)
* [License](#license)


<a name="installation"></a>
## Installation 
   
   There are two ways of installing the library for Pepipost either you can use 
   
   ```pip install pepipost``` 
   
   **OR**
   
   ```git clone https://github.com/hellovikram/pepipost-python.git pepipost_python``` 
   
   Below are the steps inorder to install the library
   
### Prerequisites
   * Python (2 >=2.7.9 or 3 >= 3.4)
   * Python IDE (we are using [Pycharm](https://www.jetbrains.com/pycharm/download/) )
   * Python packages  
      * nose
      * jsonpickle
      * requests
      * cachecontrol
      * python-dateutil
     
   Installation of PIP can be done from [here](https://pip.pypa.io/en/stable/installing/).
   
   We recommend using PIP Dependency manager in order to install all the dependencies which we had mentioned in ```requirements.txt``` files that comes in SDK.
   
   
### Defining Enviroment variable.   
   
   * Python and PIP Should be defined in your PATH.
   * Check using 
   
     ```pip --version```   --> Will display the version of PIP dependency manager installed.

     ```python --version```  --> Will display the version of Python installed 
     
     which should be >=2.7.1 if you are using python 2 else it can be >=3.4 if you are using python 3.
     
     ![image]()
     
   * Use Command line to navigate to directory 
      
     ```cd pepipost_python```
      

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

   3. Add a new Test Project

      Create a new directory by right clicking on the solution name as shown below:

      ![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=pepipost-Python&projectName=pepipost)

      Name the directory as "test"

      ![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
      Add a python file to this project with the name "testsdk"

      ![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=pepipost-Python&projectName=pepipost)

      Name it "testsdk"

      ![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

   4. Importing files from python library

      Inorder to import file you need to just copy the [sample file from here](#sample). 

      ![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=pepipost-Python&libraryName=pepipost.pepipost_client&projectName=pepipost&className=PepipostClient)

   5. Update API key and Sending Domain
   
      * apikey: This will be available under: Login to your Pepipost account -> Settings -> Integration.
      
      * FromEmail: If your fromemail address is e.g. info@mydomain.com, then the Sending Domain mydomain need to be verified and active under your Pepipost account. You can manage the Sending Domain under: Login to Pepipost -> Settings -> Sending Domains.
      
   6. Run the Test Project
   
      To run the file 
      
      ```ctrl+F5```
      
      **OR** 
      
      Right click on your Python file inside your Test project and click on ```Run```

      ![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=pepipost-Python&libraryName=pepipost.pepipost_client&projectName=pepipost&className=PepipostClient)

<a name="sample"></a>
### Sample Example

```python
from pepipost.pepipost_client import PepipostClient
from pepipost.models.email_body import EmailBody
from pepipost.models.personalizations import Personalizations
from pepipost.models.attachments import Attachments
from pepipost.models.mfrom import From
from pepipost.models.email_body_attachments import EmailBodyAttachments
from pepipost.models.settings import Settings
from pepipost.exceptions.api_exception import APIException
import jsonpickle

client = PepipostClient()
email_controller = client.email
body = EmailBody()
body.personalizations = []

api_key = 'api_key here '
body.personalizations.append(Personalizations())
body.personalizations[0].recipient = 'recipient@your-mail.com'

body.tags = 'tagsPython'
body.mfrom = From()

body.mfrom.from_email = 'example@your-verified-domain'
body.mfrom.from_name = 'Example Pepi'
body.subject = 'Emailing with Pepipost is easy'
body.content = '<html><body>Hey,<br><br>Do you know integration is even simpler in Pepipost, <br>with Python <br> Happy Mailing ! <br><br>Pepipost </body></html>'
body.settings = Settings()

body.settings.footer = 1
body.settings.clicktrack = 1
body.settings.opentrack = 1
body.settings.unsubscribe = 1

try:
    result = email_controller.create_send_email(api_key, body)
    if not (result.error_info.error_message is None):
        print("Reason :: " + str(result.error_info.error_message) + "\n" + "Message :: " + str(result.message))
    else:
        print("Message :: " + result.message)
except APIException as e:
    print(e)

```

<a name="announcements"></a>
# Announcements

v2.5.0 has been released! Please see the [release notes](https://github.com/pepipost/pepipost-sdk-csharp/releases/tag/v2.5.0) for details.

All updates to this library are documented in our [releases](https://github.com/pepipost/pepipost-sdk-csharp/releases). For any queries, feel free to reach out us at dx@pepipost.com

<a name="roadmap"></a>
## Roadmap

If you are interested in the future direction of this project, please take a look at our open [issues](https://github.com/pepipost/pepipost-sdk-csharp/issues) and [pull requests](https://github.com/pepipost/pepipost-sdk-csharp/pulls). We would love to hear your feedback.

<a name="about"></a>
## About
pepipost-php-sdk library is guided and supported by the [Pepipost Developer Experience Team](https://github.com/orgs/pepipost/teams/pepis/members) .
This pepipost-php-sdk library is maintained and funded by Pepipost Ltd. The names and logos for pepipost-php-sdk are trademarks of Pepipost Ltd.

<a name="license"></a>
## License
This code library was semi-automatically generated by APIMATIC v2.0 and licensed under The MIT License (MIT). 





