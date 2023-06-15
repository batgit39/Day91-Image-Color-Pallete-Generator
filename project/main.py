from flask import Flask, render_template, request
from extract_colors import extract_colors

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded file from the form
        file = request.files['image']

        # Save the uploaded file temporarily
        file_path = './temp.png'
        file.save(file_path)

        # Process the file and retrieve the top 10 most common colors
        colors = extract_colors(file_path)

        # Render the results template with the extracted colors
        return render_template('results.html', colors=colors)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

