from flask import Flask, request, render_template
from textblob import TextBlob  # Corrected import
from newspaper import Article
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    title = ''
    publish_date = ''
    authors = []
    summary = ''

    if request.method == 'POST':
        url = request.form['url']
        if url:
            try:
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()
                # Extract the desired information
                title = article.title
                summary = article.summary
                authors = article.authors
                publish_date = article.publish_date.strftime('%B %d, %Y') if article.publish_date else 'N/A'
            except Exception as e:
                summary = f"Error processing the article: {str(e)}"

    return render_template('index.html', title=title, summary=summary, authors=authors, publish_date=publish_date)



if __name__ == "__main__":
    app.run(debug=True)
