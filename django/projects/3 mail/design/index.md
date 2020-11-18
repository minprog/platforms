# Mail: Design Document


## Understanding

In the distribution code is a Django project called `project3` that contains a single app called `mail`.

First, after making and applying migrations for the project, run `python manage.py runserver` to start the web server. Open the web server in your browser, and use the "Register" link to register for a new account. The emails you'll be sending and receiving in this project will be entirely stored in your database (they won't actually be sent to real email servers), so you're welcome to choose any email address (e.g. `foo@example.com`) and password you'd like for this project: credentials need not be valid credentials for actual email addresses.

Once you're signed in, you should see yourself taken to the Inbox page of the mail client, though this page is mostly blank (for now). Click the buttons to navigate to your Sent and Archived mailboxes, and notice how those, too, are currently blank. Click the "Compose" button, and you'll be taken to a form that will let you compose a new email. Each time you click a button, though, you're not being taken to a new route or making a new web request: instead, this entire application is just a single page, with JavaScript used to control the user interface. Let's now take a closer look at the distribution code to see how that works.

Take a look at `mail/urls.py` and notice that the default route loads an `index` function in `views.py`. So let's up `views.py` and look at the `index` function. Notice that, as long as the user is signed in, this function renders the `mail/inbox.html` template. Let's look at that template, stored at `mail/templates/mail/inbox.html`. You'll notice that in the body of the page, the user's email address is first displayed in an `h2` element. After that, the page has a sequence of buttons for navigating between various pages of the app. Below that, notice that this page has two main sections, each defined by a `div` element. The first (with an `id` of `emails-view`) contains the content of an email mailbox (initially empty). The second (with an `id` of `compose-view`) contains a form where the user can compose a new email. The buttons along the top, then, need to selectively show and hide these views: the compose button, for example, should hide the `emails-view` and show the `compose-view`; the inbox button, meanwhile, should hide the `compose-view` and show the `emails-view`.

How do they do that? Notice at the bottom of `inbox.html`, the JavaScript file `mail/inbox.js` is included. Open that file, stored at `mail/static/mail/inbox.js`, and take a look. Notice that when the DOM content of the page has been loaded, we attach event listeners to each of the buttons. When the `inbox` button is clicked, for example, we call the `load_mailbox` function with the argument `'inbox'`; when the `compose` button is clicked, meanwhile, we call the `compose_email` function. What do these functions do? The `compose_email` function first hides the `emails-view` (by setting its `style.display` property to `none`) and shows the `compose-view` (by setting its `style.display` property to `block`). After that, the function takes all of the form input fields (where the user might type in a recipient email address, subject line, and email body) and sets their value to the empty string `''` to clear them out. This means that every time you click the "Compose" button, you should be presented with a blank email form: you can test this by typing values into form, switching the view to the Inbox, and then switching back to the Compose view.

Meanwhile, the `load_mailbox` function first shows the `emails-view` and hides the `compose-view`. The `load_mailbox` function also takes an argument, which will be the name of the mailbox that the user is trying to view. For this project, you'll design an email client with three mailboxes: an `inbox`, a `sent` mailbox of all sent mail, and an `archive` of emails that were once in the inbox but have since been archived. The argument to `load_mailbox`, then, will be one of those three values, and the `load_mailbox` function displays the name of the selected mailbox by updating the `innerHTML` of the `emails-view` (after capitalizing the first character). This is why, when you choose a mailbox name in the browser, you see the name of that mailbox (capitalized) appear in the DOM: the `load_mailbox` function is updating the `emails-view` to include the appropriate text.

Of course, this application is incomplete. All of the mailboxes simply show the name of the mailbox (Inbox, Sent, Archive) but don't actually show any emails yet. There's no view yet to actually see the contents of any email. And the compose form will let you type in the contents of an email, but the button to send the email doesn't actually do anything. That's where you come in!

### API

You'll get mail, send mail, and update emails by using this application's API. We've written the entire API for you (and documented it below), so that you can use it in your JavaScript code. (In fact, note that we have written **all** of the Python code for you for this project. You should be able to complete this project by just writing HTML and JavaScript).

This application supports the following API routes:

#### `GET /emails/<str:mailbox>`

Sending a `GET` request to `/emails/<mailbox>` where `<mailbox>` is either `inbox`, `sent`, or `archive` will return back to you (in JSON form) a list of all emails in that mailbox, in reverse chronological order. For example, if you send a `GET` request to `/emails/inbox`, you might get a JSON response like the below (representing two emails):


    [
        {
            "id": 100,
            "sender": "foo@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Hello!",
            "body": "Hello, world!",
            "timestamp": "Jan 2 2020, 12:00 AM",
            "read": false,
            "archived": false
        },
        {
            "id": 95,
            "sender": "baz@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Meeting Tomorrow",
            "body": "What time are we meeting?",
            "timestamp": "Jan 1 2020, 12:00 AM",
            "read": true,
            "archived": false
        }
    ]

Notice that each email specifies its `id` (a unique identifier), a `sender` email address, an array of `recipients`, a string for `subject`, `body`, and `timestamp`, as well as two boolean values indicating whether the email has been `read` and whether the email has been `archived`.

How would you get access to such values in JavaScript? Recall that in JavaScript, you can use `fetch` to make a web request. Therefore, the following JavaScript code

    fetch('/emails/inbox')
    .then(response => response.json())
    .then(emails => {
        // Print emails
        console.log(emails);

        // ... do something else with emails ...
    });

would make a `GET` request to `/emails/inbox`, convert the resulting response into JSON, and then provide to you the array of emails inside of the variable `emails`. You can print that value out to the browser's console using `console.log` (if you don't have any emails in your inbox, this will be an empty array), or do something else with that array.

Note also that if you request an invalid mailbox (anything other than `inbox`, `sent`, or `archive`), you'll instead get back the JSON response `{"error": "Invalid mailbox."}`.

#### `GET /emails/<int:email_id>`

Sending a `GET` request to `/emails/email_id` where `email_id` is an integer id for an email will return a JSON representation of the email, like the below:

    {
            "id": 100,
            "sender": "foo@example.com",
            "recipients": ["bar@example.com"],
            "subject": "Hello!",
            "body": "Hello, world!",
            "timestamp": "Jan 2 2020, 12:00 AM",
            "read": false,
            "archived": false
    }

Note that if the email doesn't exist, or if the user does not have access to the email, the route instead return a 404 Not Found error with a JSON response of `{"error": "Email not found."}`.

To get email number 100, for example, you might write JavaScript code like


    fetch('/emails/100')
    .then(response => response.json())
    .then(email => {
        // Print email
        console.log(email);

        // ... do something else with email ...
    });

#### `POST /emails`

So far, we've seen how to get emails: either all of the emails in a mailbox, or just a single email. To send an email, you can send a `POST` request to the `/emails` route. The route requires three pieces of data to be submitted: a `recipients` value (a comma-separated string of all users to send an email to), a `subject` string, and a `body` string. For example, you could write JavaScript code like

    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
          recipients: 'baz@example.com',
          subject: 'Meeting time',
          body: 'How about we meet tomorrow at 3pm?'
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    });

If the email is sent successfully, the route will respond with a 201 status code and a JSON response of `{"message": "Email sent successfully."}`.

Note that there must be at least one email recipient: if one isn't provided, the route will instead respond with a 400 status code and a JSON response of `{"error": "At least one recipient required."}`. All recipients must also be valid users who have registered on this particular web application: if you try to send an email to `baz@example.com` but there is no user with that email address, you'll get a JSON response of `{"error": "User with email baz@example.com does not exist."}`.

#### `PUT /emails/<int:email_id>`

The final route that you'll need is the ability to mark an email as read/unread or as archived/unarchived. To do so, send a `PUT` request (instead of a `GET`) request to `/emails/<email_id>` where `email_id` is the id of the email you're trying to modify. For example, JavaScript code like

    fetch('/emails/100', {
      method: 'PUT',
      body: JSON.stringify({
          archived: true
      })
    })


would mark email number 100 as archived. The body of the `PUT` request could also be `{archived: false}` to unarchive the message, and likewise could be either `{read: true}` or `read: false}` to mark the email as read or unread, respectively.

Using these four API routes (getting all emails in a mailbox, getting a single email, sending an email, and updating an existing email), you should have all the tools you now need to complete this project!


## Creating a design document

Your first to-do is to read the project specification in full and try to imagine what the website will look like. Then, with your partner, create a design document that describes **what** you are going to make and what it will look like. While doing this, there are also some technical challenges that you need to take into account as much as possible.

For this project, we would like you to take the items below as a guide for producing design documentation:

- The project requirements describe the application **workflow**, the steps that users can take to reach certain goals. Use the descriptions of the workflow to make a complete sketch of all pages, including all user interface elements, with lines pointing from buttons toward pages that those buttons lead to.

- Analyse which **models** you're going to need, and create a [Class Diagram](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) specifying all of them. You can do this on paper or user an online tool like [diagrams.net](https://app.diagrams.net).

- The information from the database is needed on different pages. Make an overview of which pages will be using what information from the database.

You should put your lists and sketches in a separate folder in your GitHub repository and embed the pictures in your `README.md` for easy reference.


## Form

<div class="form-check">
  <input name="form[design_doc_done]" class="form-check-input" type="checkbox" value="yes" id="check1" required>
  <label class="form-check-label" for="check1">
    I have added a design document (as Markdown) to my repository as README.md in the root folder
  </label>
</div>

<div class="form-check">
  <input name="form[images]" class="form-check-input" type="checkbox" value="yes" id="check2" required>
  <label class="form-check-label" for="check2">
    I have added neat sketches of all pages in one or more images that are well-readable, and embedded those pictures in the design document using Markdown image tags
  </label>
</div>

<div class="form-check">
  <input name="form[images_dir]" class="form-check-input" type="checkbox" value="yes" id="check3" required>
  <label class="form-check-label" for="check3">
    I have put all images in a separate folder, not in the root folder
  </label>
</div>

<div class="form-check">
  <input name="form[discussed]" class="form-check-input" type="checkbox" value="yes" id="check4" required>
  <label class="form-check-label" for="check4">
    I have discussed my design with another student to get preliminary feedback and to check for completeness
  </label>
</div>

<div class="form-check">
  <input name="form[discussed]" class="form-check-input" type="checkbox" value="yes" id="check5" required>
  <label class="form-check-label" for="check5">
    I have pushed the Markdown to GitHub and checked that it is well-readable when navigating to it via the GitHub website
  </label>
</div>
