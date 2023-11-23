# api-py
Minimal microservice for single module with basic CRUD operations using flask


## How to Setup

### Pre-requisites
- Install Python
- Setup virtual environment
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use "venv\Scripts\activate"
    ```
- Install dependencies
    ```bash
    pip install -r requirements.txt
    ```

### Start in Dev Mode
Run following commands

```bash
python app.py
```

## To Test
To test run the following commands

```bash
# To get all data
curl localhost:5000/books

# To create new data
curl -X POST -H 'content-type:application/json' -d '{"title":"title", "author":"author"}' localhost:5000/books 

# To get specific Data based on id
# Replace :id with the value of id returned in above command
curl -X GET localhost:5000/books/:id

# To update specific Data based on id
# Replace :id with the value of id returned in above command

curl -X PUT -H 'content-type:application/json' -d '{"title":"title1", "author":"author1"}' localhost:5000/books/:id  

# To delete specific Data based on id
# Replace :id with the value of id returned in above command
curl -X DELETE localhost:5000/books/:id  #replace id with the value of id returned in above command
```

You can test the same using postman