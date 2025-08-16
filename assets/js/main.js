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
        return '\n            <div class="footer-content">\n                <div class="footer-section">\n                    <div class="footer-brand">\n                        <h3>International Math Hub</h3>\n                        <p>Empowering Mongolian students with world-class mathematics education. Expert tutors, personalized learning, and comprehensive resources for every grade level.</p>\n                    </div>\n                </div>\n                <div class="footer-section">\n                    <h4>Services</h4>\n                    <ul>\n                        <li><a href="' + prefix + 'tutoring.html">Online Tutoring</a></li>\n                        <li><a href="' + prefix + 'exam-prep.html">Learning Resources</a></li>\n                    </ul>\n                </div>\n                <div class="footer-section">\n                    <h4>Support</h4>\n                    <ul>\n                        <li><a href="' + prefix + 'contact.html">Contact Us</a></li>\n                        <li><a href="mailto:imathhub@gmail.com">Email Us</a></li>\n                        <li><a href="' + prefix + 'about.html">About</a></li>\n                        <li><a href="' + prefix + 'blog.html">Blog</a></li>\n\n                    </ul>\n                </div>\n                <div class="footer-section">\n                    <h4>Connect</h4>\n                    <div class="social-links">\n                        <a href="mailto:imathhub@gmail.com" class="social-link" title="Email"><i class="fas fa-envelope"></i></a>\n                        <a href="https://www.facebook.com/mongolmath/" class="social-link" title="Facebook"><i class="fab fa-facebook-f"></i></a>\n                        <a href="https://www.youtube.com/@InternationalMathematicsHub" class="social-link" title="YouTube"><i class="fab fa-youtube"></i></a>\n                        <a href="https://x.com/mongolmath" class="social-link" title="X"><i class="fab fa-twitter"></i></a>\n                        <a href="https://www.instagram.com/mongolmath/" class="social-link" title="Instagram"><i class="fab fa-instagram"></i></a>\n                    </div>\n                </div>\n            </div>\n            <div class="footer-bottom">\n                <div class="footer-bottom-content">\n                    <div class="footer-legal">\n                        <ul>\n                            <li><a href="#">Terms of Service</a></li>\n                            <li><a href="#">Privacy Policy</a></li>\n                            <li><a href="#">Cookie Policy</a></li>\n                        </ul>\n                    </div>\n                    <div class="footer-copyright">\n                        <p>&copy; 2025 International Math Hub. All rights reserved.</p>\n                    </div>\n                </div>\n            </div>\n        ';
    }

    document.addEventListener('DOMContentLoaded', function() {
        var footer = document.querySelector('#footer');
        if (!footer) return;
        var prefix = getPrefix();
        footer.innerHTML = buildFooterHTML(prefix);
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
        ensureFavicon(prefix + 'images/logo.png');
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