import os

def choose_random_dress():
    dresses = []
    folder_dir = "./dresses"
    for images in os.listdir(folder_dir):
        if (images.endswith(".png") or images.endswith("jpg")):
            dresses.append(images)
    return dresses
    
choose_random_dress()