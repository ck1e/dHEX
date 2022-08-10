from django.shortcuts import render
from django.http import HttpResponseRedirect
from PIL import Image


def main(request, template_name):
    if request.method == 'GET':
        return render(request, template_name)

    if request.method == 'POST':
        if request.FILES:
            img = Image.open(request.FILES['file-img'])
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            colors = []
            for req in request.POST:
                if 'custom-color' in req:
                    colors.append(hex_to_rgb(request.POST[req]))

            return render(request, 'elements.html', {
                    'colors': count_pixel(img.getcolors(256000000), colors)
            })
        else:
            return render(request, template_name)


def count_pixel(colors, search_colors):
    result = {}
    for color in colors:
        if color[1] in search_colors:
            result[rgb_to_hex(color[1])] = color[0]

    return result


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % (rgb[0], rgb[1], rgb[2])
