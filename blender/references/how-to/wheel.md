# ホイールのモデリング方法

CB400SF は 17インチ、5本スポーク（キャストホイール）。

---

## 構成パーツ

```
wheel
├── rim（リム）     ← タイヤが乗る外周部分
├── hub（ハブ）     ← 中心のアクスル取付部
└── spoke × 5      ← リムとハブをつなぐ
```

---

## リムの作り方

1. `Shift+A` → Mesh → **Circle**（Vertices: 64）
2. `E → S` で外側へ押し出してリム断面（コの字断面）を作る
3. **Screw モディファイア**（Axis: Y、Angle: 360°、Steps: 64）で回転体にする
4. または断面を Curve で描いて **Spin**（`Alt+R`）してもよい

リム外径: 17インチ = **432mm**（半径 216mm）

---

## スポークの作り方

1. Cylinder（径 φ15mm、長さ = ハブ〜リム間距離）を1本作る
2. 形状を整えて（端が太くなる形）1本完成させる
3. `Shift+A` → Empty → Plain Axes を原点に配置
4. **Array モディファイア** → Object Offset で Empty を指定
5. Empty を Z軸で `360°÷5 = 72°` 回転 → Count: 5 でスポーク5本

---

## ブレーキディスクの作り方

1. Cylinder（薄い円板）でディスク形状を作る
   - 外径: **φ 296mm**（フロント）/ **φ 240mm**（リア）
   - 厚み: 5mm
2. 穴パターンは Boolean で6〜8個の小円を Difference

---

## 寸法まとめ

| | フロント | リア |
|--|---------|------|
| ホイール径 | 17インチ（432mm） | 17インチ（432mm） |
| ブレーキディスク径 | φ 296mm | φ 240mm |
| スポーク本数 | 5本 | 5本 |

---

## 参考動画

- [Blender Tutorial - Modeling Motorcycle Tires with Tread](https://www.youtube.com/watch?v=oSH-nuPZTeY) — ホイール含む
- [Modeling a Motorbike in Blender - Part 1: The Tire](https://www.youtube.com/watch?v=rxu06q1ZK_Q)
