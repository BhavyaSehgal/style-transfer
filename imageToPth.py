from PIL import Image
import torch
from torchvision import transforms

img = Image.open("images/style-images/nature_style.jpg")
convert_tensor = transforms.ToTensor()

ti = convert_tensor(img)
print(ti)