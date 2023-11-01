import argparse
from pathlib import Path

import cv2
from tqdm import tqdm


def image2video(image_dir: Path, video_path: Path, fps):
    image_paths = image_dir.glob('*')
    image_paths = sorted(image_paths)

    writer = None

    pbar = tqdm(image_paths)
    for im_path in pbar:
        frame = cv2.imread(str(im_path))

        if writer is None:
            writer = cv2.VideoWriter(video_path,
                                     cv2.VideoWriter_fourcc(*'MP4V'),
                                     fps,
                                     frame.shape[0:2][::-1],  # convert (H, W, C) -> (W, H)
                                     isColor=True)
        writer.write(frame)

    writer.release()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('image_dir')
    parser.add_argument('video_path')
    parser.add_argument('fps', type=int)
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    image2video(Path(args.image_dir), args.video_path, args.fps)
