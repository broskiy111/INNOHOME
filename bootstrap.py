import re
import codecs

def setup_files():
    with codecs.open("index.html", "r", "utf-8") as f:
        html = f.read()

    # The nav block to replace:
    # <nav class="hidden md:flex items-center gap-10"> ... </nav>
    # <div class="flex items-center gap-4"> ... </div>
    
    # Let's find the header end. The header ends at </header>
    header_match = re.search(r'(<header.*?>.*?</header>)', html, re.DOTALL)
    header_html = header_match.group(1)

    def nav_replacement(active):
        h = "text-white underline underline-offset-8 decoration-primary" if active == 'index' else "text-slate-400 hover:text-white"
        s = "text-white underline underline-offset-8 decoration-primary" if active == 'services' else "text-slate-400 hover:text-white"
        e = "text-white underline underline-offset-8 decoration-primary" if active == 'engineering' else "text-slate-400 hover:text-white"
        p = "text-white underline underline-offset-8 decoration-primary" if active == 'portfolio' else "text-slate-400 hover:text-white"

        return f'''<nav class="hidden md:flex items-center gap-10">
                    <a class="text-sm font-medium {h} transition-colors" href="index.html">Главная</a>
                    <a class="text-sm font-medium {s} transition-colors" href="services.html">Услуги</a>
                    <a class="text-sm font-medium {e} transition-colors" href="engineering.html">Инженерные системы</a>
                    <a class="text-sm font-medium {p} transition-colors" href="portfolio.html">Объекты интеграции</a>
                </nav>
                <div class="flex items-center gap-4">
                    <a href="index.html#contact">
                        <button class="hidden sm:flex min-w-[120px] items-center justify-center rounded bg-primary px-5 py-2 text-sm font-bold text-background-dark hover:bg-white transition-all">
                            Контакты
                        </button>
                    </a>
                </div>'''

    def replace_nav(html_content, active):
        # find the <nav... to the end of the </div> after it
        new_nav = nav_replacement(active)
        return re.sub(r'<nav class="hidden md:flex items-center gap-10">.*?</button>\s*</a>\s*</div>', new_nav, html_content, flags=re.DOTALL)

    # 1. NEW index.html
    # Remove <div id="services"> ... </div>
    # Remove <div id="portfolio"> ... </div>
    idx_html = html
    idx_html = re.sub(r'<div id="services".*?</div>\s*<div id="portfolio"', '<div id="portfolio"', idx_html, flags=re.DOTALL)
    idx_html = re.sub(r'<div id="portfolio".*?</div>\s*<div id="contact"', '<div id="contact"', idx_html, flags=re.DOTALL)
    idx_html = replace_nav(idx_html, 'index')
    with codecs.open("index.html", "w", "utf-8") as f:
        f.write(idx_html)

    # 2. portfolio.html
    # Keep header and footer, only <div id="portfolio"> in main
    port_html = html
    port_html = re.sub(r'<div id="home">.*?</div>\s*<div id="services"', '<div id="services"', port_html, flags=re.DOTALL)
    port_html = re.sub(r'<div id="services".*?</div>\s*<div id="portfolio"', '<div id="portfolio"', port_html, flags=re.DOTALL)
    port_html = re.sub(r'<div id="contact".*?</div>\s*<footer', '<footer', port_html, flags=re.DOTALL)
    port_html = replace_nav(port_html, 'portfolio')
    with codecs.open("portfolio.html", "w", "utf-8") as f:
        f.write(port_html)
        
    # 3. engineering.html (old services)
    eng_html = html
    eng_html = re.sub(r'<div id="home">.*?</div>\s*<div id="services"', '<div id="services"', eng_html, flags=re.DOTALL)
    eng_html = re.sub(r'<div id="portfolio".*?</div>\s*<div id="contact"', '<div id="contact"', eng_html, flags=re.DOTALL)
    eng_html = re.sub(r'<div id="contact".*?</div>\s*<footer', '<footer', eng_html, flags=re.DOTALL)
    eng_html = replace_nav(eng_html, 'engineering')
    with codecs.open("engineering.html", "w", "utf-8") as f:
        f.write(eng_html)

    # 4. services.html (the new one based on c:\Users\ARCHIVE STUDIO\Downloads\services\code.html)
    with codecs.open(r"c:\Users\ARCHIVE STUDIO\Downloads\services\code.html", "r", "utf-8") as fs:
        serv_html = fs.read()
    
    # We will just replace the header in services with the same header from index.html (but active 'services')
    # The services page has its own <header ...> ... </header>
    new_header = replace_nav(header_match.group(1), 'services')
    serv_html = re.sub(r'<header.*?>.*?</header>', new_header, serv_html, flags=re.DOTALL)
    with codecs.open("services.html", "w", "utf-8") as f:
        f.write(serv_html)

    print("Successfully built initial templates.")

setup_files()
