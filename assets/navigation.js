/* Loving Grace's main navigation: visible without JavaScript, compact on phones. */
(() => {
  const header = document.querySelector('header.site');
  const button = header?.querySelector('.nav-toggle');
  const navigation = header?.querySelector('#site-navigation');
  if (!button || !navigation) return;

  const mobile = window.matchMedia('(max-width: 1100px)');
  let expanded = false;

  function render() {
    const open = mobile.matches && expanded;
    button.hidden = !mobile.matches;
    navigation.hidden = mobile.matches && !open;
    button.setAttribute('aria-expanded', String(open));
    button.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
    button.textContent = open ? 'Close' : 'Menu';
    header.classList.toggle('nav-open', open);
  }

  function close(restoreFocus = false) {
    if (!expanded) return;
    expanded = false;
    render();
    if (restoreFocus && mobile.matches) button.focus();
  }

  button.addEventListener('click', () => {
    expanded = !expanded;
    render();
  });
  navigation.addEventListener('click', event => {
    if (event.target.closest('a')) close();
  });
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && expanded) {
      event.preventDefault();
      close(true);
    }
  });
  document.addEventListener('pointerdown', event => {
    if (!header.contains(event.target)) close();
  });
  const changeLayout = () => {
    const focusedLink = navigation.contains(document.activeElement);
    const focusedButton = document.activeElement === button;
    expanded = false;
    render();
    if (mobile.matches && focusedLink) button.focus();
    else if (!mobile.matches && focusedButton) {
      (navigation.querySelector('[aria-current="page"]') || navigation.querySelector('a'))?.focus();
    }
  };
  if (mobile.addEventListener) mobile.addEventListener('change', changeLayout);
  else mobile.addListener(changeLayout);
  window.addEventListener('pageshow', () => { expanded = false; render(); });

  header.classList.add('nav-ready');
  render();
})();
