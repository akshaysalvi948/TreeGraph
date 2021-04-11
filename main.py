from flask import Flask, request, make_response
from tree_logic import ParentChildNode
import json
# import request.
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/get_tree/<user_node>', methods=['POST'])
def get_nodes(user_node):
    output_dict = ParentChildNode().get_nodes(user_node)
    msg = f'outputnodes {output_dict} created'
    return make_response(msg, 201)
    # else:
    #     return "check the method"
    # return "fetched tress"


if __name__ == '__main__':
    app.run()