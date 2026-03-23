// --- NAVIGATION & MOBILE MENU ---
const nav = document.querySelector('.sticky-nav');
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navLinksGroup = document.querySelector('.nav-links');

if (nav) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });
}

if (mobileMenuBtn && navLinksGroup) {
    mobileMenuBtn.addEventListener('click', () => {
        nav.classList.toggle('mobile-active');
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }
    });
}

// Ensure mobile menu resets on window resize
window.addEventListener('resize', () => {
    if (window.innerWidth > 992) {
        if (nav && nav.classList.contains('mobile-active')) {
            nav.classList.remove('mobile-active');
            const icon = mobileMenuBtn ? mobileMenuBtn.querySelector('i') : null;
            if (icon) {
                icon.classList.add('fa-bars');
                icon.classList.remove('fa-times');
            }
        }
    }
});

// --- DYNAMIC SERVICE SYSTEM (DASHBOARDS) ---

/**
 * Global Service Application
 * Handles both initial load and manual switches
 */
window.applyServiceGlobal = (service) => {
    if (!service) return;

    // 1. Remove any old service classes from body
    document.body.classList.remove('user-seo', 'user-website');
    
    // 2. Add the new service class
    document.body.classList.add(`user-${service}`);
    
    // 3. Update dynamic text elements
    const logoText = document.getElementById('logoText');
    const footerLogoText = document.getElementById('footerLogoText');
    const giantTextLogo = document.getElementById('giantTextLogo');
    const switchBtn = document.getElementById('serviceSwitcher');

    if (service === 'website') {
        if (logoText) logoText.textContent = 'WEB';
        if (footerLogoText) footerLogoText.textContent = 'WEB';
        if (giantTextLogo) giantTextLogo.textContent = 'WEB DESIGN';
        if (switchBtn) {
            const span = switchBtn.querySelector('span');
            if (span) span.innerHTML = 'Move To<br>SEO';
        }
    } else {
        if (logoText) logoText.textContent = 'SEO';
        if (footerLogoText) footerLogoText.textContent = 'SEO';
        if (giantTextLogo) giantTextLogo.textContent = 'SEO EXPERT';
        if (switchBtn) {
            const span = switchBtn.querySelector('span');
            if (span) span.innerHTML = 'Move To<br>WEB';
        }
    }

    // 4. Reset & Refresh Animations for the newly visible content
    initAnimations();
    if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.refresh();
    }
};

/**
 * Handle Service Selection
 */
window.selectService = (service) => {
    localStorage.setItem('selectedService', service);
    const modal = document.getElementById('serviceModal');
    
    // Check if gsap is available
    if (typeof gsap !== 'undefined' && modal) {
        gsap.to(modal, {
            opacity: 0,
            duration: 0.5,
            onComplete: () => {
                modal.classList.remove('active');
                modal.remove(); // Clean up from DOM
                window.applyServiceGlobal(service);
            }
        });
    } else {
        if (modal) {
            modal.classList.remove('active');
            modal.remove();
        }
        window.applyServiceGlobal(service);
    }
};

/**
 * Inject Selection Modal into the page if not selected
 */
const injectServiceModal = () => {
    if (document.getElementById('serviceModal')) return;

    const modalHTML = `
        <div id="serviceModal" class="selection-modal">
            <div class="modal-content glass-card">
                <div class="modal-header text-center">
                    <span class="badge">Welcome</span>
                    <h2 class="reveal-up">Select Your Interest</h2>
                    <p class="reveal-up">Personalize your experience on our platform.</p>
                </div>
                <div class="service-options">
                    <div class="option-card glass-card reveal-up" onclick="selectService('seo')">
                        <div class="option-icon"><i class="fas fa-chart-line" style="color: var(--cyan-secondary);"></i></div>
                        <h3>SEO Expertise</h3>
                        <p>Dominating organic search & technical excellence.</p>
                        <span class="btn btn-outline btn-sm">Explore SEO Dashboard</span>
                    </div>
                    <div class="option-card glass-card reveal-up" onclick="selectService('website')">
                        <div class="option-icon"><i class="fas fa-laptop-code" style="color: var(--purple-accent);"></i></div>
                        <h3>Web Design</h3>
                        <p>Building premium, high-performance websites & UI/UX.</p>
                        <span class="btn btn-primary btn-sm" style="background: var(--purple-accent);">Explore Web Dashboard</span>
                    </div>
                </div>
            </div>
        </div>
    `;

    document.body.insertAdjacentHTML('beforeend', modalHTML);
    const modal = document.getElementById('serviceModal');
    
    // Add Mouse Glow Logic
    modal.addEventListener('mousemove', (e) => {
        const cards = modal.querySelectorAll('.option-card');
        cards.forEach(card => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            card.style.setProperty('--x', `${x}px`);
            card.style.setProperty('--y', `${y}px`);
        });
    });

    // Force a small delay to ensure DOM is ready, then add class
    setTimeout(() => {
        if (modal) {
            modal.classList.add('active');
            if (typeof gsap !== 'undefined') {
                gsap.from(modal.querySelector('.modal-content'), {
                    scale: 0.9,
                    y: 40,
                    opacity: 0,
                    duration: 1.2,
                    ease: 'expo.out'
                });
                gsap.from(modal.querySelectorAll('.option-card'), {
                    y: 60,
                    opacity: 0,
                    duration: 1,
                    stagger: 0.2,
                    delay: 0.3,
                    ease: 'power3.out'
                });
            }
        }
    }, 10);
};

// --- GSAP ANIMATIONS ---
function initAnimations() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') return;

    gsap.registerPlugin(ScrollTrigger);

    // Initial state setup
    gsap.set('.reveal-up', { opacity: 0, y: 30 });

    // Reveal elements on scroll
    ScrollTrigger.batch('.reveal-up', {
        onEnter: (elements) => {
            gsap.to(elements, {
                opacity: 1,
                y: 0,
                duration: 0.8,
                stagger: 0.15,
                ease: 'power3.out',
                overwrite: true
            });
        },
        start: 'top 85%',
        once: true
    });

    // Giant text marquee-like animation on scroll
    const giantText = document.querySelector('.giant-text');
    if (giantText) {
        gsap.to(giantText, {
            scrollTrigger: {
                trigger: '.footer',
                start: 'top bottom',
                end: 'bottom bottom',
                scrub: 1
            },
            opacity: 1,
            x: -20,
            ease: 'none'
        });
    }
}

// --- FAQ ACCORDION ---
function initFAQ() {
    const faqQuestions = document.querySelectorAll('.faq-question');
    faqQuestions.forEach(question => {
        question.addEventListener('click', () => {
            const item = question.parentElement;
            item.classList.toggle('active');
        });
    });
}

/**
 * Core Initialization
 */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Force Selection on Index Page Reload
    const isHomePage = window.location.pathname.endsWith('index.html') || window.location.pathname === '/' || window.location.pathname.endsWith('/');
    const savedService = localStorage.getItem('selectedService');
    
    if (isHomePage) {
        // Always show modal on home page as requested
        injectServiceModal();
        if (savedService) applyServiceGlobal(savedService); // Apply default but keep modal visible
    } else {
        // For subpages, use saved preference or default to SEO
        applyServiceGlobal(savedService || 'seo');
    }

    // 2. Initialize FAQ logic
    initFAQ();

    // 3. Initialize Blog Filters (if on blog page)
    initBlogFilters();

    // 4. Setup GSAP
    initAnimations();
});

/**
 * Blog Filtering & Search Engine
 */
function initBlogFilters() {
    const searchInput = document.querySelector('.search-input-group input');
    const tags = document.querySelectorAll('.tag');
    const posts = document.querySelectorAll('.blog-card');

    if (!searchInput || !posts.length) return;

    function filterPosts() {
        const searchTerm = searchInput.value.toLowerCase();
        const activeTag = document.querySelector('.tag.active').textContent.toLowerCase();

        posts.forEach(post => {
            const title = post.querySelector('h3').textContent.toLowerCase();
            const content = post.querySelector('p').textContent.toLowerCase();
            const textMatch = title.includes(searchTerm) || content.includes(searchTerm);
            
            // Basic tag logic
            const tagMatch = activeTag === 'all insights' || 
                             title.includes(activeTag) || 
                             content.includes(activeTag) ||
                             searchTerm.includes(activeTag);

            if (textMatch && tagMatch) {
                if (post.style.display === 'none') {
                    post.style.display = 'flex';
                    gsap.fromTo(post, {opacity: 0, y: 20}, {opacity: 1, y: 0, duration: 0.4});
                }
            } else {
                post.style.display = 'none';
            }
        });
    }

    // Input Search listener
    searchInput.addEventListener('input', filterPosts);

    // Tag click listener
    tags.forEach(tag => {
        tag.addEventListener('click', () => {
            tags.forEach(t => t.classList.remove('active'));
            tag.classList.add('active');
            filterPosts();
        });
    });
}

/**
 * Re-export manual toggle
 */
window.toggleService = () => {
    const current = localStorage.getItem('selectedService') || 'seo';
    const next = current === 'seo' ? 'website' : 'seo';
    window.selectService(next);
};
