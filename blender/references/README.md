# blender/references/ — リファレンス画像

---

## blueprint/

| ファイル | 内容 | 出典 |
|----------|------|------|
| `cb400sf_2018_blueprint.jpg` | 三面図（上面・側面・正面・背面）、寸法入り | the-blueprints.com |

> ⚠️ 500px制限版。フル解像度（1146×524）はthe-blueprints.comのアカウント登録が必要。

---

## photos/detail/

NC42型の詳細写真（黒カラー）。色に関係なく形状・パネルライン確認に使う。

| ファイル | アングル |
|----------|----------|
| `cb400sf-191.jpg` | 前斜め右（フロント〜エンジン） |
| `cb400sf-192.jpg` | 右側面（エンジン近接） |
| `cb400sf-193.jpg` | 右前斜め |
| `cb400sf-194.jpg` | 前斜め右（全体） |
| `cb400sf-195.jpg` | 右側面（全体） |
| `cb400sf-196.jpg` | 後ろ斜め右 |
| `cb400sf-197.jpg` | 後ろ斜め左 |
| `cb400sf-198.jpg` | 左側面 |
| `cb400sf-199.jpg` | 純粋な右側面（★Blenderリファレンスに最適） |
| `cb400sf-055.jpg` | エンジン近接 |
| `cb400sf-057.jpg` | フロント近接 |

出典: web-motocar.com（非公式写真集）

---

## photos/red/

キャンディークロモスフィアレッドの実車写真 → **手動保存が必要**

Honda公式サイトはリファラーチェックでダイレクトDLをブロックしているため、
ブラウザで以下のページを開いて手動保存すること：

- [Honda公式 デザインページ（赤のカラーを選択）](https://www.honda.co.jp/CB400SF/design/)
  - カラーセレクターで「キャンディークロモスフィアレッド」を選択
  - 各アングルの画像を右クリック保存 → このフォルダへ

保存時の推奨ファイル名:
```
honda_official_red_side.png
honda_official_red_front.png
honda_official_red_rear.png
honda_official_red_3quarter.png
```

---

## Blenderでの使い方（優先順位）

1. `cb400sf-199.jpg` — 右側面　→ Right View（NumPad 3）のリファレンスに
2. `blueprint/cb400sf_2018_blueprint.jpg` — 三面図　→ 正面・側面両方に活用
3. `cb400sf-055.jpg` — エンジン近接　→ エンジンモデリング時に参照
4. `photos/red/`の画像 → マテリアル・カラーリングの参考
