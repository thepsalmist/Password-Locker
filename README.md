# Password_Locker

#### By Xavier Frankline.

## Description

Password_Locker is an application that helps users manage their passwords and generate new passwords for the sites that they visit.
The application is based on python and runs on terminal.

## User Stories and Behaviours

## User Stories

As a user, one should be able to do the following:
1\. Create a password_locker account with their details(name,username & password)
2\. Store their already existing user credentials in the application
3\. Create new account credentials in the application(ability to generate password automatically)
4\. View the saved account credentials and delete them if need be.

## Behaviours

| Behavior Our program should handle | Input Example         | Output Example                                                                                                                   |
| ---------------------------------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| Display short-codes for navigation | Terminal cd~ ./run.py | Welcome to password vault.Use the shortcodes below to navigate:  1. SU- Sign Up 2. LI- Log in to your 3. EX- Exit                |
| Display details for user sign-up   | Enter SU              | Fill in the details below to Sign-up for a new account:  FirtsName:, Last Name:, UserName:, Password                             |
| Display for login                  | Enter Li              | Log In with your username and password:                                                                                          |
| Display short-codes for navigation | Login                 | Use these short codes: 1. cc- Create new credentials  2. dc- Displaying saved credentials  3. dd- Delete credentials 4. ex- Exit |

## Setup and Installation Requirements

### Prerequisites

-   python3.6
-   pip

### Cloning

-   In your terminal:

          $ git clone https://github.com/thepsalmist/Password-Locker
          $ cd Password-Locker

## Running the Application

-   To run the application, in your terminal:

          $ chmod +x run.py
          $ ./run.py

## Technologies Used

      * Python3.6

## License

MIT License
Copyright (c) 2019 [thepsalmist](https://github.com/thepsalmist)
