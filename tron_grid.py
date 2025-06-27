import numpy as np
from PIL import Image, ImageDraw
import imageio

# Video parameters
WIDTH, HEIGHT = 1280, 720
DURATION = 10    # seconds
FPS = 30
FRAMES = DURATION * FPS

# Grid styling
HORIZON_Y    = (HEIGHT // 2) + 30
LINE_RGB     = np.array([0, 187, 187], dtype=np.uint8)  # #00BBBB
BG_COLOR     = (0, 20, 24)

# Horizontal & vertical grid setup
NUM_H        = 8
h_rel        = np.linspace(0, 1, NUM_H)
NUM_V        = 8
horizon_vx   = np.linspace(WIDTH*0.1, WIDTH*0.9, NUM_V)
start_xs     = np.linspace(-WIDTH*0.3, WIDTH*1.3, NUM_V)

# Build a thin glow band ±Glow_Width around the horizon
Glow_Width   = 100   # pixels above and below horizon
band_height  = 2*Glow_Width + 1

max_alpha = 60
alphas       = np.concatenate([
    np.linspace(0, 60, Glow_Width, dtype=np.uint8),
    [60],
    np.linspace(60, 0, Glow_Width, dtype=np.uint8)
])
glow_band    = np.zeros((band_height, WIDTH, 4), dtype=np.uint8)
glow_band[..., 0] = LINE_RGB[0]
glow_band[..., 1] = LINE_RGB[1]
glow_band[..., 2] = LINE_RGB[2]
glow_band[..., 3] = alphas[:, None]

writer = imageio.get_writer('tron_grid.mp4', fps=FPS, codec='libx264')

for f in range(FRAMES):
    t = f / (FRAMES - 1) * 2
    img = Image.new('RGB', (WIDTH, HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(img)

    min_brightness = 0.4  # 20% of LINE_RGB

    # 1) Horizontal grid lines
    for r in h_rel:
        y_norm   = (r + t) % 1.0
        y        = int(HORIZON_Y + y_norm * (HEIGHT - HORIZON_Y))
        thickness= int(1 + 3 * (1 - y_norm))
        # color    = tuple((LINE_RGB * y_norm).astype(np.uint8))
        brightness = y_norm * (1 - min_brightness) + min_brightness
        color = tuple((LINE_RGB * brightness).astype(np.uint8))
        draw.line([(0, y), (WIDTH, y)], fill=color, width=thickness)

    # 2) Vertical grid lines (fixed endpoints, half-faded)
    for i in range(NUM_V):
        x0       = start_xs[i]
        vx       = horizon_vx[i]
        avg_a    = 0.8
        color_v  = tuple((LINE_RGB * avg_a).astype(np.uint8))
        draw.line([(x0, HEIGHT), (vx, HORIZON_Y)], fill=color_v, width=1)

    # 3) Composite the thin glow band at the horizon
    glow_img   = Image.fromarray(glow_band, mode='RGBA')
    canvas_rgba= img.convert('RGBA')
    # Position so that the glow band centers on HORIZON_Y
    canvas_rgba.alpha_composite(glow_img, (0, HORIZON_Y - Glow_Width))

    writer.append_data(np.array(canvas_rgba.convert('RGB')))

writer.close()
print("tron_grid.mp4 generated!")
