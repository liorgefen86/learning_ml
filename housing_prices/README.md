# Housing prices in California

The objective of this project is to go through the different steps of a machine learning project and get familiarized with them. The different steps will be added here as I go through the steps.

### - Big picture of the project:

Before the data is gathered of any algorithm is applied, we most first look
at the big picture of the project and ask ourselves several questions about it.
 - What is the frame of the project, its reason
 - How it fits an actual solution? (if there is any available)
 - What kind of problem should it tackle?
    - Supervised/unsupervised, etc.
    - Regression or classification, or ...
    - What learning technique should be applied (online, batch, etc.)
 - What performance measure should be used:
    - A well known performance measure is the **Root Mean Square Error** or **RMSE**
    
#### Data pipeline
Data analysis projects are usually built around pipelines. But what are pipelines?
Pipelines are a set of instructions/actions that will be applied to the data at different stages.
A pipeline can be the copy data from one data store to a new location and load it in a pandas dataframe.
The order in which data pipelines are ordered is what constitute a **data flow**.

#### Performance measure
It is important to select a performance measure which will give us an 
indication on how well the model is performing. The performance measure should be
selected according to the type of analysis we are going to perform.
For instance, for a regression problem, a typical performance measure is the 
**Root Mean Square Error** or **RMSE**. Its mathematical formula is in the jupyter notebook.

### - Getting Data
The next step is to gather the data we will be using. Usually, data will be in a database, such a Relational Database.
Here, we will just download the data, contained in a CSV file, and read it with **Pandas**.
It is good practice to automate the process so data can be retrieved easily on other system, without performing all the steps again and again.
For this, we need to create functions that will handle different steps in the process.
The first function will download the data and decompress it. The second function will read the file
and return a **Pandas** dataframe (see __data_manip.py__ file).

Before proceeding with any analysis on a dataset, it is best to split it first into a training and testing datsets.
Splitting the dataset before any analysis helps avoiding **data snooping bias**.
By doing an analysis on the entire data, the data scientist might find over optimistic patterns
that will fit well on the test dataset but won't necessarily generalize well the model.
