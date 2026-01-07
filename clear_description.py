layer = iface.activeLayer()

import re

for feature in layer.getFeatures():
    raw_desc = str(feature['description'])

    # Удалим все <img ...> теги
    raw_desc = re.sub(r'<img[^>]*>', '', raw_desc)

    # Удалим все <br> теги
    cleaned = re.sub(r'<br\s*/?>', '\n', raw_desc)

    # Извлекаем все строки, содержащие ссылки
    urls = re.findall(r'https?://[^\s<>\n"]+', cleaned)

    # Берем первую ссылку, если есть
    final_desc = urls[0] if urls else ''

    layer.changeAttributeValue(feature.id(), layer.fields().indexOf('description'), final_desc)