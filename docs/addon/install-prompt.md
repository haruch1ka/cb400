# Blender アドオン環境再現プロンプト

新しいマシンで Blender アドオン環境を再現する際、以下のプロンプトを Claude（または他のAIアシスタント）にそのまま渡すこと。

---

```
Blender 5.x のアドオン環境を再現したい。以下の5つのアドオンをインストール・有効化する手順を案内してほしい。ダウンロードが必要なものは私が手動で行うので、URLと手順を順番に示して。自動化できる部分（ファイル配置など）はコマンドで実行して。

## 前提
- OS: Windows
- アドオン配置先: %APPDATA%\Blender Foundation\Blender\<バージョン>\scripts\addons\
- このプロンプトと同じフォルダ（docs/addon/）に自作アドオン flip_view_y.py が同梱されている

## インストール対象

1. **Flip View Y（自作・同梱）**
   - docs/addon/flip_view_y.py を scripts\addons\ にコピーするだけ
   - Preferences → Add-ons で「Flip View Y」を有効化
   - 動作確認: 3D View で Shift + Numpad 9 を押すと視点のYが反転する

2. **Classic Modifier Menu v1.3.0**
   - 入手元: https://quackers.gumroad.com/l/classic_modifier_menu （Gumroad、無料〜任意価格）
   - zip をダウンロード後、Preferences → Add-ons → Install from Disk で導入・有効化

3. **Modifier List v1.7.5**
   - 入手元: https://github.com/Symstract/modifier_list の Releases ページ
   - zip をダウンロード後、Preferences → Add-ons → Install from Disk で導入・有効化
   - 動作確認: 3D View で Alt + Space でポップアップが出る

4. **QuickSnap v1.4.9 以降**
   - 入手元: https://github.com/JulienHeijmans/quicksnap の Releases ページ
     （Blender 5 対応は v1.4.9 以降が必要）
   - zip をダウンロード後、Preferences → Add-ons → Install from Disk で導入・有効化
   - 動作確認: Ctrl + Shift + V でスナップモードが起動する

5. **LoopTools（拡張機能）**
   - Blender 内で Preferences → Get Extensions →「looptools」を検索 → Install
   - もしくは https://extensions.blender.org/add-ons/looptools/ から
   - 動作確認: 編集モードのサイドバー Edit タブに LoopTools パネルが出る

## 完了条件
- 5つすべてが Preferences → Add-ons で有効（チェック済み）になっている
- 各動作確認が通る
- 最後に Preferences の自動保存が有効か確認（無効なら Save Preferences を実行）
```
