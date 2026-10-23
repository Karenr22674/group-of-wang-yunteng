import urllib.request
import urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

names = ['Sijia Liu', 'Guanglei Zhou', 'Lingfeng Guo', 'Jiaxin Liu', 'Xinying Han', 'Xin Liu']

print("=== 严格核验课题组成员与王允腾老师的真实共同发表文献 ===")

for name in names:
    query = urllib.parse.quote(f"{name} Yunteng Wang")
    url = f"https://api.crossref.org/works?query.author={query}&rows=15"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as r:
            items = json.loads(r.read().decode('utf-8'))['message']['items']
            matched = []
            for it in items:
                authors = [a.get('family', '') + ' ' + a.get('given', '') for a in it.get('author', [])]
                # 必须双方都在作者中
                has_member = any(name.lower().split()[-1] in a.lower() for a in authors)
                has_wyt = any('wang' in a.lower() and ('yunteng' in a.lower() or 'y.' in a.lower()) for a in authors)
                if has_member and has_wyt:
                    matched.append({
                        'title': it.get('title', [''])[0],
                        'doi': it.get('DOI', ''),
                        'journal': it.get('container-title', [''])[0],
                        'year': it.get('issued', {}).get('date-parts', [[None]])[0][0],
                        'authors': authors
                    })
            print(f"\n>> {name}: 经 Crossref 检验的真实共同发表共 {len(matched)} 篇")
            for m in matched:
                print(f"   - [{m['year']}] {m['title']}")
                print(f"     期刊: {m['journal']} | DOI: https://doi.org/{m['doi']}")
                print(f"     真实作者: {', '.join(m['authors'])}")
    except Exception as e:
        print(f"Error for {name}: {e}")
