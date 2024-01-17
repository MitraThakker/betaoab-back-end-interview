from flask import Flask, jsonify, request, Response

app = Flask('admin')


@app.route('/', methods=['GET'])
def index():
    return "Hello, world!"


@app.route('/api/links', methods=['GET'])
def list_all_links():
    try:
        return jsonify()
    except Exception:
        return Response("error", status=503)


@app.route('/api/links/<int:link_id>', methods=['GET'])
def link_details(link_id: int):
    try:
        return jsonify(), 200
    except Exception:
        return Response("error", status=500)


@app.route('/api/links', methods=['POST'])
def add_link():
    req = request.get_json()
    if req:
        return jsonify(req), 200
    return Response("error", status=400)


@app.route('/api/links/<int:link_id>/upvote', methods=['POST'])
def upvote_link(link_id: int):
    if link_id:
        return Response("success", status=200)
    else:
        return Response("error", status=400)


@app.route('/api/links/<int:link_id>/downvote', methods=['POST'])
def downvote_link(link_id: int):
    if link_id:
        return Response("success", status=200)
    else:
        return Response("error", status=400)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
