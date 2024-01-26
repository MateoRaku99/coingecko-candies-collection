## Coingecko Candies Collection

This program automates the collection of daily candies from the Coingecko website using the Selenium web driver and the undetected-chrome plugin. It utilizes a test framework with pytest to ensure reliable and repeatable candy collection.

### Purpose

The primary purpose of this program is to automate the process of collecting daily candies from the Coingecko website. This is done using a Selenium web driver to interact with the website and collect the necessary information. The undetected-chrome plugin is used to bypass browser detection and prevent Coingecko from blocking the automated script.

### Steps

* Automatically identifies and interacts with the Coingecko login page
* Logs in to the Coingecko account using Gmail authenticator
* Collects the daily candies and updates the corresponding balance
* Logs out of the Coingecko account

### Features
* test with collection ability
* wrapper for the screenshot capture whenever the test fails
* send_email function whenever the test fails
* configuration for the cron execution

### Configuration
- copy repo
- install reqs
- create your .yaml file with Gmail address and password for the coingecko account(based in yaml in repo)
- put the email address that will be sender and the second one should be a receiver
- very important - to have full access to email through the email service you need to change access inside your Gmail account in the security tab: enable 2FA authentication, and after that set an app key(last position inside the 2FA authentication) - and then use that password as a password for the email (only in send_email function!)
!!! do not use the same email address to collect candies and send an email when a test fails!!!
- ```screenshot_path``` - create a folder, and set the path where screens can be placed
    
    

### How to config cron (it is optional when you don't want to test manually)
cron execution -> open your terminal and use the command:
        ```crontab -e```
The config page should be open, insert the command to run the test: 
        ```13 13 * * * cd "/path/to/your/test_folder" && /path/to/your/pytest test_undetected.py  > logs.txt```
        
In that example, you can see that test will run at 1:13 PM/ 13:13
Part of the logs is optional, but if you want to see output from the test, it is better to create logs.txt in your test location.
The test will run in normal window mode, so don't be surprised once it starts :) 
In case the test will not run, you need to go to your security/permissions settings and add full permission to the 'Full disk access' to your terminal, cron, and crontab.


### How to run it from the terminal
Once you finish the configuration - run a test with the command:
``` pytest tests/test_undetected.py -rA ```
Of course -rA is optional here - to see more details about run
