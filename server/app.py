from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': "Harry Potter and the Philosopher's Stone",
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'wings of fire',
        'author': 'raji',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Rabindra Nath Tagore',
        'author': 'Geetanjali',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Sir Thomas Moor',
        'author': 'Utopia',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Crime and Punishment',
        'author': 'decapiyoo',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Adventures of Tom Sawyer',
        'author': 'Mark Twain	',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Agni Veena',
        'author': 'Kazi Nasrul Islam',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Animal Farm ',
        'author': ' George Orwell',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Ben Hur',
        'author': 'Lewis Wallace',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Baburnama',
        'author': 'Babur',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Arthashastra',
        'author': 'Kautilya',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Anand Math',
        'author': 'Bankimchandra Chattopadhyay',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Mein Kampf',
        'author': 'Adolf Hitler',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Vicar of Wakefield',
        'author': 'Oliver Goldsmith',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Decline and Fall of the Roman Empire',
        'author': 'Edward Gibbon',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Time Machine',
        'author': 'H.G. Wells',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'A passage to India',
        'author': 'E.M.Forster',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Moon and Sixpence',
        'author': ' Somerset Maughan',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Far from the Madding Crowd',
        'author': 'Thomas Hardy',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Pilgrim’s Progress',
        'author': 'John Bunyan',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Merchant of Venice',
        'author': 'Shakespeare',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Antony and Cleopatra',
        'author': 'Shakespeare',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Geetanjali',
        'author': 'Ramya',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Utopia',
        'author': 'Sir Thomas Moor',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Chitra',
        'author': 'Seuss',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Divine Comedy',
        'author': 'Dante',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Wild Iris',
        'author': 'Louis Gluck',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Canterbury Tales',
        'author': 'Chaucer',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Count of Monte Cristo',
        'author': 'Alexander Dumas',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Das Kapital',
        'author': 'Karl Marx',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Origin of Species',
        'author': 'Charles Darwin',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'A Tale of Two Cities',
        'author': 'Charles Dickens',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'David Copperfield',
        'author': 'Charles Dickens',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Discovery of India',
        'author': 'Pandit Jawaharlal Nehru',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Avigyan Sakuntalam',
        'author': 'Kalidas',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Adventures of Sherlock Holmes',
        'author': 'Arthur Conan Doyle',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'The Lady of the Last Minstrel',
        'author': 'Sir Walter Scott',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Akbar-Nama',
        'author': 'Abul Fazal',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'A Dangerous place',
        'author': 'D.P. Moynihan',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Gulliver’s Travels',
        'author': 'Jonathan Swift',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Le Contract Social',
        'author': 'Jean Jacques Rousseau',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Anna Karenina',
        'author': 'Leo Tolstoy',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Around the World in eighty days',
        'author': 'Jules Verne',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Arms and the Man',
        'author': ' G.B.Shaw',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Ancient Mariner',
        'author': 'Coleridge',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'romromio sulite',
        'author': 'RR',
        'read': True
    },


]


bookcount = len(BOOKS)

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        global bookcount
        bookcount += 1
        response_object['message'] = 'Book added!'
    else:
        start = int(request.args.get('start', 0))
        end = int(request.args.get('end', len(BOOKS)))

        books_slice = BOOKS[start:end]

        response_object['books'] = books_slice
        response_object['bookcount'] = bookcount

    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': book_id,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    elif request.method == 'DELETE':
        if remove_book(book_id):
            global bookcount
            bookcount -= 1
            response_object['message'] = 'Book removed!'
        else:
            response_object['status'] = 'error'
            response_object['message'] = 'Book not found!'
    
    response_object['bookcount'] = bookcount
    return jsonify(response_object)

def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False

if __name__ == '__main__':
    app.run()
