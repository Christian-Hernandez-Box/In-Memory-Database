# InMemoryDatabase

`InMemoryDatabase` is a simple in-memory key-value store with basic transaction support. It provides methods to set, get, and delete key-value pairs and allows for transactional operations with the ability to begin, rollback, and commit transactions.

## Features

- **Set**: Add a new key-value pair to the database.
- **Get**: Retrieve the value associated with a key.
- **Delete**: Remove a key-value pair from the database.
- **Transactions**: Begin, rollback, and commit transactions.

## Installation

No installation is required as this is a pure Python implementation. Just copy the `InMemoryDatabase` class into your project.

## Usage

Here's how to use the `InMemoryDatabase`:

```python
from in_memory_database import InMemoryDatabase

# Initialize the database
db = InMemoryDatabase()

# Set Method
db.set('test1', 'value1')  # Output: Value has been set successfully.
db.set('test2', 'value2')  # Output: Value has been set successfully.
db.set('test1', 'value1')  # Output: Provided name already in database.

# Get Method
db.get('test1')  # Output: value1
db.get('test2')  # Output: value2
db.get('test3')  # Output: Null

# Delete Method
db.delete('test1')  # Output: Value successfully deleted.
db.get('test1')     # Output: Null
db.delete('test3')  # Output: Provided name not in database.

# Transaction Methods
db.begin()          # Start a new transaction
db.set('test3', 'value3')
db.get('test3')     # Output: value3
db.rollback()       # Rollback the transaction
db.get('test3')     # Output: Null
db.begin()          # Start another transaction
db.set('test4', 'value4')
db.commit()         # Commit the transaction
db.get('test4')     # Output: value4
