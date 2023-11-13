import pythoncom
import pyWinhook as pyHook
import hashlib

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

def OnKeyboardEvent(event):
    #ユーザーがエンターキーまたはタブキーを押したら入力が確定となる
    #それまでは入力された文字を表示しない
    #辞書を作り、キーを'Window'番号で管理し、キーを入力文字として管理しておく
    inputStrDict = {}
    #入力が確定したら、辞書からキーを削除する
    # ここにキーイベントを処理するコードを記述
    print('Key:', event.Key)
    print('WindowName:', event.WindowName)
    return True

if __name__ == '__main__':
    """メイン処理
    """
    # ログイン処理失敗したら終了
    if not Login():
        exit(-1)
    
    # フックマネージャーの作成
    hm = pyHook.HookManager()
    # キーボードイベントの設定
    hm.KeyDown = OnKeyboardEvent
    # フックの開始
    hm.HookKeyboard()

    # メッセージを処理する
    pythoncom.PumpMessages()
