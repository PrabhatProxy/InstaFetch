import instaloader
import csv
import pandas as pd

def fetch_likes(post_url):
    # Load the post
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split('/')[-2])
    except instaloader.exceptions.NotFoundException:
        print(f"Post not found for URL: {post_url}. Make sure the URL is correct.")
        return []
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(f"This post belongs to a private account that you don't follow for URL: {post_url}.")
        return []

    # Fetch likes
    likes = [like.username for like in post.get_likes()]

    return likes

def fetch_likes_for_links(input_file, output_dir):
    # Read input CSV
    data = pd.read_csv(input_file)

    # Fetch likes for each link and save to separate CSV files
    for index, row in data.iterrows():
        entry_number = row['EntryNumber']
        post_url = row['Link']
        likes = fetch_likes(post_url)

        # Save likes to CSV
        output_file = f"{output_dir}/{entry_number}.csv"
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Username'])
            for username in likes:
                writer.writerow([username])

        print(f"Likes fetched successfully for Entry Number {entry_number} and saved to '{output_file}'.")

if __name__ == "__main__":
    input_file = "compare_bulk.csv"  # Replace with the CSV file containing 'Entry Number' and 'Link' columns
    output_dir = "out"  # Replace with the directory where you want to save the output CSV files

    # Create an instance of Instaloader and login
    L = instaloader.Instaloader()
    L.login("USERNAME", "PASSWORD")  # Replace with your Instagram username and password

    fetch_likes_for_links(input_file, output_dir)
