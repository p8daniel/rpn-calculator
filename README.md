
# API for calculator in Reverse Polish Notation (RPN)

The service implement an algorithm for calculator in Reverse Polish Notation (RPN)

The API allow sending operations to be performed and return the result.

Operations and Results are saved in a database.

The API include a route that allows retrieving the data in a CSV file.



## CALCULATION EXAMPLES


### Example 1:
**Infix Notation:** 3+4×2

**RPN Notation:** 3 4 2 × +

**Result:** 11

### Example 2:
**Infix Notation:** (5+3)×(12/4)

**RPN Notation:** 5 3 + 12 4 / ×

**Result:** 24

### Example 3:
**Infix Notation:** 8/(4−2)

**RPN Notation:** 8 4 2 − /

**Result:** 4


## How to use

To launch the infrastructure needed (database), use Docker and Docker-compose :

```
$ docker compose up -d
```

Run the firt alembic migration to create the tables in the database:

```
$ alembic upgrade head
```

Access the front interface at http://localhost:8000
