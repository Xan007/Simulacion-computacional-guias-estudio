# -*- coding: utf-8 -*-
import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

guias_dir = r'C:\Users\sierr\Documents\Simulacion-computacional-estudio\guias_estudio'

for fname in sorted(os.listdir(guias_dir)):
    if fname.endswith('.md'):
        path = os.path.join(guias_dir, fname)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for ANSI escape sequences
        ansi = re.findall(r'\[\d+;\d+u|\x1b|\\x1b', content)
        if ansi:
            print(f'[!] ANSI escape found in {fname}: {ansi}')
        
        # Check for nested $ or $$ inside math blocks
        # Display math $$ ... $$
        display_maths = re.findall(r'\$\$([\s\S]*?)\$\$', content)
        for dm in display_maths:
            if '$' in dm:
                print(f'[!] Inner $ found inside $$ in {fname}: {repr(dm[:100])}')
        
        # Check for unclosed $ or $$
        dollar_count = content.count('$')
        if dollar_count % 2 != 0:
            print(f'[!] Odd number of $ in {fname}: count = {dollar_count}')

