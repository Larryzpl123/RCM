import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.axis('off')
fig.patch.set_facecolor('#FAFAFA')

title = "Ring-Closing Metathesis (RCM)\nCatalytic Cycle"
ax.text(0, 5.4, title, ha='center', va='center', fontsize=18,
        fontweight='bold', color='#1a1a2e', family='sans-serif')

# --- Cycle layout (6 nodes around a circle) ---
n_steps = 6
radius = 3.5
angles = [90, 30, -30, -90, -150, 150]  # degrees, starting from top
angles_rad = [np.radians(a) for a in angles]

positions = [(radius * np.cos(a), radius * np.sin(a)) for a in angles_rad]

# Step labels (short chemical descriptions)
step_labels = [
    "[Ru]=CHR\n(Grubbs Catalyst)",
    "[Ru]=CH₂\n+\nDiene Substrate",
    "Metallacyclo-\nbutane\n(1st [2+2])",
    "[Ru]=CH–(chain)–CH=CH₂\n(New Carbene)",
    "Metallacyclo-\nbutane\n(Intramolecular\n2nd [2+2])",
    "Cyclic Alkene\nProduct\n+ [Ru]=CH₂",
]

# Colors for each node
colors = [
    '#4361ee',  # catalyst
    '#7209b7',  # coordination
    '#e63946',  # metallacyclobutane 1
    '#f77f00',  # new carbene
    '#e63946',  # metallacyclobutane 2
    '#2a9d8f',  # product
]

# Arrow labels between steps
arrow_labels = [
    "Coordination\nof diene",
    "[2+2]\nCycloaddition",
    "[2+2]\nCycloreversion",
    "Intramolecular\n[2+2] cycloaddition",
    "[2+2]\nCycloreversion",
    "Catalyst\nregeneration",
]

# Step numbers
step_nums = ["1", "2", "3", "4", "5", "6"]

# Draw nodes
box_w, box_h = 2.2, 1.6
for i, (x, y) in enumerate(positions):
    bbox = mpatches.FancyBboxPatch(
        (x - box_w/2, y - box_h/2), box_w, box_h,
        boxstyle="round,pad=0.15",
        facecolor=colors[i], edgecolor='white',
        linewidth=2, alpha=0.88
    )
    ax.add_patch(bbox)
    ax.text(x, y, step_labels[i], ha='center', va='center',
            fontsize=9, color='white', fontweight='bold',
            family='monospace', linespacing=1.3)
    # Step number badge
    badge_x = x - box_w/2 + 0.18
    badge_y = y + box_h/2 - 0.18
    circle = plt.Circle((badge_x, badge_y), 0.18, color='white', zorder=5)
    ax.add_patch(circle)
    ax.text(badge_x, badge_y, step_nums[i], ha='center', va='center',
            fontsize=8, fontweight='bold', color=colors[i], zorder=6)

# Draw arrows between nodes
for i in range(n_steps):
    j = (i + 1) % n_steps
    x1, y1 = positions[i]
    x2, y2 = positions[j]

    # Shorten arrows so they don't overlap boxes
    dx, dy = x2 - x1, y2 - y1
    dist = np.sqrt(dx**2 + dy**2)
    shrink = 1.25
    sx1 = x1 + shrink * dx / dist
    sy1 = y1 + shrink * dy / dist
    sx2 = x2 - shrink * dx / dist
    sy2 = y2 - shrink * dy / dist

    ax.annotate(
        '', xy=(sx2, sy2), xytext=(sx1, sy1),
        arrowprops=dict(
            arrowstyle='->', color='#333', lw=2.0,
            connectionstyle='arc3,rad=0.15',
            shrinkA=0, shrinkB=0
        )
    )

    # Place arrow label at midpoint, offset outward
    mx = (sx1 + sx2) / 2
    my = (sy1 + sy2) / 2
    # Offset outward from center
    omx = mx - 0
    omy = my - 0
    odist = np.sqrt(omx**2 + omy**2) + 1e-9
    offset = 0.65
    lx = mx + offset * omx / odist
    ly = my + offset * omy / odist

    ax.text(lx, ly, arrow_labels[i], ha='center', va='center',
            fontsize=7.5, color='#555', fontstyle='italic',
            family='sans-serif', linespacing=1.2,
            bbox=dict(boxstyle='round,pad=0.2', fc='#FAFAFA', ec='none', alpha=0.85))

# Center annotation
ax.text(0, 0, "CH₂=CH₂\n(ethylene\nbyproduct\nreleased)",
        ha='center', va='center', fontsize=10, color='#888',
        fontstyle='italic', family='sans-serif',
        bbox=dict(boxstyle='round,pad=0.4', fc='#fff3cd', ec='#ffc107', lw=1.5))

# Bottom legend
legend_text = (
    "Catalyst: Grubbs 1st or 2nd gen (Ru-based)  •  "
    "Key: two [2+2] cycloaddition / cycloreversion pairs close the ring"
)
ax.text(0, -5.5, legend_text, ha='center', va='center',
        fontsize=8.5, color='#666', family='sans-serif')

plt.tight_layout()
plt.savefig('/home/claude/rcm_cycle.png', dpi=200, bbox_inches='tight',
            facecolor='#FAFAFA')
print("Saved rcm_cycle.png")
