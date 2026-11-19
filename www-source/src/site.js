(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  try { if (window.lucide) window.lucide.createIcons(); } catch (e) {}

  /* Mobile menu */
  var mb = $('.menu-btn'), nav = $('#nav');
  if (mb && nav) {
    mb.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      mb.setAttribute('aria-expanded', String(open));
      mb.textContent = open ? 'Close' : 'Menu';
    });
    nav.addEventListener('click', function (e) { if (e.target.tagName === 'A') { nav.classList.remove('open'); mb.setAttribute('aria-expanded', 'false'); mb.textContent = 'Menu'; } });
  }

  /* Hero diagram: drop the moving pulses for reduced motion */
  if (reduce) $$('animateMotion').forEach(function (el) { el.parentNode.removeChild(el); });

  /* Process line fills when it scrolls into view */
  var steps = $('.steps');
  if (steps) {
    if (reduce || !('IntersectionObserver' in window)) { steps.classList.add('in'); }
    else {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { steps.classList.add('in'); io.disconnect(); } }); }, { threshold: 0.3 });
      io.observe(steps);
    }
  }

  /* Time zones */
  var clocks = $$('[data-tz]');
  if (clocks.length) {
    var local = 'UTC';
    try { local = Intl.DateTimeFormat().resolvedOptions().timeZone || 'UTC'; } catch (e) {}
    var us = $('[data-tz="local"]');
    if (us) {
      us.setAttribute('data-tz', local);
      var sm = $('small', us); if (sm) sm.textContent = local.replace(/_/g, ' ');
    }
    var tick = function () {
      var now = new Date();
      $$('[data-tz]').forEach(function (el) {
        var tz = el.getAttribute('data-tz'), out = '--:--';
        try { out = new Intl.DateTimeFormat('en-GB', { hour: '2-digit', minute: '2-digit', hour12: false, timeZone: tz }).format(now); } catch (e) {}
        var t = $('time', el); if (t) t.textContent = out;
      });
    };
    tick(); setInterval(tick, 20000);
  }

  /* Enquiry form: builds a ready-to-send email, since this site has no mail server of its own */
  var form = $('#enquiry');
  if (form) {
    var TO = form.getAttribute('data-to');
    var draft = $('#draft'), pre = $('#draftText'), openA = $('#openMail'), copyB = $('#copyDraft'), status = $('#copyStatus');
    var need = function (id, msg) {
      var f = $('#' + id), er = $('#' + id + '-err'), bad = false;
      if (id === 'email') bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value.trim());
      else bad = !f.value.trim();
      f.setAttribute('aria-invalid', String(bad)); er.textContent = bad ? msg : '';
      return !bad;
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = [need('name', 'Enter your name.'), need('email', 'Enter a valid email address.'), need('message', 'Tell us a little about what you need.')];
      if (ok.indexOf(false) !== -1) { var first = $('[aria-invalid="true"]', form); if (first) first.focus(); return; }
      var v = function (id) { return $('#' + id).value.trim(); };
      var subject = 'Project enquiry' + (v('service') ? ': ' + v('service') : '') + (v('company') ? ' (' + v('company') + ')' : '');
      var body = 'Name: ' + v('name') + '\nEmail: ' + v('email') + (v('company') ? '\nCompany: ' + v('company') : '') + (v('country') ? '\nCountry: ' + v('country') : '') + (v('service') ? '\nInterested in: ' + v('service') : '') + '\n\n' + v('message');
      pre.textContent = 'To: ' + TO + '\nSubject: ' + subject + '\n\n' + body;
      openA.href = 'mailto:' + TO + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      draft.hidden = false; status.textContent = '';
      draft.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'nearest' });
    });
    copyB.addEventListener('click', function () {
      var txt = pre.textContent, done = function () { status.textContent = 'Copied. Paste it into an email to ' + TO + '.'; };
      var fallback = function () { try { var r = document.createRange(); r.selectNodeContents(pre); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); status.textContent = 'Selected. Copy it with your keyboard.'; } catch (e) {} };
      try { navigator.clipboard.writeText(txt).then(done, fallback); } catch (e) { fallback(); }
    });
    $$('input, textarea', form).forEach(function (f) { f.addEventListener('input', function () { if (f.getAttribute('aria-invalid') === 'true') need(f.id, f.id === 'email' ? 'Enter a valid email address.' : 'This field is required.'); }); });
  }
})();
