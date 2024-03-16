[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/zY-T8p5T)
# Lab 0

## Course Information
- **Course:** CSC 101
- **Instructor:** Prof. Vanessa Rivera
- **Term:** 2023-24 Winter Quarter

## Overview
This first "lab" will get you acquainted with our assignment format by guiding you in setting up the software we will be using during the course on your personal computer.

You will install the following software:
- **Python:** The programming language we will be using in this course
- **PyCharm:** An Integrated Development Environment (IDE) that allows us to write Python code efficiently.
- **Git:** Version Control Software (VCS) that will be used for managing and uploading your code-based work.

You will also learn the process for submitting code projects in our class. This is a two-step process that requires you to (1) submit your code to GitHub and (2) submit a screenshot showing proof of your submission.

> [!NOTE]
>
> Although completion of this "zeroth" lab is suggested before class begins, it is okay to ask for installation help and verification during lab.

## Learning Objectives
In completing this assessment, you will be able to:
- Use Python, PyCharm, and Git on your personal computer. (🌐)
- Use Git to commit and push changes to a remote repository. (🌐)

## Instructions
### Task 1: Install Python
**🎯 Task Goal:** Download and install Python.

**The Python Interpreter:** Python is a popular, high-level programming language known for its readability and versatility.
The Python interpreter is a program that reads and executes the code you write.
By installing it, you gain the power to run Python scripts.

1. **Access the Python Website:** Open the [python.org: Downloads](https://www.python.org/downloads/) page in a web browser.
2. **Begin the Download:** Click the yellow "Download Python" button to download Python.
3. **Run the Installer:** Open the downloaded file and follow the installer's steps.
   - **For Windows Users:** Ensure that the "Add Python to PATH" option is selected on the first screen of the installer. Afterward, you may proceed using the default options.

**🎉 Task Complete:** Once the installer finishes, you have successfully installed Python on your computer.
If you'd like, you can try to experiment with Python's **interactive mode** by running the application you just installed. We will typically use a different program to write Python code, however.

### Task 2: Install PyCharm
**🎯 Task Goal:** Download and install the PyCharm IDE.

**PyCharm:** Integrated Development Environments (IDEs) are software tools that provide comprehensive facilities for software development.
PyCharm, developed by JetBrains, is a widely used IDE for Python.
It offers features like code analysis, debugging, and testing, making Python coding easier and more efficient.

1. **Access the JetBrains Website:** Open the [JetBrains.com: Get Your Educational Tool](https://www.jetbrains.com/edu-products/download/#section=pycharm-edu) page in a web browser.
2. **Select the Correct Version:** Next to the blue "Download" button, ensure that the correct version for your operating system is selected by pressing the blue downward arrow button.
   - **Choosing for Apple Machines:** If using a Mac, click the Apple Icon then select "About this Mac".
   Look for either "Processor" or "Chip" information.
   If you see "Intel", you have an Intel Mac.
   If you see anything like "M1", "M1Pro", "M2", etc., then you have an Apple Silicon Mac.
   - **Ask for Help:** If you are unsure, please ask me or an assistant instructor. We're happy to help.
3. **Begin the Download:** Press the blue "Download" button to download PyCharm.
4. **Follow Installation Steps:** Open the downloaded file and proceed based on your system:
   - **Windows:** Use default values in the installer.
   - **macOS:** Drag PyCharm into your application folder from the `.dmg` file.
   - **Linux:** Extract the `.targ.gz` file to your chosen location.

**🎉 Installation Complete:** Once finished, you have successfully installed PyCharm on your computer.
You are ready to proceed to the next task.

### Task 3: Install Git
**🎯 Task Goal:** Ensure Git is installed on your system.

**Version Control Using Git:** Version Control Systems (VCS) are essential tools for managing changes to computer programs, documents, or other collections of information.
Git is one popular version control system.
GitHub, a web-based platform, uses Git and helps in hosting and managing code.
In this course, we'll use GitHub to manage assignments, streamlining the submission and feedback process.

1. **Open PyCharm:** Run PyCharm.
2. **Choose "Get from VCS":**  In PyCharm's main window, select "Get from VCS".
3. **Install Git:** Follow the prompt to "Download and Install" Git.
   - **No Download Option:** If Git is already installed, you will not see this option and may proceed to Task 2.
4. **Progress Bar:** You may see several confirmation dialogs and will eventually be given an installation progress bar.
   - **For Mac Users:** This may take a significant amount of time on macOS. Be prepared.
5. **Close PyCharm:** When finished, close PyCharm to complete the installation.

**🎉 Task Complete:** You've successfully installed Python, PyCharm, and Git; your development environment is now set up.
These tools are key for completing your coding projects and assignments.
You are ready to proceed to the next task.

### Task 4: Downloading An Assignment from GitHub

**🎯 Task Goal:** Use PyCharm to clone an assignment from GitHub.

> [!IMPORTANT]
> 
> This part requires you to have created a GitHub account.

**GitHub Classroom:** GitHub Classroom is a tool that streamlines the use of GitHub in a classroom setting.
It allows me to efficiently distribute and collect your code assignments on GitHub.
Each assignment you receive will have a unique link that creates your personal copy of the assignment in your GitHub account.

**Accepting an Assignment:** Every lab assignment starts with accepting it on GitHub Classroom.
This process ensures that you have your copy of the assignment in your GitHub account, where you can work on it independently.

1. **Access the Assignment Link:** You will receive a unique link for each assignment. Click on this link to start the process.
2. **Accept the Assignment:** After clicking the link, you'll be taken to a GitHub page. Click on the "Accept this assignment" button. This creates a new repository under your GitHub account for the assignment.
3. **Copy the Repository URL:** Once accepted, GitHub will set up your repository. This may take a few moments. After the repository is created, you'll be redirected to its page on GitHub. Find the green "Code" button, and under it, you'll see a URL. This is the repository's URL, which you'll need to *clone* the repository in PyCharm. Click the "Copy" button to copy this URL.

**Cloning with PyCharm:** PyCharm makes it easy to download a copy of your assignment.
By cloning your Git repository via PyCharm, you’re not only downloading the assignment files but also setting up a direct connection to your GitHub repository for easy updates and submissions.

1. **Open PyCharm:** Start PyCharm on your computer.
2. **Choose "Get from VCS":** In the PyCharm welcome window, click on "Get from VCS".
3. **Paste the Repository URL:** In the new window that opens, you'll see a field labeled 'URL'.
   Paste the repository URL you copied from GitHub here.
   - **Verify Your GitHub Account:** You may be asked to verify your GitHub account.
     Use the option to log in via GitHub.com and use your GitHub account credentials.
4. **Clone and Open the Project:** Click the "Clone" button.
  PyCharm will now download a copy of your GitHub and open it as a new project.

**🎉 Task Complete:** You've successfully acquired your first lab assignment and have it ready within PyCharm.
You may proceed to the next task, which will be your first coding task!

### Task 5: Modify the "Hello World" Program
**🎯 Task Goal:** Modify the `hello.py` script to display your name.

**Hello World:** The "Hello World" program is traditionally the first program that programmers learn to write.
These programs typically output the message "Hello World" using a **print statement**.
Here, you will modify one such "Hello World" program.

1. **Open the Script:** In PyCharm, you should see the files `hello.py` and `README.md` within the Project tool window on the left side of the main window. Double-click the `hello.py` file to open it in the PyCharm Editor tool window.
   - **I Don't See Any Files:** If you do not see a list of files, you can open the Project tool window by clicking on the "folder" button on the left side of the main window.
2. **Run the Script:** Press the "Run" button (depicted by a green right arrow) to run the `hello.py` program.
   You will see the "Run tool window" appear on the bottom part of the main window, which will display the following message:
 
   ```
   Hello Enter Your Name Here!
   ```
3. **Modify the Script:** This script uses **strings** (text within quotation marks) to represent a name.
   Find the string `'Enter Your Name Here'` and change it to **your full name**.
   Be sure to include the single quotation marks!
4. **Run the Modified Script:** Press the "Run" button
   The Run tool window will display the word "Hello" with your name.

**🎉 Task Complete:** You've just completed your first coding task.
While this task is complete, however, your changes exist only on your local machine.
In the next task, we'll synchronize your updates to GitHub, ensuring I can properly access and grade your work.

### Task 6: Submit Work to GitHub and Canvas
**🎯 Task Goal:** Push your code update to GitHub and submit a screenshot to Canvas.

**Version Control and Submission:** Learning to use version control systems like GitHub is an essential skill for modern programmers.
I use Git myself creating your assignments.
In this task, you will **commit** (record) and then **push** (upload) your modified `hello.py` script to GitHub using PyCharm, then submit evidence of your work on Canvas.
You will follow this process for each lab assignment in this course.

1. **Commit Your Changes:** In PyCharm, right-click on the `hello.py` file in the Project tool window and select `Git` > `Commit...`.

   - In the commit dialog, enter a message like "Updated hello.py with my name", then click `Commit`.
2. **Push to GitHub:** After committing, click the `Git` option in the top menu and select `Push`.
   - In the push dialog, confirm that your commit is listed and click `Push`.
   - This action synchronizes your local changes with the GitHub Classroom repository.
3. **Verify on GitHub:** Open a web browser and navigate to [GitHub.com](https://github.com).
   - Go to your repository page to confirm that your updated `hello.py` is there. You should see the commit message you entered earlier.
4. **Submit to Canvas:** Take a screenshot of your GitHub repository page, ensuring that the repository name and your recent commit (with its completion checkmark) are visible.
   - Submit this screenshot to the designated assignment area on Canvas.
   - See the "Resources" section below for system-specific instructions on how to save a screenshot.

**🎉 Task Complete:** You have now successfully navigated the process of code modification, version control, and assignment submission.
This not only completes your task but also gives you practical experience with tools you'll frequently use in this class and as a professional programmer.

## Resources
- [JetBrains.com: User Interface](https://www.jetbrains.com/help/pycharm/guided-tour-around-the-user-interface.html#editor): A guide that describes key components of the PyCharm interface.
- [JetBrains.com: Commit and push changes to Git repository](https://www.jetbrains.com/help/pycharm/commit-and-push-changes.html): A guide that describes the commit and push process in PyCharm. The keyboard shortcuts and menu names are most important here.
- [Microsoft: How to take screenshots on Windows 11](https://www.microsoft.com/en-us/windows/learning-center/how-to-screenshot-windows-11): A guide that describes how to take a screenshot on a Windows system.
- [Apple: Take a screenshot on your Mac](https://support.apple.com/en-us/102646): A guide that demonstrates how to take a screenshot on an Apple system.


