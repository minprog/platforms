# Flack

## Objectives

* Learn to use JavaScript to run code client-side.
* Become more comfortable with building web user interfaces.
* Gain experience with Socket.IO to communicate between clients and servers.

## Overview

In this project, you'll build an online messaging service using Flask, similar
in spirit to [Slack](https://slack.com/). Users will be able to sign into your
site with a display name, create channels (i.e. chatroom's) to communicate in,
as well as see and join existing channels. Once a channel is selected, users
will be able to send and receive messages with one another in real time.
Finally, you'll add a personal touch to your chat application of your choosing!

## Preparations

Before your do anything else, watch and understand these video lectures:

- Lecture 4, [ORMs, APIs](/lectures/orms)
- Lecture 5, [Javascript](/lectures/javascript)
- Lecture 6, [Front ends](/lectures/frontends)

## Milestones

We recommend that you try to meet the following milestones:

* Complete the Display Name, Channel Creation, and Channel List steps.
* Complete the Messages View and Sending Messages steps.
* Complete the Remembering the Channel and Personal Touch steps.

## Getting Started

### GitHub Classroom

1. [Click here](https://classroom.github.com/a/pELlBdNK) to go to the GitHub Classroom page for starting the assignment.
2. Click the green "Accept this assignment" button. This will create a GitHub repository for your project. Recall that a git repository is just a location where your code will be stored and which can be used to keep track of changes you make to your code over time.
3. Click on the link that follows "Your assignment has been created here", which will direct you to the GitHub repository page for your project. It may take a few seconds for GitHub to finish creating your repository.
4. In the upper-right corner of the repository page, click the "Fork" button, and then (if prompted) click on your username. This will create a fork of your project repository, a version of the repository that belongs to your GitHub account.
5. Now, you should be looking at a GitHub repository titled username/flack-username, where username is your GitHub username. This will be the repository to which you will push all of your code while working on your project. When working on the project, do not directly push to the uva-webapps/flack-username repository: always push your code to your username/flack-username repository.

### Python and Flask

Make sure you installed Python (Instruction for [Windows](/installation/Windows) and [macOS](/installation/macOS)).

To run this Flask application:

Open "Git Bash" on Windows or the "Terminal" on macOS or Linux.

`cd` to a directory where you want to put your project.

Clone your `username/flack-username` repository from GitHub and navigate into this directory.

Run

    $ pip3 install -r requirements.txt

to make sure all of the necessary Python packages (Flask and SQLAlchemy, for instance) are installed.

Run

    $ export FLASK_APP=application.py

to the environment variable `FLASK_APP` to be `application.py`.

Run `flask run` to start up your Flask application.
If you navigate to the URL provided by `flask`, you should see the text
   `"Project 2: TODO"`!

## Requirements

Alright, it's time to actually build your web application! Here are the
requirements:

* **Display Name**: When a user visits your web application for the first time,
  they should be prompted to type in a display name that will eventually be
  associated with every message the user sends. If a user closes the page and
  returns to your app later, the display name should still be remembered.
* **Channel Creation**: Any user should be able to create a new channel, so long
  as its name doesn't conflict with the name of an existing channel.
* **Channel List**: Users should be able to see a list of all current channels,
  and selecting one should allow the user to view the channel. We leave it to
  you to decide how to display such a list.
* **Messages View**: Once a channel is selected, the user should see any
  messages that have already been sent in that channel, up to a maximum of 100
  messages. Your app should only store the 100 most recent messages per channel
  in server-side memory.
* **Sending Messages**: Once in a channel, users should be able to send text
  messages to others the channel. When a user sends a message, their display
  name and the timestamp of the message should be associated with the message.
  All users in the channel should then see the new message (with display name
  and timestamp) appear on their channel page. Sending and receiving messages
  should NOT require reloading the page.
* **Remembering the Channel**: If a user is on a channel page, closes the web
  browser window, and goes back to your web application, your application should
  remember what channel the user was on previously and take the user back to
  that channel.
* **Personal Touch**: Add at least one additional feature to your chat application
  of your choosing! Feel free to be creative, but if you're looking for ideas,
  possibilities include: supporting deleting one's own messages, supporting use
  attachments (file uploads) as messages, or supporting private messaging
  between two users.
* In `README.md`, include a short writeup describing your project, what's
  contained in each file, and (optionally) any other additional information the
  staff should know about your project. Also, include a description of your
  personal touch and what you chose to add to the project.
* If you've added any Python packages that need to be installed in order to run
  your web application, be sure to add them to `requirements.txt`!

Beyond these requirements, the design, look, and feel of the website are up to
you! You're also welcome to add additional features to your website, so long as
you meet the requirements laid out in the above specification!



## Hints

* You shouldn't need to use a database for this assignment. However, you should
  feel free to store any data you need in memory in your Flask application, as
  via using one or more global variables defined in `application.py`.
* You will likely find that [local
  storage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)
  will prove helpful for storing data client-side that will be saved across
  browser sessions.
* When getting the error: `ValueError: signal only works in main thread` it
  means you have set `FLASK_DEBUG` to `1`. To resolve this issue run
  `unset FLASK_DEBUG` to disable debug mode as is isn't compatible with
  Flask-SocketIO.


## Testing

When testing your website, try testing is with multiple different browsers.
Also make sure you tested your website with different channels open.

## How to Submit

1. Using Git, push your work to GitHub. Ask for help if needed!
2. Go to the GitHub page for your username/flack-username repository (note: this is different from the uva-webapps/flack-username repository).
3. On the right side of the screen, click the Pull request button.
4. Make sure that the "base fork" is uva-webapps/flack-username, and the "head fork" is username/flack-username.
5. Click "Create pull request".
6. On the next page, click the "Create pull request" button again.
7. Click "Merge pull request".
8. Click "Confirm merge".
9. Submit the link to your project's GitHub repository below (the one with uva-webapps/flack-username).
10. On (or before) the date of the deadline, show your working website to one of the staff.
