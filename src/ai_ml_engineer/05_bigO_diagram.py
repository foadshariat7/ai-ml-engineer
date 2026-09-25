import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.widgets import Slider, RadioButtons


# ---------------------------------------------------------
# Big-O functions
# ---------------------------------------------------------

def constant(n):
    return np.ones_like(n, dtype=float)


def logarithmic(n):
    return np.log2(n)


def linear(n):
    return n


def n_log_n(n):
    return n * np.log2(n)


def quadratic(n):
    return n ** 2


def exponential(n):
    return 2.0 ** n


def factorial_values(n):
    return np.array(
        [float(math.factorial(int(x))) for x in n]
    )


# ---------------------------------------------------------
# Input range
# ---------------------------------------------------------

x = np.arange(1, 65)

functions = {
    "O(1)": constant(x),
    "O(log n)": logarithmic(x),
    "O(n)": linear(x),
    "O(n log n)": n_log_n(x),
    "O(n²)": quadratic(x),
    "O(2ⁿ)": exponential(x),
    "O(n!)": factorial_values(x),
}


# ---------------------------------------------------------
# Figure
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(12, 7))

# Make room for slider and controls
plt.subplots_adjust(
    left=0.10,
    right=0.82,
    bottom=0.27,
    top=0.88
)


# ---------------------------------------------------------
# Draw lines
# ---------------------------------------------------------

lines = {}

for label, y in functions.items():
    line, = ax.plot(
        x,
        y,
        linewidth=2.5,
        label=label
    )

    lines[label] = line


# ---------------------------------------------------------
# Initial n
# ---------------------------------------------------------

initial_n = 16


# Vertical selected-n line
selected_line = ax.axvline(
    initial_n,
    linestyle="--",
    linewidth=1.5
)


# Selected points
selected_points = {}

for label, line in lines.items():

    y_value = line.get_ydata()[initial_n - 1]

    point, = ax.plot(
        initial_n,
        y_value,
        "o",
        markersize=7
    )

    # Keep same color as line
    point.set_color(line.get_color())

    selected_points[label] = point


# ---------------------------------------------------------
# Chart labels
# ---------------------------------------------------------

ax.set_title(
    "Big-O Growth Comparison",
    fontsize=18,
    fontweight="bold"
)

ax.set_xlabel(
    "Input size n",
    fontsize=13,
    fontweight="bold"
)

ax.set_ylabel(
    "Operations",
    fontsize=13,
    fontweight="bold"
)

ax.grid(
    True,
    alpha=0.25
)


# Start in linear mode
ax.set_xlim(1, 64)
ax.set_ylim(0, 300)


# ---------------------------------------------------------
# Legend
# ---------------------------------------------------------

legend = ax.legend(
    loc="upper left",
    ncol=2,
    fontsize=10
)

# Make legend items clickable
legend_lines = {}

for legend_line, original_line in zip(
    legend.get_lines(),
    lines.values()
):
    legend_line.set_picker(True)
    legend_line.set_pickradius(10)

    legend_lines[legend_line] = original_line


# ---------------------------------------------------------
# Slider
# ---------------------------------------------------------

slider_ax = plt.axes(
    [0.15, 0.12, 0.58, 0.04]
)

n_slider = Slider(
    ax=slider_ax,
    label="n",
    valmin=1,
    valmax=64,
    valinit=initial_n,
    valstep=1
)


# ---------------------------------------------------------
# Linear / Log scale selector
# ---------------------------------------------------------

radio_ax = plt.axes(
    [0.84, 0.55, 0.13, 0.15]
)

scale_selector = RadioButtons(
    radio_ax,
    ("Linear", "Log"),
    active=0
)


# ---------------------------------------------------------
# Text displaying current values
# ---------------------------------------------------------

value_text = fig.text(
    0.10,
    0.02,
    "",
    fontsize=10
)


# ---------------------------------------------------------
# Format large values
# ---------------------------------------------------------

def format_number(value):

    if value < 1_000_000:
        return f"{value:,.2f}"

    return f"{value:.3e}"


# ---------------------------------------------------------
# Update displayed values
# ---------------------------------------------------------

def update_text(n):

    values = {
        "O(1)": 1,
        "O(log n)": math.log2(n),
        "O(n)": n,
        "O(n log n)": n * math.log2(n),
        "O(n²)": n ** 2,
        "O(2ⁿ)": 2 ** n,
        "O(n!)": math.factorial(n),
    }

    text = (
        f"n = {n}     "
        f"O(1) = {format_number(values['O(1)'])}     "
        f"O(log n) = {format_number(values['O(log n)'])}     "
        f"O(n) = {format_number(values['O(n)'])}\n"
        f"O(n log n) = {format_number(values['O(n log n)'])}     "
        f"O(n²) = {format_number(values['O(n²)'])}     "
        f"O(2ⁿ) = {format_number(values['O(2ⁿ)'])}     "
        f"O(n!) = {format_number(values['O(n!)'])}"
    )

    value_text.set_text(text)


update_text(initial_n)


# ---------------------------------------------------------
# Slider callback
# ---------------------------------------------------------

def update_slider(value):

    n = int(n_slider.val)

    # Move vertical line
    selected_line.set_xdata([n, n])

    # Move selected dots
    for label, line in lines.items():

        y_value = line.get_ydata()[n - 1]

        selected_points[label].set_data(
            [n],
            [y_value]
        )

    update_text(n)

    fig.canvas.draw_idle()


n_slider.on_changed(update_slider)


# ---------------------------------------------------------
# Scale callback
# ---------------------------------------------------------

def change_scale(label):

    if label == "Linear":

        ax.set_yscale("linear")

        # Intentionally limited so smaller
        # growth functions remain visible
        ax.set_ylim(0, 300)

    else:

        ax.set_yscale("log")

        max_factorial = float(math.factorial(64))

        ax.set_ylim(
            1,
            max_factorial * 10
        )

    fig.canvas.draw_idle()


scale_selector.on_clicked(change_scale)


# ---------------------------------------------------------
# Click legend to hide/show curves
# ---------------------------------------------------------

def legend_click(event):

    legend_line = event.artist

    if legend_line not in legend_lines:
        return

    original_line = legend_lines[legend_line]

    visible = not original_line.get_visible()

    original_line.set_visible(visible)

    label = original_line.get_label()

    selected_points[label].set_visible(visible)

    # Fade legend item when hidden
    legend_line.set_alpha(
        1.0 if visible else 0.25
    )

    fig.canvas.draw_idle()


fig.canvas.mpl_connect(
    "pick_event",
    legend_click
)


# ---------------------------------------------------------
# Show
# ---------------------------------------------------------

plt.show()