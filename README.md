[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21816349)
# Security Device Monitoring for Events

## Overview

We will be doing the following steps to monitor for events on the Raspberry Pi:

1. Write code in GitHub Codespaces (VS Code in the cloud) to monitor for a button press
2. Test the code on GitHub Codespaces
3. Push the code to your GitHub repository
4. Clone (download) the code from the GitHub repository to the Raspberry Pi using SSH
5. Test the code on the Raspberry Pi to monitor for a button press

## Writing the Code on the Raspberry Pi

## Part 1: Write the code in GitHub Codespaces (VS Code in the cloud)

We are going to walk through step by step how to write code on your raspberry pi. Just like your previous assignments involving the Raspberry Pi, you will need to be on campus in order to successfully complete steps 4 and 5 above.

- Step 1. [Accept the assignment](https://classroom.github.com/a/yyg0HVzL).
- Step 2: Click the Open in GitHub Codespaces button.
- Step 3: You need to create a new file. To create a new file either right-click in the empty space in the left panel and click New File or click the New File button next to the assignment title. 
- Step 4. Add the following code to prepare the Raspberry Pi to watch for button presses:
```
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# Set General Purpose Input Output (GPIO) Pin 4 (position 7) to be an input pin and set initial value to be pulled low (off)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
```
- Step 5. Now add a `while` statement that will run forever (this is so we will **always** notice when we press a button):
```
while True: # Run forever
```
- Step 6. Next add an `if` statement to check whether the GPIO pin is receiving power:
```
    if GPIO.input(7) == GPIO.HIGH:
```
- Step 7. Last add a print statement showing an alert:
```
    print("Someone has pressed the alert button!")
```

## Part 2: Test the code on GitHub Codespaces
- Step 1: Run the program in the Codespace to be sure it works. To run your code, simply type the command `pytest` in the Codespace terminal and hit Enter.
     - Note: testing pieces of the project early and often will help you later in case you need to troubleshoot. For example, let's assume you get to the end of this assignment, and your code is not running on your Raspberry Pi. If you have already tested your code in Codespaces, you know that the problem is coming from one of the steps after this one. Taking time to test your code as you go is always worth it.
- Step 2: You will know if your code works if you see a green check mark and a message stating that the test passed in the Codespace terminal.

## Part 3: Push (upload) the code to GitHub
- Step 1: Push the code to GitHub using the Source Control button on the left panel.
- Step 2: Add a commit message that describes the change you made. In this case, since you changed your name, you might write "Changed name to [Your Name]." 
- Step 3: Click Commit
- Step 4: Codespaces will now ask you a series of questions. To make everything work properly, select the following options: 
    - In the center of your screen you will see a message that says, "There are no staged changes to commit. Would you like to stage all your changes and commit them directly?" Click Always - you can think of this like putting some items in a box you are about to ship. We call it staging because we are preparing the files before we commit (upload) the code.
    - On the left panel, where you clicked Commit before, you will now see an option to sync changes. Click Sync Changes - this means push (upload) and pull (download) the latest changes you've made to your GitHub repository or project:
    - In the center of your screen you will see a message that says,  "This action will pull and push commits from and to "origin/main"." Click OK, Don't Show Again - see previous step explanation
    - In the bottom right corner, you will see a message asking you if you would like VS code to periodically run "git fetch." Click No - this will allow you to choose when you want to pull (download) code changes
    - Your code has now been pushed (uploaded) to GitHub! That's how we share code with our co-workers in real programming teams.
Next, we will copy the program to the Raspberry Pi. Important: you must be on campus to finish this assignment. Your computer and pi must be connected to the same network: ensign-tech-lab

Next, we will copy the program to the Raspberry Pi. Important: you must be on campus to finish this assignment. Your computer and pi must be connected to the same network: ensign-tech-lab

## Part 4: Use SSH to connect your Raspberry Pi to your computer 
**Important:** you must be on campus to finish this assignmnet. Your computer and pi must be connected to the same network: ensign-tech-lab\

The way you run commands directly on the raspberry pi is by using SSH. You need to use an SSH to connect your pi to your computer and to connect your pi to GitHub. Fortunately, you already know how to use SSH to connect your computer to your Raspberry Pi, so these first few steps will be very easy.

- Step 1: Plug in the Raspberry Pi, and turn it on. Be sure the green light is on. Wait 5 minutes while the pi starts up completely.
- Step 2: Open PowerShell (Windows) or Mac Terminal (Apple) on your computer
Open PowerShell by typing Power in the Windows search bar and clicking PowerShell
- Step 3: Write an SSH command to connect to the Raspberry Pi. If you need to remember how to write that command, you can reference the Raspberry Pi Set-Up assignment. If your pi has connected successfully, you will see the green text with the name of your Raspberry Pi.

## Part 5: Install the GPIO Library on the Raspberry Pi
To enable Python to talk with the General Purpose Input Output (GPIO) pins, we must install a special Linux package called `python3-rpi.gpio`. Install it using the following command in Powershell or Mac Terminal:
- `sudo apt-get install python3-rpi.gpio`

## Part 6: Clone (download) the code from the GitHub repository to the Raspberry Pi

You can now copy the program from Codespaces to the Raspberry Pi.
- Step 1: Click the [assignment link](https://classroom.github.com/a/yyg0HVzL). This is the same link from Part 1, Step 1.
- Step 2: Click the blue link to your GitHub repository
- Step 3: Click the green Code button
- Step 4: Click the Local tab, and then the SSH tab
- Step 5: Copy the url

## Part 7: Test the code on the Raspberry Pi (back in PowerShell/Mac Terminal)
- Step 1: Back in your PowerShell or Mac Terminal type the following command: git clone [URI] . Replace [URI] with the URI you copied from the previous step.
- Step 2: Type the command cd ./2-9* This takes you to the directory where the code was downloaded so you can run the program you created.   
- Step 3: Now you are going to run the code you wrote in Part 1. To do this, type the command: python app.py . This is the name of your program. 
- Step 4: Press the button (switch) you assembled as part of your Raspberry Pi set up earlier
- Step 5: Watch the Powershell/Mac Terminal for the message about an alert.
- Step 6: Notice there are multiple messages. Why is this?
- Step 7: Stop the program on the Raspberry Pi by holding down the `Control(CTRL)` key and the `C` key on your keyboard.
- Step 7: Try making some changes in the Codespace that might reduce the number of times you see the messages. P
- Step 8: Push the code to GitHub
- Step 9: Back in Powershell/Mac Terminal use the command: `git pull` to download the code
- Step 10: Run the program again: `python app.py`
- Stepp 11: What happened?
- Step 5: Take a screenshot of the terminal with your messages.


Excellent work! You have run your first program on your pi.

## Submission

Submit your screenshot of the terminal in Canvas.

Also submit your code to GitHub in this repository. If you need a refresher on how to submit code to GitHub, you can look at the How to Submit Labs page on Canvas.
