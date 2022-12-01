# **Elanco SE Challange - 2022**
## Introduction
- The goal of this project is to make a web based application which can extract data from Elanco API and display on web page.   
- This application is made using of django and python.
## Usage
- Make sure you have python3 is install and added to system enviroment.
- If not, then download it from [here](https://www.python.org/downloads/)
### Create Virtualenv
- It is best practice to provide a dedicated environment for each Django project you create.
- To create a virtual environment for your project, open a new command prompt, navigate to the folder where you want to create your project and then enter the following.

>`py -m venv project-name`

- This will create a folder called ‘project-name’ if it does not already exist and set up the virtual environment. To activate the environment, run.
> `project-name\Scripts\activate.bat`
- Django can be installed easily using pip within your virtual environment.
>`py -m pip install Django`
- Then copy this files and paste it in under a new folder **sampleApp** under **Scripts folder**.
- To run this project, you need to cd in to Script folder and run `activate` in cmd.
- It will activate your virtual enviroment and then **cd into sampleApp**.
And run this command.
>`python manage.py runserver`
- Then go to below link to use app locally
>`http://127.0.0.1:8000/`