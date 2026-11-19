# Shared header, footer, logo and company details. Edit COMPANY here and rebuild.
COMPANY = {
    "name": "Rhema Solutions",
    "phone_display": "+91 63696 35002",
    "phone_tel": "+916369635002",
    "email_general": "hello@rhema.co.in",
    "email_sales": "sales@rhema.co.in",
    "email_support": "support@rhema.co.in",
}

LOGO = ('<svg viewBox="0 0 64 64" aria-hidden="true"><rect x="1" y="1" width="62" height="62" rx="15" fill="#0F172A" stroke="var(--line-strong)" stroke-width="2"/>'
        '<rect x="15" y="14" width="9" height="36" rx="2.2" fill="#fff"/><path d="M29 14h8a11 11 0 0 1 0 22h-8z" fill="#fff"/>'
        '<path d="M31 41h12.5l9.5 9H40.5z" fill="#60A5FA"/></svg>')

INTEL_LOGO = ('<svg class="logo" viewBox="0 0 64 64" aria-hidden="true"><defs><linearGradient id="ig" x1="0" y1="0" x2="64" y2="64" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#2563EB"/><stop offset="1" stop-color="#7C3AED"/></linearGradient></defs>'
              '<rect width="64" height="64" fill="url(#ig)"/><rect x="15" y="14" width="9" height="36" rx="2.2" fill="#fff"/><path d="M29 14h8a11 11 0 0 1 0 22h-8z" fill="#fff"/>'
              '<path d="M31 41h12.5l9.5 9H40.5z" fill="#fff"/></svg>')

NAV = [("services", "services.html", "Services"), ("products", "products.html", "Products"),
       ("about", "about.html", "About"), ("contact", "contact.html", "Contact")]


def header(current):
    links = ""
    for key, href, label in NAV:
        cur = ' aria-current="page"' if key == current else ""
        links += f'<a href="{href}"{cur}>{label}</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="hdr-in">
  <a class="brand" href="index.html" aria-label="Rhema Solutions, home">{LOGO}<span><b>Rhema</b> Solutions</span></a>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
  <nav id="nav" class="nav" aria-label="Main">{links}<a class="btn sm" href="contact.html">Start a project</a></nav>
</div></header>'''


def footer():
    c = COMPANY
    return f'''<footer class="ftr"><div class="wrap">
  <div class="ftr-grid">
    <div class="ftr-brand">
      <a class="brand" href="index.html" aria-label="Rhema Solutions, home">{LOGO}<span><b>Rhema</b> Solutions</span></a>
      <p>Custom software, automation and AI for businesses and organisations worldwide.</p>
    </div>
    <div><h4>Services</h4><ul>
      <li><a href="services.html#custom-software">Custom software development</a></li>
      <li><a href="services.html#automation">Business process automation</a></li>
      <li><a href="services.html#saas">SaaS product development</a></li>
      <li><a href="services.html#ai">AI-enabled solutions</a></li></ul></div>
    <div><h4>Products</h4><ul>
      <li><a href="products.html#intelligence">Rhema Intelligence</a></li>
      <li><a href="https://vbs.rhema.co.in" target="_blank" rel="noopener">Rhema VBS</a></li>
      <li><a href="https://cbms.rhema.co.in" target="_blank" rel="noopener">Rhema BMS</a></li>
      <li><a href="https://gym.rhema.co.in" target="_blank" rel="noopener">Rhema Gym ERP</a></li></ul></div>
    <div><h4>Contact</h4><ul>
      <li><a href="tel:{c['phone_tel']}">{c['phone_display']}</a></li>
      <li><a href="mailto:{c['email_general']}">{c['email_general']}</a></li>
      <li><a href="mailto:{c['email_sales']}">{c['email_sales']}</a></li>
      <li><a href="about.html">About us</a></li></ul></div>
  </div>
  <div class="ftr-base"><span>&copy; 2026 Rhema Solutions. All rights reserved.</span><span>Technology that moves you forward.</span></div>
</div></footer>'''


def cta(title="Tell us what you want to build.", text="Share a short brief and we will reply by email with next steps."):
    c = COMPANY
    return f'''<section class="sec" aria-labelledby="cta-h"><div class="wrap"><div class="cta">
  <div><h2 id="cta-h">{title}</h2><p>{text}</p></div>
  <div class="side">
    <div class="cta-row"><a class="btn light" href="contact.html">Start a project</a><a class="btn ghost" href="services.html">Our services</a></div>
    <a class="phone" href="tel:{c['phone_tel']}">{c['phone_display']}</a>
  </div>
</div></div></section>'''


def clocks():
    return '''<div class="clocks" aria-label="Current time in several time zones">
  <div class="clocks-head"><span>Time right now</span><span>Hours are shown in 24-hour time</span></div>
  <div class="clock us" data-tz="local"><div class="zone"><span class="zone-name">Your time</span><small>Where you are</small></div><time>--:--</time></div>
  <div class="clock" data-tz="Asia/Kolkata"><div class="zone">India (IST)<small>Where our team is based</small></div><time>--:--</time></div>
  <div class="clock" data-tz="Europe/London"><div class="zone">London<small>UK and Europe</small></div><time>--:--</time></div>
  <div class="clock" data-tz="America/New_York"><div class="zone">New York<small>US East</small></div><time>--:--</time></div>
  <div class="clock" data-tz="Asia/Dubai"><div class="zone">Dubai<small>Middle East</small></div><time>--:--</time></div>
  <div class="clock" data-tz="Asia/Singapore"><div class="zone">Singapore<small>South-East Asia</small></div><time>--:--</time></div>
</div>'''
