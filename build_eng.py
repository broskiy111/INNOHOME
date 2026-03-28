import codecs

with codecs.open("engineering.html", "r", "utf-8") as f:
    eng_html = f.read()

items_html = """<div class="grid grid-cols-1 md:grid-cols-3 gap-12 lg:gap-20">
                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">01 / Автоматизация</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">hub</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAmHyEYxHeHIDLt5sBfUC0yN-84xbT9n7QfrrN0AULrJ13vOH6TUrZz4o4si50zIOzI4_i5Mahv3Wa7_K0tyMEOK1TeoPRhP_QJNeu05JkTW7Ok5yFt1U3Q4BcZ83f9e-JfMTERL9-BStrlGTs78IjcHcVtGUyb0RrguUd_0BjtVvWGaheT8UxAPoXnb2RrtJayFX-6fopo2uEXOWU3CObaJ2_c_2kd9x4QOJfYHb8-e0o7x-wS5K9jaxEpDCa2I6IYWRx5VC8orwc" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Автоматизация</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Современные инженерные системы немыслимы без автоматизации. Мы предлагаем возможность полностью автоматического и эффективного управления Вашей инженерией в единой экосистеме. Только представьте – больше никаких десятков пультов и коряво переведенных программ управления устройствами, «отваливающихся» девайсов и выключателей освещения в стиле пианино. Большинство рутинных задач автоматизировано и ежедневно подстраивается под Ваши привычки, обеспечивая исключительный комфорт и радость общения с близкими.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">02 / Отопление</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">device_thermostat</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDboShOUbP5vXiriXWn97zpRkITTs0JLjcH4rT6qe7jVmSOe9CUO63PXT52htkmzqP6SoL-AKN2YJn-uNHtONhzxBYlaFujJocBO_VP1L1H-xCeSIxlTqMJlgWqtl9FQ375pKka0mO1ul1CtQXwUfSrWMvCk44bYWUZ_FhAdQo2CnSAAGZS7p86kp4SgOgamSlxXljQlndeBd9YI-pIM0EdUgdI89FvCJNEB675baPevoZWCL6Y9gQ-cBXWBTDYaWDjTsK4dPRFzHA" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Отопление</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Хотите полностью раскрыть возможности Вашей системы отопления, а не просто установить нагревательный прибор? Современные решения позволяют поддерживать индивидуальную температуру в каждом помещении в зависимости от погодных условий, интенсивности солнечного освещения, цикла дня и присутствия Вас на объекте. Это обеспечивает комфорт для пользователей и помогает значительно сократить расходы на энергоресурсы.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">03 / Электроснабжение</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">electrical_services</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAyDkgVBLGDKBGYKYWWQKSy3tXWqP4gdH9YhLYECRzfPnU_5yfiP4W7UO-dk5BHebP-5rWRhuYDDFmncGnh0xVXmWosEPWkkMFfaBJjk0zyB1xAv-vDq5JG-SL3fi4AzLLg2RMiAw5RcKKUmoForoqIWacWQTqqxUZr_rGgYCDZ-CkbAwlRUDqJNyQYZen2mhojxfkPpOEV52UkHS96Yz0-PKnuOP0cN86dj1pflvvTKLv6rwD3y_H2EjiklOU3DtGEdEQJ0CLFhco" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Электроснабжение</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Интеллектуальный контроль электроснабжения обеспечивает стабильную и безопасную работу всех электрических систем здания в любых, даже непредвиденных ситуациях. Умное распределение нагрузки, мониторинг потребления, возможность генерации «зеленой» энергии позволяют гарантированно обеспечить автономность электросистемы и ваше спокойствие.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">04 / Климат</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">mode_fan</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDpl5U79b1HFEdoVbKgIbPRxi-7kLCjHu4yEvNtMfYVveL5-f2jds7QA0vn4XVmuZab4UCgZis2ZrrNK6a98KUPzCaNhNzn0wSDeqtKArPINepRoKkW27esMalRft7JdQxifYOJzdfaGdp2x36h8sIax8NsobYjd45kdw8OabJXkJdQIo5XTSddIAivFg0lUd43BGP2ADdleRRHkIPENNep6vLLfmTrJq2lY8SJg1UQvJF58No7VHrk79WbARZ5qWMvHV-HKDuSLzQ" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Климат</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Спальня, сауна или ледовая арена? Инженерные системы управления климатом автоматически регулируют температуру, влажность и качество воздуха в помещениях. В результате создаётся комфортная среда, которая позволяет добиться максимальной эффективности деятельности людей и положительно влияет на их самочувствие.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">05 / Безопасность</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">videocam</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAmHyEYxHeHIDLt5sBfUC0yN-84xbT9n7QfrrN0AULrJ13vOH6TUrZz4o4si50zIOzI4_i5Mahv3Wa7_K0tyMEOK1TeoPRhP_QJNeu05JkTW7Ok5yFt1U3Q4BcZ83f9e-JfMTERL9-BStrlGTs78IjcHcVtGUyb0RrguUd_0BjtVvWGaheT8UxAPoXnb2RrtJayFX-6fopo2uEXOWU3CObaJ2_c_2kd9x4QOJfYHb8-e0o7x-wS5K9jaxEpDCa2I6IYWRx5VC8orwc" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Безопасность</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Комплексные решения безопасности объединяют видеонаблюдение с распознаванием лиц или объектов, учет нахождения и опасное поведение на охраняемой территории, датчики движения, задымления, протечки, сигнализацию и систему оповещения. При необходимости дом может «оживать», имитируя Ваше присутствие. И это лишь малая часть элементов безопасности.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">06 / Аудио</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">speaker</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDboShOUbP5vXiriXWn97zpRkITTs0JLjcH4rT6qe7jVmSOe9CUO63PXT52htkmzqP6SoL-AKN2YJn-uNHtONhzxBYlaFujJocBO_VP1L1H-xCeSIxlTqMJlgWqtl9FQ375pKka0mO1ul1CtQXwUfSrWMvCk44bYWUZ_FhAdQo2CnSAAGZS7p86kp4SgOgamSlxXljQlndeBd9YI-pIM0EdUgdI89FvCJNEB675baPevoZWCL6Y9gQ-cBXWBTDYaWDjTsK4dPRFzHA" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Аудио</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Интегрированная мультирум аудиосистема позволяет организовать качественное и индивидуальное звуковое сопровождение в различных зонах. Управление музыкой и звуком становится персональным и удобным, создавая идеально комфортную атмосферу для жильцов, сотрудников и посетителей.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">07 / Контроль доступа</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">lock</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAyDkgVBLGDKBGYKYWWQKSy3tXWqP4gdH9YhLYECRzfPnU_5yfiP4W7UO-dk5BHebP-5rWRhuYDDFmncGnh0xVXmWosEPWkkMFfaBJjk0zyB1xAv-vDq5JG-SL3fi4AzLLg2RMiAw5RcKKUmoForoqIWacWQTqqxUZr_rGgYCDZ-CkbAwlRUDqJNyQYZen2mhojxfkPpOEV52UkHS96Yz0-PKnuOP0cN86dj1pflvvTKLv6rwD3y_H2EjiklOU3DtGEdEQJ0CLFhco" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Контроль доступа</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Система позволяет деликатно узнать, что Ваши дети вернулись из школы, утром выпустить собаку на прогулку по лужайке, дистанционно открыть дверь или ворота сотруднику службы доставки, выдать разовый пароль доступа обслуживающему персоналу в заданный интервал времени, при этом обеспечить безусловную безопасность вашей недвижимости.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">08 / Освещение</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">lightbulb</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDpl5U79b1HFEdoVbKgIbPRxi-7kLCjHu4yEvNtMfYVveL5-f2jds7QA0vn4XVmuZab4UCgZis2ZrrNK6a98KUPzCaNhNzn0wSDeqtKArPINepRoKkW27esMalRft7JdQxifYOJzdfaGdp2x36h8sIax8NsobYjd45kdw8OabJXkJdQIo5XTSddIAivFg0lUd43BGP2ADdleRRHkIPENNep6vLLfmTrJq2lY8SJg1UQvJF58No7VHrk79WbARZ5qWMvHV-HKDuSLzQ" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Освещение</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Создать интимную атмосферу, добраться до санузла ночью не разбудив домочадцев или устроить первоклассную вечеринку с ярким и выразительным освещением? Широкий функционал сценарного света долгое время будет радовать Вас новыми красками и привычными уютными оттенками.</p>
                            </div>
                        </div>

                        <div class="group relative flex flex-col gap-6 border-t border-white/5 pt-10">
                            <div class="flex items-center justify-between">
                                <span class="text-xs font-mono text-primary/40">09 / Управление</span>
                                <span class="material-symbols-outlined text-4xl text-primary opacity-50 group-hover:opacity-100 transition-opacity">settings_remote</span>
                            </div>
                            <div class="aspect-video w-full overflow-hidden rounded bg-slate-900">
                                <img class="h-full w-full object-cover opacity-60 group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDboShOUbP5vXiriXWn97zpRkITTs0JLjcH4rT6qe7jVmSOe9CUO63PXT52htkmzqP6SoL-AKN2YJn-uNHtONhzxBYlaFujJocBO_VP1L1H-xCeSIxlTqMJlgWqtl9FQ375pKka0mO1ul1CtQXwUfSrWMvCk44bYWUZ_FhAdQo2CnSAAGZS7p86kp4SgOgamSlxXljQlndeBd9YI-pIM0EdUgdI89FvCJNEB675baPevoZWCL6Y9gQ-cBXWBTDYaWDjTsK4dPRFzHA" />
                            </div>
                            <div>
                                <h3 class="text-2xl font-bold text-white mb-3">Управление</h3>
                                <p class="text-slate-400 leading-relaxed mb-6">Единая мультиплатформенная система объединяет управление инженерией в понятном приложении, с одинаково удобным интерфейсом всех устройств — часы, смартфон, планшет, компьютер, автомобиль или голосовое управление. Ваши данные обрабатываются локально на сервере для абсолютной безопасности.</p>
                            </div>
                        </div>
                    </div>"""

target_start = eng_html.find('<div class="grid grid-cols-1 md:grid-cols-2 gap-12 lg:gap-20">')
target_end = eng_html.find('</section>', target_start)
# We find the nearest </div> before </section> actually, but wait...
target_end = eng_html.rfind('</div>', target_start, target_end)

if target_start != -1 and target_end != -1:
    new_html = eng_html[:target_start] + items_html + eng_html[target_end+6:]
    with codecs.open("engineering.html", "w", "utf-8") as f:
        f.write(new_html)
    print("Success")
else:
    print("Failed to find target")

