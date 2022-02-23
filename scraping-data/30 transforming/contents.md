# Transforming

We are on our way to answer the question:

What year had the best average IMDB rating for its top 5 movies?

For most years the current data contains many more movies than just the top 5. So we should first do a transformation.

## Goal

Create a new program called `extract.py`. The idea of the program is that you can call it like this:

    $ python3 extract.py data/movies.csv data/top5.csv

This will create a new file, `top5.csv` in the directory `data` that contains a subset from `movies.csv`.

The program has the following requirements:

- It accepts two positional command line arguments the input file and the output file. You should use argparse for this.
- The program reads the data from the input file into a pandas DataFrame.
- It will filter the DataFrame such that it only contains the top N (default is 5) movies from every year.
- It should accept an optional argument `-n` that will allow us to select a lower `N`, so that we could also use the program to generate a top 4 or lower. So we could in principle use the following command to create a top 3: `$ python3 extract.py -n 3 data/movies.csv data/top3.csv`
- The result is written as a `.csv` to the output file.
- The resulting output `.csv` should be sorted by year (ascending)

Do not forget to keep an eye on code design. Use functions, choose useful names for your variables, prevent code repetition, place comments, etc.

## Checking your answer

You can apply some common sense testing to see if your answer is correct:

How many lines do you expect the file to have?

Does the top 5 in your file correspond to what you find on IMDB?

> You can manipulate the dates in the URL (`https://www.imdb.com/search/title/?title_type=feature&release_date=1930-01-01,2020-01-01&num_votes=5000,&sort=user_rating,desc&start=1&view=advanced`) to have IMDB generate a top 50 for a specific year.

## Done

In the next step you will visualize the date to finally answer the question: What year had the best average IMDB rating for its top 5 movies?
