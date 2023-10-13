import random
import os

votes = {}

def handle_response(user_message, author):
    if user_message == "vote_start":
        votes.clear()
        return choose_random_dress()
    if "vote " in user_message:
        score = float(user_message.split(" ")[-1])
        if score < 0:
            score = 0
        if score > 10:
            score = 10
        votes[author] = score
        print(votes)
    if user_message == "vote_end":
        return f"*With {len(votes)} vote(s), Lomo gets a score of **{sum(value for _, value in votes.items()) / len(votes):.2f} out of 10***"

def choose_random_dress():
    dresses = []
    folder_dir = "./dresses"
    for images in os.listdir(folder_dir):
        if (images.endswith(".png") or images.endswith("jpg")):
            dresses.append(images)
    return dresses[random.randint(0, len(dresses))]

