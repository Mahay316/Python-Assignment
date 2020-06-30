with open('a.html', 'r', encoding='utf-8') as src:
    with open('b.js', 'w', encoding='utf-8') as dst:
        for line in src:
            dst.write(f'content += \'{line.strip()}\';\n')
