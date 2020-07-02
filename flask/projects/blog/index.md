# Blog

## Objectives

* Learn to use Jekyll to create a more complex website.
* Better understand how to separate responsibilities in your code.

## What you need to find out

How to:

* install Ruby and Jekyll,
* configure Jekyll,
* write Markdown,
* write templates with Liquid,
* embed SCSS into a Jekyll project,
* put all elements together, and
* put your Jekyll site on GitHub Pages.

## Preparations

For this project, you'll be using Jekyll, which is a **static site generator**. It allows you to define some logic using a programming language called Liquid, write templates in HTML, add layout using CSS, and write "blog posts" using Markdown. Mike Dane provides a short introduction:

![embed](https://www.youtube.com/embed/T1itpPvFWHI)

> All of these languages serve their own purposes. It's quite a bit of work to master all of these, but it will eventually allow you to write each of the parts of your website more easily. We call this **separation of concerns**: your project is separated in multiple parts, each having a specific purpose.
> 
> In the case of creating web pages with HTML, we usually include separate files written in the languages CSS and Javascript. Their purposes are also separate: HTML is for writing content and some layout, CSS is for specifying layout rules, and Javascript is for defining user interactions.
>
> In Jekyll, we acknowledge that HTML is sometimes used for layout purposes, and we separate out the content into Markdown files, simplifying writing content even more. HTML is only used for layout and defining components on the website. So, more separation of concerns!
> 
> Separating these parts will allow you to keep track of each more easily. As your programming projects grow, this becomes more and more important.

Jekyll is able to take your files and from those generate a HTML/CSS-based website that may be put online. Even better, you can put your Jekyll website on GitHub, make changes, and GitHub Pages will put it online for you.

## Getting Started

You are going to need to install Jekyll to be able to generate your website skeleton, and to test your site locally (i.e., on your own computer). Later on, you will put the site on GitHub Pages.

1. Follow Mike's instructions to perform the installation on either Mac or Windows:

    ![embed](https://www.youtube.com/embed/WhrU9m82Wm8)
    ![embed](https://www.youtube.com/embed/LfP7Y9Ja6Qc)

2. Then, generate a new website according to the example:

    ![embed](https://www.youtube.com/embed/pxua_1vyFck)

## The Parts and the Whole

- First, let's have a look at **front matter**. Using front matter, you can attach variables to your written content for the website. For example, if you have a Markdown file for a blog post, you can attach a *category* to it, if your site supports showing different categories of posts.

    ![embed](https://www.youtube.com/embed/ZtEbGztktvc)

- Then, learn to create a new blog post file in Markdown, using the example from the following video:

    ![embed](https://www.youtube.com/embed/gsYqPL9EFwQ)

    You'll need to get a bit more background on [Markdown](https://daringfireball.net/projects/markdown/basics).

- But besides blog posts, you will generally need to add a few pages to the website containing more static content. For example, on how to contact you or your business. Have a look:

    ![embed](https://www.youtube.com/embed/1na-IWfv08M)

These are the basics parts of any Jekyll website.

## How it all Works

Now let's dive into the details of Jekyll. You aren't quite tied to creating a website just like in the examples. Almost anything in Jekyll is customizable.

- You can specify defaults for front matter variables:

    ![embed](https://www.youtube.com/embed/CLCaJJ1zUHU)

- You can choose a different theme for your website (with some important caveats!):

    ![embed](https://www.youtube.com/embed/NoRS2D-cyko)

- You can create your own layout files using HTML:

    ![embed](https://www.youtube.com/embed/bDQsGdCWv4I)

- You can use the values of variables inside your layouts to make the code more "modular":

    ![embed](https://www.youtube.com/embed/nLJBF2KiOZw)

    (See the [Variables](https://jekyllrb.com/docs/variables/) references on the Jekyll website.)

- You can create "lists" from any collection of posts:

    ![embed](https://www.youtube.com/embed/6N1X5XffuUA)

Note that Jekyll has [built-in support for SCSS](https://jekyllrb.com/docs/assets/). Any `.scss` files in the `css/` folder will automatically be compiled into CSS that the browser can display.

## Intermezzo: Github Pages URL structure

It's nice to preview your Jekyll site before you push your `gh-pages` branch to GitHub (which may sometimes be a bit slow to pick up changes). However, you may run into problems getting your internal links right, because on GitHub, your site will live inside a directory, while on your computer, it will not. In order to assure your site builds properly, you should use the `relative_url` filter for your links:

    For styles with static names:
    
      <link href="{{ "/assets/css/style.css" | relative_url }}" rel="stylesheet">
    
    For documents/pages whose URLs can change:
    
      [{{ page.title }}]("{{ page.url | relative_url }}")

The filter will prepend your site's `url` value to a link. The value of `url` can be defined in your site's config file.

## Starting the project

To get started, accept your assignment on GitHub classroom and initialize your project:

1. [Click here](https://classroom.github.com/a/6Zf8e6MY) to go to the GitHub Classroom page for starting the assignment.
2. Click the green "Accept this assignment" button. This will create a GitHub repository for your project. Recall that a git repository is just a location where your code will be stored and which can be used to keep track of changes you make to your code over time.
3. Click on the link that follows "Your assignment has been created here", which will direct you to the GitHub repository page for your project. It may take a few seconds for GitHub to finish creating your repository.
4. Now, you should be looking at a GitHub repository titled `uva-webapps/blog-username`, where username is your GitHub username. This will be the repository to which you will push all of your code while working on your project (unlike for the first project, you will commit directly to this repository).
5. *Before you go on*, submit the link to your repository through the form at the very bottom of this page. If your do not see a form, make sure that you're logged in!
6. GitHub Pages should already be enabled for the repository. Navigate to the main page of the repository and click "Environments" > "Deployments" and then on the "View deployment" button. You should be able to see the brief text that is in `README.md`. **However,** due to a bug, you may get a 404 error. In that case, just add a slash (`/`) to the URL and it should work!
7. Bookmark your website's URL so you can refer to it while developing your Jekyll blog.
8. Start creating your Jekyll project inside your clone of the `uva-webprog/blog-username` directory:

		# creates a jekyll project in the 'current' directory
		jekyll new .

To create your blog, it might be instructive to follow the step-by-step instructions on [Convert an HTML site to Jekyll](https://jekyllrb.com/tutorials/convert-site-to-jekyll/). However, keep in mind the requirements while making your site! You'll need to have a rough idea of what you're working towards.

## Requirements

Based on your earlier "Homepage" project, create a Jekyll-based website for yourself or some other
topic of choice. Again, the subject matter, look and feel, and design of the site are entirely up
to you, subject to the following requirements:

* Your website must contain at least four different pages, and it
  should be possible to get from any page on your website to any other page by
  following one or more hyperlinks.
* Your website's content (pages and posts) must be written in Markdown.
* Your website must contain at least two different layouts, which must be written in HTML.
* Your website's homepage's layout must include a list of the blog posts from the `_posts` directory.
* Your website's layouts must be based on at least one "[include](https://jekyllrb.com/docs/includes/)" file.
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
* Also in `README.md`, prominently feature a link to the live GitHub Pages version of your blog.

## How to Submit

You should have submitted your repository's URL while starting the project, in the "Starting the project" section, above!

Example: `https://github.com/uva-webapps/blog-username`
