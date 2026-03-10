import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Первый слайд (Home Hero)
html = re.sub(
    r'Future<br /><span([^>]+)>Habitation</span>',
    r'Инновационное<br /><span\1>жилое пространство</span>',
    html
)
html = html.replace(
    'Redefining the boundaries of living space through cinematic aesthetics and high-end structural\n                        engineering.',
    'Переосмысление границ жилого пространства с помощью высококачественной инженерной конструкции.'
)

# 2. Второй слайд (Services/Advanced Laboratory)
html = re.sub(
    r'Advanced<br /><span class="font-black not-italic ml-8">Laboratory</span>',
    r'Передовые<br /><span class="font-black not-italic ml-8">возможности</span>',
    html
)
html = html.replace(
    '"Architecture is the learned game, correct and magnificent, of forms assembled in the\n                            light."',
    '"Технологии, меняющие будущее, строятся на основе глубоких знаний и смелых решений."'
)
html = html.replace(
    'Advanced thermal engineering\n                                for optimal comfort. Our systems integrate high-efficiency heating and air purification\n                                into the architectural fabric, maintaining perfect equilibrium in every season.',
    'Передовая теплоэнергетика для оптимального комфорта. Наши системы интегрируют высокоэффективное отопление и очистку воздуха в жилую архитектуру, сохраняя идеальное равновесие в каждом сезоне.'
)

# 3. Index / Selected Works
html = html.replace(
    'Curated architectural statements.',
    'Универсальные решения для вашего проекта'
)

# 4. The Methodology
html = re.sub(
    r'The<br /><span\s+class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-white/20">Methodology</span>',
    r'The<br /><span class="text-transparent bg-clip-text bg-gradient-to-r from-primary to-white/20">Methodology</span>',
    html # replacing The Methodology with same tags but Russian? Wait. Let's just do text:
)
html = re.sub(
    r'(<h2 class="text-6xl font-black text-white uppercase tracking-tighter leading-none">\s*)The<br /><span([^>]+)>Methodology</span>(\s*</h2>)',
    r'\1Наш<br /><span\2>процесс</span>\3',
    html
)
html = html.replace(
    'Our process is a rigorous dialogue between intuition and engineering, ensuring every\n                                detail serves a purpose.',
    'Наш процесс - это баланс между интуицией и инженерией, обеспечивающий, чтобы каждая деталь служила цели.'
)

# Stage 01
html = html.replace('Stage\n                                    01', 'Этап\n                                    1')
html = html.replace('>Concept Origin\n                                </h4>', '>Концепция и стратегия\n                                </h4>')
html = html.replace(
    'Deep immersion into site\n                                    context and client narrative to establish a unique architectural DNA.',
    'Глубокое погружение в контекст и потребности клиента для разработки уникальной архитектуры умного дома.'
)

# Stage 02
html = html.replace('Stage\n                                    02', 'Этап\n                                    2')
html = html.replace('>Virtual Tectonics\n                                </h4>', '>Персональное проектирование\n                                </h4>')
html = html.replace(
    'Advanced digital\n                                    fabrication and 3D prototyping to test material limits and spatial flow.',
    'Использование цифровых технологий для создания уникальных решений, идеально подходящих под нужды каждого клиента и особенности его пространства.'
)

# Stage 03
html = html.replace('Stage\n                                    03', 'Этап\n                                    3')
html = html.replace('>Material\n                                    Realization</h4>', '>Реализация и внедрение</h4>')
html = html.replace(
    'The final act of precision\n                                    construction where sketches transform into enduring structural reality.',
    'Точный процесс строительства, где цифровые концепты становятся реальными и долговечными технологиями умного дома.'
)

# 5. Наши основные возможности 
html = html.replace('Our Core Capabilities', 'Наши основные возможности')
# 01
html = html.replace('01 / Automation', '01 / Автоматизация')
html = html.replace('>Home Automation</h3>', '>Умный дом</h3>')
html = html.replace(
    'Comprehensive smart home orchestration that\n                                disappears into your architecture. We create intuitive environments that respond to your\n                                presence with surgical precision.',
    'Полное управление умным домом, органично интегрированное в архитектуру. Мы создаём интуитивно понятные среды, которые реагируют на ваше присутствие с точностью до миллиметра.'
)

# 02
html = html.replace('02 / Climate', '02 / Климат')
html = html.replace('>Precision Heating</h3>', '>Управление климатом</h3>')
html = html.replace(
    'Advanced thermal engineering for the modern\n                                residence. Multi-zone climate control systems designed for invisible installation and\n                                absolute efficiency.',
    'Современные системы для точного контроля температуры, влажности и качества воздуха в доме. Мульти зонные установки для эффективного климат-контроля, интегрированные для скрытой установки и обеспечения максимального комфорта.'
)

# 03
html = html.replace('03 / Infrastructure', '03 / Инфраструктура')
html = html.replace('>Integrated Power</h3>', '>Интеллектуальное электроснабжение</h3>')
html = html.replace(
    'Uninterruptible power solutions and energy\n                                management. We engineer robust electrical backbones that support the most demanding\n                                smart home ecosystems.',
    'Продвинутые решения для бесперебойного питания и управления энергией. Мы создаем надежные системы, обеспечивающие поддержку сложных экосистем умных домов, с акцентом на эффективность и безопасность.'
)

# 04
html = html.replace('04 / Surveillance', '04 / Безопасность')
html = html.replace('>Network &amp; Security</h3>', '>Слаботочные системы</h3>')
html = html.replace(
    'High-speed low-current networking and\n                                AI-powered video surveillance. Enterprise-grade connectivity paired with sophisticated\n                                perimeter protection.',
    'Высокоскоростные слаботочные сети и видеонаблюдение на основе искусственного интеллекта. Корпоративный уровень подключения и продвинутая защита периметра.'
)

# 6. Last page
html = html.replace('Build Your <br />Legacy.', 'Ваша мечта, <br />наша реальность.')
html = html.replace(
    'Transforming spaces into intelligent environments. Let\'s start the conversation about your next\n              architectural masterpiece.',
    'Преобразуем ваши идеи в умные и комфортные решения. Начните путь к идеальному дому с нами.'
)

# Navigation
html = html.replace('>Home</a>', '>Главная</a>')
html = html.replace('>Services</a>', '>Услуги</a>')
html = html.replace('>Portfolio</a>', '>Портфолио</a>')
html = html.replace('>Contact</a>', '>Контакты</a>')
html = html.replace('Get Started\n                        </button>', 'Начать\n                        </button>')

# Some missing text replacements
html = html.replace('Explore Houses', 'Смотреть проекты')
html = html.replace('Our Process', 'Наш подход')
html = html.replace('Scroll to discover', 'Листайте вниз')

html = html.replace('ARCHITECTURAL <br />INTELLIGENCE.', 'АРХИТЕКТУРНЫЙ <br />ИНТЕЛЛЕКТ.')
html = html.replace(
    'Experience the synergy of architectural depth and advanced home intelligence. We redefine luxury\n                        through invisible technology and effortless control.',
    'Почувствуйте синергию архитектурной глубины и передового интеллекта дома. Мы переопределяем роскошь через невидимые технологии и безупречное управление.'
)

html = html.replace('Book a Consultation', 'Оставить заявку')

# Contact Form
html = html.replace('Design\n              Consultation', 'Запрос на Консультацию')
html = html.replace('The Form', 'Отправить заявку')
html = html.replace('Submit your project details for a\n                private assessment.', 'Оставьте данные для обсуждения проекта.')
html = html.replace('>Full\n                    Name</label>', '>Имя и Фамилия</label>')
html = html.replace('>Email\n                    Address</label>', '>Почта</label>')
html = html.replace('>Inquiry\n                  Type</label>', '>Тип запроса</label>')
html = html.replace('>The\n                  Vision</label>', '>Описание</label>')
html = html.replace('placeholder="John Doe"', 'placeholder="Иван Иванов"')
html = html.replace('placeholder="john@example.com"', 'placeholder="ivan@example.com"')
html = html.replace('placeholder="Tell us about your space..."', 'placeholder="Расскажите о вашем проекте..."')
html = html.replace('>Initialize\n                  Project</span>', '>Отправить\n                  Заявку</span>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Done")
