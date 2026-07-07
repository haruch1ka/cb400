# Blender アドオン構成

Blender 5.1 環境（`%APPDATA%\Blender Foundation\Blender\5.1\`）にインストール済みのアドオン一覧。
別マシンで環境を再現する場合は [`install-prompt.md`](install-prompt.md) を Claude に渡すこと。

## インストール済みアドオン

### 1. Flip View Y（自作）

| 項目 | 内容 |
|------|------|
| バージョン | 1.0 |
| 作者 | user（自作） |
| 入手元 | このフォルダの [`flip_view_y.py`](flip_view_y.py)（ソース同梱） |
| 場所 | 3D View |
| ショートカット | `Shift + Numpad 9` |

視点のY成分だけ反転する（X・Zは維持）。ブループリントを左右から見比べるモデリング作業用。

### 2. Classic Modifier Menu

| 項目 | 内容 |
|------|------|
| バージョン | 1.3.0 |
| 作者 | Quackers |
| 入手元 | [Gumroad](https://quackers.gumroad.com/l/classic_modifier_menu) |
| 対応 | Blender 4.0+ |
| 場所 | Properties エディタ |

Blender 4.0 で変更された「Add Modifier」メニューを、4.0 以前のクラシックなレイアウトに戻す。検索や `Shift + A` 呼び出しなど新機能は維持される。

### 3. Modifier List

| 項目 | 内容 |
|------|------|
| バージョン | 1.7.5 |
| 作者 | Antti Tikka |
| 入手元 | [GitHub (Symstract/modifier_list)](https://github.com/Symstract/modifier_list) |
| 場所 | Properties エディタ / 3D View サイドバー / `Alt + Space` ポップアップ |

モディファイアの代替UIレイアウト。リスト形式の表示・サイドバータブ・ポップアップなど操作性を強化する。

### 4. QuickSnap

| 項目 | 内容 |
|------|------|
| バージョン | 1.4.9 |
| 作者 | Julien Heijmans |
| 入手元 | [GitHub (JulienHeijmans/quicksnap)](https://github.com/JulienHeijmans/quicksnap) |
| ショートカット | `Ctrl + Shift + V` |

オブジェクト・頂点・カーブポイントを他のオブジェクト原点・頂点等へ素早くスナップする。Maya / 3ds Max の Vertex Snap 相当。

### 5. LoopTools（拡張機能）

| 項目 | 内容 |
|------|------|
| バージョン | 4.7.7 |
| 入手元 | [Blender Extensions](https://extensions.blender.org/add-ons/looptools/)（公式拡張プラットフォーム） |
| 場所 | 3D View → サイドバー → Edit タブ / 編集モードのコンテキストメニュー |

Circle・Bridge・Relax・Space などメッシュモデリング補助ツール群。旧同梱アドオンで、現在は拡張機能として配布。

## インストール形態の違い

- **1〜4** は従来型アドオン：`scripts\addons\` に配置（zip を Preferences → Add-ons → Install から導入）
- **5** は Extensions 形式：Blender 内の Get Extensions から直接インストール（`extensions\blender_org\` に配置される）
