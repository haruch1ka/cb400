# フレームのモデリング方法

---

## 基本アプローチ: パイプ断面 + Curve / Screw

フレームパイプは「円形断面をカーブに沿わせる」方法が最も直感的。

### 手法A: Curve オブジェクト（推奨）

1. `Shift+A` → Curve → **BézierCurve** でパイプの経路を描く
2. Curve プロパティ → Geometry → **Bevel → Round**
3. Depth でパイプ径を設定（メインパイプ: 約 25〜30mm）
4. 形が決まったら `Alt+C` → Mesh に変換してトポロジーを整える

### 手法B: Cylinder を変形（ブロッキング向き）

1. Cylinder を追加してパイプ1本分の長さに整える
2. 端点を `G` で動かして角度を付ける
3. 接合部（T字・Y字）は別 Cylinder と Boolean で合わせる

---

## ダイヤモンドフレームの構成

```
ヘッドパイプ（上端）
  ├── メインチューブ（上）  → エンジン上部へ
  ├── ダウンチューブ        → エンジン下部へ
  └── シートレール          → シート下へ
```

CB400SF のキャスター角: **25.5°**（ヘッドパイプの前傾角度）

---

## 寸法目安

| 部位 | パイプ径（目安） |
|------|----------------|
| メインチューブ | φ 28mm |
| ダウンチューブ | φ 25mm |
| シートレール | φ 22mm |
| エンジンマウント | φ 18mm |

---

## 参考動画

- [Blender Pipe / Tube Modeling with Curve](https://www.youtube.com/results?search_query=blender+pipe+frame+curve+modeling)
- [Modeling a Sci-Fi Motorcycle in Blender（CG Cookie）](https://www.youtube.com/watch?v=EnEWjuigTUU) — フレーム構造の参考に
