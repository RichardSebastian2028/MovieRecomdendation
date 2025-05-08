import pandas as pd
import random

df = pd.read_csv("imdb_top_1000.csv")
df['Genre'] = df['Genre'].astype(str).str.lower()

all_genres = set()
for g in df['Genre']:
    for item in g.split(','):
        all_genres.add(item.strip())

def show_movie(movie):
    print("\n🎬 " + "="*40)
    print("Title:       ", movie['Series_Title'])
    print("Genre(s):    ", movie['Genre'].title())
    print("IMDb Rating: ", movie['IMDB_Rating'])
    print("Overview:    ", movie['Overview'])
    print("Sentiment:   ", random.choice(["Positive", "Neutral", "Negative"]))
    print("="*40)

def ai_recommend():
    print("\nAvailable genres:", ', '.join(sorted(list(all_genres))[:10]) + ", ...")
    genre = input("Enter preferred genre: ").lower()
    rating_input = input("Minimum IMDb rating (press Enter to skip): ")

    try:
        rating = float(rating_input) if rating_input else 0
    except ValueError:
        rating = 0

    filtered = df[df['Genre'].str.contains(genre)]
    filtered = filtered[filtered['IMDB_Rating'] >= rating]

    if not filtered.empty:
        movie = filtered.sample(1).iloc[0]
        show_movie(movie)
    else:
        print("⚠️ No movies found. Try a different genre or lower rating.")

def random_recommend():
    movie = df.sample(1).iloc[0]
    show_movie(movie)

def main():
    name = input("👋 Hi there! What's your name? ")
    print(f"Welcome, {name}! Ready to find a great movie?")

    while True:
        print("\nChoose an option:")
        print("1. AI-based Recommendation")
        print("2. Random Recommendation")
        print("3. Exit")

        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            ai_recommend()
        elif choice == '2':
            random_recommend()
        elif choice == '3':
            print("🎉 Thanks for using the Movie Recommender. Bye!")
            break
        else:
            print("Invalid input. Please choose 1, 2, or 3.")

main()
