import os
import requests

def download_file(url, outdir):
    outfile = url.split('/')[-1]
    outpath = os.path.join(outdir, outfile)
    with requests.get(url, stream=True) as r:
        with open(outpath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    return outpath
