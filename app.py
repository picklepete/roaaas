import json
from pathlib import Path
from flask import Flask, render_template, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rules/<rule_id>/')
@app.route('/rules/', defaults={'rule_id': None})
def get_rule(rule_id):
    with open('%s/roaaas/rules.json' % Path().absolute()) as fs:
        db = json.loads(fs.read())
    if rule_id is None:
        return db
    if rule_id in db:
        return db[rule_id]
    abort(404)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0')
