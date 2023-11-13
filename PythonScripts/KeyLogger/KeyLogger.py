import pythoncom
import pyWinhook as pyHook
import hashlib

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
    
    # フックマネージャーの作成
    hm = pyHook.HookManager()
    # キーボードイベントの設定
    hm.KeyDown = OnKeyboardEvent
    # フックの開始
    hm.HookKeyboard()

    # メッセージを処理する
    pythoncom.PumpMessages()
