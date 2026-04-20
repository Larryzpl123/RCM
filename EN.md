# Ring-Closing Metathesis (RCM) / 关环复分解反应

**A Bilingual Detailed Explanation / 双语详解** - [PDF Version / PDF 版本](RCM_Ring_Closing_Metathesis.pdf)

Compiled for Organic Chemistry Study — April 13, 2026 

---

<video src="RCM.mp4" controls width="100%"></video> 

---

## Table of Contents

1. [Introduction / 引言](#1-introduction--引言)
2. [Historical Background / 历史背景](#2-historical-background--历史背景)
3. [The General Reaction / 一般反应式](#3-the-general-reaction--一般反应式)
4. [Mechanism: The Chauvin Cycle / 机理：Chauvin 循环](#4-mechanism-the-chauvin-cycle--机理chauvin-循环)
   - 4.1 [Step-by-Step Mechanism / 逐步机理](#41-step-by-step-mechanism--逐步机理)
   - 4.2 [Catalytic Cycle Diagram / 催化循环图](#42-catalytic-cycle-diagram--催化循环图)
5. [Common Catalysts / 常用催化剂](#5-common-catalysts--常用催化剂)
6. [Ring Size and Selectivity / 环的大小与选择性](#6-ring-size-and-selectivity--环的大小与选择性)
7. [Key Factors Affecting RCM / 影响 RCM 的关键因素](#7-key-factors-affecting-rcm--影响-rcm-的关键因素)
8. [Representative Examples / 代表性反应实例](#8-representative-examples--代表性反应实例)
   - 8.1 [Five-Membered Ring Formation / 五元环形成](#81-example-1-five-membered-ring-formation--五元环形成)
   - 8.2 [Macrolactonization via RCM / 大环内酯的 RCM 合成](#82-example-2-macrolactonization-via-rcm--大环内酯的-rcm-合成)
9. [Comparison with Related Metathesis Reactions / 与相关复分解反应的比较](#9-comparison-with-related-metathesis-reactions--与相关复分解反应的比较)
10. [Applications / 应用](#10-applications--应用)
11. [Limitations and Challenges / 局限性与挑战](#11-limitations-and-challenges--局限性与挑战)
12. [Summary / 总结](#12-summary--总结)

---

## 1. Introduction / 引言

### English

**Ring-Closing Metathesis (RCM)** is an intramolecular olefin metathesis reaction in which a diene (a molecule with two carbon–carbon double bonds) is converted into a cyclic alkene, releasing a small olefin (typically ethylene, CH₂=CH₂) as a byproduct. RCM is one of the most powerful and widely used methods for constructing carbon–carbon double bonds within ring systems. It has revolutionized the synthesis of medium- and large-ring compounds, which are notoriously difficult to prepare by other methods.

The term *metathesis* comes from the Greek *metatithemi*, meaning "to transpose." In olefin metathesis, the substituents on two double bonds are formally exchanged ("transposed") through cleavage and re-formation of C=C bonds, mediated by a transition-metal carbene catalyst.

### 中文

**关环复分解反应 (Ring-Closing Metathesis, RCM)** 是一种**分子内**的烯烃复分解反应：一个含有两个碳碳双键（二烯）的分子在金属卡宾催化剂的作用下，形成一个新的环状烯烃，同时释放出一个小分子烯烃（通常为乙烯 CH₂=CH₂）。

RCM 是构建环状碳碳双键最有力的方法之一，尤其在合成中环和大环化合物方面具有革命性意义——这些化合物用其他方法通常很难制备。

"复分解"（metathesis）一词源自希腊语 *metatithemi*，意为"交换"。在烯烃复分解反应中，两个双键上的取代基通过 C=C 键的断裂和重新组合进行"交换"，这一过程由**过渡金属卡宾催化剂**介导。

---

## 2. Historical Background / 历史背景

### English

Olefin metathesis was first observed in the 1950s and 1960s in industrial polymer chemistry (e.g., the Phillips petroleum process). However, the mechanism remained a mystery until **Yves Chauvin** proposed the metal-carbene mechanism in 1971.

The development of well-defined, functional-group-tolerant catalysts by **Robert H. Grubbs** and **Richard R. Schrock** in the 1990s made RCM practical for organic synthesis. The three chemists were awarded the **2005 Nobel Prize in Chemistry** "for the development of the metathesis method in organic synthesis."

Key milestones:

- **1971** — Chauvin mechanism proposed.
- **1990** — Schrock's Mo-based alkylidene catalysts.
- **1992** — Grubbs' 1st-generation Ru catalyst (Grubbs I).
- **1999** — Grubbs' 2nd-generation catalyst (Grubbs II) with NHC ligand.
- **2000s** — Hoveyda–Grubbs catalysts and further developments.

### 中文

烯烃复分解反应最早在 1950–1960 年代的工业高分子化学中被观察到（例如 Phillips 石油公司的工艺）。但其机理直到 **Yves Chauvin**（伊夫·肖万）于 1971 年提出金属卡宾机理后才被阐明。

**Robert H. Grubbs**（罗伯特·格拉布斯）和 **Richard R. Schrock**（理查德·施罗克）在 1990 年代开发了具有良好官能团耐受性的催化剂，使得 RCM 在有机合成中变得切实可行。三位化学家于 **2005 年**因"在有机合成中发展了复分解方法"而获得**诺贝尔化学奖**。

重要里程碑：

- **1971** — Chauvin 机理被提出。
- **1990** — Schrock 的钼基烷叉催化剂。
- **1992** — Grubbs 第一代钌催化剂（Grubbs I）。
- **1999** — Grubbs 第二代催化剂（Grubbs II），含 NHC 配体。
- **2000s** — Hoveyda–Grubbs 催化剂及后续发展。

---

## 3. The General Reaction / 一般反应式

### English

The general RCM transformation can be written as:

> **diene** —[M]=CHR catalyst, solvent, Δ→ **cyclic alkene** + CH₂=CH₂ ↑

The driving force is the **release of gaseous ethylene**, which escapes the reaction mixture (Le Chatelier's principle), shifting the equilibrium toward product formation.

Typical conditions: 1–10 mol% catalyst, **dilute** conditions (to favor intramolecular cyclization over intermolecular oligomerization), refluxing CH₂Cl₂ or toluene, under inert atmosphere (N₂ or Ar).

### 中文

RCM 的一般反应可以表示为：

> **二烯** —[M]=CHR 催化剂, 溶剂, Δ→ **环状烯烃** + CH₂=CH₂ ↑

反应的**驱动力**是**气态乙烯的释放**：乙烯逸出反应体系（勒夏特列原理），使平衡向生成环状产物的方向移动。

典型条件：1–10 mol% 催化剂，**稀释条件**（有利于分子内关环，而非分子间寡聚），在 CH₂Cl₂ 或甲苯中回流，惰性气氛（N₂ 或 Ar）。

---

## 4. Mechanism: The Chauvin Cycle / 机理：Chauvin 循环

> The accepted mechanism for all olefin metathesis reactions (including RCM) is the **Chauvin mechanism**, which proceeds through a series of [2+2] cycloadditions and retro-[2+2] cycloreversions involving a **metallacyclobutane** intermediate.

### 4.1 Step-by-Step Mechanism / 逐步机理

#### English — Step-by-Step

**Step 1: Coordination.** The metal carbene catalyst [M]=CHR coordinates to one of the two olefinic groups of the diene substrate.

**Step 2: [2+2] Cycloaddition.** The metal carbene and the coordinated olefin undergo a [2+2] cycloaddition to form a four-membered **metallacyclobutane** ring. Although [2+2] cycloadditions are thermally forbidden for purely organic substrates (Woodward–Hoffmann rules), the d-orbitals of the metal make this process symmetry-allowed.

**Step 3: Retro-[2+2] Cycloreversion.** The metallacyclobutane ring opens in the productive direction to release a small olefin (ethylene) and generate a **new metal carbene species** that is now tethered to the substrate.

**Step 4: Intramolecular [2+2] Cycloaddition.** The new carbene, now part of the same molecule as the second double bond, undergoes a second [2+2] cycloaddition with the remaining olefin, forming a second metallacyclobutane — this time as part of the ring.

**Step 5: Retro-[2+2] Cycloreversion (ring closure).** The second metallacyclobutane undergoes cycloreversion to release the **cyclic alkene product** and regenerate the metal carbene catalyst, completing the catalytic cycle.

#### 中文 — 逐步解析

**第一步：配位。** 金属卡宾催化剂 [M]=CHR 与二烯底物上的**一个**烯基配位。

**第二步：[2+2] 环加成。** 金属卡宾与配位的烯烃进行 [2+2] 环加成，形成四元环**金属杂环丁烷**（metallacyclobutane）。虽然 [2+2] 环加成对纯有机底物在热条件下是对称性禁阻的（Woodward–Hoffmann 规则），但金属的 d 轨道使这一过程在对称性上是允许的。

**第三步：逆 [2+2] 环裂解。** 金属杂环丁烷以生产性方向开环，释放一个小分子烯烃（乙烯），并生成**新的金属卡宾物种**——该卡宾现已连接在底物链上。

**第四步：分子内 [2+2] 环加成。** 新生成的卡宾与分子内剩余的另一个双键发生第二次 [2+2] 环加成，形成第二个金属杂环丁烷——此时它已包含在环结构中。

**第五步：逆 [2+2] 环裂解（关环）。** 第二个金属杂环丁烷发生环裂解，释放**环状烯烃产物**并**再生催化剂**，完成催化循环。

### 4.2 Catalytic Cycle Diagram / 催化循环图

```
                    + diene substrate / + 二烯底物
                              │
        ┌─────────────────────▼──────────────────────┐
        │                                            │
        │   [M]=CHR ──── [2+2] ────► Metallacyclo-   │
        │   催化剂                     butane I       │
        │     ▲                       金属杂环丁烷 I   │
        │     │                           │          │
        │  retro-[2+2]               retro-[2+2]     │
        │  release product           −CH₂=CH₂        │
        │  释放产物                       │          │
        │     │                           ▼          │
        │   Metallacyclo- ◄── intramol.  New [M]=CH– │
        │   butane II         [2+2]      (tethered)  │
        │   金属杂环丁烷 II               新卡宾(连接)  │
        │                                            │
        └────────────────────────────────────────────┘
                              │
                              ▼
                  Cyclic alkene / 环状烯烃
```
<img src="rcm_cycle.png" alt="RCM Cycle" width="555">
---

## 5. Common Catalysts / 常用催化剂

### English

The most commonly used RCM catalysts are ruthenium-based, prized for their air stability, functional group tolerance, and ease of handling compared to Schrock's early-transition-metal catalysts.

| Catalyst | Metal | Ligand | Features |
|---|---|---|---|
| Grubbs I | Ru | PCy₃ / PCy₃ | Good activity; air-stable; less reactive with sterically hindered substrates |
| Grubbs II | Ru | NHC (SIMes) / PCy₃ | Higher activity and stability; handles more challenging substrates |
| Hoveyda–Grubbs II | Ru | NHC / chelating isopropoxybenzylidene | Recyclable; excellent thermal stability; good for electron-poor olefins |
| Schrock Mo | Mo | Imido / alkoxide | Very high reactivity; sensitive to air and moisture; less functional-group tolerant |

NHC = N-heterocyclic carbene (typically SIMes = 1,3-bis(2,4,6-trimethylphenyl)-4,5-dihydroimidazol-2-ylidene).

### 中文

最常用的 RCM 催化剂是**钌（Ru）基催化剂**，因其**空气稳定性**好、**官能团耐受性**强、操作方便而受到青睐。

| 催化剂 | 金属 | 特点 |
|---|---|---|
| Grubbs I | Ru | 活性良好；空气稳定；对空间位阻大的底物反应性较低 |
| Grubbs II | Ru | 活性和稳定性更高；可处理更具挑战性的底物 |
| Hoveyda–Grubbs II | Ru | 可回收；热稳定性优异；适用于贫电子烯烃 |
| Schrock Mo 催化剂 | Mo | 反应性极高；对空气和水敏感；官能团耐受性较低 |

NHC = N-杂环卡宾。第二代催化剂用 NHC 替代了一个 PCy₃ 配体，显著提高了催化活性。

---

## 6. Ring Size and Selectivity / 环的大小与选择性

### English

RCM is most effective for forming **five-** and **six-membered rings**, which are thermodynamically and kinetically favored (low ring strain, favorable entropy).

- **5- and 6-membered rings**: Very facile; often proceed at room temperature with low catalyst loading (1–2 mol%).
- **7- and 8-membered rings**: Moderate difficulty; may require higher temperatures, longer times, or higher catalyst loading.
- **Medium rings (9–12)**: Challenging due to transannular strain and unfavorable entropy; require high dilution and sometimes specialized catalysts.
- **Large rings (≥ 13)**: Macrocyclic RCM is possible and widely used in natural product synthesis, but requires very high dilution (typically ≤ 1 mM substrate concentration).

The competition between intramolecular RCM and intermolecular acyclic diene metathesis polymerization (ADMET) is controlled by **dilution**: lower concentration favors RCM.

### 中文

RCM 最擅长形成**五元环**和**六元环**（热力学和动力学都有利：环张力低，熵变有利）。

- **5 元和 6 元环**：非常容易；通常室温、低催化剂用量（1–2 mol%）即可进行。
- **7 元和 8 元环**：难度适中；可能需要更高温度、更长时间或更多催化剂。
- **中环 (9–12 元)**：由于跨环张力和不利熵变，较为困难；需高稀释和特殊催化剂。
- **大环 (≥ 13 元)**：大环 RCM 在天然产物合成中广泛应用，但需非常高的稀释度（底物浓度通常 ≤ 1 mM）。

分子内 RCM 与分子间非环二烯复分解聚合（ADMET）之间的竞争由**稀释度**控制：低浓度有利于 RCM。

---

## 7. Key Factors Affecting RCM / 影响 RCM 的关键因素

### English

1. **Thorpe–Ingold effect (gem-disubstitution effect).** Having substituents on the carbon chain connecting the two olefins brings the reactive ends closer together, accelerating cyclization. This conformational effect is often exploited deliberately.

2. **Olefin substitution pattern.** Terminal olefins (monosubstituted) react fastest. Disubstituted olefins are slower but still feasible. Trisubstituted olefins are challenging and require highly active catalysts (e.g., Grubbs II or Hoveyda–Grubbs II).

3. **Functional group compatibility.** Ruthenium catalysts tolerate alcohols, esters, amides, ethers, and even some amines and thiols. However, free amines, thiols, and phosphines can coordinate to the metal and poison the catalyst. *Protection* of these groups (e.g., Boc for amines) is common.

4. **Concentration.** High dilution (~1–10 mM) favors RCM over oligomerization. Slow addition of substrate (*syringe pump*) is also used.

5. **Temperature.** Refluxing CH₂Cl₂ (~40 °C) or toluene (~110 °C) is typical. Higher temperatures increase catalyst activity but may also accelerate decomposition.

6. **Ethylene removal.** Removing ethylene (by inert gas sparging or reduced pressure) drives the equilibrium forward.

### 中文

1. **Thorpe–Ingold 效应（偕二取代效应）。** 在连接两个烯烃的碳链上引入取代基，可使反应端基靠近，加速关环。此构象效应常被有意利用。

2. **烯烃取代模式。** 端烯（单取代）反应最快；二取代烯烃较慢但可行；三取代烯烃困难，需高活性催化剂。

3. **官能团兼容性。** 钌催化剂可耐受醇、酯、酰胺、醚等。但游离胺、硫醇和膦可与金属配位，毒化催化剂。常需保护这些基团（如胺用 Boc 保护）。

4. **浓度。** 高稀释（~1–10 mM）有利于 RCM 而非寡聚。注射泵缓慢加料也常使用。

5. **温度。** 常在 CH₂Cl₂（~40 °C）或甲苯（~110 °C）中回流。高温提高催化活性，但也可能加速催化剂分解。

6. **乙烯移除。** 通过惰性气体鼓泡或减压除去乙烯，推动平衡正向移动。

---

## 8. Representative Examples / 代表性反应实例

[More Examples / 更多例子](RCM_Detailed_Guide.pdf)

### 8.1 Example 1: Five-Membered Ring Formation / 五元环形成

#### English

One of the simplest demonstrations of RCM is the cyclization of diallyl ether to form 2,5-dihydrofuran:

> CH₂=CH–CH₂–O–CH₂–CH=CH₂ —Grubbs I, CH₂Cl₂→ **2,5-dihydrofuran** + CH₂=CH₂ ↑

This reaction proceeds quantitatively at room temperature within minutes, illustrating the ease of 5-membered ring closure.

#### 中文

RCM 最简单的示例之一是二烯丙基醚关环生成 2,5-二氢呋喃：

> CH₂=CH–CH₂–O–CH₂–CH=CH₂ —Grubbs I, CH₂Cl₂→ **2,5-二氢呋喃** + CH₂=CH₂ ↑

此反应在室温下数分钟内定量完成，说明五元环关环的容易程度。

### 8.2 Example 2: Macrolactonization via RCM / 大环内酯的 RCM 合成

#### English

Many biologically active natural products contain macrocyclic lactones (macrolides). RCM has been used in landmark total syntheses such as:

- **Epothilone A & B** — 16-membered macrolide anticancer agents.
- **Sch 38516 (fluvirucinin A₁)** — 14-membered ring closure by RCM.
- **Stemonamide** — a complex alkaloid synthesized using RCM as a key step.

In these syntheses, the RCM step typically requires high dilution (< 1 mM) and Grubbs II or Hoveyda–Grubbs II catalyst.

#### 中文

许多生物活性天然产物含有大环内酯结构。RCM 已在以下里程碑式全合成中应用：

- **Epothilone A/B** — 16 元大环内酯类抗癌药物。
- **Sch 38516 (fluvirucinin A₁)** — 14 元环关环。
- **Stemonamide** — 一种复杂生物碱，以 RCM 为关键步骤。

这些合成中，RCM 步骤通常需要高稀释度 (< 1 mM) 和 Grubbs II 或 Hoveyda–Grubbs II 催化剂。

---

## 9. Comparison with Related Metathesis Reactions / 与相关复分解反应的比较

| Reaction Type / 反应类型 | Substrates / 底物 | Products / 产物 | Notes / 备注 |
|---|---|---|---|
| **RCM** / 关环复分解 | Diene (intramol.) | Cyclic alkene + CH₂=CH₂ | Ring formation; dilute conditions |
| **CM** / 交叉复分解 | Two olefins (intermol.) | New olefin | E/Z selectivity can be challenging |
| **ROM** / 开环复分解 | Cyclic olefin | Diene or oligomer | Driven by ring strain release |
| **ROMP** / 开环复分解聚合 | Strained cyclic olefin | Polymer | Norbornene, cyclooctene, etc. |
| **ADMET** / 非环二烯复分解 | α,ω-diene (intermol.) | Linear polymer + CH₂=CH₂ | Competes with RCM |

---

## 10. Applications / 应用

### English

1. **Total Synthesis of Natural Products.** RCM is a go-to strategy for constructing macrocyclic frameworks found in bioactive molecules (macrolides, cyclopeptides, terpenes).

2. **Pharmaceutical Chemistry.** Several FDA-approved drugs and clinical candidates feature ring systems formed by RCM, including **simeprevir** (Hepatitis C protease inhibitor) and **BILN 2061**.

3. **Materials Science.** ROMP (the polymer counterpart) produces specialty polymers, but RCM itself is used in monomer synthesis.

4. **Green Chemistry.** Metathesis can replace multi-step sequences, improving atom economy. Ethylene is the only byproduct.

5. **Bioconjugation & Chemical Biology.** RCM has been used to "staple" α-helical peptides, reinforcing their secondary structure for therapeutic applications.

### 中文

1. **天然产物全合成。** RCM 是构建生物活性分子中大环骨架的首选策略（大环内酯、环肽、萜类化合物）。

2. **药物化学。** 多种 FDA 批准药物和临床候选药物含有由 RCM 形成的环系统，包括 **simeprevir**（丙肝蛋白酶抑制剂）和 **BILN 2061**。

3. **材料科学。** ROMP（聚合物对应版本）用于生产特种高分子，而 RCM 本身用于单体合成。

4. **绿色化学。** 复分解可替代多步合成，提高原子经济性。乙烯是唯一副产物。

5. **生物偶联与化学生物学。** RCM 已被用于"钉合"（stapling）α-螺旋肽，增强其二级结构以用于治疗。

---

## 11. Limitations and Challenges / 局限性与挑战

### English

- **E/Z selectivity.** Standard RCM gives mixtures of E and Z isomers. Z-selective catalysts (e.g., by Grubbs and Hoveyda) have been developed but are still substrate-dependent.
- **Catalyst decomposition.** Ru catalysts can decompose at high temperatures or in the presence of certain functional groups. Ruthenium residues can be difficult to remove.
- **Substrate limitations.** Electron-poor olefins (e.g., α,β-unsaturated carbonyls) and very hindered olefins are sluggish.
- **Medium ring difficulty.** Rings of 8–12 members remain challenging targets.
- **Ruthenium removal.** Trace Ru in pharmaceutical products is a regulatory concern. Scavengers (e.g., activated carbon, DMSO, lead tetraacetate) or silica chromatography are used.

### 中文

- **E/Z 选择性。** 标准 RCM 通常得到 E/Z 异构体混合物。Z-选择性催化剂已被开发，但仍取决于底物。
- **催化剂分解。** 高温或某些官能团会导致 Ru 催化剂分解。钌残留的去除可能困难。
- **底物局限性。** 贫电子烯烃（如 α,β-不饱和羰基）和空间位阻大的烯烃反应缓慢。
- **中环难题。** 8–12 元环仍然是合成中的挑战。
- **钌残留。** 药物产品中的微量 Ru 是监管关注点。需用活性炭、DMSO 或硅胶色谱除去。

---

## 12. Summary / 总结

### English — Key Takeaways

1. RCM converts a diene into a cyclic alkene + ethylene, catalyzed by metal carbenes.
2. The mechanism follows the Chauvin cycle: alternating [2+2] and retro-[2+2] steps via metallacyclobutane intermediates.
3. Grubbs-type Ru catalysts are the workhorses due to their stability and functional group tolerance.
4. Ring size, dilution, olefin substitution, and the Thorpe–Ingold effect are critical for success.
5. RCM is indispensable in modern organic synthesis, from natural products to pharmaceuticals.

### 中文 — 核心要点

1. RCM 将二烯转化为环状烯烃 + 乙烯，由金属卡宾催化。
2. 机理遵循 Chauvin 循环：通过金属杂环丁烷中间体交替进行 [2+2] 和逆 [2+2] 步骤。
3. Grubbs 型 Ru 催化剂因其稳定性和官能团耐受性而成为主力。
4. 环大小、稀释度、烯烃取代模式和 Thorpe–Ingold 效应是成功的关键因素。
5. RCM 在现代有机合成中不可或缺，从天然产物到药物合成。
