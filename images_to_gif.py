import os
import imageio

# from progressbar import Bar, BouncingBar, Counter, ETA, \
    # AdaptiveETA, FileTransferSpeed, FormatLabel, Percentage, \
    # ProgressBar, ReverseBar, RotatingMarker, \
    # SimpleProgress, Timer, UnknownLength

from progressbar import Bar, Percentage, ProgressBar

duration = 0.1
paths = [r'A:\fotos\1',
         r'A:\fotos\2',
         r'A:\fotos\3',
]

output = 'movie.gif'

for path in paths:
    print(path)
    file_write = os.path.join(path, output)

    filenames = []
    images = []
    all_filenames = os.listdir(path)
    
    files_count = len(all_filenames)
    pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=files_count).start()

    for i, file in enumerate(all_filenames):
      if file.endswith('jpg'):
        file_read = os.path.join(path, file)
        pbar.update(i+1)
        images.append(imageio.imread(file_read))

    pbar.finish()

    print('writing gif...')
    imageio.mimsave(file_write, images, duration=duration)

print('DONE')