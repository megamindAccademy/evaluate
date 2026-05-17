// Encouraging and pampering messages for kids (رسايل تشجيعية ودلع للأطفال)
const messages = [
    "🌟 يا بطل ميجامايندز الخارق! ذكائك يضيء العالم كله، استمر يا مبدع!",
    "🚀 أنت عبقري المستقبل! كل سطر كود تكتبه يجعلك أقرب لتحقيق أحلامك الكبيرة!",
    "💖 يا سكر الأكاديمية! ابتسامتك الجميلة وحماسك للتعلم يفرح قلوبنا جميعاً!",
    "🤖 يا مهندس الروبوتات الذكي! أفكارك مذهلة ومستقبلك مشرق مثل النجوم!",
    "✨ يا نجم البرمجة اللامع! لا يوجد شيء صعب عليك، أنت بطل التحديات!",
    "🎉 حماسك رائع يا فنان! نحن فخورون جداً بوجودك معنا في عائلة ميجامايندز!",
    "💡 يا صاحب الأفكار الذهبية! تفكيرك الإبداعي سيجعل العالم مكاناً أجمل بكثير!",
    "👑 يا ملك التقنية الصغير! واصل إبداعك، الأكاديمية كلها تصفق لنجاحك!",
    "🌈 يا شمس ميجامايندز المشرقة! تعلمك اليوم يصنع مستقبلك العظيم غداً!",
    "🏆 أنت بطل حقيقي! كل خطوة تخطوها في التعلم هي انتصار كبير نفتخر به!"
];

// --- FIREBASE REALTIME DATABASE CONFIGURATION ---
const firebaseConfig = {
  apiKey: "AIzaSyCmTP8whtgR5IKF59Bi_olMvNsVw2LaSsI",
  authDomain: "megamindsacademy-ev.firebaseapp.com",
  databaseURL: "https://megamindsacademy-ev-default-rtdb.firebaseio.com",
  projectId: "megamindsacademy-ev",
  storageBucket: "megamindsacademy-ev.firebasestorage.app",
  messagingSenderId: "329252604781",
  appId: "1:329252604781:web:4d6583392031571258a864"
};

// Initialize Firebase & Analytics if available
try {
    if (typeof firebase !== 'undefined') {
        if (firebase.apps.length === 0) {
            firebase.initializeApp(firebaseConfig);
        }
        if (firebase.analytics) {
            firebase.analytics();
            console.log("Firebase Analytics initialized successfully in script.js!");
        }
    }
} catch (e) {
    console.error("Firebase Analytics initialization error:", e);
}

// Web Audio API for synthesized cheerful sound effects
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playHappyChime() {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    const now = audioCtx.currentTime;
    const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
    notes.forEach((freq, index) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0, now + index * 0.1);
        gain.gain.linearRampToValueAtTime(0.3, now + index * 0.1 + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, now + index * 0.1 + 0.4);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + index * 0.1);
        osc.stop(now + index * 0.1 + 0.45);
    });
}

function playPopupSound() {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(440, now); // A4
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.2); // A5
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.4, now + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.35);
}

// Lightweight Custom Confetti Animation
function triggerConfetti() {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '9999';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const pieces = [];
    const numberOfPieces = 150;
    const colors = ['#ff7b00', '#ffb703', '#219ebc', '#8338ec', '#06d6a0', '#ff6b8b'];

    for (let i = 0; i < numberOfPieces; i++) {
        pieces.push({
            x: canvas.width * Math.random(),
            y: canvas.height * Math.random() - canvas.height,
            rotation: Math.random() * 360,
            rotationSpeed: (Math.random() - 0.5) * 10,
            size: Math.random() * 12 + 8,
            speedY: Math.random() * 5 + 3,
            speedX: (Math.random() - 0.5) * 4,
            color: colors[Math.floor(Math.random() * colors.length)],
            shape: Math.random() > 0.5 ? 'circle' : 'rect'
        });
    }

    let startTime = Date.now();
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let activePieces = 0;

        pieces.forEach(p => {
            p.y += p.speedY;
            p.x += p.speedX;
            p.rotation += p.rotationSpeed;
            if (p.y < canvas.height) activePieces++;

            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate((p.rotation * Math.PI) / 180);
            ctx.fillStyle = p.color;
            if (p.shape === 'circle') {
                ctx.beginPath();
                ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
                ctx.fill();
            } else {
                ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
            }
            ctx.restore();
        });

        if (activePieces > 0 && Date.now() - startTime < 5000) {
            requestAnimationFrame(animate);
        } else {
            if (canvas.parentNode) document.body.removeChild(canvas);
        }
    }
    animate();
}

// DOM Elements & Auto Discovery Logic
document.addEventListener('DOMContentLoaded', () => {
    const encourageBtn = document.getElementById('btnEncourage');
    const messageDisplay = document.getElementById('messageDisplay');
    const modalOverlay = document.getElementById('modalOverlay');
    const modalTitle = document.getElementById('modalTitle');
    const modalText = document.getElementById('modalText');
    const modalCloseBtn = document.getElementById('modalClose');
    const modalOkBtn = document.getElementById('modalOkBtn');
    const dynamicCoursesGrid = document.getElementById('dynamicCoursesGrid');
    const dynamicCurriculumsGrid = document.getElementById('dynamicCurriculumsGrid');

    // Encouragement Button Click
    if (encourageBtn) {
        encourageBtn.addEventListener('click', () => {
            playHappyChime();
            triggerConfetti();

            // Pick a random message
            const randomMsg = messages[Math.floor(Math.random() * messages.length)];
            messageDisplay.textContent = randomMsg;
            
            // Re-trigger animation
            messageDisplay.classList.remove('active');
            void messageDisplay.offsetWidth; // Trigger reflow
            messageDisplay.classList.add('active');
        });
    }

    // Modal Close Helpers
    const closeModal = () => {
        if (modalOverlay) modalOverlay.classList.remove('active');
    };

    if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
    if (modalOkBtn) modalOkBtn.addEventListener('click', closeModal);
    if (modalOverlay) {
        modalOverlay.addEventListener('click', (e) => {
            if (e.target === modalOverlay) closeModal();
        });
    }

    // ==========================================
    // AUTO DISCOVERY OF COURSES & CURRICULUMS
    // ==========================================
    if (dynamicCoursesGrid || dynamicCurriculumsGrid) {
        fetch('./database/courses_index.json')
            .then(response => {
                if (!response.ok) throw new Error('courses_index.json not found');
                return response.json();
            })
            .then(coursesList => {
                coursesList.forEach(courseId => {
                    fetch(`./database/${courseId}/manifest.json`)
                        .then(res => {
                            if (!res.ok) throw new Error(`Manifest not found for ${courseId}`);
                            return res.json();
                        })
                        .then(manifest => {
                            if (dynamicCurriculumsGrid) {
                                renderDiscoveredCurriculumCard(manifest, dynamicCurriculumsGrid, modalOverlay, modalTitle, modalText);
                            }
                            if (dynamicCoursesGrid) {
                                renderDiscoveredCourseCard(manifest, dynamicCoursesGrid, modalOverlay, modalTitle, modalText);
                            }
                        })
                        .catch(err => console.error(`Error discovering course ${courseId}:`, err));
                });
            })
            .catch(error => console.error('Error loading courses index:', error));
    }
});

// Render Discovered Curriculum Card Helper
function renderDiscoveredCurriculumCard(manifest, gridEl, modalOverlay, modalTitle, modalText) {
    const card = document.createElement('article');
    card.className = 'curriculum-card';
    card.id = `curr_card_${manifest.course_id}`;

    const isActive = (manifest.status === 'active');
    const badgeClass = isActive ? 'badge-active' : 'badge-upcoming';
    const badgeText = isActive ? 'منهج تفاعلي 🌟' : 'قريباً ⏳';

    card.innerHTML = `
        <span class="card-badge ${badgeClass}">${badgeText}</span>
        <div class="card-icon ${manifest.icon_bg_class || 'icon-main'}">${manifest.icon || '📚'}</div>
        <h3 class="card-title">${manifest.course_title}</h3>
        <p class="card-desc">${manifest.desc}</p>
    `;

    if (isActive) {
        // Active Direct Link Button
        const linkBtn = document.createElement('a');
        linkBtn.href = `./curriculum.html?course=${manifest.course_id}`;
        linkBtn.className = 'card-btn btn-curriculum-card';
        linkBtn.innerHTML = `<span>📖 ادخل المنهج التفاعلي 🚀</span>`;
        card.appendChild(linkBtn);
    } else {
        // Upcoming Modal Popup Button
        const modalBtn = document.createElement('button');
        modalBtn.className = 'card-btn btn-upcoming';
        modalBtn.innerHTML = `<span>أنا مستعد للمغامرة! 💪</span>`;
        modalBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (modalTitle) modalTitle.textContent = `منهج ${manifest.course_title}`;
            if (modalText) modalText.textContent = manifest.upcoming_msg || 'هذا المنهج التفاعلي قيد التجهيز في مختبراتنا السحرية!';
            if (modalOverlay) modalOverlay.classList.add('active');
            playPopupSound();
            triggerConfetti();
        });
        card.appendChild(modalBtn);
    }

    gridEl.appendChild(card);
}

// Render Discovered Course Card Helper
function renderDiscoveredCourseCard(manifest, gridEl, modalOverlay, modalTitle, modalText) {
    const card = document.createElement('article');
    card.className = 'quiz-card';
    card.id = `card_${manifest.course_id}`;

    const isActive = (manifest.status === 'active');
    const badgeClass = isActive ? 'badge-active' : 'badge-upcoming';
    const badgeText = isActive ? 'متاح الآن 🌟' : 'قريباً ⏳';

    card.innerHTML = `
        <span class="card-badge ${badgeClass}">${badgeText}</span>
        <div class="card-icon ${manifest.icon_bg_class || 'icon-main'}">${manifest.icon || '📚'}</div>
        <h3 class="card-title">${manifest.course_title}</h3>
        <p class="card-desc">${manifest.desc}</p>
    `;

    if (isActive) {
        // Active Direct Link Button
        const linkBtn = document.createElement('a');
        linkBtn.href = `./quiz.html?course=${manifest.course_id}`;
        linkBtn.className = 'card-btn btn-active';
        linkBtn.innerHTML = `<span>ابدأ التحدي والاختبار 🚀</span>`;
        card.appendChild(linkBtn);
    } else {
        // Upcoming Modal Popup Button
        const modalBtn = document.createElement('button');
        modalBtn.className = 'card-btn btn-upcoming';
        modalBtn.innerHTML = `<span>أنا مستعد للتحدي! 💪</span>`;
        modalBtn.addEventListener('click', (e) => {
            e.preventDefault();
            if (modalTitle) modalTitle.textContent = `اختبار ${manifest.course_title}`;
            if (modalText) modalText.textContent = manifest.upcoming_msg || 'هذا التحدي قيد التجهيز في مختبراتنا!';
            if (modalOverlay) modalOverlay.classList.add('active');
            playPopupSound();
            triggerConfetti();
        });
        card.appendChild(modalBtn);
    }

    gridEl.appendChild(card);
}
