# CB400SF 参考資料リンク集

対象: NC42型、キャンディークロモスフィアレッド（2018年追加色）
収集日: 2026-06-18

---

## ブループリント（三面図）

モデリングの最重要資料。側面図・正面図・上面図が揃っている。

| リンク | 内容 |
|--------|------|
| [CB400 Super Four (2018) Blueprint](https://www.the-blueprints.com/blueprints/motorcycles/honda-motor/84265/view/honda_cb400_super_four_2018/) | **最優先** NC42後期に最も近い年式 |
| [CB400 Super Four (2006) Blueprint](https://www.the-blueprints.com/blueprints/motorcycles/honda-motor/8682/view/honda_cb400_super_four_2006/) | NC39型、エンジン形状の参考に |
| [CB400 Super Four (一般) Blueprint](https://www.the-blueprints.com/blueprints/motorcycles/honda-motor/9254/view/honda_cb400_super_four/) | 汎用版 |

> **使い方**: the-blueprints.com の画像を右クリックで保存し、`docs/references/images/` に配置してBlenderのリファレンス画像として使用する。

---

## 実車写真

### Honda公式
| リンク | 内容 |
|--------|------|
| [Honda公式 CB400SF デザインページ](https://www.honda.co.jp/CB400SF/design/) | カラーリング公式写真（キャンディーレッドあり） |
| [Honda公式 スペック・サイズ](https://www.honda.co.jp/CB400SF/spec/) | 寸法図（ディメンション図）掲載 |
| [Honda取扱説明書 PDF](https://www.honda.co.jp/ownersmanual/pdf/motor/cb400superfour/30MFM610_web.pdf) | フレーム構造・各部名称の参考 |

### 写真資料集
| リンク | 内容 |
|--------|------|
| [NC42 CB400SF 写真資料](https://mihiro.sakura.ne.jp/shimoken/cb400sf-003.htm) | NC42の多角度写真集（非公式・詳細） |
| [バイクの系譜 CB400SF Revo NC42](https://bike-lineage.org/honda/cb400sf/revo.html) | 歴史と各部詳細写真 |

### キャンディークロモスフィアレッド関連
| リンク | 内容 |
|--------|------|
| [新色追加ニュース（2018）](https://response.jp/article/2018/06/08/310629.html) | 追加時の公式カラー写真 |
| [CBXカラー解説](https://clicccar.com/2018/06/13/597886/) | カラーリングの由来・詳細写真 |

---

## カラーリング詳細

### キャンディークロモスフィアレッド（Candy Chromosphere Red）

| 項目 | 内容 |
|------|------|
| 配色 | 赤 × パールサンビームホワイト × 黒ライン |
| 別名 | 「CBXカラー」（CBX400F復刻配色） |
| 適用パーツ | タンク・サイドカバー・リアシートカウル |
| 追加年 | 2018年（NC42後期） |

### Blenderマテリアル設定の目安

```
タンク本体:
  - Base Color: 深みのある赤（キャンディー塗装 → Subsurface/透過感）
  - Metallic: 0.0
  - Roughness: 0.05〜0.1（高光沢クリア層）
  - Clearcoat: 使用（BSDF Principled の Clearcoat = 1.0）

ホワイトライン:
  - Base Color: パールホワイト（#F5F0E8 程度）
  - Roughness: 0.1

ブラックライン:
  - Base Color: #1A1A1A
  - Roughness: 0.15
```

> **キャンディー塗装の表現**: 通常の赤より暗めのベースに強いClearcoatを重ねると実車に近くなる。参考HEX: `#8B0000`（ダークレッド）ベース + Clearcoat反射。

---

## パーツカタログ・構造資料

| リンク | 内容 |
|--------|------|
| [CMSNL パーツリスト（NC39）](https://www.cmsnl.com/honda-cb400-super-four-2005-5-japan-nc39-110_model49744/partslist/) | 部品名・形状の参照（NC42とほぼ同一） |
| [Honda FactBook CB400SF SPEC III](https://www.honda.co.jp/factbook/motor/cb400sfspec3/200312/014.html) | エンジン構造の詳細 |
| [NC42サービスマニュアル情報](http://tokidokidokin.com/2010/09/cb400sf-revo-nc42cb400a9-j%E3%81%AE%E3%82%B5%E3%83%BC%E3%83%93%E3%82%B9%E3%83%9E%E3%83%8B%E3%83%A5%E3%82%A3%E3%83%AB%E3%81%A8%E3%83%91%E3%83%BC%E3%83%84%E3%82%AB%E3%82%BF%E3%83%AD%E3%82%B0%EF%BC%88/) | サービスマニュアル入手先情報 |

---

## 今すぐやること（Phase 0 残タスク）

1. [CB400 Super Four (2018) Blueprint](https://www.the-blueprints.com/blueprints/motorcycles/honda-motor/84265/view/honda_cb400_super_four_2018/) を開いて画像を保存 → `docs/references/images/blueprint_side.png` 等
2. [Honda公式スペックページ](https://www.honda.co.jp/CB400SF/spec/) のディメンション図を保存
3. [Honda公式デザインページ](https://www.honda.co.jp/CB400SF/design/) でキャンディーレッドの実車写真を保存
