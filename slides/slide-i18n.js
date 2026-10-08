(() => {
  const copyNode = document.getElementById('slide-locales');
  const languageNav = document.querySelector('[data-language-switch]');
  if (!copyNode || !languageNav) return;

  let locales;
  try {
    locales = JSON.parse(copyNode.textContent || '{}');
  } catch {
    return;
  }

  const supportedLanguages = new Set(['ko', 'ja', 'en']);
  const sectionNodes = Array.from(document.querySelectorAll('.grid > section'));

  function applyLanguage(requestedLanguage, updateUrl = false) {
    const language = supportedLanguages.has(requestedLanguage) ? requestedLanguage : 'ko';
    if (language === 'ko') {
      document.documentElement.lang = 'ko';
      languageNav.setAttribute('aria-label', '언어 선택');
      languageNav.querySelectorAll('[data-language]').forEach((button) => {
        const selected = button.dataset.language === 'ko';
        button.setAttribute('aria-pressed', String(selected));
        button.classList.toggle('active', selected);
      });
      if (updateUrl) {
        const url = new URL(window.location.href);
        url.searchParams.set('lang', 'ko');
        window.location.assign(url);
      }
      return;
    }

    const copy = locales[language];
    if (!copy || !Array.isArray(copy.sections) || copy.sections.length !== sectionNodes.length) return;

    const sectionCopyIsValid = copy.sections.every((section, index) => {
      const sectionNode = sectionNodes[index];
      const list = sectionNode.querySelector('ul');
      const paragraph = sectionNode.querySelector('p');
      if (Array.isArray(section.items)) {
        return Boolean(list) && list.querySelectorAll('li').length === section.items.length;
      }
      return Boolean(paragraph && typeof section.text === 'string');
    });
    if (!sectionCopyIsValid) return;

    document.documentElement.lang = language;
    document.title = copy.documentTitle;
    document.querySelector('meta[name="description"]')?.setAttribute('content', copy.description);

    const notice = document.querySelector('.notice');
    const noticeTitle = document.createElement('strong');
    noticeTitle.textContent = copy.noticeTitle;
    notice.replaceChildren(noticeTitle, document.createTextNode(` — ${copy.notice}`));

    const eyebrow = document.querySelector('.eyebrow');
    const title = document.querySelector('main h1');
    const lead = document.querySelector('.lead');
    const status = document.querySelector('.status');
    const footer = document.querySelector('.foot');
    if (!eyebrow || !title || !lead || !status || !footer) return;

    eyebrow.textContent = copy.eyebrow;
    title.textContent = copy.title;
    lead.textContent = copy.lead;
    status.textContent = copy.status;
    footer.textContent = copy.foot;

    sectionNodes.forEach((sectionNode, index) => {
      const sectionCopy = copy.sections[index];
      sectionNode.querySelector('h2').textContent = sectionCopy.title;
      if (Array.isArray(sectionCopy.items)) {
        sectionNode.querySelectorAll('li').forEach((item, itemIndex) => {
          item.textContent = sectionCopy.items[itemIndex];
        });
      } else {
        sectionNode.querySelector('p').textContent = sectionCopy.text;
      }
    });

    languageNav.setAttribute('aria-label', copy.languageLabel);
    languageNav.querySelectorAll('[data-language]').forEach((button) => {
      const selected = button.dataset.language === language;
      button.setAttribute('aria-pressed', String(selected));
      button.classList.toggle('active', selected);
    });

    if (updateUrl) {
      const url = new URL(window.location.href);
      url.searchParams.set('lang', language);
      window.history.replaceState(null, '', url);
    }
  }

  languageNav.querySelectorAll('[data-language]').forEach((button) => {
    button.addEventListener('click', () => applyLanguage(button.dataset.language, true));
  });

  const queryLanguage = new URLSearchParams(window.location.search).get('lang');
  applyLanguage(queryLanguage || document.documentElement.lang);
})();
