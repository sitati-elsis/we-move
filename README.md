This task enables us to develop a greater understanding of churn and retention around our subscription events.

Below are a set of guidelines we can use to set up the project on our local machines and run it locally:

* Install  PostgreSQL  on you local machine.  
You can follow [this guide](https://www.codementor.io/engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb)
if your local machine is a Macbook

* Install Jupyter Notebooks on your local machine
``` 
pip install jupyterlab
```

# Project Installation

Clone this repo:
```
$ git clone https://Elsis@bitbucket.org/Elsis/note_book_test.git
```


Navigate to the `dev-task-elsis` directory:

```
$ cd dev-task-elsis
```

Create a virtual environment and activate it using [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Install dependancies:

```
$ pip install -r requirements.txt
```

Change the postgres database credentials in the `database_operations.py` file to your local postgres database
credentials

Open the project using Jupyter notebooks

```
$ Jupyter notebook
```

Run the cells in the `etl.ipynb` notebook to perform the various transformations

### Testing

Run the cells in the `test.ipynb` notebook to see the records being stored in the data warehouse tables which are a result of the

transformations happening in the `etl.ipynb` notebook

### Task 2

Run the cells in the `business_questions.ipynb` in order to see the views created and sql queries which will enable us to 

answer business questions for task 2