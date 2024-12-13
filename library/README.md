
# library_manager

`library_manager` est un package Python simple pour gérer un système de bibliothèque.

## Installation

Pour installer le package localement, utilisez la commande suivante :

bash
pip install .

## Utilisation_example

python
from library import Library, Book

library = Library("City Library")
book = Book("1984", "George Orwell", "1234567890")
library.add_book(book)

print(library.list_books())