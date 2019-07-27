import os
import imageio

duration = 0.25
path_images = input('pfad?: ') #r'C:\Users\x123069\Desktop\D\pys\images_to_gif\images'
path_result = r'C:\Users\x123069\Desktop\D\pys\images_to_gif'
all_filenames = os.listdir(path_images)

filenames = []
images = []

for file in all_filenames:
  if file.endswith('jpg'):
    images.append(imageio.imread(os.path.join(path_images, file)))

imageio.mimsave(os.path.join(path_result, 'result.gif'), images, duration=duration)
