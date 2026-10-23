document.documentElement.style.scrollBehavior='smooth';
document.addEventListener('DOMContentLoaded',()=>{document.querySelectorAll('input[type=date]').forEach(el=>{el.min=new Date().toISOString().split('T')[0]})});
