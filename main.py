from flask import Flask, request
# import request.
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/get_tree', methods=['POST'])
def get_nodes():
    user = request.form['node1']
    return redirect(url_for('success',name = user))
    # return "fetched tress"


if __name__ == '__main__':
    app.run()