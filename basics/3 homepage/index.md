# Homepage

## Objectives

* Become comfortable with HTML and CSS to design and style webpages.
* Learn to use SCSS to write more complex stylesheets for your webpages.

## What you need to find out

How to:

* write HTML tags to structure a page
* use CSS and SCSS to style a page
* use git to manage to project's files
* use GitHub to host your website
* work with **sass** in the terminal

## Preparations

Before your do anything else, watch and understand these video lectures:

- Lecture 0, [Git](/lectures/git)
- Lecture 1, [HTML and CSS](/lectures/html)

If you have any questions about the lectures, please post a question!

## Getting Started

In this course, we'll use GitHub Classroom to distribute project starter files. To begin this project:

1. [Click here](https://classroom.github.com/a/_ZZS7O_t) to go to the GitHub Classroom page for starting the assignment.
2. Click the green "Accept this assignment" button. This will create a GitHub repository for your project. Recall that a git repository is just a location where your code will be stored and which can be used to keep track of changes you make to your code over time.
3. Click on the link that follows "Your assignment has been created here", which will direct you to the GitHub repository page for your project. It may take a few seconds for GitHub to finish creating your repository.
4. Now, you should be looking at a GitHub repository titled uva-webapps/homepage-username, where username is your GitHub username. This will be the repository to which you will push all of your code while working on your project. You will commit directly to this repository.
5. *Before you go on*, submit the link to your repository through the form at the very bottom of this page. If your do not see a form, make sure that you're logged in!
6. Because we added a git branch called `"gh-pages"`, GitHub Pages should already be enabled for the repository. Navigate to the main page of the repository and click "environment" > "Deployments" and then on the "View deployment" button. You should see the URL at which your GitHub pages website will (soon) live! But first, we'll need to add some HTML to your repository.

### Your First Webpage

Okay, let's add a simple webpage to your repository. First, on your working repository page (https://github.com/uva-webapps/homepage-username), click on the green "Clone or download" button. Copy the "Clone with HTTPS" link to your clipboard (if familiar with SSH, you can use that instead).

Open "Git Bash" on Windows or the "Terminal" on macOS.

`cd` to a directory where you want to put your project and run

    git clone repository_url homepage

where `repository_url` is the link you just copied from GitHub. You will be prompted for your GitHub username and password


Go ahead and run `cd homepage` to enter your repository. Now, run

    touch index.html

to create a new `index.html` file in your repository. Open the file with your
favorite text editor. Then, paste in the following contents:

    <!DOCTYPE html>
    <html>
        <head>
            <title>My Webpage</title>
        </head>
        <body>
            Hello, world!
        </body>
    </html>

Then, save your `index.html` file.

Okay, it's time to push our HTML file to your repository on GitHub! In your terimal window, in your project0 directory, run:

    git add index.html

to let `git` know that you want to include `index.html` in your next commit to this repository. Now, run:

    git commit -m "Add first webpage"

to commit your changes to this repository. The string after `-m` is your commit message, a short written description of the changes you've made in this commit. Writing succinct, informative commit messages will help you refer back to old changes later!

Now, let's push our changes online. Run:

    git push

and your commit should be pushed to GitHub, and deployed to GitHub Pages. If you check your repository page on GitHub, and then check the GitHub Pages link that was generated for you earlier, you should see a webpage that just says "Hello, world!" with a title of "My Webpage." Your webpage is now deployed to the internet!

## Requirements

Alright, now it's time to make your website your own. Design a personal webpage
about yourself, one of your interests, or any other topic of your choice. The
subject matter, look and feel, and design of the site are entirely up to you,
subject to the following requirements:

* Your website must contain at least four different `.html` pages, and it
  should be possible to get from any page on your website to any other page by
  following one or more hyperlinks.
* Your website must include at least one list (ordered or unordered), at least
  one table, and at least one image.
* Your website must have at least one stylesheet file.
* Your stylesheet(s) must use at least five different CSS properties, and at
  least five different types of CSS selectors. You must use the `#id` selector
  at least once, and the `.class` selector at least once.
* Your stylesheet(s) must include at least one mobile-responsive `@media` query,
  such that something about the styling changes for smaller screens.
* You must use Bootstrap 4 on your website, taking advantage of at least one
  Bootstrap [component](https://getbootstrap.com/docs/4.3/components/),
  and using at least two Bootstrap columns for layout purposes using
  Bootstrap's [grid model](https://getbootstrap.com/docs/4.3/layout/grid/).
* Your stylesheets must use at least one SCSS variable, at least one example of
  SCSS nesting, and at least one use of SCSS inheritance.
* In `README.md`, include a short writeup describing your project, what's
  contained in each file, and (optionally) any other additional information the
  staff should know about your project.
* Also in `README.md`, prominently feature a link to the live GitHub Pages version of your homepage.

Note that not all of the above requirements are covered in [Lecture 0](/lectures/git), some will
be introduced in [Lecture 1](/lectures/html).

## How to Submit

You should have submitted your repository's URL while starting the project, in the "Starting the project" section, above!

Example: `https://github.com/uva-webapps/homepage-username`
