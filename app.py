from flask import Flask, render_template, jsonify, request, flash
from utils.blockchain import Blockchain
from utils.document import Document
import hashlib

blockchain = Blockchain()

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def index():
    return render_template('explore.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')

        file = request.files['file']
        sideA = request.form.get('sideA')
        sideB = request.form.get('sideB')
        description = request.form.get('description')
        checksum = hashlib.sha256(file.read()).hexdigest()

        doc = Document(sideA, sideB, checksum, description)
        blockchain.append_document(doc)

        flash('Document with checksum ' + checksum + ' uploaded and enqueued in blockchain');

    return render_template('upload.html')

@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file selected')

        file = request.files['file']
        checksum = hashlib.sha256(file.read()).hexdigest()
        result = blockchain.look_for_document_by_checksum(checksum)
        return render_template('verify_result.html', result=result)

    return render_template('verify.html')

@app.route('/api/dumpChain')
def dump_chain():
    return jsonify(blockchain.dump_chain())