/*
	Dopetrope by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function($) {

	var	$window = $(window),
		$body = $('body');

	// Breakpoints.
		breakpoints({
			xlarge:  [ '1281px',  '1680px' ],
			large:   [ '981px',   '1280px' ],
			medium:  [ '737px',   '980px'  ],
			small:   [ null,      '736px'  ]
		});

	// Play initial animations on page load.
		$window.on('load', function() {
			window.setTimeout(function() {
				$body.removeClass('is-preload');
			}, 100);
		});

	// Dropdowns.
		$('#nav > ul').dropotron({
			mode: 'fade',
			noOpenerFade: true,
			alignment: 'center'
		});

	// Nav.
    // Mobile navigation has been removed as requested

		// Title Bar and Panel have been removed
    
})(jQuery);

document.addEventListener('DOMContentLoaded', function() {
    const sections = document.querySelectorAll('.fullscreen-section');
    let currentSection = 0;
    let isScrolling = false;
    let touchStartY = 0;

    // Set initial active section
    sections[0].classList.add('active');

    function scrollToSection(index) {
        if (index >= 0 && index < sections.length && !isScrolling) {
            isScrolling = true;
            
            // Remove active class from current section
            sections[currentSection].classList.remove('active');
            
            // Add active class to new section
            sections[index].classList.add('active');
            
            // Smooth scroll to the section
            sections[index].scrollIntoView({ behavior: 'smooth' });
            
            currentSection = index;
            
            // Reset scrolling lock after animation
            setTimeout(() => {
                isScrolling = false;
            }, 1000);
        }
    }

    // Handle mouse wheel scrolling
    window.addEventListener('wheel', function(e) {
        e.preventDefault();
        if (!isScrolling) {
            if (e.deltaY > 0) {
                scrollToSection(currentSection + 1);
            } else {
                scrollToSection(currentSection - 1);
            }
        }
    }, { passive: false });

    // Handle touch events for mobile
    document.addEventListener('touchstart', function(e) {
        touchStartY = e.touches[0].clientY;
    }, { passive: true });

    document.addEventListener('touchmove', function(e) {
        if (isScrolling) return;
        
        const touchEndY = e.touches[0].clientY;
        const diff = touchStartY - touchEndY;
        
        if (Math.abs(diff) > 50) { // Minimum swipe distance
            if (diff > 0) {
                scrollToSection(currentSection + 1);
            } else {
                scrollToSection(currentSection - 1);
            }
        }
    }, { passive: false });

    // Optional: Add keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
            scrollToSection(currentSection + 1);
        } else if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
            scrollToSection(currentSection - 1);
        }
    });
});