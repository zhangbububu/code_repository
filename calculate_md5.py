import hashlib
def calculate_md5(fpath: str, chunk_size: int = 1024 * 1024) -> str:
    md5 = hashlib.md5()
    with open(fpath, "rb") as f:
        cnt = 0
        for chunk in iter(lambda: f.read(2), b""):
            print(chunk)
            md5.update(chunk)
    return md5.hexdigest()

calculate_md5('untitled1.txt')