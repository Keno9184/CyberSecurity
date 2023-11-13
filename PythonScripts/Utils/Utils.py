def Login() -> bool:
    """ログイン処理

    Returns:
        bool: ログイン成功したかどうか
    """
    #TODO correctHashはサーバーなどから取得する
    correctHash = '9168832d9baa72d5220bc5368b84b9da17930d617765fd8abd3c808f07533f5b'
    userId = input('Enter the id →')
    userPassword = input('Enter the password →')
    calcedHash = CalcHash(userId + userPassword)
    
    if calcedHash != correctHash:
        return False
    return True

def CalcHash(src:str) -> str:
    """ハッシュ値の計算

    Args:
        src (str): ハッシュ計算元の文字列

    Returns:
        str: ハッシュ値
    """
    sha256Obj = hashlib.sha256()
    sha256Obj.update(src.encode('utf-8'))
    return sha256Obj.hexdigest()