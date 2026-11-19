import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__) + "/src")
from partials import COMPANY as C, header, footer, cta, clocks, INTEL_LOGO

ROOT = os.path.dirname(os.path.abspath(__file__))
css = open(f"{ROOT}/src/styles.css").read()
js = open(f"{ROOT}/src/site.js").read()
os.makedirs(f"{ROOT}/dist", exist_ok=True)

PAGES = {
    "index": ("Rhema Solutions", "home", "Rhema Solutions builds custom software, business process automation, SaaS products and AI-enabled solutions for businesses worldwide."),
    "services": ("Services | Rhema Solutions", "services", "Custom software development, business process automation, SaaS product development and AI-enabled solutions from Rhema Solutions."),
    "products": ("Products | Rhema Solutions", "products", "Rhema Intelligence, Rhema VBS, Rhema BMS and Rhema Gym ERP: software products built and supported by Rhema Solutions."),
    "about": ("About | Rhema Solutions", "about", "Rhema Solutions builds practical software products and digital solutions for businesses and organisations around the world."),
    "contact": ("Contact | Rhema Solutions", "contact", "Contact Rhema Solutions by phone or email to discuss custom software, automation, SaaS or AI projects."),
}

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;650;700;800&display=swap">')
LUCIDE = '<script src="https://unpkg.com/lucide@0.468.0/dist/umd/lucide.min.js"></script>'

LD = json.dumps({
    "@context": "https://schema.org", "@type": "Organization", "name": "Rhema Solutions",
    "url": "https://www.rhema.co.in", "logo": "https://www.rhema.co.in/favicon.svg",
    "description": PAGES["index"][2], "telephone": C["phone_tel"], "email": C["email_general"],
    "contactPoint": [{"@type": "ContactPoint", "contactType": "sales", "telephone": C["phone_tel"], "email": C["email_sales"], "availableLanguage": "English"},
                     {"@type": "ContactPoint", "contactType": "customer support", "email": C["email_support"], "availableLanguage": "English"}],
})

for name, (title, key, desc) in PAGES.items():
    body = open(f"{ROOT}/src/pages/{name}.html").read()
    rep = {"{{HEADER}}": header(key), "{{FOOTER}}": footer(), "{{CTA}}": cta(), "{{CLOCKS}}": clocks(), "{{INTEL_LOGO}}": INTEL_LOGO,
           "{{PHONE}}": C["phone_display"], "{{PHONE_TEL}}": C["phone_tel"], "{{EMAIL_GENERAL}}": C["email_general"],
           "{{EMAIL_SALES}}": C["email_sales"], "{{EMAIL_SUPPORT}}": C["email_support"]}
    for k, v in rep.items():
        body = body.replace(k, v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", body)
    assert not left, (name, left)
    ld = f'<script type="application/ld+json">{LD}</script>' if name == "index" else ""
    head = (f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<meta name="description" content="{desc}">\n'
            f'<meta name="theme-color" content="#0f172a">\n<meta property="og:title" content="{title}">\n<meta property="og:description" content="{desc}">\n'
            f'<link rel="icon" type="image/svg+xml" href="favicon.svg">\n{FONTS}\n<style>\n{css}\n</style>\n')
    tail = f"\n{LUCIDE}\n<script>\n{js}\n</script>\n{ld}\n"
    if name == "index":  # the artifact host wraps this file in its own document skeleton
        out = head + body + tail
    else:
        out = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
               + head + "</head><body>\n" + body + tail + "</body></html>\n")
    open(f"{ROOT}/dist/{name}.html", "w").write(out)
    print(name, len(out))
open(f"{ROOT}/dist/favicon.svg", "w").write(open(f"{ROOT}/src/favicon.svg").read())
