from pathlib import Path
from PIL import Image
import json

root = Path(__file__).parent
source = root.parent / 'fullbody-chibi-white'
items = []
for path in sorted(source.glob('*.png'), key=lambda p:p.stem.lower()):
    for size, folder, quality in [(1000,'images',91),(360,'thumbs',83)]:
        dest = root / folder
        dest.mkdir(exist_ok=True)
        with Image.open(path) as im:
            im = im.convert('RGB')
            im.thumbnail((size,size),Image.Resampling.LANCZOS)
            im.save(dest / (path.stem+'.webp'),'WEBP',quality=quality,method=6)
    items.append({'name':path.stem,'image':'images/'+path.stem+'.webp','thumb':'thumbs/'+path.stem+'.webp'})
(root/'characters.json').write_text(json.dumps(items,ensure_ascii=False),encoding='utf-8')
print(f'Built {len(items)} characters')
