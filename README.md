# Bevo-Search

**Devpost**
https://devpost.com/software/bevo-search

**About The Projects**

This project is built using Python as a backend and Unity and C# as a frontend. Behind the gaming-styled animatated interface, where an animated Bevo is the guide, the desktop app uses InterSystem's Vector Search to optimize email search. It returns the results with the most relevance to the search queries outdoing the gmail search in long sentences.


**Pre requisites:**

Python should be installed

Relevant Python code must be ran in Iris-env 

Requires Google API Key to fetch email data

Require Windows Operating System

**Installation guide:**

The file is submitted as a raw file with hardcoded paths. The user should be update the paths based on their local path. This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.
```
git clone 
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

Setup the Gmail API and download the credentials.json. Keep the credentials and the clone file in the same directory.

The csv and exe should be in the same directory. 


**Usage**

It optimizes the search for the emails by leveraging vector search, which highlights and focuses on the semantic relation between words, giving more relevant answer to longer phrases compared to Gmail's regular search bar.


**Contributors:**

Bolong Tang, 
Pascal Garcia, 
Ayush Pokharel, 
Arjit Magar

---

**Vector_Search_Isolated**

This is the folder which contains the vector search file by itself to demonstrate that the search function works.

In order to use it, put appfunctions.py, emails_received.csv (generated from gmailapi.py), input.txt, and output.txt into the same folder. 

Make sure that the Python file runs in the Iris environment. 

The input.txt contains the inputs. 
Line 1: search term/phrase
Line 2: displayed result amount
Line 3: Either DESC or ASC, meaning "ranking from most relevant", and "ranking from least relevant". 
The latter two cannot be changed in the final Unity app. Line 2 is set at 25 and line 3 is set at DESC.

This files makes use of the InterSystem Iris Data Platform.

The search result would be stored into output.txt after appfunctions.py is ran.

---

**Gmail_API.py**

This file pulls email data from Gmail and returns a dataframe with three columns 'From', 'Subject', and 'Message'. 

It requires entering a personal Google API key to be used.

A finished csv file is uploaded to Vector_Search_Isolated. 

---

**Unity**

This folder contains the Unity file that interactively uses Vector Search on Gmail with inputted search phrases. In it, Bevo speaks to help the user search in an entertaining way.

The Python files in this folder differ from the ones in Vector_Search_Isolated in how their paths are defined. These paths are hardcoded, while the ones in Vector_Search_Isolated are relative. 

It contains all the C# scripts. 

