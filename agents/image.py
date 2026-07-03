from PIL import Image
from transformers import pipeline

classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

def image_recognition(image_path):

    image = Image.open(image_path)

    result = classifier(image)

    return result