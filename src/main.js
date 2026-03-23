// --- NAVIGATION & MOBILE MENU ---
const nav = document.querySelector('.sticky-nav');
const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
const navLinks = document.querySelector('.nav-links');

window.addEventListener('scroll', () => {
    if (nav && window.scrollY > 50) {
        nav.classList.add('scrolled');
    } else if (nav) {
        nav.classList.remove('scrolled');
    }
});

if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
        nav.classList.toggle('mobile-active');
        const icon = mobileMenuBtn.querySelector('i');
        if (icon) {
            icon.classList.toggle('fa-bars');
            icon.classList.toggle('fa-times');
        }
    });
}

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
        if (switchBtn) switchBtn.innerHTML = 'Move to SEO Dashboard';
    } else {
        if (logoText) logoText.textContent = 'SEO';
        if (footerLogoText) footerLogoText.textContent = 'SEO';
        if (giantTextLogo) giantTextLogo.textContent = 'SEO EXPERT';
        if (switchBtn) switchBtn.innerHTML = 'Move to Website Dashboard';
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
    
    // Force a small delay to ensure DOM is ready, then add class
    setTimeout(() => {
        if (modal) {
            modal.classList.add('active');
            if (typeof gsap !== 'undefined') {
                gsap.from(modal.querySelector('.modal-content'), {
                    y: 30,
                    opacity: 0,
                    duration: 0.8,
                    ease: 'power3.out'
                });
            }
        }
    }, 10);
};

/**
 * Switch Service (Manual Toggle)
 */
window.toggleService = () => {
    const current = localStorage.getItem('selectedService') || 'seo';
    const next = current === 'seo' ? 'website' : 'seo';
    window.selectService(next);
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
            opacity: 0.2,
            x: -100,
            ease: 'none'
        });
    }
}

// --- FAQ SYSTEM ---
const initFAQ = () => {
    const questions = document.querySelectorAll('.faq-question');
    questions.forEach(q => {
        q.addEventListener('click', () => {
            const item = q.parentElement;
            const isActive = item.classList.contains('active');
            
            // Close all other items for a clean accordion effect
            document.querySelectorAll('.faq-item').forEach(el => el.classList.remove('active'));
            
            if (isActive) {
                item.classList.remove('active');
            } else {
                item.classList.add('active');
            }
        });
    });
};

// --- INITIALIZATION ---
window.addEventListener('DOMContentLoaded', () => {
    // 1. Check URL Parameters for Deep Linking (e.g. ?service=website)
    const urlParams = new URLSearchParams(window.location.search);
    const serviceParam = urlParams.get('service');
    
    if (serviceParam === 'seo' || serviceParam === 'website') {
        localStorage.setItem('selectedService', serviceParam);
        window.applyServiceGlobal(serviceParam);
        return;
    }

    // 2. Check localStorage
    const savedService = localStorage.getItem('selectedService');
    
    if (savedService) {
        window.applyServiceGlobal(savedService);
    } else {
        // 3. Show Modal if no selection exists on ANY page
        injectServiceModal();
    }
    
    // 4. Initialize FAQ
    initFAQ();
});

// Refresh ScrollTrigger on resize
window.addEventListener('resize', () => {
    if (typeof ScrollTrigger !== 'undefined') {
        ScrollTrigger.refresh();
    }
});
