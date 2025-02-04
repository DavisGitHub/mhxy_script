import os
from PIL import Image, ImageDraw, ImageFont

def create_custom_icon():
    # 创建必要的目录
    if not os.path.exists('src/assets'):
        os.makedirs('src/assets')
    
    if not os.path.exists('src/assets/icon.iconset'):
        os.makedirs('src/assets/icon.iconset')

    # 创建基础图标（1024x1024）
    size = 1024
    image = Image.new('RGB', (size, size), color='#2B2B2B')
    draw = ImageDraw.Draw(image)
    
    # 绘制圆形背景
    circle_bbox = (50, 50, size-50, size-50)
    draw.ellipse(circle_bbox, fill='#4A90E2')
    
    # 添加文字
    try:
        # 使用默认字体
        font = ImageFont.load_default()
        text = "梦"
        # 计算文字位置使其居中
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (size - text_width) // 2
        y = (size - text_height) // 2
        # 放大文字以使其更清晰
        draw.text((x, y), text, fill='white', font=font, size=800)
    except Exception as e:
        print(f"无法绘制文字: {e}")
    
    # 保存不同尺寸的图标
    sizes = [16, 32, 64, 128, 256, 512, 1024]
    
    for s in sizes:
        resized = image.resize((s, s), Image.Resampling.LANCZOS)
        resized.save(f'src/assets/icon.iconset/icon_{s}x{s}.png')
        # 创建 @2x 版本
        if s < 512:
            resized = image.resize((s*2, s*2), Image.Resampling.LANCZOS)
            resized.save(f'src/assets/icon.iconset/icon_{s}x{s}@2x.png')

if __name__ == '__main__':
    create_custom_icon()