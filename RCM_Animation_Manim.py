"""
Ring-Closing Metathesis (RCM) Animation — Round 6 fixes.

Round 6 targeted fixes (functional only — no new content):
  R6-1/3. MCB I ring is now ANCHORED at the diene chain: the ring's two
          bottom carbons stay exactly at c1a and c2a's original positions
          on the substrate. The ring grows UPWARD from there. This also
          fixes Cl and H2 no longer being clipped off the left edge, since
          the ring sits further right than before (ring center ~-3.5, -0.6
          instead of ~-4.4, -1.1).
  R6-2.   Step 3 retro-[2+2] is now strictly 2-AND-2. The two bonds that
          are KEPT (left = Ru-Ca, right = Cph-Cb) transform into the
          primary line of each new double bond. The two bonds that BREAK
          (top = Ru-Cph, bot = Ca-Cb) collapse to zero-length at their old
          midpoints, then are removed. The two new parallel (second) lines
          are Created. No more 'bond coming out of nowhere' / duplicate
          destinations.
  R6-6.   Same 2-AND-2 fix applied to step 5 retro-MCB II: keep left
          (C4-Ru) and right (Ca-C3); break top (Ru-Ca) and bot (C3-C4);
          Create the parallel lines for the regenerated Ru=CH2 and the new
          product C=C.

Round 5 fixes still in place (z-order, HUD placement, box consistency,
ring label offsets, regen position, single-motion step 4).
"""

from manim import *


# ---------- helpers ----------

def atom(label, color=WHITE, radius=0.22):
    base = Dot(radius=radius, color=color).set_fill(color, opacity=1.0)
    highlight = Dot(radius=radius * 0.38, color=WHITE)
    highlight.set_fill(WHITE, opacity=0.55)
    highlight.move_to(base.get_center() + np.array([-radius * 0.33,
                                                     radius * 0.33, 0.0]))
    rim = Circle(radius=radius, color=BLACK, stroke_width=1.4)
    rim.move_to(base.get_center())
    font_size = max(14, int(20 * radius / 0.22))
    txt = Text(label, font_size=font_size, weight=BOLD, color=BLACK)
    txt.move_to(base.get_center())
    group = VGroup(base, highlight, rim, txt)
    group.atom_radius = radius
    group.set_z_index(2)  # atoms render ABOVE bonds
    return group


def _radius_of(x):
    r = getattr(x, "atom_radius", None)
    return r if r is not None else 0.0


def bond(a, b, double=False, color=WHITE, gap=0.12, stroke_width=4):
    p1 = (np.array(a.get_center()) if hasattr(a, "get_center")
          else np.array(a, dtype=float))
    p2 = (np.array(b.get_center()) if hasattr(b, "get_center")
          else np.array(b, dtype=float))
    r_a = _radius_of(a) + 0.03
    r_b = _radius_of(b) + 0.03
    vec = p2 - p1
    length = float(np.linalg.norm(vec))
    if length > r_a + r_b + 1e-6:
        u = vec / length
        p1 = p1 + u * r_a
        p2 = p2 - u * r_b
        vec = p2 - p1
    if double and float(np.linalg.norm(vec)) > 1e-6:
        norm = np.array([-vec[1], vec[0], 0.0])
        n = norm / np.linalg.norm(norm) * gap
        result = VGroup(
            Line(p1 + n, p2 + n, color=color, stroke_width=stroke_width),
            Line(p1 - n, p2 - n, color=color, stroke_width=stroke_width),
        )
    else:
        result = Line(p1, p2, color=color, stroke_width=stroke_width)
    result.set_z_index(0)  # bonds BEHIND atoms
    return result


def _plain_line(a, b, color=WHITE, stroke_width=4):
    line = Line(np.array(a, dtype=float), np.array(b, dtype=float),
                color=color, stroke_width=stroke_width)
    line.set_z_index(0)
    return line


def _parallel_line(a, b, offset_vec, color=WHITE, stroke_width=4):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    o = np.array(offset_vec, dtype=float)
    line = Line(a + o, b + o, color=color, stroke_width=stroke_width)
    line.set_z_index(0)
    return line


def _ext_label(s, font_size=20, color=WHITE):
    """External text label (H2, L, Cl, Ph) -- always renders on top."""
    t = Text(s, font_size=font_size, color=color)
    t.set_z_index(3)
    return t


# ---------- main scene ----------

class RingClosingMetathesis(Scene):
    PHASES = {
        1: "Coordination",
        2: "[2+2] Cycloaddition",
        3: "Retro-[2+2]",
        4: "[2+2] Cycloaddition",
        5: "Retro-[2+2] & Release",
    }

    def construct(self):
        # ================= TITLE =================
        title = Text("Ring-Closing Metathesis", font_size=44, weight=BOLD)
        subtitle = Text("(RCM) - Grubbs Catalyst Mechanism",
                        font_size=26, color=GRAY_B)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(Write(title), FadeIn(subtitle, shift=UP))
        self.wait(1.0)
        self.play(FadeOut(title), FadeOut(subtitle))

        # ================= OVERALL =================
        overall = Text("Overall:  diene  ->  cycloalkene  +  ethylene",
                       font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(overall))

        # Substrate parked well below the HUD.
        substrate = self.build_diene()
        substrate.move_to(ORIGIN).shift(DOWN * 1.4)
        self.play(FadeIn(substrate))
        self.wait(0.5)

        # Tight rectangles around each C=C ONLY (H2 excluded on BOTH sides).
        rect1 = SurroundingRectangle(
            VGroup(substrate[0][0], substrate[0][1], substrate[0][3]),
            color=BLUE, buff=0.2)
        rect2 = SurroundingRectangle(
            VGroup(substrate[2][0], substrate[2][1], substrate[2][3]),
            color=RED, buff=0.2)
        lbl1 = Text("alkene 1", font_size=20, color=BLUE).next_to(rect1, UP, buff=0.18)
        lbl2 = Text("alkene 2", font_size=20, color=RED).next_to(rect2, UP, buff=0.18)
        self.play(Create(rect1), Create(rect2), Write(lbl1), Write(lbl2))
        self.wait(1.0)
        self.play(FadeOut(rect1), FadeOut(rect2),
                  FadeOut(lbl1), FadeOut(lbl2),
                  FadeOut(overall))

        # ================= HUD — appears BEFORE step 1 =================
        (header, cycle_group, indicator, product_indicator,
         positions, endpoints, hud_dots) = self.build_overlay()
        TL, TR, BR, BL, exit_bot = endpoints
        diene_dot_hud, product_dot_hud = hud_dots

        # Indicator starts as a BLUE hollow circle around the HUD blue dot.
        indicator.set_color(BLUE).set_stroke(BLUE, width=3)
        indicator.set_fill(BLUE, opacity=0)
        indicator.move_to(diene_dot_hud.get_center())

        self.play(
            FadeIn(cycle_group),
            FadeIn(diene_dot_hud),
            FadeIn(product_dot_hud),
            FadeIn(indicator),
            FadeIn(header),
        )
        self.wait(0.6)

        # ================= STEP 1 — Coordination =================
        self.set_step(1, "Ru catalyst approaches alkene 1",
                      header, indicator, positions,
                      indicator_pre_move=True, indicator_target=TL)

        catalyst = self.build_catalyst()
        catalyst.to_edge(LEFT, buff=0.35).shift(UP * 0.8)
        self.play(FadeIn(catalyst))
        self.wait(0.3)

        approach_target = substrate[0].get_center() + LEFT * 1.8 + UP * 0.55
        self.play(catalyst.animate.move_to(approach_target), run_time=1.2)
        self.wait(0.3)

        # Handles on the catalyst + substrate parts we'll morph.
        ru      = catalyst[0]
        cat_db  = catalyst[1]
        ch      = catalyst[2]
        ph_lbl  = catalyst[3]
        l_lbl   = catalyst[4]
        cl_lbl  = catalyst[5]

        c1a = substrate[0][0]
        c2a = substrate[0][1]
        h2_left = substrate[0][2]
        alk_db = substrate[0][3]

        c3a = substrate[2][0]
        c4a = substrate[2][1]
        h2_right = substrate[2][2]
        alk2_db = substrate[2][3]

        tb1 = substrate[1][0]
        t1  = substrate[1][1]
        tb2 = substrate[1][2]
        t2  = substrate[1][3]
        tb3 = substrate[1][4]
        t3  = substrate[1][5]
        tb4 = substrate[1][6]

        # ================= STEP 2 — [2+2] -> MCB I =================
        self.set_step(2, "Four-membered ring forms",
                      header, indicator, positions)

        # Ring is ANCHORED at the diene chain: the two bottom carbons of
        # MCB I STAY exactly at c1a and c2a's current positions (alkene 1).
        # The ring builds UPWARD from there — Ru and Cph drop in above.
        # Width = 1 (preserves c1-c2 spacing); height = 1.
        ca_t  = c1a.get_center().copy()
        cb_t  = c2a.get_center().copy()
        ru_t  = ca_t + UP * 1.0
        cph_t = cb_t + UP * 1.0
        ring1_center = (ca_t + cb_t + ru_t + cph_t) / 4

        top_tgt1   = _plain_line(ru_t,  cph_t)
        right_tgt1 = _plain_line(cph_t, cb_t)
        bot_tgt1   = _plain_line(cb_t,  ca_t)
        left_tgt1  = _plain_line(ca_t,  ru_t)
        tb1_tgt1   = _plain_line(cb_t,  t1.get_center())

        self.play(
            ru.animate.move_to(ru_t),
            ch.animate.move_to(cph_t),
            # c1a and c2a STAY (no move_to) — they're already at ca_t/cb_t.
            # labels pushed OUTSIDE the 1.6-radius orange highlight
            ph_lbl.animate.move_to(cph_t + UP * 1.2),
            l_lbl.animate.move_to(ru_t + UP * 1.2),
            cl_lbl.animate.move_to(ru_t + LEFT * 1.2),
            h2_left.animate.move_to(ca_t + LEFT * 1.2),
            # 4 bond lines physically stretch into the 4 ring edges
            Transform(cat_db[0], top_tgt1),
            Transform(cat_db[1], left_tgt1),
            Transform(alk_db[0], right_tgt1),
            Transform(alk_db[1], bot_tgt1),
            Transform(tb1, tb1_tgt1),
            run_time=1.7,
        )
        self.wait(0.35)

        ring1_hl_center = (ru_t + cph_t + ca_t + cb_t) / 4
        ring_highlight1 = Circle(radius=1.3, color=ORANGE, stroke_width=5)
        ring_highlight1.move_to(ring1_hl_center)
        rlbl1 = Text("metallacyclobutane I", font_size=22, color=ORANGE)
        rlbl1.next_to(ring_highlight1, DOWN, buff=0.35)
        self.play(Create(ring_highlight1), Write(rlbl1))
        self.wait(1.1)
        self.play(FadeOut(ring_highlight1), FadeOut(rlbl1))

        # ================= STEP 3 — Retro MCB I (left edge shortens on-axis) =================
        self.set_step(3, "Releases ethylene; new Ru=CH alkylidene",
                      header, indicator, positions)

        ax_x = (ru_t[0] + ca_t[0]) / 2
        ru_3      = np.array([ax_x, ru_t[1] - 0.1, 0.0])
        chain_c_3 = np.array([ax_x, ca_t[1] + 0.1, 0.0])

        rc_primary   = _plain_line(ru_3, chain_c_3)
        n_off = np.array([0.13, 0.0, 0.0])
        rc_secondary = _plain_line(ru_3 + n_off, chain_c_3 + n_off)

        eth_c1_3 = cph_t + UP * 0.7 + RIGHT * 0.9
        eth_c2_3 = cb_t  + UP * 0.7 + RIGHT * 1.9
        eth_upper_3, eth_lower_3 = self._double_pair(eth_c1_3, eth_c2_3)

        tb1_tgt3 = _plain_line(chain_c_3, t1.get_center())

        # Collapse targets for the 2 bonds that BREAK: zero-length lines at
        # the old midpoint of each broken edge. They read as 'the bond
        # shrinks to nothing' rather than duplicating a destination.
        top_break_pt_3 = (ru_t + cph_t) / 2
        bot_break_pt_3 = (ca_t + cb_t) / 2
        top_break_3 = _plain_line(top_break_pt_3, top_break_pt_3)
        bot_break_3 = _plain_line(bot_break_pt_3, bot_break_pt_3)

        self.play(
            ru.animate.move_to(ru_3),
            c1a.animate.move_to(chain_c_3),
            ch.animate.move_to(eth_c1_3),
            c2a.animate.move_to(eth_c2_3),
            ph_lbl.animate.move_to(eth_c1_3 + UP * 0.4),
            l_lbl.animate.move_to(ru_3 + UP * 0.55),
            cl_lbl.animate.move_to(ru_3 + LEFT * 0.65),
            h2_left.animate.move_to(chain_c_3 + LEFT * 0.55),
            # KEEP 2 bonds -> primary line of each new double.
            Transform(cat_db[1], rc_primary),    # left (Ru-Ca) -> Ru=C primary
            Transform(alk_db[0], eth_upper_3),   # right (Cph-Cb) -> ethylene primary
            # BREAK 2 bonds -> collapse to their old midpoint.
            Transform(cat_db[0], top_break_3),   # top (Ru-Cph) breaks
            Transform(alk_db[1], bot_break_3),   # bot (Ca-Cb) breaks
            Transform(tb1, tb1_tgt3),
            # CREATE 2 new parallel lines (second line of each double).
            Create(rc_secondary),
            Create(eth_lower_3),
            run_time=1.7,
        )
        self.wait(0.35)

        # Drop the collapsed bond lines now that they've shrunk to a point.
        self.remove(cat_db[0], alk_db[1])

        # Ethylene flies off: the 2 C atoms + Ph label + BOTH ethylene lines.
        ethylene_group = VGroup(ch, c2a, ph_lbl, alk_db[0], eth_lower_3)
        self.play(ethylene_group.animate.shift(UP * 2.2 + RIGHT * 3.0),
                  run_time=1.0)
        self.remove(ethylene_group)
        self.wait(0.2)

        # ================= STEP 4 — [2+2] -> MCB II (one clean motion) =================
        self.set_step(4, "Ru=CH closes onto alkene 2",
                      header, indicator, positions)

        # MCB II ring center — fixed position, clear of HUD, clear of everything.
        ring2_center = np.array([0.5, -1.0, 0.0])
        ru2_t = ring2_center + LEFT * 0.7 + UP * 0.6
        ca2_t = ring2_center + RIGHT * 0.7 + UP * 0.6
        c3_t  = ring2_center + RIGHT * 0.7 + DOWN * 0.6
        c4_t  = ring2_center + LEFT * 0.7 + DOWN * 0.6

        # Tether loops around the RIGHT side of the ring, outside the orange circle.
        t1_2 = ca2_t + RIGHT * 1.1 + UP * 0.05
        t2_2 = ring2_center + RIGHT * 2.1
        t3_2 = c3_t + RIGHT * 1.1 + DOWN * 0.05

        top_tgt2   = _plain_line(ru2_t, ca2_t)
        left_tgt2  = _plain_line(c4_t,  ru2_t)
        right_tgt2 = _plain_line(ca2_t, c3_t)
        bot_tgt2   = _plain_line(c3_t,  c4_t)
        tb1_tgt2   = _plain_line(ca2_t, t1_2)
        tb2_tgt2   = _plain_line(t1_2,  t2_2)
        tb3_tgt2   = _plain_line(t2_2,  t3_2)
        tb4_tgt2   = _plain_line(t3_2,  c3_t)

        self.play(
            ru.animate.move_to(ru2_t),
            c1a.animate.move_to(ca2_t),
            c3a.animate.move_to(c3_t),
            c4a.animate.move_to(c4_t),
            t1.animate.move_to(t1_2),
            t2.animate.move_to(t2_2),
            t3.animate.move_to(t3_2),
            l_lbl.animate.move_to(ru2_t + UP * 1.2),
            cl_lbl.animate.move_to(ru2_t + LEFT * 1.2),
            h2_left.animate.move_to(ca2_t + UP * 1.2),
            h2_right.animate.move_to(c4_t + LEFT * 1.2),
            # Ru=c_a double bond -> top + left ring edges.
            Transform(cat_db[1],    top_tgt2),
            Transform(rc_secondary, left_tgt2),
            # c3=c4 double bond -> right + bot ring edges.
            Transform(alk2_db[0], right_tgt2),
            Transform(alk2_db[1], bot_tgt2),
            # Tether follows atom positions.
            Transform(tb1, tb1_tgt2),
            Transform(tb2, tb2_tgt2),
            Transform(tb3, tb3_tgt2),
            Transform(tb4, tb4_tgt2),
            run_time=1.9,
        )
        self.wait(0.35)

        ring2_hl_center = (ru2_t + ca2_t + c3_t + c4_t) / 4
        ring_highlight2 = Circle(radius=1.45, color=ORANGE, stroke_width=5)
        ring_highlight2.move_to(ring2_hl_center)
        rlbl2 = Text("metallacyclobutane II", font_size=22, color=ORANGE)
        rlbl2.next_to(ring_highlight2, DOWN, buff=0.35)
        self.play(Create(ring_highlight2), Write(rlbl2))
        self.wait(1.0)
        self.play(FadeOut(ring_highlight2), FadeOut(rlbl2))

        # ================= STEP 5 — Retro MCB II -> product + regen =================
        self.set_step(5, "Ring closes into cyclic alkene",
                      header, indicator, positions,
                      split=True, product_indicator=product_indicator,
                      endpoints=endpoints, product_dot=product_dot_hud)

        # Product = cyclopentene at lower-center.
        prod_center = np.array([-0.5, -1.7, 0.0])
        r_ring = 1.05
        pos = []
        for i in range(5):
            a = PI / 2 - 2 * PI * i / 5
            pos.append(prod_center + r_ring
                       * np.array([np.cos(a), np.sin(a), 0.0]))
        ca_p, c3_p, t3_p, t2_p, t1_p = pos

        pdb_primary   = _plain_line(ca_p, c3_p, color=YELLOW)
        pdb_secondary = _parallel_line(ca_p, c3_p, np.array([0.0, 0.12, 0.0]),
                                        color=YELLOW)

        # Regenerated Ru=CH2 parked at y=0 (vertical middle) — well below HUD.
        regen_ru = np.array([4.8, 0.0, 0.0])
        regen_ch = regen_ru + RIGHT * 0.7
        rgn_primary   = _plain_line(regen_ru, regen_ch)
        rgn_secondary = _parallel_line(regen_ru, regen_ch,
                                        np.array([0.0, 0.13, 0.0]))

        e_c3_t3 = _plain_line(c3_p, t3_p)
        e_t3_t2 = _plain_line(t3_p, t2_p)
        e_t2_t1 = _plain_line(t2_p, t1_p)
        e_t1_ca = _plain_line(t1_p, ca_p)

        # Collapse targets for the 2 bonds that BREAK in MCB II retro.
        # Top edge of MCB II = Ru-Ca (cat_db[1]); bot edge = C3-C4 (alk2_db[1]).
        top_break_pt_5 = (ru2_t + ca2_t) / 2
        bot_break_pt_5 = (c3_t + c4_t) / 2
        top_break_5 = _plain_line(top_break_pt_5, top_break_pt_5)
        bot_break_5 = _plain_line(bot_break_pt_5, bot_break_pt_5)

        self.play(
            c1a.animate.move_to(ca_p),
            c3a.animate.move_to(c3_p),
            t3.animate.move_to(t3_p),
            t2.animate.move_to(t2_p),
            t1.animate.move_to(t1_p),
            ru.animate.move_to(regen_ru),
            c4a.animate.move_to(regen_ch),
            l_lbl.animate.move_to(regen_ru + UP * 0.45),
            cl_lbl.animate.move_to(regen_ru + DOWN * 0.45),
            # H2 pushed higher so it sits clear of the green box border.
            h2_left.animate.move_to(ca_p + UP * 0.75),
            h2_right.animate.move_to(regen_ch + RIGHT * 0.4),
            # KEEP 2 bonds -> primary line of each new double.
            Transform(rc_secondary, rgn_primary),  # left (C4-Ru) -> regen Ru=C primary
            Transform(alk2_db[0], pdb_primary),    # right (Ca-C3) -> product C=C primary
            # BREAK 2 bonds -> collapse to their old midpoint.
            Transform(cat_db[1], top_break_5),     # top (Ru-Ca) breaks
            Transform(alk2_db[1], bot_break_5),    # bot (C3-C4) breaks
            # Tether follows the new ring.
            Transform(tb1, e_t1_ca),
            Transform(tb2, e_t2_t1),
            Transform(tb3, e_t3_t2),
            Transform(tb4, e_c3_t3),
            # CREATE 2 new parallel lines.
            Create(rgn_secondary),
            Create(pdb_secondary),
            run_time=2.0,
        )
        self.wait(0.5)

        # Drop the collapsed bond lines now that they've shrunk to a point.
        self.remove(cat_db[1], alk2_db[1])

        prod_lbl = Text("cyclic alkene", font_size=22, color=GREEN)
        prod_lbl.move_to(prod_center + DOWN * (r_ring + 0.5))
        # Regen catalyst name BELOW the catalyst (clear of HUD entirely).
        regen_lbl = Text("regenerated catalyst", font_size=18, color=PURPLE_B)
        regen_lbl.move_to(regen_ru + DOWN * 0.9)
        self.play(Write(prod_lbl), Write(regen_lbl))
        self.wait(0.4)

        # Tight green box around just the 5 ring carbons (H2 is above, OUTSIDE).
        ring_atoms = VGroup(c1a, c3a, t3, t2, t1)
        box = SurroundingRectangle(ring_atoms, color=GREEN, buff=0.15)

        banner = Text("Result: ring closed! Catalyst turns over.",
                      font_size=22, color=GREEN)
        banner.move_to(np.array([0.0, 3.25, 0.0]))
        self.play(Create(box), FadeIn(banner))
        self.wait(3.0)
        self.play(*[FadeOut(m) for m in self.mobjects])

    # ================= HUD =================

    def _double_pair(self, a, b, gap=0.12, color=WHITE, stroke_width=4):
        p1 = np.array(a, dtype=float)
        p2 = np.array(b, dtype=float)
        vec = p2 - p1
        L = float(np.linalg.norm(vec))
        if L < 1e-6:
            return (Line(p1, p2, color=color, stroke_width=stroke_width),
                    Line(p1, p2, color=color, stroke_width=stroke_width))
        norm = np.array([-vec[1], vec[0], 0.0])
        n = norm / np.linalg.norm(norm) * gap
        return (Line(p1 + n, p2 + n, color=color, stroke_width=stroke_width),
                Line(p1 - n, p2 - n, color=color, stroke_width=stroke_width))

    def build_overlay(self):
        """HUD cycle: shifted LEFT + DOWN so every label fits in-frame."""
        # LEFT (5.05 -> 4.7) and DOWN (2.40 -> 2.0).
        box_cx, box_cy = 4.7, 2.0
        w, h = 1.7, 1.2
        TL = np.array([box_cx - w / 2, box_cy + h / 2, 0.0])
        TR = np.array([box_cx + w / 2, box_cy + h / 2, 0.0])
        BR = np.array([box_cx + w / 2, box_cy - h / 2, 0.0])
        BL = np.array([box_cx - w / 2, box_cy - h / 2, 0.0])
        positions = [TL, TR, BR, BL, TL]

        def arr(a, b, color=GRAY_B, sw=2.2, tip=0.13):
            return Arrow(a, b, buff=0.14, color=color, stroke_width=sw,
                         tip_length=tip, max_tip_length_to_length_ratio=0.3)

        loop = VGroup(arr(TL, TR), arr(TR, BR), arr(BR, BL), arr(BL, TL))
        nodes = VGroup(*[Dot(p, color=GRAY_B, radius=0.05)
                         for p in [TL, TR, BR, BL]])

        # Entry arrow + 'diene' label + small blue pickup dot.
        entry_top = TL + UP * 0.6
        entry = arr(entry_top, TL, color=BLUE_C, sw=2.5)
        entry_lbl = Text("diene", font_size=18, color=BLUE_C)
        entry_lbl.move_to(entry_top + UP * 0.22)
        diene_dot_hud = Dot(entry_top + DOWN * 0.02,
                             color=BLUE, radius=0.05)

        # Exit arrow + 'product' label + green dropoff dot, bumped lower.
        exit_bot = BL + DOWN * 0.9
        exit_ar = arr(BL, exit_bot, color=GREEN_C, sw=2.5)
        exit_lbl = Text("product", font_size=16, color=GREEN_C)
        exit_lbl.move_to(exit_bot + DOWN * 0.22)
        product_dot_hud = Dot(exit_bot + UP * 0.02,
                               color=GREEN, radius=0.05)

        # C2H4 side arrow — pulled slightly IN so label stays in frame.
        eth_right = TR + RIGHT * 0.55
        eth_ar = arr(TR, eth_right, color=GRAY_C, sw=1.8, tip=0.09)
        eth_lbl = Text("C2H4", font_size=16, color=GRAY_C)
        eth_lbl.move_to(eth_right + RIGHT * 0.25)

        # Node labels — placed so HUD arrows don't cut through them.
        tl_lbl = Text("M=CHR", font_size=14, color=GRAY_B)
        tl_lbl.move_to(TL + LEFT * 0.55)
        tr_lbl = Text("MCB I", font_size=14, color=GRAY_B)
        tr_lbl.move_to(TR + UP * 0.28)
        br_lbl = Text("M=CH'", font_size=14, color=GRAY_B)
        br_lbl.move_to(BR + RIGHT * 0.55)
        # MCB II to the LEFT of BL (was below — exit arrow cut through it).
        bl_lbl = Text("MCB II", font_size=14, color=GRAY_B)
        bl_lbl.move_to(BL + LEFT * 0.55)

        cycle_group = VGroup(
            loop, entry, exit_ar, eth_ar, nodes,
            entry_lbl, exit_lbl, eth_lbl,
            tl_lbl, tr_lbl, br_lbl, bl_lbl,
        )

        # SMALLER indicator so it doesn't overflow the HUD cells.
        indicator = Circle(radius=0.12, color=YELLOW, stroke_width=3)
        indicator.set_fill(YELLOW, opacity=0)
        product_indicator = Circle(radius=0.12, color=GREEN_C, stroke_width=3)
        product_indicator.set_fill(GREEN_C, opacity=0)
        product_indicator.move_to(BL).set_opacity(0)

        header = self._build_header(
            1, self.PHASES[1], "Ru catalyst approaches alkene 1")

        return (header, cycle_group, indicator, product_indicator,
                positions, (TL, TR, BR, BL, exit_bot),
                (diene_dot_hud, product_dot_hud))

    def _build_header(self, num, phase, desc):
        top = Text(f"Step {num}: {phase}", font_size=22,
                   weight=BOLD, color=YELLOW)
        bot = Text(desc, font_size=16, color=WHITE)
        grp = VGroup(top, bot).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        grp.to_corner(UL, buff=0.35)
        return grp

    def set_step(self, num, desc, header, indicator, positions,
                 split=False, product_indicator=None, endpoints=None,
                 indicator_pre_move=False, indicator_target=None,
                 product_dot=None):
        phase = self.PHASES.get(num, "")
        new_header = self._build_header(num, phase, desc)

        if indicator_pre_move:
            self.play(
                Transform(header, new_header),
                indicator.animate
                    .set_color(YELLOW)
                    .set_stroke(YELLOW, width=3)
                    .move_to(indicator_target),
                run_time=1.3,
            )
            return

        if not split:
            self.play(
                Transform(header, new_header),
                indicator.animate.move_to(positions[num - 1]),
                run_time=0.7,
            )
            return

        # Step 5 split: top / bottom halves; Create fills the missing halves.
        assert endpoints is not None
        TL, TR, BR, BL, _ = endpoints
        r = 0.12  # matches shrunken indicator

        top_half = Arc(radius=r, start_angle=0, angle=PI,
                       arc_center=BL, color=YELLOW, stroke_width=3)
        bot_half = Arc(radius=r, start_angle=PI, angle=PI,
                       arc_center=BL, color=YELLOW, stroke_width=3)

        prod_pos = (product_dot.get_center() if product_dot is not None
                    else BL + DOWN * 1.5)

        top_fill = Arc(radius=r, start_angle=PI, angle=PI,
                       arc_center=TL, color=YELLOW, stroke_width=3)
        bot_fill = Arc(radius=r, start_angle=0, angle=PI,
                       arc_center=prod_pos, color=GREEN_C, stroke_width=3)

        self.remove(indicator)
        self.add(top_half, bot_half)

        self.play(
            Transform(header, new_header),
            top_half.animate.shift(TL - BL),
            bot_half.animate
                .shift(prod_pos - BL)
                .set_color(GREEN_C)
                .set_stroke(GREEN_C, width=3),
            Create(top_fill),
            Create(bot_fill),
            run_time=1.6,
        )

    # ================= BUILDERS =================

    def build_diene(self):
        c1 = atom("C", color=GRAY).shift(LEFT * 4)
        c2 = atom("C", color=GRAY).shift(LEFT * 3)
        h_left = _ext_label("H2", font_size=20, color=WHITE).next_to(c1, LEFT, buff=0.32)
        db_left = bond(c1, c2, double=True)
        left_alk = VGroup(c1, c2, h_left, db_left)

        t1 = atom("C", color=GRAY).shift(LEFT * 1.5 + DOWN * 0.4)
        t2 = atom("C", color=GRAY).shift(DOWN * 0.6)
        t3 = atom("C", color=GRAY).shift(RIGHT * 1.5 + DOWN * 0.4)
        tb1 = bond(c2, t1)
        tb2 = bond(t1, t2)
        tb3 = bond(t2, t3)

        c3 = atom("C", color=GRAY).shift(RIGHT * 3)
        c4 = atom("C", color=GRAY).shift(RIGHT * 4)
        h_right = _ext_label("H2", font_size=20, color=WHITE).next_to(c4, RIGHT, buff=0.32)
        db_right = bond(c3, c4, double=True)
        tb4 = bond(t3, c3)

        tether = VGroup(tb1, t1, tb2, t2, tb3, t3, tb4)
        right_alk = VGroup(c3, c4, h_right, db_right)
        return VGroup(left_alk, tether, right_alk)

    def build_catalyst(self):
        ru = atom("Ru", color=PURPLE, radius=0.3)
        ch = atom("C", color=GRAY).next_to(ru, RIGHT, buff=0.55)
        ph = _ext_label("Ph", font_size=20, color=WHITE).next_to(ch, RIGHT, buff=0.22)
        db = bond(ru, ch, double=True)
        l1 = _ext_label("L", font_size=18, color=GRAY_B).next_to(ru, UP, buff=0.28)
        l2 = _ext_label("Cl", font_size=16, color=GREEN).next_to(ru, DOWN, buff=0.28)
        return VGroup(ru, db, ch, ph, l1, l2)
