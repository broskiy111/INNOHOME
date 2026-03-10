import os

base_dir = r"c:\Users\ARCHIVE STUDIO\Downloads\stitch_process"
homepage_src = os.path.join(base_dir, "homepage_updated_services_flow", "code.html")
index_dest = os.path.join(base_dir, "index.html")

# 1. Сборка главной страницы (index.html)
with open(homepage_src, "r", encoding="utf-8") as f:
    html = f.read()

html = html.replace(
    'href="#">Services</a>',
    'href="services_updated_directions/code.html">Services</a>'
)
html = html.replace(
    'href="#">Projects</a>',
    'href="projects_cinematic_dark/code.html">Projects</a>'
)
html = html.replace(
    'href="#">Contacts</a>',
    'href="contacts_atmospheric_architectural_theme/code.html">Contacts</a>'
)
# Ссылка на кнопке "Contact Us" тоже
html = html.replace(
    '<button class="bg-primary text-background-dark px-6 py-2.5 text-[11px] uppercase tracking-[0.2em] font-bold hover:bg-white transition-all rounded">\n                    Contact Us\n                </button>',
    '<a href="contacts_atmospheric_architectural_theme/code.html"><button class="bg-primary text-background-dark px-6 py-2.5 text-[11px] uppercase tracking-[0.2em] font-bold hover:bg-white transition-all rounded">\n                    Contact Us\n                </button></a>'
)

with open(index_dest, "w", encoding="utf-8") as f:
    f.write(html)
print("Created index.html with links")

# 2. Обновление страницы Services
services_path = os.path.join(base_dir, "services_updated_directions", "code.html")
with open(services_path, "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace('href="#">Home</a>', 'href="/index.html">Home</a>')
html = html.replace('href="#">Portfolio</a>', 'href="/projects_cinematic_dark/code.html">Portfolio</a>')
html = html.replace('href="#">Contact</a>', 'href="/contacts_atmospheric_architectural_theme/code.html">Contact</a>')
with open(services_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Services page")

# 3. Обновление страницы Projects
projects_path = os.path.join(base_dir, "projects_cinematic_dark", "code.html")
with open(projects_path, "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace('href="#">Home</a>', 'href="/index.html">Home</a>')
html = html.replace('href="#">Contact</a>', 'href="/contacts_atmospheric_architectural_theme/code.html">Contact</a>')
with open(projects_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Projects page")

# 4. Обновление страницы Contacts
contacts_path = os.path.join(base_dir, "contacts_atmospheric_architectural_theme", "code.html")
with open(contacts_path, "r", encoding="utf-8") as f:
    html = f.read()
html = html.replace('href="#">Home</a>', 'href="/index.html">Home</a>')
html = html.replace('href="#">Products</a>', 'href="/projects_cinematic_dark/code.html">Products</a>')
html = html.replace('href="#">Solutions</a>', 'href="/services_updated_directions/code.html">Solutions</a>')
html = html.replace('href="#">Support</a>', 'href="/contacts_atmospheric_architectural_theme/code.html">Support</a>')
with open(contacts_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated Contacts page")
