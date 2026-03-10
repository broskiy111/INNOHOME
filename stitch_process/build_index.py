import os

homepage_html = open('homepage_updated_services_flow/code.html', encoding='utf-8').read()
services_html = open('services_updated_directions/code.html', encoding='utf-8').read()
projects_html = open('projects_cinematic_dark/code.html', encoding='utf-8').read()
contacts_html = open('contacts_atmospheric_architectural_theme/code.html', encoding='utf-8').read()

def extract_tag(html, tag):
    start = html.find(f'<{tag}')
    if start == -1: return ''
    end = html.find(f'</{tag}>', start)
    if end == -1: return ''
    return html[start:end+len(f'</{tag}>')]

main_home = extract_tag(homepage_html, 'main')
main_services = extract_tag(services_html, 'main')
main_projects = extract_tag(projects_html, 'main')
main_contacts = extract_tag(contacts_html, 'main')
footer = extract_tag(homepage_html, 'footer')

output = f"""<!DOCTYPE html>
<html class="dark" lang="en">
<head>
    <meta charset="utf-8" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <title>InnoHome Architecture</title>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;300;400;500;700;900&display=swap" rel="stylesheet" />
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
    <script id="tailwind-config">
        tailwind.config = {{
            darkMode: "class",
            theme: {{
                extend: {{
                    colors: {{
                        "primary": "#e6e6e6",
                        "background-light": "#f7f7f7",
                        "background-dark": "#0a0a0a",
                    }},
                    fontFamily: {{
                        "display": ["Inter", "sans-serif"]
                    }},
                    borderRadius: {{ "DEFAULT": "0.125rem", "lg": "0.25rem", "xl": "0.5rem", "full": "0.75rem" }},
                }},
            }},
        }}
    </script>
    <style>
        html {{ scroll-behavior: smooth; }}
        .atmospheric-gradient {{ background: radial-gradient(circle at 50% -20%, #262626 0%, #0a0a0a 70%); }}
        .glass-panel {{ background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255, 255, 255, 0.05); }}
        .text-kern-wide {{ letter-spacing: 0.3em; }}
        .grayscale-hover {{ filter: grayscale(100%); transition: filter 0.3s ease; }}
        .grayscale-hover:hover {{ filter: grayscale(0%); }}
    </style>
</head>
<body class="bg-background-light dark:bg-background-dark font-display text-slate-900 dark:text-slate-100 selection:bg-primary selection:text-background-dark">
    <div class="relative min-h-screen flex flex-col atmospheric-gradient">
        <!-- Navigation -->
        <header class="fixed top-0 z-50 w-full border-b border-white/10 bg-background-dark/80 backdrop-blur-md">
            <div class="mx-auto flex max-w-7xl items-center justify-between px-6 py-4 lg:px-10">
                <div class="flex items-center gap-3">
                    <div class="text-primary">
                        <span class="material-symbols-outlined text-3xl">polyline</span>
                    </div>
                    <h2 class="text-xl font-bold tracking-tight text-white uppercase">InnoHome</h2>
                </div>
                <nav class="hidden md:flex items-center gap-10">
                    <a class="text-sm font-medium text-slate-400 hover:text-white transition-colors" href="#home">Home</a>
                    <a class="text-sm font-medium text-slate-400 hover:text-white transition-colors" href="#services">Services</a>
                    <a class="text-sm font-medium text-slate-400 hover:text-white transition-colors" href="#portfolio">Portfolio</a>
                    <a class="text-sm font-medium text-slate-400 hover:text-white transition-colors" href="#contact">Contact</a>
                </nav>
                <div class="flex items-center gap-4">
                    <a href="#contact">
                        <button class="hidden sm:flex min-w-[120px] items-center justify-center rounded bg-primary px-5 py-2 text-sm font-bold text-background-dark hover:bg-white transition-all">
                            Get Started
                        </button>
                    </a>
                </div>
            </div>
        </header>

        <div id="home">{main_home}</div>
        <div id="services" class="scroll-mt-24 bg-background-dark">{main_services}</div>
        <div id="portfolio" class="scroll-mt-24 bg-background-dark">{main_projects}</div>
        <div id="contact" class="scroll-mt-24 bg-background-dark">{main_contacts}</div>
        
        {footer}
    </div>
</body>
</html>
"""

open('index.html', 'w', encoding='utf-8').write(output)
print("index.html created!")
