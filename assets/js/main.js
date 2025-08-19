/*
	Dopetrope by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body');

    // Breakpoints (guarded for pages that don't include breakpoints.min.js)
        if (typeof window.breakpoints === 'function') {
            breakpoints({
                xlarge:  [ '1281px',  '1680px' ],
                large:   [ '981px',   '1280px' ],
                medium:  [ '737px',   '980px'  ],
                small:   [ null,      '736px'  ]
            });
        }

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Modern dropdown functionality replaced dropotron

	// Nav.
    // Mobile navigation has been removed as requested

		// Title Bar and Panel have been removed
    
})(jQuery);

// Disable snap-scrolling by default. To enable, add class `enable-fullscreen-scroll` to <body>.
document.addEventListener('DOMContentLoaded', function() {
    if (!document.body.classList.contains('enable-fullscreen-scroll')) return;

    const sections = document.querySelectorAll('.fullscreen-section');
    if (!sections.length) return;

    let currentSection = 0;
    let isScrolling = false;
    let touchStartY = 0;

    sections[0].classList.add('active');

    function scrollToSection(index) {
        if (index >= 0 && index < sections.length && !isScrolling) {
            isScrolling = true;
            sections[currentSection].classList.remove('active');
            sections[index].classList.add('active');
            sections[index].scrollIntoView({ behavior: 'smooth' });
            currentSection = index;
            setTimeout(() => { isScrolling = false; }, 1000);
        }
    }

    window.addEventListener('wheel', function(e) {
        e.preventDefault();
        if (!isScrolling) {
            if (e.deltaY > 0) scrollToSection(currentSection + 1);
            else scrollToSection(currentSection - 1);
        }
    }, { passive: false });

    document.addEventListener('touchstart', function(e) {
        touchStartY = e.touches[0].clientY;
    }, { passive: true });

    document.addEventListener('touchmove', function(e) {
        if (isScrolling) return;
        const touchEndY = e.touches[0].clientY;
        const diff = touchStartY - touchEndY;
        if (Math.abs(diff) > 50) {
            if (diff > 0) scrollToSection(currentSection + 1);
            else scrollToSection(currentSection - 1);
        }
    }, { passive: false });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') scrollToSection(currentSection + 1);
        else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') scrollToSection(currentSection - 1);
    });
});

// Unified footer injection for ALL pages
(function injectUnifiedFooter() {
    function getPrefix() {
        var path = window.location.pathname || '';
        return path.indexOf('/topics/') !== -1 ? '../../' : '';
    }

    function buildFooterHTML(prefix) {
        return '\n            <div class="footer-content">\n                <div class="footer-section">\n                    <div class="footer-brand">\n                        <h3>Mongol Potential</h3>\n                        <p>Helping Mongol minds reach their full potential. Personalized tutoring and comprehensive resources.</p>\n                    </div>\n                </div>\n                <div class="footer-section">\n                    <h4>Services</h4>\n                    <ul>\n                        <li><a href="' + prefix + 'tutoring.html">Online Tutoring</a></li>\n                        <li><a href="' + prefix + 'exam-prep.html">Learning Resources</a></li>\n                    </ul>\n                </div>\n                <div class="footer-section">\n                    <h4>Support</h4>\n                    <ul>\n                        <li><a href="' + prefix + 'contact.html">Contact Us</a></li>\n                        <li><a href="mailto:imathhub@gmail.com">Email Us</a></li>\n                        <li><a href="' + prefix + 'company.html">About</a></li>\n                        <li><a href="' + prefix + 'blog.html">Blog</a></li>\n\n                    </ul>\n                </div>\n                <div class="footer-section">\n                    <h4>Connect</h4>\n                    <div class="social-links">\n                        <a href="mailto:imathhub@gmail.com" class="social-link" title="Email"><i class="fas fa-envelope"></i></a>\n                        <a href="https://www.facebook.com/mongolpotential" class="social-link" title="Facebook"><i class="fab fa-facebook-f"></i></a>\n                        <a href="https://www.youtube.com/@InternationalMathematicsHub" class="social-link" title="YouTube"><i class="fab fa-youtube"></i></a>\n                        <a href="https://x.com/mongolmath" class="social-link" title="X"><i class="fab fa-twitter"></i></a>\n                        <a href="https://www.instagram.com/mongolpotential" class="social-link" title="Instagram"><i class="fab fa-instagram"></i></a>\n                    </div>\n                </div>\n            </div>\n            <div class="footer-bottom">\n                <div class="footer-bottom-content">\n                    <div class="footer-legal">\n                        <ul>\n                            <li><a href="' + prefix + 'terms.html">Terms of Service</a></li>\n                            <li><a href="' + prefix + 'privacy.html">Privacy Policy</a></li>\n                            <li><a href="' + prefix + 'cookies.html">Cookie Policy</a></li>\n                        </ul>\n                    </div>\n                    <div class="footer-copyright">\n                        <p>&copy; 2025 Mongol Potential. All rights reserved.</p>\n                    </div>\n                </div>\n            </div>\n        ';
    }

    document.addEventListener('DOMContentLoaded', function() {
        var footer = document.querySelector('#footer');
        if (!footer) return;
        var prefix = getPrefix();
        footer.innerHTML = buildFooterHTML(prefix);
        try { window.dispatchEvent(new CustomEvent('footer:ready')); } catch (e) {}
    });
})();

// Unified navigation injection for ALL pages
(function injectUnifiedNav() {
    function buildNavHTML() {
        return '\n<ul>\n' +
        '    <li><a href="index.html">Home</a></li>\n' +
        '    <li class="has-dropdown">\n' +
        '        <a href="exam-prep.html">Exam Prep</a>\n' +
        '        <div class="dropdown">\n' +
        '            <div class="dropdown-grid">\n' +
        '                <a href="exam-prep.html#sat" class="dropdown-item">\n' +
        '                    <i class="fas fa-graduation-cap"></i>\n' +
        '                    <span>SAT Math</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#act" class="dropdown-item">\n' +
        '                    <i class="fas fa-check-circle"></i>\n' +
        '                    <span>ACT Math</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#psat" class="dropdown-item">\n' +
        '                    <i class="fas fa-clipboard-check"></i>\n' +
        '                    <span>PSAT/NMSQT</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#gre" class="dropdown-item">\n' +
        '                    <i class="fas fa-chart-line"></i>\n' +
        '                    <span>GRE Quant</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#gmat" class="dropdown-item">\n' +
        '                    <i class="fas fa-briefcase"></i>\n' +
        '                    <span>GMAT Quant</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#ib" class="dropdown-item">\n' +
        '                    <i class="fas fa-globe"></i>\n' +
        '                    <span>IB Math</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#igcse" class="dropdown-item">\n' +
        '                    <i class="fas fa-book"></i>\n' +
        '                    <span>IGCSE/GCSE Math</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#olympiad" class="dropdown-item">\n' +
        '                    <i class="fas fa-trophy"></i>\n' +
        '                    <span>Math Olympiad</span>\n' +
        '                </a>\n' +
        '                <a href="exam-prep.html#ap" class="dropdown-item">\n' +
        '                    <i class="fas fa-medal"></i>\n' +
        '                    <span>AP Prep</span>\n' +
        '                </a>\n' +
        '                <a href="tutoring.html" class="dropdown-item">\n' +
        '                    <i class="fas fa-user-graduate"></i>\n' +
        '                    <span>1-on-1 Tutoring</span>\n' +
        '                </a>\n' +
        '            </div>\n' +
        '        </div>\n' +
        '    </li>\n' +
        '    <li class="has-dropdown">\n' +
        '        <a href="grades.html">Grades</a>\n' +
        '        <div class="dropdown">\n' +
        '            <div class="dropdown-grid">\n' +
        '                <a href="grades.html#elementary" class="dropdown-item">\n' +
        '                    <i class="fas fa-child"></i>\n' +
        '                    <span>Elementary School</span>\n' +
        '                </a>\n' +
        '                <a href="grades.html#middle" class="dropdown-item">\n' +
        '                    <i class="fas fa-school"></i>\n' +
        '                    <span>Middle School</span>\n' +
        '                </a>\n' +
        '                <a href="grades.html#high" class="dropdown-item">\n' +
        '                    <i class="fas fa-university"></i>\n' +
        '                    <span>High School</span>\n' +
        '                </a>\n' +
        '                <a href="grades.html#college" class="dropdown-item">\n' +
        '                    <i class="fas fa-graduation-cap"></i>\n' +
        '                    <span>College</span>\n' +
        '                </a>\n' +
        '                <a href="grades.html#adult" class="dropdown-item">\n' +
        '                    <i class="fas fa-user-tie"></i>\n' +
        '                    <span>Adult Learning</span>\n' +
        '                </a>\n' +
        '            </div>\n' +
        '        </div>\n' +
        '    </li>\n' +
        '    <li class="has-dropdown">\n' +
        '        <a href="company.html">About Us</a>\n' +
        '        <div class="dropdown">\n' +
        '            <div class="dropdown-grid">\n' +
        '                <a href="company.html#about" class="dropdown-item">\n' +
        '                    <i class="fas fa-info-circle"></i>\n' +
        '                    <span>About</span>\n' +
        '                </a>\n' +
        '                <a href="company.html#careers" class="dropdown-item">\n' +
        '                    <i class="fas fa-briefcase"></i>\n' +
        '                    <span>Careers</span>\n' +
        '                </a>\n' +
        '                <a href="contact.html" class="dropdown-item">\n' +
        '                    <i class="fas fa-envelope"></i>\n' +
        '                    <span>Contact</span>\n' +
        '                </a>\n' +
        '                <a href="company.html#team" class="dropdown-item">\n' +
        '                    <i class="fas fa-users"></i>\n' +
        '                    <span>Our Team</span>\n' +
        '                </a>\n' +
        '            </div>\n' +
        '        </div>\n' +
        '    </li>\n' +
        '    <li><a href="contact.html">Contact</a></li>\n' +
        '    <li><a href="blog.html">Blog</a></li>\n' +
        '</ul>\n';
    }

    document.addEventListener('DOMContentLoaded', function() {
        var nav = document.querySelector('#nav');
        if (!nav) return;
        nav.innerHTML = buildNavHTML();
    });
})();

// Favicon setup for all pages
(function injectFavicon() {
    function getPrefixForFavicon() {
        var path = window.location.pathname || '';
        return path.indexOf('/topics/') !== -1 ? '../../' : '';
    }
    function ensureFavicon(href) {
        var head = document.head || document.getElementsByTagName('head')[0];
        if (!head) return;
        var selectors = ['link[rel="icon"]','link[rel="shortcut icon"]','link[rel="apple-touch-icon"]'];
        selectors.forEach(function(sel){ document.querySelectorAll(sel).forEach(function(n){ n.parentNode.removeChild(n); }); });
        var linkIcon = document.createElement('link');
        linkIcon.rel = 'icon';
        linkIcon.type = 'image/png';
        linkIcon.href = href;
        head.appendChild(linkIcon);
        var linkShortcut = document.createElement('link');
        linkShortcut.rel = 'shortcut icon';
        linkShortcut.type = 'image/png';
        linkShortcut.href = href;
        head.appendChild(linkShortcut);
        var appleIcon = document.createElement('link');
        appleIcon.rel = 'apple-touch-icon';
        appleIcon.href = href;
        head.appendChild(appleIcon);
    }
    document.addEventListener('DOMContentLoaded', function() {
        var prefix = getPrefixForFavicon();
        ensureFavicon(prefix + 'images/mongol.png');
    });
})();

// Modern Dropdown Navigation Functionality with mobile toggle injection
function toggleMobileNav() {
    const nav = document.getElementById('nav');
    if (!nav) return;
    nav.classList.toggle('mobile-open');
    const toggleBtn = document.querySelector('.mobile-menu-toggle');
    if (toggleBtn) toggleBtn.classList.toggle('active');
}

document.addEventListener('DOMContentLoaded', function() {
    function ensureTogglePresence() {
        const headerContainer = document.querySelector('#header .header-container');
        const existing = document.querySelector('.mobile-menu-toggle');
        if (!headerContainer) return;
        if (!existing) {
            const btn = document.createElement('button');
            btn.className = 'mobile-menu-toggle';
            btn.setAttribute('aria-label', 'Toggle navigation');
            btn.setAttribute('aria-expanded', 'false');
            btn.innerHTML = '<i class="fas fa-bars" aria-hidden="true"></i>';
            // Place it at the far right (as the last child) for mobile
            headerContainer.appendChild(btn);
            btn.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                toggleMobileNav();
                btn.setAttribute('aria-expanded', document.getElementById('nav').classList.contains('mobile-open') ? 'true' : 'false');
            });
        }
    }

    ensureTogglePresence();

    // Touch-friendly dropdowns: link navigates; caret toggles
    function setupMobileDropdowns() {
        const dropdownItems = document.querySelectorAll('#nav > ul > li.has-dropdown');
        dropdownItems.forEach(item => {
            const link = item.querySelector(':scope > a');
            if (!link) return;

            // Insert caret toggle if not present
            let caret = item.querySelector(':scope > button.nav-caret');
            if (!caret) {
                caret = document.createElement('button');
                caret.className = 'nav-caret';
                caret.type = 'button';
                caret.setAttribute('aria-label', 'Expand menu');
                caret.innerHTML = '<i class="fas fa-chevron-down" aria-hidden="true"></i>';
                item.appendChild(caret);
            }

            caret.onclick = function(e) {
                e.preventDefault();
                e.stopPropagation();
                const isOpen = item.classList.contains('mobile-open');
                // Close others, toggle current
                document.querySelectorAll('#nav > ul > li.has-dropdown').forEach(i => i.classList.remove('mobile-open'));
                item.classList.toggle('mobile-open', !isOpen);
            };
        });
    }

    if (window.innerWidth <= 1024) setupMobileDropdowns();

    // Close dropdowns when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.has-dropdown')) {
            document.querySelectorAll('#nav > ul > li.has-dropdown').forEach(item => item.classList.remove('mobile-open'));
        }
    });

    // Reset state on resize
    window.addEventListener('resize', function() {
        const nav = document.getElementById('nav');
        if (!nav) return;
        ensureTogglePresence();
        if (window.innerWidth <= 1024) {
            setupMobileDropdowns();
        } else {
            document.querySelectorAll('#nav > ul > li.has-dropdown').forEach(item => item.classList.remove('mobile-open'));
            nav.classList.remove('mobile-open');
            const toggleBtn = document.querySelector('.mobile-menu-toggle');
            if (toggleBtn) toggleBtn.classList.remove('active');
        }
    });
});

// Lightweight i18n (EN/MN) with language switcher
(function enableI18n() {
    var I18N = {
        en: {
            'nav.home': 'Home',
            'nav.examPrep': 'Exam Prep',
            'nav.grades': 'Grades',
            'nav.about': 'About Us',
            'nav.contact': 'Contact',
            'nav.blog': 'Blog',

            'footer.brand': 'Helping Mongol minds reach their full potential. Personalized tutoring and comprehensive resources.',
            'footer.services': 'Services',
            'footer.support': 'Support',
            'footer.connect': 'Connect',
            'footer.onlineTutoring': 'Online Tutoring',
            'footer.learningResources': 'Learning Resources',
            'footer.contactUs': 'Contact Us',
            'footer.emailUs': 'Email Us',
            'footer.about': 'About',
            'footer.blog': 'Blog',
            'footer.terms': 'Terms of Service',
            'footer.privacy': 'Privacy Policy',
            'footer.cookies': 'Cookie Policy',
            'footer.copyright': '© 2025 Mongol Potential. All rights reserved.',

            'policy.terms': 'Terms & Conditions',
            'policy.privacy': 'Privacy Policy',
            'policy.cookies': 'Cookie Policy',
            'policy.lastUpdated': 'Last updated:'
        },
        mn: {
            'nav.home': 'Нүүр',
            'nav.examPrep': 'Шалгалтын бэлтгэл',
            'nav.grades': 'Ангиуд',
            'nav.about': 'Бидний тухай',
            'nav.contact': 'Холбоо барих',
            'nav.blog': 'Блог',

            'footer.brand': 'Helping Mongol minds reach their full potential. Personalized tutoring and comprehensive resources.',
            'footer.services': 'Үйлчилгээ',
            'footer.support': 'Тусламж',
            'footer.connect': 'Холбогдох',
            'footer.onlineTutoring': 'Онлайн давтлага',
            'footer.learningResources': 'Сургалтын нөөц',
            'footer.contactUs': 'Бидэнтэй холбоо барих',
            'footer.emailUs': 'И-мэйл илгээх',
            'footer.about': 'Тухай',
            'footer.blog': 'Блог',
            'footer.terms': 'Үйлчилгээний нөхцөл',
            'footer.privacy': 'Нууцлалын бодлого',
            'footer.cookies': 'Күүки бодлого',
            'footer.copyright': '© 2025 Mongol Potential. Бүх эрх хамгаалагдсан.',

            'policy.terms': 'Үйлчилгээний нөхцөл',
            'policy.privacy': 'Нууцлалын бодлого',
            'policy.cookies': 'Күүки бодлого',
            'policy.lastUpdated': 'Сүүлийн шинэчлэл:'
        }
    };

    function getLang() {
        try {
            var saved = localStorage.getItem('imathhub_lang');
            if (saved) return saved;
        } catch (e) {}
        // default: English
        return 'en';
    }

    function setLang(lang) {
        try { localStorage.setItem('imathhub_lang', lang); } catch (e) {}
        document.documentElement.setAttribute('lang', lang);
        // Use curated translations for accuracy
        applyTranslations();
    }

    function t(key) {
        var lang = getLang();
        var dict = I18N[lang] || I18N.en;
        return dict[key] || I18N.en[key] || key;
    }

    function translateNav() {
        var nav = document.querySelector('#nav');
        if (!nav) return;
        nav.querySelectorAll(':scope > ul > li > a').forEach(function(a) {
            var href = (a.getAttribute('href') || '').toLowerCase();
            if (href.endsWith('index.html')) a.textContent = t('nav.home');
            else if (href.endsWith('exam-prep.html')) a.textContent = t('nav.examPrep');
            else if (href.endsWith('grades.html')) a.textContent = t('nav.grades');
            else if (href.endsWith('company.html')) a.textContent = t('nav.about');
            else if (href.endsWith('contact.html')) a.textContent = t('nav.contact');
            else if (href.endsWith('blog.html')) a.textContent = t('nav.blog');
        });
    }

    function translateFooter() {
        var footer = document.querySelector('#footer');
        if (!footer) return;
        // Headings
        footer.querySelectorAll('.footer-section h4').forEach(function(h4) {
            var txt = (h4.textContent || '').trim().toLowerCase();
            if (txt === 'services') h4.textContent = t('footer.services');
            else if (txt === 'support') h4.textContent = t('footer.support');
            else if (txt === 'connect') h4.textContent = t('footer.connect');
        });
        var brand = footer.querySelector('.footer-brand p');
        if (brand) brand.textContent = t('footer.brand');

        // Links by href
        footer.querySelectorAll('a').forEach(function(a) {
            var href = (a.getAttribute('href') || '').toLowerCase();
            if (href.indexOf('tutoring.html') !== -1) a.textContent = t('footer.onlineTutoring');
            else if (href.indexOf('exam-prep.html') !== -1) a.textContent = t('footer.learningResources');
            else if (href.indexOf('contact.html') !== -1) a.textContent = t('footer.contactUs');
            else if (href.indexOf('company.html') !== -1) a.textContent = t('footer.about');
            else if (href.indexOf('blog.html') !== -1) a.textContent = t('footer.blog');
            else if (href.indexOf('terms.html') !== -1) a.textContent = t('footer.terms');
            else if (href.indexOf('privacy.html') !== -1) a.textContent = t('footer.privacy');
            else if (href.indexOf('cookies.html') !== -1) a.textContent = t('footer.cookies');
        });

        var cr = footer.querySelector('.footer-bottom .footer-copyright p');
        if (cr) cr.textContent = t('footer.copyright');
    }

    function translatePolicyHeaders() {
        var h1 = document.querySelector('.policy header h1');
        if (h1) {
            var txt = (h1.textContent || '').trim().toLowerCase();
            if (txt.indexOf('terms') !== -1) h1.textContent = t('policy.terms');
            else if (txt.indexOf('privacy') !== -1) h1.textContent = t('policy.privacy');
            else if (txt.indexOf('cookie') !== -1) h1.textContent = t('policy.cookies');
        }
        var upd = document.querySelector('.policy header .text-secondary');
        if (upd) {
            var val = upd.textContent || '';
            var datePart = val.replace(/^[^:]*:/, '').trim();
            upd.textContent = t('policy.lastUpdated') + ' ' + datePart;
        }
    }

    function applyTranslations() {
        var lang = getLang();
        document.documentElement.setAttribute('lang', lang);
        // Curated dictionary-based translations for higher accuracy
        translateNav();
        translateFooter();
        translatePolicyHeaders();
    }

    function injectLangSwitcher() {
        var container = document.querySelector('#header .header-container');
        if (!container) return;
        if (document.querySelector('.lang-switcher')) return;

        // Inject minimal styles for visibility on white header
        if (!document.getElementById('lang-switcher-styles')) {
            var st = document.createElement('style');
            st.id = 'lang-switcher-styles';
            st.textContent = '\n.lang-switcher{position:relative;margin-left:12px;}\n.lang-btn{display:flex;align-items:center;gap:6px;padding:6px 10px;border:1px solid #E5E7EB;border-radius:8px;background:#ffffff;color:#1f2937;cursor:pointer;font-weight:600;}\n.lang-btn i{color:#1f2937;}\n.lang-menu{position:absolute;right:0;top:110%;background:#ffffff;border:1px solid #E5E7EB;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,0.08);padding:6px;display:none;z-index:1000;min-width:140px;}\n.lang-menu.open{display:block;}\n.lang-item{display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:6px;color:#1f2937;cursor:pointer;white-space:nowrap;}\n.lang-item:hover{background:#F3F4F6;}\n.lang-flag{font-size:16px;line-height:1;}\n@media (max-width: 480px){.lang-btn{padding:6px 8px}}\n';
            document.head.appendChild(st);
        }

        var wrap = document.createElement('div');
        wrap.className = 'lang-switcher';

        var btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'lang-btn';
        btn.setAttribute('aria-haspopup', 'menu');
        btn.setAttribute('aria-expanded', 'false');
        btn.innerHTML = '<i class="fas fa-globe" aria-hidden="true"></i><span class="lang-label"></span>';

        var menu = document.createElement('div');
        menu.className = 'lang-menu';
        menu.setAttribute('role', 'menu');
        menu.innerHTML = '\n            <div class="lang-item" data-lang="en" role="menuitem"><span class="lang-flag">🇺🇸</span><span>English</span></div>\n            <div class="lang-item" data-lang="mn" role="menuitem"><span class="lang-flag">🇲🇳</span><span>Монгол</span></div>\n        ';

        function updateLabel() {
            var current = getLang();
            var label = btn.querySelector('.lang-label');
            label.textContent = current === 'mn' ? 'MN' : 'EN';
        }

        btn.addEventListener('click', function(e){
            e.preventDefault();
            var isOpen = menu.classList.contains('open');
            menu.classList.toggle('open', !isOpen);
            btn.setAttribute('aria-expanded', String(!isOpen));
        });

        menu.addEventListener('click', function(e){
            var item = e.target.closest('.lang-item');
            if (!item) return;
            var lang = item.getAttribute('data-lang');
            setLang(lang);
            updateLabel();
            menu.classList.remove('open');
            btn.setAttribute('aria-expanded', 'false');
        });

        document.addEventListener('click', function(e){
            if (!wrap.contains(e.target)) {
                menu.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
            }
        });

        document.addEventListener('keydown', function(e){
            if (e.key === 'Escape') {
                menu.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
            }
        });

        updateLabel();
        wrap.appendChild(btn);
        wrap.appendChild(menu);
        container.appendChild(wrap);
    }

    document.addEventListener('DOMContentLoaded', function() {
        injectLangSwitcher();
        // Defer to ensure footer has been injected
        setTimeout(applyTranslations, 0);
    });
    window.addEventListener('footer:ready', applyTranslations);
})();