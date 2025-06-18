import csv
import praw

#autenthication
#Provide your Reddit API credentials, follow some internet instructions to get them (easy to find)
# Make sure to replace 'INSERT_CLIENT_ID_HERE' and 'INSERT_CLIENT' with your actual credentials.

reddit = praw.Reddit(
    client_id='INSERT_CLIENT_ID_HERE',
    client_secret='INSERT_CLIENT',
    user_agent='script by u/TuoUsername'
)

# for example, let's fetch the top 10 posts from the 'python' subreddit
for post in reddit.subreddit('python').top(limit=10):
    print(f"TITOLO: {post.title}")
    print(f"AUTORE: {post.author}")
    print(f"PUNTEGGIO: {post.score}")
    print(f"URL: {post.url}")
    print('-' * 40)

# Note: Make sure to handle exceptions and errors in a real-world application.
# This is a basic example to get you started with the Reddit API using PRAW.

# You can also explore other functionalities like commenting, submitting posts, etc.
subreddit_nome = 'artificial'  # ex: 'technology', 'ai', 'machinelearning'

# you can change the subreddit name to any subreddit you want to scrape and creating a CSV file
output_file = f'{subreddit_nome}_post_commenti.csv'

# Preparazione del file CSV
with open(output_file, mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([
        'post_id', 'post_title', 'post_author', 'post_score', 'post_url',
        'comment_id', 'comment_author', 'comment_score', 'comment_body'
    ])
 # Estrai i 5 post principali
    for post in reddit.subreddit(subreddit_nome).top(limit=5):
        print(f"Post: {post.title}")
        post.comments.replace_more(limit=0)  # evita "[MoreComments]"

        # Scrive nel CSV ogni commento associato al post
        for comment in post.comments[:5]:  # solo i primi 5 commenti principali
            writer.writerow([
                post.id,
                post.title,
                str(post.author),
                post.score,
                post.url,
                comment.id,
                str(comment.author),
                comment.score,
                comment.body.replace('\n', ' ').strip()
            ])