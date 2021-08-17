# Scraping

What was the best year for movies?

This is often debated on the internet:

- https://www.washingtonpost.com/news/style/wp/2018/12/28/feature/what-was-the-best-year-in-movie-history/
- https://www.independent.co.uk/arts-entertainment/films/features/film-history-best-year-1999-star-wars-matrix-fight-club-sixth-sense-a9036911.html
- https://www.reddit.com/r/movies/comments/5m6jrp/best_year_for_movies/
- https://www.maxim.com/entertainment/10-movies-prove-1994-was-best-year-film-history
- ...

Let's try to see if we can find some data to settle these discussions. For this we need to do some *web scraping*.

Web scraping is a way of extracting data from websites. While this process could be done manually (by reading information on a website, and then copying that information to a file) it is usually done through the use of software. Scraping can be a valuable tool for extracting data. A website might not give you an option to download the content, either through an API or a direct download link. One example of such a website is the IMDB page that we will be scraping in this exercise.

In order to answer the questions we'll have to make some radical assumptions. Most importantly we're going to assume that the top 5 movies of each year are indicative of how good for movies that year is. So we'll reformulate the question:

What year had the best average IMDB rating for it's top 5 movies?

Admittedly a much less catchy question.

## Provided code

Download the provided code for this assignment: []

## Libraries

In this assignment you will learn to use three libraries:

- You'll use *BeautifulSoup* to parse the Document Object Model (DOM) if IMDB. We provide some scaffolding for the programming exercise. [BeautifulSoup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- *Pandas* provide a convenient way to store and manipulate data in python. [Pandas documentation](https://pandas.pydata.org/docs/)
- With *Argparse* you can manage command line arguments for your programming. [Argparse documentation](https://docs.python.org/3/library/argparse.html)

## Pipeline

For this exercise you will set up a data pipeline with the following steps:

| Pipeline step          	| This week                                                                                     |
|------------------------	|---------------------------------------------------------------------------------------------- |
| Asking a Question      	| What was the best year for movies?                                                            |
| Acquiring the data     	| Using pandas to scrape IMDB pages to a CSV file (`scraper.py`)                                |
| Transforming the data 	| Use the acquired CSV to generate another file containing a top 5 for each year (`extract.py`) |
| Visualizing the data  	| Plotting the average score for the top 5 movies for each year (`visualize_years.py`)          |

## Before starting

1. For this assignment you'll need to have the following Python 3 libraries installed: Requests, Pandas, and BeautifulSoup4.

2. To get you started we have provided you with some code (`scraper.py` and `helpers.py`). `helpers.py` contains the function `simple_get` for loading a webpage. The file `scraper.py` is the file you'll be editing. To get started, it already contains some code that imports `simple_get` and uses it to load the correct IMDB address and prints the first line.

3. When scraping a website there can be inconsistencies in the HTML. It could for instance be that there are missing data (for instance the realease year for a film or the runtime). Make sure to check this and insert an appropriate value when something is missing.

## DOM scraping and traversal

A webpage is a document. This document can be either displayed in the browser window or as the HTML source. The Document Object Model (DOM) represents that same document so it can be manipulated. The DOM is an object-oriented representation of the webpage and can be used as a programming interface for HTML and XML documents. It represents the page so that programs can change the document structure, style, and content.

![embed](https://www.youtube.com/embed/YK78KhMf7bs?t=68)

![embed](https://www.youtube.com/embed/GBKwdFEyJks)

## BeautifulSoup

To scrape data from webpages, we will be using BeautifulSoup, a Python web mining module. Its description is as follows: _Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work._

This is the introductory exercise to BeautifulSoup. We will try to guide you along as much as possible, but you should read up on documentation and get used to doing that. It's a really useful skill and a big part of programming is self-­learning! Watch the following videos on HTML and the DOM. Ignore any reference to JavaScript (you may replace it in your mind with BeautifulSoup), as it will not be needed in our exercises.

![embed](https://www.youtube.com/embed/ng2o98k983k)

### Building `scraper.py`

To get you started we have provided you with a script (`scraper.py`) that loads the correct IMDB address.

Open up and read the `scraper.py`-file. Note that this is just some scaffolding, so you actually don't have to use this at all. As long as your code runs at the end of the day and produces the right results in a CSV file, we're happy.

We can run the file using the command:

    python scraper.py data/movies.csv

This does a number of things:

- It reads the following URL: https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=1&view=advanced
- The function `extract_movies()` reads the header from the webpage and prints it. This print statement is just an example to get you started, but should be removed. The function shouldn't print anything when it's finished.
- The function `extract_movies()` returns a pandas DataFrame with nonsense values. This is also just an example to get you started. This dataframe should be filled with the values from the website.
- The DataFrame is written to the csv file: data/movies.csv

## Step 1

### Goal
First, implement the `extract_movies()` function. It should extract a `DataFrame` containing the highest rated movies from the passed DOM (which is of the IMDB page). Each movie entry should be a dictionary that contains the following fields:

  - Title
  - Rating
  - Year of release (only a number!)
  - Actors/actresses (separated by a semicolon `;` if more than one)
  - Runtime (only a number!)
  - URL (a URL to the landing page for that film)

### Example

When we run your program:

    $ python scraper.py data/top50.csv

It should produce a file called `top50/csv` in the directory `data` containing the following data:

    title,rating,year,actors,runtime,url
    Hababam Sinifi,9.3,1975,Kemal Sunal;Münir Özkul;Halit Akçatepe;Tarik Akan,87,https://www.imdb.com//title/tt0252487/
    The Shawshank Redemption,9.3,1994,Tim Robbins;Morgan Freeman;Bob Gunton;William Sadler,142,https://www.imdb.com//title/tt0111161/
    Aynabaji,9.2,2016,Chanchal Chowdhury;Masuma Rahman Nabila;Bijori Barkatullah;Partha Barua,147,https://www.imdb.com//title/tt5354160/

    ...

    The Matrix,8.7,1999,Lilly Wachowski;Keanu Reeves;Laurence Fishburne;Carrie-Anne Moss;Hugo Weaving,136,https://www.imdb.com//title/tt0133093/
    Lepa sela lepo gore,8.7,1996,Dragan Bjelogrlic;Nikola Kojo;Dragan Maksimovic;Zoran Cvijanovic,115,https://www.imdb.com//title/tt0116860/

(in total it should contain 51 lines)

You can cross check the output with the information on the [IMDB page](https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=1&view=advanced).

### Hints

#### HTML

`print()` is probably going to be your best friend for debugging, so print often, especially if something goes wrong.

Take a look at the following attributes, taken from the BeautifulSoup documentation, that show some basic functionalities of BeautifulSoup.

        soup.title
        # <title>The Dormouse's story</title>

        soup.title.name
        # u'title'

        soup.title.string
        # u'The Dormouse's story'

        soup.title.parent.name
        # u'head'

        soup.p
        # <p class="title"><b>The Dormouse's story</b></p>

        soup.p['class']
        # u'title'

        soup.a
        # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

        soup.find_all('a')
        # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
        #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
        #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

        soup.find(id="link3")
        # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

An easy method to finding what class, tag, or id to target with BeautifulSoup is:
- Go to the webpage in your favorite browser
- Right click on the element you are interested in
- Click 'Inspect element'

This will open the browser's inspector functionality which shows you the source HTML of the element you have clicked. Hovering over this HTML source will show the corresponding webpage element.

Also have a look at the `find()` function in the documentation of BeautifulSoup4 and look for the CSS selectors, they will make this exercise much easier!

#### Regex
You might need to filter out some characters from a string. _Especially retrieving multiple actors will become very difficult with BeautifulSoup only._ One method to do this is through the use of [Regular Expressions]. After importing `re`, `re.findall` can be used to find all occurances in a string, while `re.search` can be used to find the first occurence. Keep in mind that the resulting type after these Regular Expressions is still a string!

    >>> import re
    >>> re.findall(r'\d+', '123 dogs jumped the fence and ate over 4400 sheep!')
    ['123', '4400']
    >>> re.search(r'\d{4}', '123 dogs jumped the fence and ate over 4400 sheep!').group()
    '4400'

[Regular Expressions]: https://www.w3schools.com/python/python_regex.asp

Then, implement the `save_csv(outfile, movies)` function. It should write the list of the highest rated movies (`movies`) to `outfile`.


#### Use comments

Keep in mind that the use of BeautifulSoup and RegEx will not necessarily result in _beautiful_ code. In fact, data collection through scraping is known to be a very messy practice. You might need to heavily comment code to make sure that it is understandable. **Especially** retrieving actors will be very messy.

## Step 2

In order to decide which year was best for films, we will need a lot more movies than just the top50. IMDB does not provide a single wat to directly load a page with the top 4000 or so movies. But on the website, by clicking *next*, we can load the next 50 movies, and the next, and the next, etc.

If we pay attention to the URL we see that one thing changes, every time we load the next 50:

1. `https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=1&view=advanced`
2. `https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=51&view=advanced`
3. `https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=101&view=advanced`
4. ...

The value for `start` increases by 50 every time. So first it's `start=1`, then `start=51`, then `start=101`, etc. We can use this to collect as many top rated movies as we'd like.

### Goal

Adapt your code to collect the top N rated movies.

- Write a loop that calls `extract_movies()` for each successive URL and collects the DataFrame's. (If you wrote it well, you should not have to adapt the function `extract_movies()` itself.)
- In the end all the DataFrames should be concatenated into one big DataFrame, that is then saved as a `.csv`.
- The loop should continue until we know that we have **at least 5 movies for every year** between 1930 and 2020.
- Note that the code should be adaptive. If we decide to provide another period (than between 1930 and 2020) with the optional parameters `-s` and `-e`, it should generate a top N for only that period.
- The resulting `.csv` should be sorted by year (ascending).

### Example

When we run your program:

    $ python scraper.py -s 1930 -e 2020 -m 5 data/movies.csv

You should wind up with a large (thousands of lines) `.csv` file, like this:

    title,rating,year,actors,runtime,url
    Animal Crackers,7.5,1930,Groucho Marx;Harpo Marx;Chico Marx;The Marx Brothers,97,https://www.imdb.com//title/tt0020640/
    Hell's Angels,7.3,1930,Edmund Goulding;James Whale;Ben Lyon;James Hall;Jean Harlow;John Darrow,127,https://www.imdb.com//title/tt0020960/
    Der blaue Engel,7.7,1930,Emil Jannings;Marlene Dietrich;Kurt Gerron;Rosa Valetti,104,https://www.imdb.com//title/tt0020697/

    ...

    Sound of Metal,7.8,2019,Riz Ahmed;Olivia Cooke;Paul Raci;Lauren Ridloff,120,https://www.imdb.com//title/tt5363618/
    The Boy Who Harnessed the Wind,7.6,2019,Chiwetel Ejiofor;Maxwell Simba;Felix Lemburo;Robert Agengo,113,https://www.imdb.com//title/tt7533152/
    Batla House,7.2,2019,Nora Fatehi;Mrunal Thakur;John Abraham;Rajesh Sharma,146,https://www.imdb.com//title/tt8869978/


## Done

In the next part we will focus on transforming the data.
