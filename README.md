# -Netflix-Style-Movie-Recommendation-System
README.md
markdown
Copy
Edit
# 🎬 Netflix-Style Movie Recommendation System

A simple Netflix-style movie recommendation system using **content-based filtering**. Built with **Python** and **Streamlit**, it recommends movies based on plot similarity using TF-IDF and cosine similarity. It also shows posters of recommended movies using the **TMDB API**.

---

## 🔧 Features

- 🎥 Recommend movies based on content similarity (movie overview)
- 🖼️ Fetch movie posters using TMDB API
- 🧠 Use of TF-IDF vectorizer for NLP
- 🌐 Interactive UI with Streamlit

---

## 🗂️ Project Structure

Netflix-Recommendation-System/
│
├── app.py # Main Streamlit app
├── recommender.py # Recommendation logic
├── fetch_poster.py # Poster retrieval via TMDB API
├── movies.csv # Movie metadata
├── similarity.pkl # Precomputed similarity matrix
├── requirements.txt # Python dependencies
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🧪 Demo

When you run the app, it will look like this:

🎬 Netflix-style Movie Recommender
[ Select a movie from dropdown ]
[ Show Recommendations ]
=> Shows 5 recommended movie names with their posters.

yaml
Copy
Edit

---

## 🧰 Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- TMDB API
- TF-IDF Vectorization
- Cosine Similarity

---

## 📝 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Netflix-Recommendation-System.git
cd Netflix-Recommendation-System
2. Install Dependencies
Make sure you have Python 3.7+ installed.

bash
Copy
Edit
pip install -r requirements.txt
3. Get TMDB API Key
Visit https://www.themoviedb.org/settings/api and create an account.

Generate an API key.

Replace "YOUR_API_KEY" in fetch_poster.py with your actual API key.

python
Copy
Edit
url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY&language=en-US"
4. Prepare Dataset
Download TMDB 5000 Movie Dataset from Kaggle:
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Keep the important columns: id, title, overview.

Save it as movies.csv.

5. Generate Similarity Matrix
Run the following code once to create similarity.pkl:

python
Copy
Edit
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df = pd.read_csv('movies.csv')
df['overview'] = df['overview'].fillna('')
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['overview'])
similarity = cosine_similarity(tfidf_matrix)

pickle.dump(similarity, open('similarity.pkl', 'wb'))
6. Run the App
bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

📷 Example Output

📜 License
This project is open-source and free to use.

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.









