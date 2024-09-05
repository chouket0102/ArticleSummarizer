
from textblob import TextBlob  # Corrected import
from newspaper import Article
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')


url = "https://www.sciencenews.org/article/ai-snake-oil-how-to-spot-hype"
article = Article(url)

# Download and parse the article
article.download()
article.parse()
article.nlp()

# Print article details
print(f"Title: {article.title}")
print(f"Authors: {article.authors}")
print(f"Publication Date: {article.publish_date}")
print(f"Summary: {article.summary}")
