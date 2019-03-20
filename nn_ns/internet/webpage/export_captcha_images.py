
import shelve
from pathlib import Path

this_folder = Path(__file__).parent
class Global:
    captcha_image_db_fname = "captcha_image_db_fname.dat"
    captcha_image_folder = this_folder / "captcha_images"

Global.captcha_image_folder.mkdir()
captcha_image_db = shelve.open(Global.captcha_image_db_fname, 'r')
for key, (correct, image_bytes) in captcha_image_db.items():
    if not correct: continue
    fname = Global.captcha_image_folder / f'{key}.jpg'
    if fname.exists(): continue
    with open(fname, 'xb') as fout:
        fout.write(image_bytes)



