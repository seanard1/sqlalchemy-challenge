# sqlalchemy-challenge

Challenge for Module 10 with SQL Alchemy and Flask

## Instructions/Premise

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

## Modules

sqlalchemy

flask

matplotlib

pandas

datetime

## Summary

This repository takes a look at climate data from Hawaii using SQLalchemy and Flask to parse and showcase the data.

The Jupyter Notebook climate_analysis explores the data using a number of queries, showing charts related to both rainfall and temperatures as desired. It uses specific session queries to the engine created with SQLalchemy to bring back the exact results we want, then converts the data to a Pandas dataframe in order to plot it using Matplotlib.

The app.py Python file is designed to showcase the data using Flask to create an API that users can query for different parts of the data. This includes the ability to see summary statistics between two dates of the user's choosing. 

## Citations

Virtually all of the code came from in-class sessions for this challenge, with most of my citations for this week coming from pesky chart formatting with Matplotlib. I have a few new tools we did not go over in the past in trying to get these charts to look good.

- https://stackoverflow.com/questions/5735208/remove-the-legend-on-a-matplotlib-figure

The legend on the chart was unneccesary but was coming in automatically. This was what I found to remove it. 

- https://stackoverflow.com/questions/67253174/how-to-set-space-between-the-axis-and-the-label

- https://stackoverflow.com/questions/12750355/python-matplotlib-figure-title-overlaps-axes-label-when-using-twiny

These two links came from trying to give some breathing room to the labels and titles on the charts. It felt too cramped when the default settings flowed in. 

- https://docs.kanaries.net/tutorials/Matplotlib/matplotlib-savefig-cuts-off-labels

Probably as a result of the above formatting, I needed a solution for the savefig execution cutting off the labels for the exported PNGs.

- https://www.w3schools.com/html/html_entities.asp

One small challenge came outside the charts, which was the < > not appearing in the available routes. Luckily Module 11's first class clued me into where to look.