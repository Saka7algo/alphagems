from pathlib import Path
from PIL import Image
import json
root=Path(__file__).parent
previous={x['name']:x for x in json.loads((root/'characters.json').read_text(encoding='utf-8-sig'))}
items=[]
for p in sorted((root.parent/'fullbody-chibi-white').glob('*.png'),key=lambda p:p.stem.lower()):
    for size,folder,quality in [(1000,'images',91),(360,'thumbs',83)]:
        dest=root/folder/(p.stem+'.webp')
        if not dest.exists():
            with Image.open(p) as im:
                im=im.convert('RGB'); im.thumbnail((size,size),Image.Resampling.LANCZOS)
                im.save(dest,'WEBP',quality=quality,method=6)
    items.append(previous.get(p.stem,{'name':p.stem,'image':'images/'+p.stem+'.webp','thumb':'thumbs/'+p.stem+'.webp'}))
assert len({i['name'].lower() for i in items})==len(items)
for i in items:
    for k in ['image','thumb']:assert (root/i[k].split('?')[0]).is_file()
(root/'characters.json').write_text(json.dumps(items,ensure_ascii=False),encoding='utf-8')
print(f'Validated {len(items)} characters and all image paths')
