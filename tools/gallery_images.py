# Gallery images for the grey-box project pages.
# The pages' galleries (PAGE[slug].gal in index.html) use images from juangarcia.mx, kept in assets/source/juangarcia-mx-framer,
# which is git-ignored (it holds NDA media), so the site can't load them from there online. This writes a web copy of each one:
# assets/data/gallery/<slug>/<same name>.jpg, at most 2000 px on the long edge, flattened on white.
# Keep GALLERY in step with the gal entries in index.html. Coltrane is left out: its page on juangarcia.mx is behind an NDA.
# usage: python3 tools/gallery_images.py
import os
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets/source/juangarcia-mx-framer')
OUT = os.path.join(ROOT, 'assets/data/gallery')
MAXE = 2000   # px, long edge
GALLERY = {
    'aido':            ['4dj4EfZzTxnDeZG7XxE5iwCm64', 'Fr69H4xHQibJKHpeqCDAmmdNs', 'fn1yhOxuLAkH9PY8uhtvYHnXo', 'xC15zmxP3ZiXeq89w57DOfoAIo'],
    'jiviniti':        ['KBbAoVYRrb4arcJXpbaFaDXoY', '2SdUihpGPCI5XExYTfIKuauzY', 'mrvMPyaWg35xEfy3YCKxfl6bHE'],
    'around':          ['faH2cajHbJyh6w72m55ML3hUo', '0v81dGEocNOj8jhSeNKQzn8XPc', 'X4PI1XXIjznWX9yWMHFVJea53i8', 'GRQ3Jsiwa1pXyWkO5kXON7rFYx8',
                        'BUcNO5Ek5rR35PdmdkG2rcVezIM', 'aRAJeXnUB84mG9IQCYI6d9gi1F0', 'VDoryMPJYHtgw9XdL6gGZgRmc0', 'dToVcCBwQOt5W4GkONxuEbmkWJg',
                        'RBx50eSy8Nhkjs8FheD5bMc03o', 'mp1xgkWRRxLGAgm8ouRfwC4Dlw', 'red3buiCNiT0cnhhHoU6UP7nJg0', 'z0XmwYl7d80Ii6W4UER9uNUZ3M'],
    'chiefchallenges': ['W2p3OtPCtZir49JEneaCNIt5H44', 'Ogx0C5ufvhUS5dpapZLlPXLrc', 'oLbZEzAYZ1fDl8sJyXJVKcgURbc', 'dJFrCFjRd4FfmXCie2dVVdEXoCY',
                        'IWSJSvabtSqAtoZOIeCUo16FPEw', 'jkT1rpJSLAfH6yBLHcCMl6MrGw'],
    'hule':            ['gpyIuovAyqj1WhMemSUhGGMY5S4', 'wmfFUI4TuUY4bxV6W5BAbg8U', 'XWRlbHbJH8vA604MtCjRnLcbJs', 'mCuu4jX4TY3EvgnUHxdW9M7Akw',
                        'myirq2AlGlRJeD4wkLFqDHSu8', 'kPbErLuZPSM7egXhQ4Ct8z42wBw'],
    'luum':            ['KENgZqF7DAIygHWG95F0pXtlYw', '8N9xPa7Keq7j6QZqkpZid3LCnNs', 'VafjmCf8qtENL8Qx5mCYev511g', 'gnVu6qkYY0ujrdajmFfjHbRRZ38'],
    'nocturna':        ['NVzEnwngZ9Q1O4tTv3JBTdzU24', 'OyYcVa1cOhAd6QjzeaQyK1maZc', 'Q89pv1sBlG3TrXh9Pz93IeOn4zM'],
    'suraja':          ['p0dEAYKK3h6XUistEUOzcM42CsU', 'aSTxMkhr3E5ci3U3uMycznQozr4', 'bcTBNmAEbwfNxy4xQl46plNiifE', 'cjEXv9fDllha03TvO8PhmIFX6vg'],
    'surrealelfs':     ['AIPIpusja0IJPYytZtbKOfPqY', 'LTaWnGWcqTUw43WmiDcUre1iQ', 'aQtaYlf5m4vPwZvSboLn0PM1Qs', 'YMbS5FDeLHy2ljpioRiqWmpbn7k',
                        'IvQSrtgz2nRFIO6XiOxU41QS5ns', 'vfZH27nLOViwqGFu9rekXhXmww', 'jLAR4aRoHR07eqiFs5DDUeU0i44', 'mEvTuYGxxAwendvLsEZlshvsBSI'],
    'rmc':             ['XFA9Ng18HCQzwugu8GvVXWIMMs', 'Q3eQ855Ov2jXXtILfFdtfoq2U', 'jtfxoFylXqHVrGOIp3DdhV47Y'],
    'genesis':         ['zh2iOPNAlckYQ59vrpUB5bt9yA', 'Geh1MY62D8oqbahELqhrnE9TLDw', 'vh7YQsuL8iKINmNk2ABxETiUniE'],
    'trascender':      ['F8wrDvW11MsMljyiNikXFik', 'QVBJKNcb64TeE1ZuBcUWdeHcdhc', 'iJiQcsyvC9T0jrQVCqwGfjyIk'],
}
for slug, names in GALLERY.items():
    os.makedirs(os.path.join(OUT, slug), exist_ok=True)
    media = os.path.join(SRC, slug, 'media')
    for n in names:
        f = next(x for x in os.listdir(media) if os.path.splitext(x)[0] == n)
        im = Image.open(os.path.join(media, f)).convert('RGBA')
        bg = Image.new('RGB', im.size, 'white'); bg.paste(im, mask=im.getchannel('A')); im = bg
        k = MAXE / max(im.size)
        if k < 1: im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        p = os.path.join(OUT, slug, n + '.jpg')
        im.save(p, quality=82, optimize=True, progressive=True)
        print(f'{slug}/{n}.jpg  {im.width}x{im.height}  {os.path.getsize(p) // 1024} KB')
