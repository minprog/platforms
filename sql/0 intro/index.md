# Introduction

This module is all about extracting data from a database. You will learn a new specialized language to interact with databases: SQL short for Structured Query Language. Through which you can extract data from a movies database like so:

        SELECT UPPER(title), COUNT(title) FROM shows ORDER BY COUNT(title) DESC LIMIT 10

Arguably a little cryptic, but SQL does read as a somewhat English-like language. The line above selects the uppercase of the title and counts the occurances of each tile from a database table called shows, orders the results by that count in a descending order and gives back the top 10. That is the advantage of specialized languages like SQL, with very little code, you are able to express much of what you need. 

With SQL you will able to Create, Read, Update or Delete (CRUD) data in a persistent relational database. These types of databases are capable of quickly retrieving and searching through its contents. All while giving you the programmer the tools to store an enourmous amount of data and efficiently too!