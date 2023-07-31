import instaloader
import csv
import argparse
import getpass

def fetch_likes_to_csv(post_url, output_file, username, password):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Login
    L.login(username, password)

    # Load the post
    try:
        post = instaloader.Post.from_shortcode(L.context, post_url.split('/')[-2])
    except instaloader.exceptions.NotFoundException:
        print("Post not found. Make sure the URL is correct.")
        return
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print("This post belongs to a private account that you don't follow.")
        return

    # Fetch likes
    likes = [like.username for like in post.get_likes()]

    # Export to CSV
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Username'])
        for username in likes:
            writer.writerow([username])

    print(f"Likes fetched successfully and saved to '{output_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch likes from an Instagram post and export to CSV.")
    parser.add_argument("post_url", help="URL of the Instagram post")
    parser.add_argument("output_file", help="Output CSV file name")
    args = parser.parse_args()

    # Prompt the user for Instagram credentials
    username = "USERNAME"
    password = "PASSWORD"

    fetch_likes_to_csv(args.post_url, args.output_file, username, password)
