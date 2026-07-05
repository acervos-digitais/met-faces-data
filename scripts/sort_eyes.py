from shutil import copy2
from os import listdir, makedirs
from PIL import Image as PImage

DATA_DIR = "."
IMG_DIR = f"{DATA_DIR}/image"
IMG_COLOR_DIR = f"{IMG_DIR}/eyes-color"
IMG_ALIGNED_DIR_prefix = f"{IMG_DIR}/eyes-color-aligned"

eye_files = sorted(f for f in listdir(f"{IMG_COLOR_DIR}") if f.endswith("avif"))

eye_areas = []
for f in eye_files:
  img = PImage.open(f"{IMG_COLOR_DIR}/{f}")
  eye_areas.append({
    "fname": f,
    "area": img.width * img.height
  })
  img.close()

eyes_by_area = sorted(eye_areas, key=lambda x: x["area"], reverse=True)
fname_by_area = [e["fname"] for e in eyes_by_area]

for angle in ["01", "10", "15"]:
  img_in_dir = f"{IMG_ALIGNED_DIR_prefix}-{angle}"
  img_out_dir = f"{img_in_dir}-sorted"
  makedirs(img_out_dir, exist_ok=True)

  for cnt,fname in enumerate(fname_by_area):
    fpath_in = f"{img_in_dir}/{fname}"
    cnt_str = f"0000{cnt}"[-4:]
    fpath_out = f"{img_out_dir}/{cnt_str}_{fname}"
    copy2(fpath_in, fpath_out)
