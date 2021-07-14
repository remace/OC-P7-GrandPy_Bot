from flask import Flask, render_template
import config
app = Flask(__name__)

@app.route('/')
def index():
    page_static_data = {}
    page_static_data["tab_title"] = config.PAGE_TITLE
    page_static_data["header_title"] = config.HEADER_TITLE
    page_static_data["header_subtitle"] = config.HEADER_SUBTITLE
    return render_template('index.html', static= page_static_data)

if __name__ == "__main__":
    app.run(debug=True)