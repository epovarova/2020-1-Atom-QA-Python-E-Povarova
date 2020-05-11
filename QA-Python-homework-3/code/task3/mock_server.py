import threading

from flask import Flask, abort, request, jsonify

app = Flask(__name__)
books = {}


def run_mock(host, port):
    server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/books/<book_id>')
def get_book_by_id(book_id: int):
    book = books.get(int(book_id))
    if book:
        return jsonify(book)
    else:
        abort(404)


@app.route('/books')
def get_books():
    return jsonify(books)


@app.route('/new_book', methods=['POST'])
def post_book():
    author = request.form['author']
    name = request.form['name']
    data = {'author': author, 'name': name}
    books.update({len(books): data})
    return data, 200


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return 'Server shutting down...'


if __name__ == '__main__':
    run_mock('127.0.0.1', 5000)
