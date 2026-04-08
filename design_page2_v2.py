from PIL import Image, ImageDraw, ImageFont
import math

# 設定
WIDTH = 1920
HEIGHT = 1080
OUTPUT_PATH = 'page2-bg-professional.png'

# 顏色
COLORS = {
    'navy': '#1A1A5E',
    'navy_light': '#2A2A7E',
    'pink': '#FF6B9D',
    'light_pink': '#FFB3CC',
    'light_pink_bg': '#FFF0F5',
    'white': '#FFFFFF',
}

# 創建圖片
img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS['light_pink_bg'])
draw = ImageDraw.Draw(img)

# 1. 主漸層背景（左上深藍到右下粉白）
for y in range(HEIGHT):
    for x in range(WIDTH):
        # 對角線漸變
        ratio = (x + y) / (WIDTH + HEIGHT)
        
        # 深藍到淺粉 gradient
        r = int(26 * (1-ratio) + 255 * ratio * 0.2 + 255 * 0.8 * ratio)
        g = int(26 * (1-ratio) + 240 * ratio * 0.3 + 240 * 0.7 * ratio)
        b = int(94 * (1-ratio) + 126 * ratio * 0.4 + 245 * 0.6 * ratio)
        
        draw.point((x, y), fill=(r, g, b))

# 2. 網格線（細緻的專業感）
grid_spacing = 60
for i in range(0, WIDTH, grid_spacing):
    alpha = 25
    draw.line([(i, 0), (i, HEIGHT)], fill=(255, 255, 255, alpha), width=1)
for j in range(0, HEIGHT, grid_spacing):
    alpha = 25
    draw.line([(0, j), (WIDTH, j)], fill=(255, 255, 255, alpha), width=1)

# 3. 裝飾性幾何圖形 - 左上
draw.line([(20, 20), (150, 20)], fill=COLORS['pink'], width=3)
draw.line([(20, 20), (20, 150)], fill=COLORS['pink'], width=3)
draw.line([(20, 150), (60, 150)], fill=COLORS['pink'], width=3)
draw.line([(150, 20), (150, 60)], fill=COLORS['pink'], width=3)

# 4. 裝飾性幾何圖形 - 右下
draw.line([(WIDTH-20, HEIGHT-20), (WIDTH-150, HEIGHT-20)], fill=COLORS['navy'], width=3)
draw.line([(WIDTH-20, HEIGHT-20), (WIDTH-20, HEIGHT-150)], fill=COLORS['navy'], width=3)
draw.line([(WIDTH-150, HEIGHT-20), (WIDTH-150, HEIGHT-60)], fill=COLORS['navy'], width=3)
draw.line([(WIDTH-20, HEIGHT-150), (WIDTH-60, HEIGHT-150)], fill=COLORS['navy'], width=3)

# 5. 對角線光效（增加層次）
for i in range(0, WIDTH + HEIGHT, 4):
    x1 = max(0, i - HEIGHT)
    y1 = min(HEIGHT, i)
    x2 = min(WIDTH, i)
    y2 = max(0, i - WIDTH)
    alpha = int(15 * math.sin(i / 200))
    if alpha > 0:
        draw.line([(x1, y1), (x2, y2)], fill=(255, 255, 255, alpha), width=1)

# 6. 底部陰影效果（增加深度）
for i in range(0, 100):
    y = HEIGHT - i
    alpha = int(i / 3)
    draw.line([(0, y), (WIDTH, y)], fill=(26, 26, 94, alpha), width=1)

# 7. 右上角小裝飾點
for i in range(5):
    x = WIDTH - 40 - (i * 25)
    y = 40 + (i * 15)
    r = 4
    draw.ellipse([(x-r, y-r), (x+r, y+r)], fill=COLORS['pink'], outline=None)

# 保存
img.save(OUTPUT_PATH, 'PNG')
print(f'✅ 專業商務風設計完成：{OUTPUT_PATH}')
print(f'尺寸：{WIDTH}x{HEIGHT}')
