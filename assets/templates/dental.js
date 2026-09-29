(() => {
  const toggle=document.querySelector('.menu-toggle'), menu=document.querySelector('#d-navigation');
  function closeMenu(){ menu.hidden=true;toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Open navigation'); }
  toggle.addEventListener('click',()=>{const open=menu.hidden;menu.hidden=!open;toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Close navigation':'Open navigation');});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!menu.hidden){closeMenu();toggle.focus();}});
  // Same-site links: close the drawer, carry a preselected service to the booking form, and animate the page swap
  // where the browser has no cross-document view transitions.
  document.addEventListener('click',e=>{
    const link=e.target.closest('a');
    if(!link)return;
    const url=new URL(link.href);
    if(url.origin!==location.origin||!url.pathname.startsWith('/services/templates/dental-clinic/')||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||e.button!==0)return;
    closeMenu();
    if(link.dataset.service)url.searchParams.set('service',link.dataset.service);
    if(url.pathname===location.pathname&&!link.dataset.service)return;
    const animate=!('onpageswap' in window)&&!matchMedia('(prefers-reduced-motion: reduce)').matches;
    if(link.dataset.service||animate){
      e.preventDefault();
      if(animate){document.body.classList.add('d-leaving');setTimeout(()=>location.assign(url.href),350);}
      else location.assign(url.href);
    }
  });
  window.addEventListener('pageshow',()=>document.body.classList.remove('d-leaving'));
  document.querySelectorAll('.care-trigger').forEach(button=>button.addEventListener('click',()=>{
    const open=button.getAttribute('aria-expanded')!=='true';
    document.querySelectorAll('.care-trigger').forEach(b=>{const active=b===button&&open;b.setAttribute('aria-expanded',String(active));document.getElementById(b.getAttribute('aria-controls')).hidden=!active;});
  }));
  const form=document.getElementById('bookingForm');
  if(form){
    const date=form.querySelector('[name=date]'),today=new Date();
    date.min=[today.getFullYear(),String(today.getMonth()+1).padStart(2,'0'),String(today.getDate()).padStart(2,'0')].join('-');
    const wanted=new URLSearchParams(location.search).get('service'),service=form.querySelector('[name=service]');
    if(wanted&&[...service.options].some(o=>o.value===wanted))service.value=wanted;
    form.addEventListener('submit',e=>{e.preventDefault();if(!form.reportValidity())return;const done=document.getElementById('bookingDone');done.classList.remove('hidden');form.querySelector('[type=submit]').disabled=true;done.scrollIntoView({behavior:'smooth',block:'nearest'});});
  }
})();
