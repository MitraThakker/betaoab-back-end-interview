import logging

from flask import Flask, jsonify, request, Response

import svc
from common.errors import InvalidUrlError

app = Flask('admin')


@app.route('/', methods=['GET'])
def index():
    return 'Hello, world!'


@app.route('/api/links', methods=['GET'])
def list_all_links():
    try:
        return jsonify(svc.list_all_links()), 200
    except Exception as e:
        logging.error(f'Error listing all links: {e}')
        return Response(f'Error: {e}', status=500)


@app.route('/api/links/<int:link_id>', methods=['GET'])
def link_details(link_id: int):
    try:
        link = svc.link_details(link_id)
        if not link:
            return jsonify({'error': f'link with id {link_id} not found'}), 404
        return jsonify(link), 200
    except Exception as e:
        logging.error(f'Error fetching link details: {e}')
        return Response(f'Error: {e}', status=500)


@app.route('/api/links', methods=['POST'])
def add_link():
    req = request.get_json()
    if not req:
        return Response("error", status=400)
    try:
        return jsonify({'link_id': svc.add_link(req)}), 200
    except InvalidUrlError:
        return jsonify({'error': f'invalid URL'}), 400
    except Exception as e:
        logging.error(f'Error when adding link: {e}')
        return Response(f'Error: {e}', status=500)


@app.route('/api/links/<int:link_id>/upvote', methods=['POST'])
def upvote_link(link_id: int):
    try:
        link = svc.upvote_link(link_id)
        if not link:
            return jsonify({'error': f'link with id {link_id} not found'}), 404
        return jsonify(link), 200
    except Exception as e:
        logging.error(f'Error fetching link details: {e}')
        return Response(f'Error: {e}', status=500)


@app.route('/api/links/<int:link_id>/downvote', methods=['POST'])
def downvote_link(link_id: int):
    try:
        link = svc.downvote_link(link_id)
        if not link:
            return jsonify({'error': f'link with id {link_id} not found'}), 404
        return jsonify(link), 200
    except Exception as e:
        logging.error(f'Error fetching link details: {e}')
        return Response(f'Error: {e}', status=500)


@app.route('/api/links/truncate', methods=['POST'])
def truncate():
    try:
        svc.truncate()
        return jsonify({}), 200
    except Exception as e:
        return Response(f'Error: {e}', status=500)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5005)
