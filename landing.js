const reveals = document.querySelectorAll('.reveal');

const revealObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  },
  { threshold: 0.08, rootMargin: '0px 0px -6% 0px' },
);

reveals.forEach((element) => revealObserver.observe(element));
