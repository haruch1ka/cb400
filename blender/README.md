# blender/ ディレクトリ構成

```
blender/
├── cb400sf_main.blend        ← メインファイル（常にここから作業）
├── cb400sf_backup_YYYYMMDD.blend  ← 節目ごとのバックアップ
│
├── textures/                 ← テクスチャ画像
│   ├── body/                 ← 外装（タンク・カウル等）
│   │   ├── candy_red_base.png
│   │   ├── pearl_white.png
│   │   └── clearcoat_roughness.png
│   ├── engine/               ← エンジン（アルミ・鉄・ゴム等）
│   └── decals/               ← エンブレム・ロゴ・ストライプ
│
├── render/                   ← レンダリング出力
│   ├── wip/                  ← 作業中チェック用（上書きOK）
│   └── final/                ← 最終出力（日付付きで保存）
│
├── hdri/                     ← HDRIライティング用画像
│   └── （Poly Haven等からダウンロードして配置）
│
└── export/                   ← 他形式エクスポート（FBX / OBJ / GLB）
```

---

## ファイル命名規則

| 種別 | 命名例 |
|------|--------|
| メインBlendファイル | `cb400sf_main.blend` |
| バックアップ | `cb400sf_backup_20260618.blend` |
| WIPレンダー | `wip_side_001.png` |
| 最終レンダー | `final_side_20260618.png` |
| テクスチャ | `body_candy_red_base.png` |

---

## Blend内コレクション構成（Outliner）

```
Scene Collection
└── CB400SF
    ├── _REFERENCE       ← リファレンス画像・計測用エンプティ（レンダー非表示）
    ├── Frame            ← フレーム・スイングアーム
    ├── Engine           ← エンジン全般・排気系
    ├── Body             ← タンク・シート・カウル・フェンダー
    ├── Suspension       ← フォーク・リアショック
    ├── Wheels           ← ホイール・タイヤ・ブレーキ
    └── Electrical       ← ライト・メーター・スイッチ類
```

---

## HDRIの入手先

無料で使えるHDRI（クレカ不要）:
- [Poly Haven](https://polyhaven.com/hdris) — `studio_small` または `studio_country_hall` が撮影風で映える
- ダウンロードした `.hdr` / `.exr` を `hdri/` に配置する
