# Blender初期セットアップ手順

---

## 1. プロジェクトファイル作成

1. Blender起動 → 「General」で新規作成
2. デフォルトの cube / light / camera を削除（A で全選択 → Delete）
3. **保存**: `blender/cb400sf_main.blend`

---

## 2. 単位設定

`Scene Properties（カメラアイコン）> Units`

| 設定 | 値 |
|------|----|
| Unit System | Metric |
| Unit Scale | 1.0 |
| Length | Millimeters（作業しやすい） |

> ※ Millimetersにすると「2080」と入力すれば全長になる。
> メートルのままなら「2.080」と入力。

---

## 3. スケール確認用エンプティ配置

```
Shift+A > Empty > Plain Axes
```

- 名前: `REF_vehicle_size`
- X方向に2.080m（全長）のスケールのガイドとして使用

実寸エンプティ：
- `REF_wheelbase`（1410mm幅でEmptyを2個配置）
- `REF_height`（Z=1080mmにEmpty）

---

## 4. リファレンス画像の設定

### 推奨画像
- 正面図（Front View）
- 右側面図（Right Side View）
- ※ 三面図（正面・側面・上面が1枚に収まったもの）が理想

### 配置方法

```
Shift+A > Image > Reference
```

- Front: NumPad 1 で正面ビュー、XZ平面に配置
- Right: NumPad 3 で側面ビュー、YZ平面に配置

### 調整
- 透明度: Image Properties > Opacity = 0.5
- ホイールベース（1410mm）に合わせてスケール調整
- Object Properties > Visibility > Show in Render: OFF（レンダリングに映らないように）

---

## 5. コレクション構成

Outliner で以下のコレクションを作成:

```
Scene Collection
└── CB400SF
    ├── _REFERENCE（リファレンス画像・エンプティ）
    ├── Frame
    ├── Engine
    ├── Body
    ├── Suspension
    ├── Wheels
    └── Electrical
```

---

## 6. オーバーレイ設定（作業効率化）

- `Viewport Overlays > Statistics: ON`（ポリゴン数確認）
- `Auto Smooth: ON`（Mesh Properties > Normals > Auto Smooth: 30°）

---

## 7. アドオン確認

以下のアドオンが有効になっているか確認:

- `Mesh: Extra Objects`（ネジ・ボルト生成に便利）
- `Add Curve: Extra Objects`（ケーブル類に使用）
- `Loop Tools`（ループ選択・整列）

`Edit > Preferences > Add-ons` で検索して有効化。
