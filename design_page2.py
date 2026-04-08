from PIL import Image, ImageDraw, ImageFont
import os

# 設定
WIDTH = 1920
HEIGHT = 1080
OUTPUT_PATH = 'page2-designed-bg.png'

# 顏色
COLORS = {
    'navy': '#1A1A5E',
    'pink': '#FF6B9D',
    'light_pink': '#FFB3CC',
    'light_pink_bg': '#FFF0F5',
    'white': '#FFFFFF',
    'gray': '#8E8E9A',
}

# 創建圖片
img = Image.new('RGB', (WIDTH, HEIGHT), color=COLORS['light_pink_bg'])
draw = ImageDraw.Draw(img)

# 添加漸層背景
for y in range(HEIGHT):
    # 從上到下的漸變
    ratio = y / HEIGHT
    r = int(255)
    g = int(240 * (1 - ratio * 0.1))
    b = int(245 * (1 - ratio * 0.05))
    
    # 添加左右漸變（中間亮）
    x_ratio = abs(WIDTH/2 - WIDTH/2) / (WIDTH/2)
    
    for x in range(WIDTH):
        x_dist = abs(WIDTH/2 - x) / (WIDTH/2)
        brightness = 1 - (x_dist * 0.1)
        
        rr = int(r * brightness)
        gg = int(g * brightness)
        bb = int(b * brightness)
        
        draw.point((x, y), fill=(rr, gg, bb))

# 添加裝飾元素 - 左上角圓形
draw.ellipse([(50, 50), (200, 200)], fill=COLORS['pink'], outline=None)
draw.ellipse([(70, 70), (180, 180)], fill=COLORS['light_pink_bg'], outline=None)

# 添加裝飾元素 - 右下角圓形
draw.ellipse([(WIDTH-200, HEIGHT-200), (WIDTH-50, HEIGHT-50)], fill=COLORS['navy'], outline=None)
draw.ellipse([(WIDTH-180, HEIGHT-180), (WIDTH-70, HEIGHT-70)], fill=COLORS['light_pink_bg'], outline=None)

# 添加裝飾線條
for i in range(5):
    y_pos = 300 + i * 150
    alpha = int(30 * (1 - i/5))
    draw.line([(100, y_pos), (WIDTH-100, y_pos)], fill=(255, 107, 157, alpha), width=2)

# 保存
img.save(OUTPUT_PATH, 'PNG')
print(f'✅ 設計完成：{OUTPUT_PATH}')
print(f'尺寸：{WIDTH}x{HEIGHT}')
