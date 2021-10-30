# Crawling

When we look at the language spoken in the top films, we see that English is very dominant. But how much so compared to other languages? And has this always been the same? Or does this depend on the decade we consider?

We are going to visualize the language representation in top rated movies, to answer the question:

How did language influence in the top rated movies change over the last 9 decades?

The problem, our current dataset does not have any language information. We will have to add that by doing some web crawling.

## Part 1: Web crawling

The file you `top5.csv` you generate before does not contain any language information. The main problem is that this information is not present on the IMDB page that we used. So we will have to get it some other way. We did store the URL's for the webpage of each movie in the `. csv` file. This links to a page with much more detailed information about each movie. This includes language information.

Your goal is to write a program called `crawler.py` that looks up this language information and creates an augmented dataset with this information.

Usage:

$ python crawler.py data/top5.csv data/top5-with-languages.csv

This will take the data from `top5.csv`, use the URL's to read the page for each movie and retrieve the languages spoken in that movie. It will write the results to `top5-with-languages.csv`. So this will look something like this:

    title,rating,year,actors,languages,runtime,url
    emlya,7.3,1930,Stepan Shkurat;Semyon Svashenko;Yuliya Solntseva;Yelena Maksimova,None;Russian,75,https://www.imdb.com//title/tt0021571/
    Animal Crackers,7.5,1930,Groucho Marx;Harpo Marx;Chico Marx;The Marx Brothers,English,97,https://www.imdb.com//title/tt0020640/
    All Quiet on the Western Front,8.1,1930,Lew Ayres;Louis Wolheim;John Wray;Arnold Lucy,English;French;German;Latin,152,https://www.imdb.com//title/tt0020629/

    ...

    Kumbalangi Nights,8.6,2019,Shane Nigam;Soubin Shahir;Fahadh Faasil;Sreenath Bhasi,Malayalam,135,https://www.imdb.com//title/tt8413338/
    Jersey,8.6,2019,Nani;Shraddha Srinath;Sathyaraj;Harish Kalyan,Telugu,157,https://www.imdb.com//title/tt8948790/
    Kaithi,8.5,2019,Karthi;Narain;Ramana;George Maryan,Tamil,145,https://www.imdb.com//title/tt9900782/

Notice the additional `languages` column. Often a movie has more than one language. They are separated by a semicolon `;`.

Requirements:

- The program accepts two positional command line arguments the input file and the output file. You should use argparse for this.
- The program reads the data from the input file into a pandas DataFrame.
- The program follows the URL for each movie and finds the languages spoken in that movie.
- The result is written as a `.csv` to the output file.
- If a movie has more than one language, they should be separated by a semicolon.
- The resulting output `.csv` should be sorted by year (ascending)

### Hints

* Have a look at the `find()` function in the documentation of BeautifulSoup4 and look for the CSS selectors, they will make this exercise much easier!
* The script will be very slow. Each page load will take a couple of seconds. And there will be hundreds of page loads. This is not a problem. But, for your own convenience, **create a small test input file with only two or three movies**, to see if it is working correctly before your run the script for the entire dataset.

## Part 2: Visualizing

Now back to the question:

How did language influence in the top rated movies change over the last 9 decades?

Write a program called `visualize_languages.py` that generates a line plot of the top 10 languages (that occur the most in our dataset) over time.

Usage:

    $ python visualize_languages.py data/top5-with-languages.csv plots/languages.png

The program has the following requirements:

- It should accept two command line arguments. The first argument is the location of the data file, the second argument is the location of the output file. So with the call above the program will generate a plot `languages.png` in the directory `plots`, based on the data of `top5-with-languages` in the directory `data`.
- It should read the input into a pandas DataFrame.
- It should output a `.png` file containing a line plot.
- The plot should have a legend making clear which line corresponds to which language.
- It should show the number of occurrences of each language *per decade*. (Each occurrence counts equally, whether it is the first language or the last language for a movie).
- The horizontal axis of the plot should have the decades (1930s to 2010s), the vertical axis should have the number of occurrences.

Looking at your plot, which was the second most influential language in the 1970s?

<textarea name="form[1]" rows="1" required=""></textarea>

And which language was the second most influential in the 2010s?

<textarea name="form[2]" rows="1" required=""></textarea>

## How to submit

Add `crawler.py` and `visualize_languages.py` to your git repository from the Scraping assignment. Then share the URL to your repository at GitHub once again below. This should look something like: `https://github.com/minprog-platforms/your_repo_name`.