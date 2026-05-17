// ==========================================
// ENGINEER PORTAL LOGIC & STORAGE ADAPTER
// ==========================================

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

let db = null;
try {
    if (typeof firebase !== 'undefined') {
        firebase.initializeApp(firebaseConfig);
        db = firebase.database();
        if (firebase.analytics) {
            firebase.analytics();
            console.log("Firebase Analytics initialized successfully in engineer.js!");
        }
        console.log("Firebase Realtime Database initialized successfully in engineer.js!");
    }
} catch (e) {
    console.error("Firebase init error:", e);
}

// DOM Elements
let viewLogin, viewDashboard, viewEvaluation;
let loginFormEl, inputUsernameEl, inputPasswordEl, loginErrorEl;
let btnLogoutEl, searchSubmissionsEl, filterStatusEl, submissionsGridEl;
let totalSubmissionsCountEl, pendingSubmissionsCountEl;
let studentEvalMetaEl, evalAnswersListEl, btnBackDashboardEl, btnSaveEvaluationEl, btnPrintEvalReportEl;
let btnRestoreHiddenEl, hiddenSubmissionsCountEl;

// App State
let currentSubmissions = [];
let currentSelectedSubmission = null;

// BiDi Text Helper for Code Snippets & Mixed Arabic/English Text
function cleanBiDiText(text) {
    if (!text) return '';
    const hasArabic = /[\u0600-\u06FF]/.test(text);
    if (!hasArabic) {
        return `<span dir="ltr" style="display: inline-block; direction: ltr; unicode-bidi: bidi-override; font-family: 'Courier New', Courier, monospace; font-size: 1.1em; font-weight: bold;">${text}</span>`;
    } else {
        return text.replace(/([a-zA-Z0-9_().=/'"*#\-]+(?:[ ]+[a-zA-Z0-9_().=/'"*#\-]+)*)/g, '<span dir="ltr" style="display: inline-block; direction: ltr; unicode-bidi: isolate; font-family: \'Courier New\', Courier, monospace; font-size: 1.1em; font-weight: bold; padding: 0 4px; color: var(--primary);">$1</span>');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Elements
    viewLogin = document.getElementById('viewLogin');
    viewDashboard = document.getElementById('viewDashboard');
    viewEvaluation = document.getElementById('viewEvaluation');

    loginFormEl = document.getElementById('engineerLoginForm');
    inputUsernameEl = document.getElementById('inputUsername');
    inputPasswordEl = document.getElementById('inputPassword');
    loginErrorEl = document.getElementById('loginError');
    btnLogoutEl = document.getElementById('btnLogout');

    searchSubmissionsEl = document.getElementById('searchSubmissions');
    filterStatusEl = document.getElementById('filterStatus');
    submissionsGridEl = document.getElementById('submissionsGrid');
    totalSubmissionsCountEl = document.getElementById('totalSubmissionsCount');
    pendingSubmissionsCountEl = document.getElementById('pendingSubmissionsCount');
    btnRestoreHiddenEl = document.getElementById('btnRestoreHidden');
    hiddenSubmissionsCountEl = document.getElementById('hiddenSubmissionsCount');

    studentEvalMetaEl = document.getElementById('studentEvalMeta');
    evalAnswersListEl = document.getElementById('evalAnswersList');
    btnBackDashboardEl = document.getElementById('btnBackDashboard');
    btnSaveEvaluationEl = document.getElementById('btnSaveEvaluation');
    btnPrintEvalReportEl = document.getElementById('btnPrintEvalReport');

    // Event Listeners
    if (loginFormEl) loginFormEl.addEventListener('submit', handleLogin);
    if (btnLogoutEl) btnLogoutEl.addEventListener('click', handleLogout);
    if (searchSubmissionsEl) searchSubmissionsEl.addEventListener('input', renderSubmissions);
    if (filterStatusEl) filterStatusEl.addEventListener('change', renderSubmissions);
    if (btnRestoreHiddenEl) btnRestoreHiddenEl.addEventListener('click', restoreAllHiddenSubmissions);
    if (btnBackDashboardEl) btnBackDashboardEl.addEventListener('click', () => showView(viewDashboard));
    if (btnSaveEvaluationEl) btnSaveEvaluationEl.addEventListener('click', saveEvaluation);
    if (btnPrintEvalReportEl) btnPrintEvalReportEl.addEventListener('click', () => window.print());

    // Dashboard Section Tabs Switching Logic
    const tabSubmissionsBtn = document.getElementById('tabSubmissionsBtn');
    const tabAidsBtn = document.getElementById('tabAidsBtn');
    const tabSettingsBtn = document.getElementById('tabSettingsBtn');
    const sectionSubmissions = document.getElementById('sectionSubmissions');
    const sectionTeachingAids = document.getElementById('sectionTeachingAids');
    const sectionSettings = document.getElementById('sectionSettings');

    const switchDashTab = (activeTabBtn, activeSection) => {
        [tabSubmissionsBtn, tabAidsBtn, tabSettingsBtn].forEach(b => b && b.classList.remove('active'));
        [sectionSubmissions, sectionTeachingAids, sectionSettings].forEach(s => s && (s.style.display = 'none'));
        
        if (activeTabBtn) activeTabBtn.classList.add('active');
        if (activeSection) activeSection.style.display = 'block';
    };

    if (tabSubmissionsBtn) tabSubmissionsBtn.addEventListener('click', () => switchDashTab(tabSubmissionsBtn, sectionSubmissions));
    if (tabAidsBtn) tabAidsBtn.addEventListener('click', () => switchDashTab(tabAidsBtn, sectionTeachingAids));
    if (tabSettingsBtn) tabSettingsBtn.addEventListener('click', () => switchDashTab(tabSettingsBtn, sectionSettings));

    // Clear LocalStorage Logic
    const btnClearLocalStorage = document.getElementById('btnClearLocalStorage');
    const clearStorageSuccess = document.getElementById('clearStorageSuccess');

    if (btnClearLocalStorage) {
        btnClearLocalStorage.addEventListener('click', () => {
            if (confirm('⚠️ هل أنت متأكد من رغبتك في مسح جميع البيانات والتخزين المحلي وتصفير النظام بالكامل؟')) {
                localStorage.clear();
                if (clearStorageSuccess) clearStorageSuccess.style.display = 'block';
                setTimeout(() => {
                    window.location.reload();
                }, 2000);
            }
        });
    }

    // Initialize Interactive Curriculum Engine
    window.currEngine = new InteractiveCurriculumEngine();
    window.currEngine.init();

    // Check Login State
    const isLoggedIn = sessionStorage.getItem('engineer_logged_in') === 'true';
    if (isLoggedIn) {
        showView(viewDashboard);
        loadSubmissions();
    } else {
        showView(viewLogin);
    }
});

// ==========================================
// INTERACTIVE CURRICULUM GAME & AUDIO ENGINE
// ==========================================

// Web Audio API oscillators for live synthesizers
function playHappyChime() {
    try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const notes = [523.25, 659.25, 783.99, 1046.50]; // C5, E5, G5, C6
        notes.forEach((freq, index) => {
            setTimeout(() => {
                const osc = audioCtx.createOscillator();
                const gainNode = audioCtx.createGain();
                osc.type = index === 3 ? 'sine' : 'triangle';
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gainNode.gain.setValueAtTime(0.12, audioCtx.currentTime);
                gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.4);
                osc.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + 0.4);
            }, index * 100);
        });
    } catch (e) {}
}

function playPopupSound() {
    try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(320, audioCtx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, audioCtx.currentTime + 0.12);
        gainNode.gain.setValueAtTime(0.12, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.12);
        osc.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.12);
    } catch (e) {}
}

function playErrorSound() {
    try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const osc = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(160, audioCtx.currentTime);
        osc.frequency.linearRampToValueAtTime(90, audioCtx.currentTime + 0.25);
        gainNode.gain.setValueAtTime(0.18, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.25);
        osc.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + 0.25);
    } catch (e) {}
}

function triggerConfetti() {
    if (typeof confetti === 'function') {
        confetti({ particleCount: 100, spread: 70, origin: { y: 0.6 } });
        return;
    }
    let canvas = document.getElementById('currConfettiCanvas');
    if (!canvas) {
        canvas = document.createElement('canvas');
        canvas.id = 'currConfettiCanvas';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.pointerEvents = 'none';
        canvas.style.zIndex = '9999';
        document.body.appendChild(canvas);
    }
    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const colors = ['#f72585', '#7209b7', '#3f37c9', '#4361ee', '#4cc9f0', '#fb8500', '#ffb703', '#06d6a0'];
    const particles = [];
    for (let i = 0; i < 70; i++) {
        particles.push({
            x: canvas.width / 2 + (Math.random() - 0.5) * 150,
            y: canvas.height * 0.5 + (Math.random() - 0.5) * 80,
            r: Math.random() * 5 + 3,
            color: colors[Math.floor(Math.random() * colors.length)],
            tilt: Math.random() * 10 - 5,
            tiltAngleIncremental: Math.random() * 0.07 + 0.02,
            tiltAngle: 0,
            vx: (Math.random() - 0.5) * 12,
            vy: -Math.random() * 12 - 4,
            g: 0.35
        });
    }
    function updateConfetti() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let active = false;
        particles.forEach(p => {
            p.vy += p.g; p.x += p.vx; p.y += p.vy;
            p.tiltAngle += p.tiltAngleIncremental;
            p.tilt = Math.sin(p.tiltAngle) * 3;
            if (p.y <= canvas.height) {
                active = true;
                ctx.beginPath();
                ctx.lineWidth = p.r;
                ctx.strokeStyle = p.color;
                ctx.moveTo(p.x + p.tilt + p.r / 2, p.y);
                ctx.lineTo(p.x + p.tilt, p.y + p.tilt + p.r / 2);
                ctx.stroke();
            }
        });
        if (active) requestAnimationFrame(updateConfetti);
        else canvas.remove();
    }
    updateConfetti();
}

// 12 Sessions Curriculum Database mapping database/senior_python/recap.json
const SESSIONS_DATA = [
    // LEVEL 1: Foundations
    {
        id: "lvl1_s1", level: 1, sessionNum: 1,
        title: "أساسيات البايثون ودالة print 🧱",
        badge: "المستوى 1 🐍 الجلسة 1",
        desc: "تعلم دالة الطباعة وإنشاء المتغيرات لتخزين البيانات السحرية في بايثون!",
        concepts: [
            { title: "ما هي لغة بايثون؟ 🤔", desc: "بايثون هي لغة برمجة قوية وسهلة جداً، تشبه لغة البشر! نستخدمها لبناء الألعاب وتطوير الذكاء الاصطناعي.", icon: "🐍" },
            { title: "دالة الطباعة print() 📢", desc: "تُستخدم دالة print لإظهار الكلمات والأرقام على الشاشة. نضع الكلمات دائماً بين علامات تنصيص ليفهم بايثون أنها نصوص.", code: "print(\"مرحباً بكم في أكاديمية ميجا مايندز! 🚀\")\nprint(5 + 10)", icon: "📢" },
            { title: "المتغيرات (Variables) 📦", desc: "المتغير هو مثل صندوق سحري نضع فيه اسماً وصورة وقيمة لنسترجعها لاحقاً. ننشئه هكذا: name = \"Ahmed\"", code: "hero_name = \"سوبر بايثون\"\nx = 10\nprint(hero_name)", icon: "📦" }
        ]
    },
    {
        id: "lvl1_s2", level: 1, sessionNum: 2,
        title: "أنواع البيانات والعمليات الحسابية 🧪",
        badge: "المستوى 1 🐍 الجلسة 2",
        desc: "اكتشف أنواع البيانات المختلفة (نصوص، أرقام، منطقي) وكيف تصنع آلة حاسبة ذكية!",
        concepts: [
            { title: "أنواع البيانات الرئيسية 📊", desc: "1. النص (String): مثل \"Alice\" ونضعه دائماً بين علامات تنصيص.\n2. العدد الصحيح (Integer): رقم بدون فاصلة مثل 15.\n3. الرقم العشري (Float): رقم بكسور مثل 3.14.\n4. المنطقي (Boolean): نعم أو لا (True أو False).", icon: "🧪" },
            { title: "العمليات الحسابية ➕", desc: "يدعم بايثون العمليات الحسابية مثل الجمع (+)، الطرح (-)، الضرب (*)، والقسمة (/).", code: "apples = 5\nbananas = 3\ntotal = apples + bananas\nprint(total)", icon: "➕" }
        ]
    },
    {
        id: "lvl1_s3", level: 1, sessionNum: 3,
        title: "اتخاذ القرار وجملة الشرط If 🚦",
        badge: "المستوى 1 🐍 الجلسة 3",
        desc: "اجعل الكود الخاص بك ذكياً! نستخدم جمل الشرط ليقرر الروبوت متى يمشي ومتى يقف.",
        concepts: [
            { title: "كيف يفكر الكمبيوتر؟ 🤔", desc: "يستخدم بايثون الشرط if (إذا تحقق هذا) و else (وإلا فافعل كذا) لاتخاذ القرارات الهامة.", icon: "🚦" },
            { title: "مثال إشارة المرور 🚦", desc: "إذا كانت الإشارة حمراء يقف، وإلا ينطلق بسلام!", code: "light = \"red\"\nif light == \"red\":\n    print(\"Stop! 🛑\")\nelse:\n    print(\"Go! 🚗\")", icon: "🚦" }
        ]
    },
    {
        id: "lvl1_s4", level: 1, sessionNum: 4,
        title: "حلقات التكرار (Loops) 🔄",
        badge: "المستوى 1 🐍 الجلسة 4",
        desc: "وفر وقتك ومجهودك! تعلم كيف تجعل بايثون يكرر المهام المتشابهة في غمضة عين.",
        concepts: [
            { title: "ما هي حلقة التكرار؟ 🔄", desc: "تُستخدم الحلقات لتكرار كود معين عدة مرات دون كتابته من جديد. نستخدم حلقة for للتكرار عدد محدد من المرات، وحلقة while للتكرار طالما تحقق الشرط.", icon: "🔄" },
            { title: "حلقة التكرار for 🔄", desc: "مثال لتكرار طباعة الكلمة 5 مرات:", code: "for i in range(5):\n    print(\"صنع كعكة لذيذة 🎂\")", icon: "🎂" }
        ]
    },

    // LEVEL 2: Data Structures & Functions
    {
        id: "lvl2_s1", level: 2, sessionNum: 5,
        title: "استقبال المدخلات وتحويل الأنواع 🔮",
        badge: "المستوى 2 🐍 الجلسة 1",
        desc: "تعلم استقبال الكلمات من المستخدم بدالة input() وتحويلها لأرقام برمجية بدالة int()!",
        concepts: [
            { title: "دالة المدخلات input() 📥", desc: "تسمح دالة input() للمستخدم بالكتابة داخل البرنامج. يستقبلها بايثون كنص (String) دائماً.", code: "name = input(\"ما هو اسمك البرمجي؟ \")\nprint(\"مرحباً بك يا بطل \" + name)", icon: "📥" },
            { title: "التحويل البرمجي (Casting) 🧪", desc: "لتحويل النص إلى عدد صحيح حتى نتمكن من القيام بالعمليات الحسابية عليه، نستخدم int().", code: "age_str = input(\"كم عمرك؟ \")\nage = int(age_str)\nnext_year = age + 1", icon: "🧪" }
        ]
    },
    {
        id: "lvl2_s2", level: 2, sessionNum: 6,
        title: "المصفوفات والقوائم السحرية (Lists) 🎒",
        badge: "المستوى 2 🐍 الجلسة 2",
        desc: "تعلم حفظ مجموعة من العناصر في حقيبة واحدة، والفرق بين القوائم القابلة للتغيير والصفوف الثابتة (Tuples)!",
        concepts: [
            { title: "القائمة (List) 🎒", desc: "القائمة هي حقيبة يمكننا إضافة عناصر إليها أو حذفها منها. نستخدم append() للإضافة و pop() للحذف.", code: "backpack = [\"تفاحة\", \"سيف\"]\nbackpack.append(\"درع\")\nprint(backpack)", icon: "🎒" },
            { title: "الصف الثابت (Tuple) 🔒", desc: "الصف الثابت هو مثل الخزنة المغلقة بأرقام سرية. لا يمكننا تعديل عناصره بعد إنشائه أبداً ويُكتب بين أقواس دائرية ().", code: "fixed_colors = (\"أحمر\", \"أخضر\")\n# fixed_colors[0] = \"أزرق\"  <- سيحدث خطأ! 🛑", icon: "🔒" }
        ]
    },
    {
        id: "lvl2_s3", level: 2, sessionNum: 7,
        title: "القواميس وتخزين البيانات (Dictionaries) 📖",
        badge: "المستوى 2 🐍 الجلسة 3",
        desc: "تعلم ربط البيانات بمفتاح وقيمة مثل القاموس الحقيقي تماماً واسترجاعها بسرعة فائقة!",
        concepts: [
            { title: "ما هو القاموس (Dictionary)؟ 📖", desc: "هو هيكل بيانات يربط المفتاح (Key) بالقيمة (Value). مثل ربط اسم الطالب بدرجته أو اسم البطل بقوته الخارقة.", icon: "📖" },
            { title: "طريقة كتابة القاموس 💻", desc: "نستخدم الأقواس المتعرجة {} ونضع نقطتين بين المفتاح والقيمة:", code: "hero = {\n    \"name\": \"سوبر بايثون\",\n    \"power\": \"أشعة الليزر\",\n    \"level\": 10\n}\nprint(hero[\"power\"])", icon: "💻" }
        ]
    },
    {
        id: "lvl2_s4", level: 2, sessionNum: 8,
        title: "بناء وتصميم الدوال البرمجية (Functions) 🧪",
        badge: "المستوى 2 🐍 الجلسة 4",
        desc: "صمم آلاتك ومصانعك الخاصة! تعلم كتابة الدوال باستخدام الكلمة المفتاحية def واستدعائها في أي وقت.",
        concepts: [
            { title: "ما هي الدالة (Function)؟ ⚙️", desc: "الدالة هي رمز أو مصنع نقوم بتعريفه مرة واحدة لتأدية مهمة محددة، ثم نستدعيه متى شئنا لتوفير تكرار الكود.", icon: "🧪" },
            { title: "كتابة الدالة def 💻", desc: "نعرف الدالة باستخدام def ونعطيها اسماً، ثم نضع الكود بداخلها:", code: "def mix_potion(ing1, ing2):\n    result = ing1 + \" مع \" + ing2\n    return \"🔮 جرعة سحرية: \" + result\n\n# استدعاء الدالة\npotion = mix_potion(\"غبار النجوم\", \"جرعة زرقاء\")", icon: "💻" }
        ]
    },

    // LEVEL 3: Advanced Challenges & Projects
    {
        id: "lvl3_s1", level: 3, sessionNum: 9,
        title: "حلقات التكرار المتداخلة ورسم الأشكال 🎨",
        badge: "المستوى 3 🐍 الجلسة 1",
        desc: "تعلم تشغيل حلقة تكرار داخل حلقة تكرار أخرى لرسم شبكات بكسل مذهلة وتصميم لوحات فنية!",
        concepts: [
            { title: "الحلقات المتداخلة (Nested Loops) 🌀", desc: "حلقة التكرار المتداخلة هي حلقة تعمل بالكامل داخل كل دورة من حلقات التكرار الخارجية. نستخدمها للمرور على شبكات ثنائية الأبعاد (صفوف وأعمدة).", icon: "🌀" },
            { title: "رسم شبكة بكسل 🎨", desc: "لكل صف r، نمر على كل عمود c لنرسم نقطة في الشبكة:", code: "for r in range(5):\n    for c in range(5):\n        print(\"🎨\", end=\"\")\n    print() # سطر جديد", icon: "🎨" }
        ]
    },
    {
        id: "lvl3_s2", level: 3, sessionNum: 10,
        title: "رسومات السلحفاة البرمجية (Turtle) 🐢",
        badge: "المستوى 3 🐍 الجلسة 2",
        desc: "أطلق العنان للفنان البرمجي بداخلك! تحكم في السلحفاة الذكية لترسم خطوطاً، دوائر، ونجوماً مضيئة.",
        concepts: [
            { title: "مكتبة السلحفاة Turtle 🐢", desc: "هي أداة رائعة في بايثون لتعليم البرمجة من خلال الرسم. نتحكم في سلحفاة صغيرة تتحرك على الشاشة وتترك خلفها خطاً ملوناً.", icon: "🐢" },
            { title: "أوامر السلحفاة الأساسية 💻", desc: "نستورد المكتبة ثم نوجه الأوامر للسلحفاة لتتحرك للأمام أو تدور بزوايا محددة:", code: "import turtle\nt = turtle.Turtle()\nt.forward(100) # تحرك للأمام\nt.left(90)     # در بزاوية 90 درجة\nt.circle(50)   # ارسم دائرة", icon: "💻" }
        ]
    },
    {
        id: "lvl3_s3", level: 3, sessionNum: 11,
        title: "البرمجة كائنية التوجه (OOP Classes) 🧬",
        badge: "المستوى 3 🐍 الجلسة 3",
        desc: "تعلم كيف تصبح صانعاً حقيقياً! صمم مخططات كائنات البناء (Classes) وتفريخ كائنات حية وأبطال خارقين.",
        concepts: [
            { title: "ما هي الفئة (Class) والكائن (Object)؟ 🧬", desc: "الفئة (Class) هي المخطط أو القالب لإنشاء أشياء متشابهة. الكائن (Object) هو العنصر الحقيقي الذي يتم تفريخه وتصنيعه من هذا المخطط.", icon: "🧬" },
            { title: "بناء فئة بطل خارق 💻", desc: "نعرف الخصائص في دالة البناء __init__ والأفعال كدوال تابعة للفئة:", code: "class Hero:\n    def __init__(self, name, power):\n        self.name = name\n        self.power = power\n\n# تفريخ كائنات حقيقية\nhero1 = Hero(\"فلاش\", \"سرعة البرق\")\nhero2 = Hero(\"هالك\", \"القوة الخارقة\")", icon: "🧬" }
        ]
    },
    {
        id: "lvl3_s4", level: 3, sessionNum: 12,
        title: "بناء خوادم وتطبيقات الويب (Flask Server) 🌐",
        badge: "المستوى 3 🐍 الجلسة 4",
        desc: "توج مهاراتك البرمجية ببناء موقع إنترنت حقيقي! تعلم استخدام Flask لتوجيه روابط المتصفح وخدمة صفحات الويب.",
        concepts: [
            { title: "ما هو خادم الويب (Web Server)؟ 🌐", desc: "هو برنامج يستمع لطلبات المتصفح (مثل طلب موقع معين) ويرد عليه بالصفحة المطلوبة (الاستجابة).", icon: "🌐" },
            { title: "إطار عمل Flask 🧪", desc: "هو مكتبة خفيفة وسهلة جداً في بايثون لإنشاء مواقع إنترنت وتوجيه الروابط (Routes):", code: "from flask import Flask\napp = Flask(__name__)\n\n@app.route(\"/\")\ndef home():\n    return \"مرحباً بكم في موقعي الأول! 🚀\"\n\nif __name__ == \"__main__\":\n    app.run()", icon: "🧪" }
        ]
    }
];

class InteractiveCurriculumEngine {
    constructor() {
        this.currentLevel = 1;
        this.activeSession = null;
        this.sessionXp = 0;
        this.completedSessions = JSON.parse(localStorage.getItem('curr_completed_sessions') || '{}');
        this.totalHeroXp = parseInt(localStorage.getItem('curr_total_hero_xp') || '0');
    }

    init() {
        // Render Level Selector event handlers inside dashboard
        const lvlBtn1 = document.getElementById('btnLevel1');
        const lvlBtn2 = document.getElementById('btnLevel2');
        const lvlBtn3 = document.getElementById('btnLevel3');

        if (lvlBtn1) lvlBtn1.onclick = () => this.selectLevel(1);
        if (lvlBtn2) lvlBtn2.onclick = () => this.selectLevel(2);
        if (lvlBtn3) lvlBtn3.onclick = () => this.selectLevel(3);

        // Render close button inside playground modal
        const exitBtn = document.getElementById('btnExitPlayground');
        if (exitBtn) exitBtn.onclick = () => this.exitPlayground();

        // Update overall score count
        this.updateTotalXpDisplay();

        // Render sessions for Level 1 by default
        this.selectLevel(1);
    }

    selectLevel(levelNum) {
        this.currentLevel = levelNum;
        playPopupSound();

        // Update buttons classes active
        for (let i = 1; i <= 3; i++) {
            const btn = document.getElementById(`btnLevel${i}`);
            if (btn) {
                if (i === levelNum) btn.classList.add('active');
                else btn.classList.remove('active');
            }
        }

        this.renderSessionCards();
    }

    renderSessionCards() {
        const grid = document.getElementById('curriculumSessionsGrid');
        if (!grid) return;

        grid.innerHTML = '';
        const sessions = SESSIONS_DATA.filter(s => s.level === this.currentLevel);

        sessions.forEach(s => {
            const isCompleted = this.completedSessions[s.id] === true;
            const card = document.createElement('div');
            card.className = `session-premium-card level-${this.currentLevel} ${isCompleted ? 'completed' : ''}`;

            card.innerHTML = `
                <div class="session-card-header">
                    <span class="session-card-badge">${s.badge}</span>
                    <span class="session-card-xp">${isCompleted ? '✅ مكتمل (+100 XP)' : '⭐ 100 XP'}</span>
                </div>
                <h4 class="session-card-title">${s.title}</h4>
                <p class="session-card-desc">${s.desc}</p>
                <button class="btn-launch-session" onclick="window.currEngine.launchSession('${s.id}')">
                    <span>${isCompleted ? '🎮 إعادة التحدي واللعب' : '🚀 انطلق والعب الآن'}</span>
                </button>
            `;
            grid.appendChild(card);
        });
    }

    launchSession(sessionId) {
        const session = SESSIONS_DATA.find(s => s.id === sessionId);
        if (!session) return;

        this.activeSession = session;
        this.sessionXp = this.completedSessions[sessionId] === true ? 100 : 0;

        playPopupSound();
        triggerConfetti();

        // Open Modal overlay
        const modal = document.getElementById('curriculumPlaygroundModal');
        if (modal) {
            modal.style.display = 'flex';
            setTimeout(() => modal.classList.add('active'), 50);
        }

        // Set text items
        const badge = document.getElementById('playgroundSessionBadge');
        const title = document.getElementById('playgroundSessionTitle');
        if (badge) badge.textContent = session.badge.toUpperCase();
        if (title) title.textContent = session.title;

        // Render explanation cards
        this.renderExplanations(session.concepts);

        // Update progress inside modal
        this.updateModalProgress();

        // Load interactive game
        this.loadSessionGame(session.id);
    }

    renderExplanations(concepts) {
        const container = document.getElementById('playgroundInfoContent');
        if (!container) return;

        container.innerHTML = '';
        concepts.forEach(c => {
            const card = document.createElement('div');
            card.className = 'concept-card-premium';
            
            let codeMarkup = '';
            if (c.code) {
                codeMarkup = `<pre class="concept-code-box" dir="ltr">${c.code}</pre>`;
            }

            card.innerHTML = `
                <div class="concept-card-header">
                    <span class="concept-card-icon">${c.icon}</span>
                    <h5 class="concept-card-title">${c.title}</h5>
                </div>
                <p class="concept-card-desc">${c.desc.replace(/\n/g, '<br>')}</p>
                ${codeMarkup}
            `;
            container.appendChild(card);
        });
    }

    updateModalProgress() {
        const text = document.getElementById('playgroundXpDisplay');
        const bar = document.getElementById('playgroundXpBar');
        if (text) text.textContent = `${this.sessionXp} / 100 XP`;
        if (bar) bar.style.width = `${this.sessionXp}%`;
    }

    addXp(points) {
        if (this.sessionXp >= 100) return;

        this.sessionXp = Math.min(100, this.sessionXp + points);
        this.updateModalProgress();

        if (this.sessionXp === 100) {
            playHappyChime();
            triggerConfetti();
            setTimeout(() => triggerConfetti(), 400);

            // Mark session as completed
            if (!this.completedSessions[this.activeSession.id]) {
                this.completedSessions[this.activeSession.id] = true;
                localStorage.setItem('curr_completed_sessions', JSON.stringify(this.completedSessions));
                
                this.totalHeroXp += 100;
                localStorage.setItem('curr_total_hero_xp', this.totalHeroXp);
                this.updateTotalXpDisplay();
                this.renderSessionCards();
            }
        } else {
            playPopupSound();
        }
    }

    updateTotalXpDisplay() {
        const xpEl = document.getElementById('totalHeroXp');
        if (xpEl) xpEl.textContent = this.totalHeroXp;
    }

    exitPlayground() {
        playPopupSound();
        const modal = document.getElementById('curriculumPlaygroundModal');
        if (modal) {
            modal.classList.remove('active');
            setTimeout(() => modal.style.display = 'none', 400);
        }
        this.activeSession = null;
    }

    loadSessionGame(sessionId) {
        const container = document.getElementById('playgroundGameContent');
        const titleEl = document.getElementById('playgroundGameTitle');
        if (!container) return;

        container.innerHTML = '';

        switch (sessionId) {
            case 'lvl1_s1':
                titleEl.textContent = "🎮 محاكي سطر الأوامر: جرب دالة الطباعة";
                this.initTerminalGame(container);
                break;
            case 'lvl1_s2':
                titleEl.textContent = "🎮 تصنيف البيانات: فرز الصناديق السحرية";
                this.initDataSortingGame(container);
                break;
            case 'lvl1_s3':
                titleEl.textContent = "🎮 إشارة المرور الذكية: تحدي If Conditions";
                this.initTrafficLightGame(container);
                break;
            case 'lvl1_s4':
                titleEl.textContent = "🎮 مصنع الكعك: تشغيل حلقة التكرار For Loop";
                this.initConveyorCakeGame(container);
                break;
            case 'lvl2_s1':
                titleEl.textContent = "🎮 بلورة المستقبل: تحدي input() و Casting";
                this.initFortuneTellerGame(container);
                break;
            case 'lvl2_s2':
                titleEl.textContent = "🎮 حقيبة الظهر ورقم الخزنة: القوائم والصفوف الثابتة";
                this.initBackpackListGame(container);
                break;
            case 'lvl2_s3':
                titleEl.textContent = "🎮 قاعدة بيانات العميل السري: تحدي Dictionaries";
                this.initSpyDatabaseGame(container);
                break;
            case 'lvl2_s4':
                titleEl.textContent = "🎮 مرجل الساحر: تركيب الجرعة باستدعاء الدوال def";
                this.initPotionBrewingGame(container);
                break;
            case 'lvl3_s1':
                titleEl.textContent = "🎮 الرسام المتنقل: تشغيل الحلقات المتداخلة";
                this.initNestedLoopsGame(container);
                break;
            case 'lvl3_s2':
                titleEl.textContent = "🎮 لوحة رسم السلحفاة: مغامرة Turtle Graphics";
                this.initTurtleGraphicsGame(container);
                break;
            case 'lvl3_s3':
                titleEl.textContent = "🎮 مصنع تفريخ الكائنات: بناء كائن Hero من الـ Class";
                this.initHeroSpawnerGame(container);
                break;
            case 'lvl3_s4':
                titleEl.textContent = "🎮 موقع الويب الأول: محاكاة خادم الويب المصغر Flask";
                this.initFlaskServerGame(container);
                break;
        }
    }

    // GAME 1: Terminal simulator (Session 1)
    initTerminalGame(container) {
        container.innerHTML = `
            <div class="term-container">
                <div class="term-header">
                    <div class="term-dots">
                        <span class="term-dot red"></span>
                        <span class="term-dot yellow"></span>
                        <span class="term-dot green"></span>
                    </div>
                    <span class="term-title">interactive_python_shell.py</span>
                </div>
                <div class="term-history" id="termHistory">>>> مرحباً بك يا بطل! اكتب أمراً برمجياً للطباعة لتشغيل المحاكي.\nمثال: print("مرحباً") أو print(10 + 20)</div>
                <div class="term-input-row">
                    <span class="term-prompt">>>></span>
                    <input type="text" id="termInput" class="term-field" placeholder="اكتب الكود البرمجي هنا واضغط Enter..." autofocus>
                </div>
            </div>
            <p class="term-help-msg">💡 تحدي البطل: اكتب دالة print كاملة لطباعة اسمك أو إجراء عملية حسابية لتجميع نقاط XP!</p>
        `;

        const input = document.getElementById('termInput');
        const history = document.getElementById('termHistory');

        input.onkeydown = (e) => {
            if (e.key === 'Enter') {
                const cmd = input.value.trim();
                if (!cmd) return;

                history.innerHTML += `\n>>> ${cmd}`;
                input.value = '';

                // Simple parser
                const printRegex = /^print\((.+)\)$/;
                const match = cmd.match(printRegex);

                if (match) {
                    const arg = match[1].trim();
                    // Check if string
                    if ((arg.startsWith('"') && arg.endsWith('"')) || (arg.startsWith("'") && arg.endsWith("'"))) {
                        const strVal = arg.slice(1, -1);
                        history.innerHTML += `\n<span class="output-val">${strVal}</span>`;
                        this.addXp(50);
                    } else {
                        // Check if math or number
                        try {
                            // Safe math evaluation
                            const cleanExpr = arg.replace(/[^0-9+\-*/().\s]/g, '');
                            if (cleanExpr) {
                                const result = Function(`"use strict"; return (${cleanExpr})`)();
                                history.innerHTML += `\n<span class="output-val">${result}</span>`;
                                this.addXp(50);
                            } else {
                                throw new Error();
                            }
                        } catch (err) {
                            history.innerHTML += `\n<span class="output-err">NameError: name '${arg}' is not defined</span>`;
                            playErrorSound();
                        }
                    }
                } else if (cmd.includes('=')) {
                    // Variable assignment
                    const parts = cmd.split('=');
                    const varName = parts[0].trim();
                    const varVal = parts[1].trim();
                    history.innerHTML += `\n<span class="output-ok">تم حفظ المتغير ${varName} بنجاح! 📦</span>`;
                    this.addXp(50);
                } else {
                    history.innerHTML += `\n<span class="output-err">SyntaxError: تذكر كتابة دالة print مع فتح القوسين وعلامات التنصيص للنصوص!</span>`;
                    playErrorSound();
                }

                history.scrollTop = history.scrollHeight;
            }
        };
    }

    // GAME 2: Data Sorting (Session 2)
    initDataSortingGame(container) {
        const items = [
            { val: '"Alice"', type: 'str', label: '"Alice" (نص)' },
            { val: '15', type: 'int', label: '15 (عدد صحيح)' },
            { val: '3.14', type: 'float', label: '3.14 (عدد عشري)' },
            { val: 'True', type: 'bool', label: 'True (منطقي)' }
        ];

        let score = 0;

        container.innerHTML = `
            <div class="sort-box-container">
                <div class="v-game-score-row">
                    <span class="v-game-score-badge">النقاط: <span id="sortScore">0 / 4</span></span>
                    <span style="font-weight: bold; color: var(--text-light);">فرز سلة البيانات السحرية 🧪</span>
                </div>
                <div class="sort-drag-items" id="sortDragItems">
                    <!-- Items rendered here -->
                </div>
                <div class="sort-baskets-grid">
                    <div class="sort-basket" id="basket_str" data-type="str">
                        <div class="sort-basket-title">String (نصوص) 📝</div>
                        <div class="sort-basket-items"></div>
                    </div>
                    <div class="sort-basket" id="basket_int" data-type="int">
                        <div class="sort-basket-title">Integer (أعداد صحيحة) 🔢</div>
                        <div class="sort-basket-items"></div>
                    </div>
                    <div class="sort-basket" id="basket_float" data-type="float">
                        <div class="sort-basket-title">Float (أعداد عشرية) 📐</div>
                        <div class="sort-basket-items"></div>
                    </div>
                    <div class="sort-basket" id="basket_bool" data-type="bool">
                        <div class="sort-basket-title">Boolean (قيم منطقية) ⚖️</div>
                        <div class="sort-basket-items"></div>
                    </div>
                </div>
            </div>
        `;

        const itemsContainer = document.getElementById('sortDragItems');
        let selectedItem = null;

        // Populate items
        items.forEach((item, idx) => {
            const btn = document.createElement('button');
            btn.className = 'sort-drag-item';
            btn.textContent = item.label;
            btn.onclick = () => {
                playPopupSound();
                selectedItem = item;
                // Highlight item
                document.querySelectorAll('.sort-drag-item').forEach(b => b.style.borderColor = '#cbd5e1');
                btn.style.borderColor = 'var(--primary)';
            };
            itemsContainer.appendChild(btn);
        });

        // Baskets logic
        const baskets = document.querySelectorAll('.sort-basket');
        baskets.forEach(basket => {
            basket.onclick = () => {
                if (!selectedItem) {
                    alert('⚠️ اختر قيمة أولاً بالضغط عليها، ثم اضغط على السلة المناسبة لفرزها!');
                    return;
                }

                const expectedType = basket.getAttribute('data-type');
                if (selectedItem.type === expectedType) {
                    // Correct!
                    score++;
                    playPopupSound();
                    
                    // Add badge to basket list
                    const basketList = basket.querySelector('.sort-basket-items');
                    const badge = document.createElement('span');
                    badge.className = 'sort-basket-item';
                    badge.textContent = selectedItem.val;
                    basketList.appendChild(badge);

                    // Remove from list
                    document.querySelectorAll('.sort-drag-item').forEach(b => {
                        if (b.textContent === selectedItem.label) b.remove();
                    });

                    document.getElementById('sortScore').textContent = `${score} / 4`;
                    this.addXp(25);

                    selectedItem = null;
                } else {
                    // Incorrect
                    playErrorSound();
                    alert('🛑 خطأ في الفرز! حاول مرة أخرى بتركيز.');
                }
            };
        });
    }

    // GAME 3: Traffic Lights (Session 3)
    initTrafficLightGame(container) {
        container.innerHTML = `
            <div class="gate-simulation-box">
                <div class="gate-visual-arena">
                    <div class="sim-car" id="simCar">🚗</div>
                    <div class="sim-gate-post"></div>
                    <div class="sim-gate-bar" id="simGateBar"></div>
                    
                    <div class="gate-light-pole">
                        <div class="gate-light-housing">
                            <div class="gate-light-bulb red" id="bulbRed"></div>
                            <div class="gate-light-bulb green" id="bulbGreen"></div>
                        </div>
                        <div class="gate-light-post"></div>
                    </div>
                    
                    <div class="gate-horizontal-road">
                        <div class="road-dashed-line"></div>
                    </div>
                </div>
                
                <div class="v-game-feedback" id="gateFeedback" style="color: #64748b;">تحدي البطل: اختبر جمل الشروط (If/Else) لتشغيل إشارة المرور وبوابات العبور!</div>
                
                <div class="v-actions-grid">
                    <button class="btn-v-choice invalid" id="btnTestRed">
                        <span>if light == "red":<br>🛑 stop_car()</span>
                    </button>
                    <button class="btn-v-choice valid" id="btnTestGreen">
                        <span>else:<br>🟢 drive_car()</span>
                    </button>
                </div>
            </div>
        `;

        const car = document.getElementById('simCar');
        const gate = document.getElementById('simGateBar');
        const redLight = document.getElementById('bulbRed');
        const greenLight = document.getElementById('bulbGreen');
        const feedback = document.getElementById('gateFeedback');

        let testedRed = false;
        let testedGreen = false;

        document.getElementById('btnTestRed').onclick = () => {
            // Activate red light
            redLight.classList.add('active');
            greenLight.classList.remove('active');
            gate.classList.remove('open');
            car.style.left = '20px'; // reset
            
            feedback.innerHTML = '🛑 الإشارة حمراء (if light == "red"): <span style="color:#ef4444;">السيارة تقف بأمان!</span>';
            playPopupSound();
            
            if (!testedRed) {
                testedRed = true;
                this.addXp(50);
            }
        };

        document.getElementById('btnTestGreen').onclick = () => {
            // Activate green light
            greenLight.classList.add('active');
            redLight.classList.remove('active');
            gate.classList.add('open');
            
            feedback.innerHTML = '🟢 الإشارة خضراء (else): <span style="color:#10b981;">بوابات العبور تفتح والسيارة تنطلق! 🚀</span>';
            playHappyChime();
            
            // Move car across screen
            setTimeout(() => {
                car.style.left = 'calc(100% - 90px)';
            }, 50);

            if (!testedGreen) {
                testedGreen = true;
                this.addXp(50);
            }
        };
    }

    // GAME 4: Conveyor loop (Session 4)
    initConveyorCakeGame(container) {
        container.innerHTML = `
            <div class="loop-belt-box">
                <div class="loop-belt-visual">
                    <div class="belt-items-container" id="beltCakesContainer">
                        <!-- Cakes spawn here -->
                    </div>
                    <div class="belt-conveyor">
                        <div class="belt-line-pattern" id="beltPattern"></div>
                    </div>
                </div>
                
                <div style="text-align: center;">
                    <button class="btn-launch-session level-1" id="btnRunLoop" style="padding: 15px 35px; font-size: 1.45rem;">
                        <span>🚀 تشغيل حلقة التكرار for i in range(5):</span>
                    </button>
                    <div style="font-size: 1.25rem; font-weight: bold; margin-top: 15px; color: var(--tertiary-dark);" id="loopProgressText">الكعكات المخبوزة: 0 / 5</div>
                </div>
            </div>
        `;

        const btn = document.getElementById('btnRunLoop');
        const pattern = document.getElementById('beltPattern');
        const cakesContainer = document.getElementById('beltCakesContainer');
        const progressText = document.getElementById('loopProgressText');

        btn.onclick = () => {
            btn.disabled = true;
            btn.style.opacity = '0.5';
            pattern.classList.add('moving');
            cakesContainer.innerHTML = '';
            
            let i = 0;
            const interval = setInterval(() => {
                i++;
                progressText.textContent = `الكعكات المخبوزة: ${i} / 5`;
                
                // Spawn cake emoji
                const cake = document.createElement('span');
                cake.className = 'belt-cake';
                cake.textContent = '🎂';
                cakesContainer.appendChild(cake);
                playPopupSound();
                
                // Add cherry on top after a short delay
                setTimeout(() => {
                    cake.textContent = '🎂🍒';
                    playPopupSound();
                }, 400);

                if (i === 5) {
                    clearInterval(interval);
                    pattern.classList.remove('moving');
                    btn.disabled = false;
                    btn.style.opacity = '1';
                    this.addXp(100);
                }
            }, 1000);
        };
    }

    // GAME 5: Fortune Teller (Session 5)
    initFortuneTellerGame(container) {
        container.innerHTML = `
            <div class="modal-concat-lab">
                <div class="concat-input-group">
                    <label>اسم البطل:</label>
                    <input type="text" id="fortuneName" class="concat-field" placeholder="اكتب اسم البطل هنا...">
                </div>
                <div class="concat-input-group">
                    <label>عمر البطل:</label>
                    <input type="number" id="fortuneAge" class="concat-field" placeholder="مثال: 12" min="5" max="99">
                </div>
                <div class="concat-input-group">
                    <label>القدرة المفضلة:</label>
                    <input type="text" id="fortunePower" class="concat-field" placeholder="مثال: الطيران، الاختفاء، قوة البرق">
                </div>
                
                <button class="btn-launch-session level-2" id="btnRevealFortune" style="margin-top: 15px; padding: 15px;">
                    <span>🔮 اقرأ المستقبل البرمجي للبطل!</span>
                </button>
                
                <div class="concat-code-preview" id="fortuneResult" style="display: none; min-height: 100px;">
                    <!-- Prophet message -->
                </div>
            </div>
        `;

        const btn = document.getElementById('btnRevealFortune');
        const nameInput = document.getElementById('fortuneName');
        const ageInput = document.getElementById('fortuneAge');
        const powerInput = document.getElementById('fortunePower');
        const resultBox = document.getElementById('fortuneResult');

        btn.onclick = () => {
            const name = nameInput.value.trim();
            const age = parseInt(ageInput.value.trim());
            const power = powerInput.value.trim();

            if (!name || isNaN(age) || !power) {
                alert('⚠️ من فضلك املأ جميع خانات المدخلات بنجاح لتشغيل البلورة السحرية!');
                return;
            }

            playHappyChime();
            triggerConfetti();

            const magicYear = 2026 + (100 - age);

            resultBox.style.display = 'block';
            resultBox.innerHTML = `
                <div class="concat-preview-line"><span class="func"># كود بايثون المستدعى خلف الكواليس:</span></div>
                <div class="concat-preview-line"><span class="var">hero_name</span> = input()  # "${name}"</div>
                <div class="concat-preview-line"><span class="var">age</span> = int(input())  # ${age}</div>
                <div class="concat-preview-line"><span class="var">magic_year</span> = 2026 + (100 - age)</div>
                <div class="concat-output-box">
                    ✨ الرؤية البرمجية للبطل {${name}}: في عام ${magicYear}، ستكون مهندس برمجيات وذكاء اصطناعي عبقري بعمر 100 عام، وتتحكم بالروبوتات وتملك مهارة خارقة هي {${power}}! 🦾🚀
                </div>
            `;

            this.addXp(100);
        };
    }

    // GAME 6: Backpack lists vs tuple error (Session 6)
    initBackpackListGame(container) {
        let backpack = ["🍎 تفاح", "⚔️ سيف", "🛡️ درع"];
        
        const renderBackpack = () => {
            const row = document.getElementById('bpSlots');
            if (!row) return;
            row.innerHTML = '';
            backpack.forEach((item, idx) => {
                row.innerHTML += `
                    <div class="bp-slot">
                        <span class="bp-slot-emoji">${item.split(' ')[0]}</span>
                        <span class="bp-slot-index">[${idx}]</span>
                    </div>
                `;
            });
            if (backpack.length === 0) {
                row.innerHTML = '<span style="color: #cbd5e1; font-weight: bold; font-size: 1.3rem;">الحقيبة فارغة تماماً! 🎒</span>';
            }
        };

        container.innerHTML = `
            <div class="bp-explorer-container">
                <div class="v-game-score-row">
                    <span class="v-game-score-badge">حقيبة البطل القابلة للتغيير (List) 🎒</span>
                </div>
                
                <div class="bp-slots-row" id="bpSlots">
                    <!-- Backpack items -->
                </div>
                
                <div class="v-actions-grid" style="grid-template-columns: repeat(3, 1fr); gap: 10px;">
                    <button class="btn-game-option" id="btnAppend" style="background:#e6f7fa; border-color:var(--tertiary);">
                        <span>append("🧬 جرعة")</span>
                    </button>
                    <button class="btn-game-option" id="btnPop" style="background:#fff2e6; border-color:var(--primary);">
                        <span>pop()</span>
                    </button>
                    <button class="btn-game-option" id="btnTupleError" style="background:#fef2f2; border-color:#ef4444; color:#b91c1c;">
                        <span>tuple_safe[0] = "🔥"</span>
                    </button>
                </div>
                
                <div class="concept-code-box" id="bpFeedback" style="display:none; font-size:1rem; color:#ef4444; background:#0f172a; border-color:#991b1b; direction:ltr;">
                    <!-- Error or list feedback -->
                </div>
            </div>
        `;

        // Delay list rendering slightly so DOM is ready
        setTimeout(renderBackpack, 50);

        let appended = false;
        let popped = false;
        let errored = false;

        document.getElementById('btnAppend').onclick = () => {
            backpack.push("🧬 جرعة");
            renderBackpack();
            playPopupSound();
            if (!appended) {
                appended = true;
                this.addXp(33);
            }
        };

        document.getElementById('btnPop').onclick = () => {
            backpack.pop();
            renderBackpack();
            playPopupSound();
            if (!popped) {
                popped = true;
                this.addXp(33);
            }
        };

        document.getElementById('btnTupleError').onclick = () => {
            playErrorSound();
            const feedback = document.getElementById('bpFeedback');
            feedback.style.display = 'block';
            feedback.innerHTML = `
                TypeError: 'tuple' object does not support item assignment<br>
                <span style="color:#e2e8f0; font-family:sans-serif; font-size:1.1rem; font-weight:bold; float:right; direction:rtl;">
                    ⚠️ تنبيه: الصفوف الثابتة (Tuples) غير قابلة للتعديل أو الإضافة! لا يمكنك اختراق خزنتها أبدًا 🔒
                </span>
            `;
            if (!errored) {
                errored = true;
                this.addXp(34);
            }
        };
    }

    // GAME 7: Dictionary Spy Database (Session 7)
    initSpyDatabaseGame(container) {
        let dictionary = {
            "name": "Falcon",
            "power": "Laser Blast",
            "code": "007"
        };

        const renderDict = () => {
            const codeBox = document.getElementById('dictCode');
            if (codeBox) {
                codeBox.textContent = `agent = ${JSON.stringify(dictionary, null, 4)}`;
            }
        };

        container.innerHTML = `
            <div class="bp-explorer-container">
                <div class="v-game-score-row">
                    <span class="v-game-score-badge">قاموس العميل السري 📖</span>
                </div>
                
                <pre class="concept-code-box" id="dictCode" style="direction:ltr; background:#0f172a; border-color:#334155; color:#a8ffb2; min-height:110px;"></pre>
                
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                    <input type="text" id="dictKey" class="concat-field" placeholder="المفتاح (Key)... e.g. age">
                    <input type="text" id="dictVal" class="concat-field" placeholder="القيمة (Value)... e.g. 15">
                </div>
                
                <div style="display:grid; grid-template-columns: 1.5fr 1fr; gap: 10px;">
                    <button class="btn-launch-session level-2" id="btnAddDict" style="padding:10px;">
                        <span>➕ أضف للقاموس agent[key] = val</span>
                    </button>
                    <button class="btn-game-option" id="btnSearchDict" style="background:#e6f7fa; border-color:var(--tertiary);">
                        <span>🔍 ابحث عن المفتاح</span>
                    </button>
                </div>
                
                <div id="dictSearchFeedback" style="font-size:1.25rem; font-weight:bold; color:var(--success); text-align:center; min-height:22px;"></div>
            </div>
        `;

        setTimeout(renderDict, 50);

        let added = false;
        let searched = false;

        document.getElementById('btnAddDict').onclick = () => {
            const key = document.getElementById('dictKey').value.trim();
            const val = document.getElementById('dictVal').value.trim();

            if (!key || !val) {
                alert('⚠️ اكتب مفتاح وقيمة صحيحة أولاً!');
                return;
            }

            dictionary[key] = val;
            renderDict();
            playPopupSound();
            
            document.getElementById('dictKey').value = '';
            document.getElementById('dictVal').value = '';

            if (!added) {
                added = true;
                this.addXp(50);
            }
        };

        document.getElementById('btnSearchDict').onclick = () => {
            const searchKey = prompt('ما هو المفتاح الذي تبحث عنه؟ (e.g. name, power)');
            if (!searchKey) return;

            const val = dictionary[searchKey];
            const feedback = document.getElementById('dictSearchFeedback');

            if (val) {
                playHappyChime();
                feedback.innerHTML = `🔍 تم العثور على المفتاح [${searchKey}]: <span style="color:var(--primary);">${val}</span>!`;
                if (!searched) {
                    searched = true;
                    this.addXp(50);
                }
            } else {
                playErrorSound();
                feedback.innerHTML = `🛑 خطأ (KeyError): المفتاح [${searchKey}] غير موجود في قاعدة البيانات!`;
            }
        };
    }

    // GAME 8: Cauldron Brewing Functions (Session 8)
    initPotionBrewingGame(container) {
        container.innerHTML = `
            <div class="potion-brewing-box">
                <div class="cauldron-visual-arena">
                    <div class="cauldron-bubbles" id="cauldronBubbles">🫧🫧</div>
                    <div class="cauldron-steam" id="cauldronSteam">💨💨</div>
                    <div class="cauldron-sprite" id="cauldronSprite">🔮</div>
                </div>
                
                <div class="v-game-feedback" id="cauldronFeedback" style="color: var(--text-light);">
                    تحدي البطل: اختر عنصرين سحريين لتمريرهما إلى دالة دمج الجرعة mix_potion()!
                </div>
                
                <div style="display:grid; grid-template-columns:1fr 1fr; gap:15px;">
                    <select id="potionIng1" class="filter-select" style="font-size:1.25rem;">
                        <option value="⭐ غبار النجوم">⭐ غبار النجوم</option>
                        <option value="🍄 فطر مضيء">🍄 فطر مضيء</option>
                        <option value="🧬 خلاصة التنين">🧬 خلاصة التنين</option>
                    </select>
                    <select id="potionIng2" class="filter-select" style="font-size:1.25rem;">
                        <option value="🧪 جرعة زرقاء">🧪 جرعة زرقاء</option>
                        <option value="🔥 لهب البركان">🔥 لهب البركان</option>
                        <option value="❄️ بلورة الجليد">❄️ بلورة الجليد</option>
                    </select>
                </div>
                
                <button class="btn-launch-session level-2" id="btnBrewPotion" style="padding:15px;">
                    <span>🧪 استدعاء الدالة mix_potion()</span>
                </button>
            </div>
        `;

        const bubbles = document.getElementById('cauldronBubbles');
        const steam = document.getElementById('cauldronSteam');
        const sprite = document.getElementById('cauldronSprite');
        const btn = document.getElementById('btnBrewPotion');
        const feedback = document.getElementById('cauldronFeedback');

        btn.onclick = () => {
            const ing1 = document.getElementById('potionIng1').value;
            const ing2 = document.getElementById('potionIng2').value;

            btn.disabled = true;
            btn.style.opacity = '0.5';
            bubbles.classList.add('active');
            steam.classList.add('active');
            sprite.textContent = '🧪';

            playPopupSound();
            
            setTimeout(() => {
                playHappyChime();
                triggerConfetti();
                
                bubbles.classList.remove('active');
                steam.classList.remove('active');
                btn.disabled = false;
                btn.style.opacity = '1';
                sprite.textContent = '🔮✨';

                feedback.innerHTML = `✨ تم استدعاء الدالة بنجاح وحصلنا على:<br><strong style="color:var(--purple); font-size:1.6rem;">جرعة ${ing1.split(' ')[1]} مع ${ing2.split(' ')[1]} الخارقة! 🥳</strong>`;
                this.addXp(100);
            }, 2500);
        };
    }

    // GAME 9: Nested Loops Grid Painter (Session 9)
    initNestedLoopsGame(container) {
        container.innerHTML = `
            <div class="pixel-grid-box">
                <div class="pixel-art-grid" id="pixelGrid">
                    <!-- 25 Cells dynamic -->
                </div>
                
                <button class="btn-launch-session level-3" id="btnRunNested" style="padding:15px;">
                    <span>🎨 تشغيل الحلقات المتداخلة (Nested Loops)</span>
                </button>
                <div style="font-size:1.25rem; font-weight:bold; color:var(--text-light);" id="nestedStatus">إحداثيات الرسم: (row, col)</div>
            </div>
        `;

        const grid = document.getElementById('pixelGrid');
        const btn = document.getElementById('btnRunNested');
        const status = document.getElementById('nestedStatus');

        // Create cells
        for (let r = 0; r < 5; r++) {
            for (let c = 0; c < 5; c++) {
                const cell = document.createElement('div');
                cell.className = 'pixel-cell';
                cell.id = `cell_${r}_${c}`;
                grid.appendChild(cell);
            }
        }

        const heartPattern = [
            '0_1', '0_3',
            '1_0', '1_1', '1_2', '1_3', '1_4',
            '2_1', '2_2', '2_3',
            '3_2',
            '4_2'
        ];

        btn.onclick = () => {
            btn.disabled = true;
            btn.style.opacity = '0.5';
            
            // Reset grid
            document.querySelectorAll('.pixel-cell').forEach(c => {
                c.className = 'pixel-cell';
            });

            let r = 0;
            let c = 0;

            const interval = setInterval(() => {
                status.textContent = `جاري الرسم: الصف ${r}، العمود ${c}`;
                const cellId = `cell_${r}_${c}`;
                const cell = document.getElementById(cellId);
                
                if (cell) {
                    cell.classList.add('scanning');
                    playPopupSound();
                    
                    setTimeout(() => {
                        cell.classList.remove('scanning');
                        if (heartPattern.includes(`${r}_${c}`)) {
                            cell.classList.add('active');
                        }
                    }, 200);
                }

                c++;
                if (c === 5) {
                    c = 0;
                    r++;
                }

                if (r === 5) {
                    clearInterval(interval);
                    status.textContent = `✨ اكتملت اللوحة! رسمنا قلباً جميلاً ❤️ باستخدام Nested Loops!`;
                    playHappyChime();
                    triggerConfetti();
                    btn.disabled = false;
                    btn.style.opacity = '1';
                    this.addXp(100);
                }
            }, 300);
        };
    }

    // GAME 10: Turtle Graphics (Session 10)
    initTurtleGraphicsGame(container) {
        container.innerHTML = `
            <div class="turtle-canvas-wrapper">
                <canvas id="turtleCanvas" width="300" height="180" style="background:#fff; border-radius:12px; border:2px solid #cbd5e1;"></canvas>
                
                <div class="turtle-control-board">
                    <button class="btn-turtle-cmd" onclick="window.currEngine.moveTurtle('forward')">🐢 forward(40)</button>
                    <button class="btn-turtle-cmd" onclick="window.currEngine.moveTurtle('left')">↩️ left(90)</button>
                    <button class="btn-turtle-cmd" onclick="window.currEngine.moveTurtle('right')">↪️ right(90)</button>
                    <button class="btn-turtle-cmd" onclick="window.currEngine.moveTurtle('circle')">⭕ draw_circle()</button>
                    <button class="btn-turtle-cmd" id="btnTurtleStar" onclick="window.currEngine.moveTurtle('star')" style="background:#fffbeb; border-color:#f59e0b;">⭐ star()</button>
                </div>
            </div>
        `;

        setTimeout(() => {
            const canvas = document.getElementById('turtleCanvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            
            // Turtle State
            this.turtleState = {
                x: 150,
                y: 90,
                angle: 0, // In degrees (0 means facing right)
                color: '#8338ec',
                cmdCount: 0
            };

            // Draw simple turtle starting position
            this.drawTurtleMascot(ctx);
        }, 50);
    }

    drawTurtleMascot(ctx) {
        ctx.beginPath();
        ctx.arc(this.turtleState.x, this.turtleState.y, 8, 0, 2 * Math.PI);
        ctx.fillStyle = '#06d6a0';
        ctx.fill();
        ctx.stroke();
    }

    moveTurtle(action) {
        const canvas = document.getElementById('turtleCanvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        ctx.strokeStyle = this.turtleState.color;
        ctx.lineWidth = 3;

        playPopupSound();
        this.turtleState.cmdCount++;

        if (action === 'forward') {
            const rad = (this.turtleState.angle * Math.PI) / 180;
            const newX = this.turtleState.x + Math.cos(rad) * 40;
            const newY = this.turtleState.y + Math.sin(rad) * 40;

            ctx.beginPath();
            ctx.moveTo(this.turtleState.x, this.turtleState.y);
            ctx.lineTo(newX, newY);
            ctx.stroke();

            this.turtleState.x = newX;
            this.turtleState.y = newY;
        } else if (action === 'left') {
            this.turtleState.angle -= 90;
        } else if (action === 'right') {
            this.turtleState.angle += 90;
        } else if (action === 'circle') {
            ctx.beginPath();
            ctx.arc(this.turtleState.x, this.turtleState.y, 25, 0, 2 * Math.PI);
            ctx.stroke();
        } else if (action === 'star') {
            // Draw a beautiful quick nested star shape
            playHappyChime();
            triggerConfetti();
            ctx.beginPath();
            for (let i = 0; i < 5; i++) {
                const rad = ((this.turtleState.angle + i * 144) * Math.PI) / 180;
                const newX = this.turtleState.x + Math.cos(rad) * 35;
                const newY = this.turtleState.y + Math.sin(rad) * 35;
                if (i === 0) ctx.moveTo(newX, newY);
                else ctx.lineTo(newX, newY);
            }
            ctx.closePath();
            ctx.stroke();
        }

        // Redraw turtle dot
        this.drawTurtleMascot(ctx);

        if (this.turtleState.cmdCount >= 4) {
            this.addXp(100);
        }
    }

    // GAME 11: Classes & Object instances (Session 11)
    initHeroSpawnerGame(container) {
        container.innerHTML = `
            <div class="bp-explorer-container">
                <div style="display:grid; grid-template-columns: 1fr 1fr; gap:10px;">
                    <input type="text" id="heroName" class="concat-field" placeholder="اسم البطل... e.g. Flash">
                    <input type="text" id="heroPower" class="concat-field" placeholder="القوة الخارقة... e.g. Speed">
                </div>
                <div class="concat-input-group">
                    <label>لون العباءة:</label>
                    <select id="heroColor" class="filter-select" style="font-size:1.15rem;">
                        <option value="#ff006e">أحمر وردي 🧣</option>
                        <option value="#8338ec">بنفسجي خارق 🔮</option>
                        <option value="#fb8500">برتقالي ناري 🔥</option>
                    </select>
                </div>
                
                <button class="btn-launch-session level-3" id="btnSpawnHero" style="padding:12px;">
                    <span>🧬 تفريخ كائن جديد hero = Hero(name, power)</span>
                </button>
                
                <div style="display:flex; gap:10px; justify-content:center; flex-wrap:wrap; min-height:80px; padding:10px; background:#f8fafc; border-radius:12px; border:2px solid #e2e8f0;" id="heroSpawns">
                    <span style="color:#cbd5e1; font-weight:bold; font-size:1.2rem; align-self:center;">لا توجد كائنات مفرخة حالياً. ابدأ التفريخ! 🧬</span>
                </div>
            </div>
        `;

        const btn = document.getElementById('btnSpawnHero');
        const spawns = document.getElementById('heroSpawns');

        let spawnCount = 0;

        btn.onclick = () => {
            const name = document.getElementById('heroName').value.trim();
            const power = document.getElementById('heroPower').value.trim();
            const color = document.getElementById('heroColor').value;

            if (!name || !power) {
                alert('⚠️ أدخل الاسم والقوة لخصائص دالة البناء __init__ أولاً!');
                return;
            }

            if (spawnCount === 0) spawns.innerHTML = '';

            playHappyChime();
            triggerConfetti();

            const heroCard = document.createElement('div');
            heroCard.style.cssText = `background:${color}; color:#fff; border-radius:10px; padding:10px 15px; text-align:center; font-weight:bold; box-shadow:0 4px 10px rgba(0,0,0,0.15); animation:spawnScale 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);`;
            heroCard.innerHTML = `
                <div>🦸 ${name}</div>
                <div style="font-size:0.9rem; opacity:0.9; margin-top:4px;">✨ ${power}</div>
            `;
            spawns.appendChild(heroCard);

            // Reset inputs
            document.getElementById('heroName').value = '';
            document.getElementById('heroPower').value = '';

            spawnCount++;
            if (spawnCount >= 2) {
                this.addXp(100);
            }
        };
    }

    // GAME 12: Flask Web routing mock (Session 12)
    initFlaskServerGame(container) {
        container.innerHTML = `
            <div class="flask-simulator-box">
                <div class="flask-browser-mockup">
                    <div class="browser-bar">
                        <div class="browser-dots">
                            <span class="browser-dot"></span>
                            <span class="browser-dot"></span>
                            <span class="browser-dot"></span>
                        </div>
                        <input type="text" class="browser-url-bar" id="browserUrl" value="http://localhost:5000/" readonly>
                    </div>
                    <div class="browser-viewport" id="browserViewport" style="font-family:sans-serif; font-size:1.3rem; color:var(--text-light);">
                        🚀 خادم الويب مغلق حالياً. اضغط تشغيل لتفعيل الخادم واستقبال طلبات الويب!
                    </div>
                </div>
                
                <div class="flask-status-card" id="flaskStatus">
                    $ python server.py<br>
                    * Serving Flask app 'server'<br>
                    * Debug mode: off
                </div>
                
                <div style="display:grid; grid-template-columns:1fr 1fr 1fr; gap:10px;">
                    <button class="btn-game-option" id="btnFlaskHome" disabled style="background:#e6f7fa;">الصفحة الرئيسية Route: /</button>
                    <button class="btn-game-option" id="btnFlaskGame" disabled style="background:#fff2e6;">قسم الألعاب Route: /game</button>
                    <button class="btn-launch-session level-3" id="btnStartFlask" style="padding:10px;">⚡ تشغيل الخادم app.run()</button>
                </div>
            </div>
        `;

        const startBtn = document.getElementById('btnStartFlask');
        const homeBtn = document.getElementById('btnFlaskHome');
        const gameBtn = document.getElementById('btnFlaskGame');
        const status = document.getElementById('flaskStatus');
        const viewport = document.getElementById('browserViewport');
        const urlBar = document.getElementById('browserUrl');

        let hitHome = false;
        let hitGame = false;

        startBtn.onclick = () => {
            playHappyChime();
            startBtn.disabled = true;
            startBtn.style.opacity = '0.5';
            status.classList.add('active');
            status.innerHTML = `
                $ python server.py<br>
                * Serving Flask app 'server'<br>
                * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)<br>
                <span style="color:#10b981; font-weight:bold;">🚀 الخادم نشط الآن! جرب مسارات الويب المختلفة.</span>
            `;

            homeBtn.disabled = false;
            gameBtn.disabled = false;
            
            // Load default home
            viewport.innerHTML = `<h1 style="color:var(--primary-dark); font-weight:900;">Welcome to Megaminds Academy! 🚀</h1><p style="font-size:1.15rem; color:#5c677d;">خادم Flask يعمل ويخدم طلبات الويب بكفاءة وسرعة.</p>`;
        };

        homeBtn.onclick = () => {
            playPopupSound();
            urlBar.value = "http://localhost:5000/";
            viewport.innerHTML = `<h1 style="color:var(--primary-dark); font-weight:900;">Welcome to Megaminds Academy! 🚀</h1><p style="font-size:1.15rem; color:#5c677d;">خادم Flask يعمل ويخدم طلبات الويب بكفاءة وسرعة.</p>`;
            
            if (!hitHome) {
                hitHome = true;
                this.addXp(50);
            }
        };

        gameBtn.onclick = () => {
            playPopupSound();
            urlBar.value = "http://localhost:5000/game";
            viewport.innerHTML = `<h1 style="color:var(--tertiary-dark); font-weight:900;">🎮 محطة الألعاب حية ونشطة!</h1><p style="font-size:1.15rem; color:#5c677d;">كود بايثون Flask أرسل صفحة الألعاب للمتصفح بنجاح.</p>`;
            
            if (!hitGame) {
                hitGame = true;
                this.addXp(50);
            }
        };
    }
}
// View Navigation Helper
function showView(viewEl) {
    [viewLogin, viewDashboard, viewEvaluation].forEach(v => { if (v) v.classList.remove('active'); });
    if (viewEl) viewEl.classList.add('active');
    
    if (viewEl === viewDashboard) {
        if (btnLogoutEl) btnLogoutEl.style.display = 'inline-flex';
        loadSubmissions();
    } else if (viewEl === viewLogin) {
        if (btnLogoutEl) btnLogoutEl.style.display = 'none';
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 1. Handle Login
function handleLogin(e) {
    e.preventDefault();
    const user = inputUsernameEl.value.trim();
    const pass = inputPasswordEl.value.trim();

    // Fixed credentials for engineers
    if ((user === 'engineer' || user === 'admin') && pass === 'megaminds') {
        sessionStorage.setItem('engineer_logged_in', 'true');
        if (loginErrorEl) loginErrorEl.style.display = 'none';
        showView(viewDashboard);
    } else {
        if (loginErrorEl) loginErrorEl.style.display = 'block';
    }
}

// Handle Logout
function handleLogout() {
    sessionStorage.removeItem('engineer_logged_in');
    showView(viewLogin);
}

// 2. Load Submissions from Storage Adapter (Firebase Realtime + LocalStorage Fallback)
function loadSubmissions() {
    if (db) {
        // Realtime cloud listener
        db.ref('submissions').on('value', (snapshot) => {
            const data = snapshot.val();
            currentSubmissions = [];
            if (data) {
                Object.keys(data).forEach(key => {
                    currentSubmissions.push(data[key]);
                });
                // Sort newest first
                currentSubmissions.sort((a,b) => new Date(b.timestamp) - new Date(a.timestamp));
            } else {
                // Check localStorage as fallback if Firebase is empty
                const backup = localStorage.getItem('megaminds_submissions');
                currentSubmissions = backup ? JSON.parse(backup) : [];
                currentSubmissions.sort((a,b) => new Date(b.timestamp) - new Date(a.timestamp));
            }
            renderSubmissions();
        }, (error) => {
            console.error("Firebase read error, falling back to localStorage:", error);
            const backup = localStorage.getItem('megaminds_submissions');
            currentSubmissions = backup ? JSON.parse(backup) : [];
            currentSubmissions.sort((a,b) => new Date(b.timestamp) - new Date(a.timestamp));
            renderSubmissions();
        });
    } else {
        // Fallback to LocalStorage
        const backup = localStorage.getItem('megaminds_submissions');
        currentSubmissions = backup ? JSON.parse(backup) : [];
        currentSubmissions.sort((a,b) => new Date(b.timestamp) - new Date(a.timestamp));
        renderSubmissions();
    }
}

// Render Submissions Grid
// Hide Submission Helper
window.hideSubmission = function(subId) {
    let hidden = JSON.parse(localStorage.getItem('megaminds_hidden_submissions') || '[]');
    if (!hidden.includes(subId)) {
        hidden.push(subId);
        localStorage.setItem('megaminds_hidden_submissions', JSON.stringify(hidden));
    }
    renderSubmissions();
};

// Restore All Hidden Submissions Helper
function restoreAllHiddenSubmissions() {
    const hidden = JSON.parse(localStorage.getItem('megaminds_hidden_submissions') || '[]');
    if (hidden.length === 0) {
        alert('ℹ️ لا توجد إجابات مخفية حالياً.');
        return;
    }
    localStorage.removeItem('megaminds_hidden_submissions');
    renderSubmissions();
    alert('✅ تم إظهار جميع الإجابات المخفية بنجاح!');
}

// Render Submissions Grid
function renderSubmissions() {
    if (!submissionsGridEl) return;

    const query = searchSubmissionsEl ? searchSubmissionsEl.value.trim().toLowerCase() : '';
    const statusFilter = filterStatusEl ? filterStatusEl.value : '';

    const hiddenSubmissions = JSON.parse(localStorage.getItem('megaminds_hidden_submissions') || '[]');
    if (hiddenSubmissionsCountEl) {
        hiddenSubmissionsCountEl.textContent = hiddenSubmissions.length;
    }

    let filtered = currentSubmissions.filter(sub => {
        if (hiddenSubmissions.includes(sub.id)) return false;

        const matchesQuery = !query || 
            (sub.studentName && sub.studentName.toLowerCase().includes(query)) ||
            (sub.groupName && sub.groupName.toLowerCase().includes(query)) ||
            (sub.teacherName && sub.teacherName.toLowerCase().includes(query)) ||
            (sub.course && sub.course.toLowerCase().includes(query));
            
        const matchesStatus = !statusFilter || sub.status === statusFilter;
        return matchesQuery && matchesStatus;
    });

    // Update Stats
    if (totalSubmissionsCountEl) totalSubmissionsCountEl.textContent = filtered.length;
    if (pendingSubmissionsCountEl) {
        pendingSubmissionsCountEl.textContent = filtered.filter(s => s.status === 'pending').length;
    }

    submissionsGridEl.innerHTML = '';

    if (filtered.length === 0) {
        submissionsGridEl.innerHTML = `<div style="grid-column: 1/-1; text-align: center; padding: 50px; font-size: 1.6rem; color: #888;">لا توجد إجابات مطابقة للبحث حالياً.</div>`;
        return;
    }

    filtered.forEach(sub => {
        const card = document.createElement('div');
        card.className = 'submission-card';
        const dateStr = new Date(sub.timestamp).toLocaleDateString('ar-EG', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
        
        card.innerHTML = `
            <div>
                <div class="sub-card-header">
                    <span class="sub-course">📘 ${sub.course}</span>
                    <div class="sub-header-actions">
                        <span class="sub-status ${sub.status === 'graded' ? 'graded' : 'pending'}">
                            ${sub.status === 'graded' ? 'تم التقييم ✅' : 'بانتظار التقييم ⏳'}
                        </span>
                        <button class="btn-hide-sub" onclick="hideSubmission('${sub.id}')" title="إخفاء هذه الإجابة">
                            <span>👁️‍🗨️ إخفاء</span>
                        </button>
                    </div>
                </div>
                <div class="sub-meta-list">
                    <div>👤 الطالب: <strong>${sub.studentName}</strong></div>
                    <div>👥 المجموعة/المستوى: <strong>${sub.groupName}</strong></div>
                    <div>👨‍🏫 المهندس المشرف: <strong>${sub.teacherName}</strong></div>
                    <div>📅 التاريخ: <strong>${dateStr}</strong></div>
                    <div>🏆 نتيجة الاختيارات التلقائية: <strong>${sub.mcqScore} / ${sub.mcqTotal}</strong></div>
                    ${sub.status === 'graded' ? `<div>⭐ درجة المهندس للمهام: <strong>${sub.engineerGrade || 0}</strong></div>` : ''}
                </div>
            </div>
            <button class="btn-review-sub" onclick="openEvaluation('${sub.id}')">
                <span>${sub.status === 'graded' ? 'عرض التقييم والتقرير 📝' : 'مراجعة وتقييم الإجابات 📝'}</span>
            </button>
        `;
        submissionsGridEl.appendChild(card);
    });
}

// Calculate total percentage helper
function calculateSubmissionPercentage(sub) {
    const mcqTotal = sub.mcqTotal || 0;
    const mcqScore = sub.mcqScore || 0;
    const taskCount = sub.answers ? sub.answers.filter(a => a.type === 'task').length : 0;
    
    // Assuming each task is out of 5 points
    const maxTotal = mcqTotal + (taskCount * 5);
    const totalScore = mcqScore + (sub.engineerGrade || 0);
    
    if (maxTotal === 0) return 0;
    return (totalScore / maxTotal) * 100;
}

// 3. Open Evaluation View for a Specific Submission
window.openEvaluation = function(subId) {
    currentSelectedSubmission = currentSubmissions.find(s => s.id === subId);
    if (!currentSelectedSubmission) return;

    const percentage = calculateSubmissionPercentage(currentSelectedSubmission);
    const certBtn = document.getElementById('btnPrintCertificateBtn');
    if (certBtn) {
        if (percentage > 85) {
            certBtn.style.display = 'inline-flex';
            certBtn.title = `متاح للطباعة (النسبة: ${percentage.toFixed(1)}%)`;
        } else {
            certBtn.style.display = 'none';
        }
    }

    // Render Student Meta
    if (studentEvalMetaEl) {
        const dateStr = new Date(currentSelectedSubmission.timestamp).toLocaleDateString('ar-EG', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
        studentEvalMetaEl.innerHTML = `
            <div>👤 الطالب: <span>${currentSelectedSubmission.studentName}</span></div>
            <div>👥 المجموعة: <span>${currentSelectedSubmission.groupName}</span></div>
            <div>👨‍🏫 المشرف: <span>${currentSelectedSubmission.teacherName}</span></div>
            <div>📘 المادة/المسار: <span>${currentSelectedSubmission.course}</span></div>
            <div>📅 وقت الإرسال: <span>${dateStr}</span></div>
            <div>🏆 نتيجة الـ MCQ: <span>${currentSelectedSubmission.mcqScore} / ${currentSelectedSubmission.mcqTotal}</span></div>
            <div>📊 النسبة الإجمالية التقديرية: <span id="liveScorePercentSpan">${percentage.toFixed(1)}%</span></div>
        `;
    }

    // Render Answers List
    if (evalAnswersListEl) {
        evalAnswersListEl.innerHTML = '';
        currentSelectedSubmission.answers.forEach((ans, idx) => {
            const card = document.createElement('div');
            card.className = 'answer-card';

            if (ans.type === 'mcq') {
                card.innerHTML = `
                    <div class="answer-card-header">
                        <span class="q-num">السؤال ${idx + 1} (اختيار متعدد)</span>
                        <span class="q-badge ${ans.isCorrect ? 'mcq-correct' : 'mcq-incorrect'}">
                            ${ans.isCorrect ? 'إجابة صحيحة تلقائياً ✅' : 'إجابة خاطئة تلقائياً ❌'}
                        </span>
                    </div>
                    <div class="q-text">${cleanBiDiText(ans.question)}</div>
                    <div class="q-student-answer">إجابة الطالب: <strong>${cleanBiDiText(ans.answer)}</strong></div>
                    ${!ans.isCorrect ? `<div class="q-correct-answer">الإجابة الصحيحة: <strong>${cleanBiDiText(ans.correctText)}</strong></div>` : ''}
                `;
            } else {
                card.innerHTML = `
                    <div class="answer-card-header">
                        <span class="q-num">السؤال ${idx + 1} (مهمة برمجة / Task)</span>
                        <span class="q-badge task-badge">تقييم المهندس 👨‍🏫</span>
                    </div>
                    <div class="q-text">${cleanBiDiText(ans.question)}</div>
                    <div class="q-student-answer code-box">${cleanBiDiText(ans.answer)}</div>
                    <div class="engineer-feedback-box">
                        <div class="engineer-box-title">✍️ صندوق تقييم المهندس المشرف (للتصحيح اليدوي):</div>
                        <div class="engineer-grading-row">
                            <label>الدرجة المستحقة للمهمة (من 5):</label>
                            <input type="number" id="taskGrade_${ans.questionId}" class="engineer-grade-input" min="0" max="5" step="0.5" placeholder="الدرجة (مثال: 5)" value="${ans.engineerGrade || currentSelectedSubmission.engineerGrade || ''}" oninput="if(this.value > 5) { alert('⚠️ عذراً، أقصى درجة للمهمة الواحدة هي 5 درجات.'); this.value = 5; } if(this.value < 0) this.value = 0; window.updateLivePercentage();">
                        </div>
                        <textarea id="taskNotes_${ans.questionId}" class="engineer-notes-textarea" placeholder="اكتب ملاحظاتك التقييمية والنصائح البرمجية للطالب هنا...">${ans.engineerNotes || currentSelectedSubmission.engineerNotes || ''}</textarea>
                    </div>
                `;
            }
            evalAnswersListEl.appendChild(card);
        });
    }

    showView(viewEvaluation);
};

// Live Percentage Update Helper
window.updateLivePercentage = function() {
    if (!currentSelectedSubmission) return;
    let totalTaskGrade = 0;
    currentSelectedSubmission.answers.forEach(ans => {
        if (ans.type === 'task') {
            const gradeInput = document.getElementById(`taskGrade_${ans.questionId}`);
            if (gradeInput && gradeInput.value !== '') {
                let val = parseFloat(gradeInput.value);
                if (val > 5) val = 5;
                if (val < 0) val = 0;
                totalTaskGrade += val;
            }
        }
    });
    
    const mcqTotal = currentSelectedSubmission.mcqTotal || 0;
    const mcqScore = currentSelectedSubmission.mcqScore || 0;
    const taskCount = currentSelectedSubmission.answers ? currentSelectedSubmission.answers.filter(a => a.type === 'task').length : 0;
    const maxTotal = mcqTotal + (taskCount * 5);
    const totalScore = mcqScore + totalTaskGrade;
    const percentage = maxTotal > 0 ? (totalScore / maxTotal) * 100 : 0;

    const certBtn = document.getElementById('btnPrintCertificateBtn');
    if (certBtn) {
        if (percentage > 85) {
            certBtn.style.display = 'inline-flex';
            certBtn.title = `متاح للطباعة (النسبة: ${percentage.toFixed(1)}%)`;
        } else {
            certBtn.style.display = 'none';
        }
    }
    const percentSpan = document.getElementById('liveScorePercentSpan');
    if (percentSpan) percentSpan.textContent = `${percentage.toFixed(1)}%`;
};

// 4. Save Evaluation
function saveEvaluation() {
    if (!currentSelectedSubmission) return;

    // Find all task grading inputs
    let totalTaskGrade = 0;
    let combinedNotes = [];

    currentSelectedSubmission.answers.forEach(ans => {
        if (ans.type === 'task') {
            const gradeInput = document.getElementById(`taskGrade_${ans.questionId}`);
            const notesInput = document.getElementById(`taskNotes_${ans.questionId}`);

            if (gradeInput && gradeInput.value !== '') {
                let val = parseFloat(gradeInput.value);
                if (val > 5) {
                    alert(`⚠️ عذراً، أقصى درجة للمهمة الواحدة هي 5 درجات. تم ضبط الدرجة إلى 5.`);
                    val = 5;
                    gradeInput.value = 5;
                }
                if (val < 0) val = 0;
                ans.engineerGrade = val;
                totalTaskGrade += ans.engineerGrade;
            }
            if (notesInput && notesInput.value.trim() !== '') {
                ans.engineerNotes = notesInput.value.trim();
                combinedNotes.push(ans.engineerNotes);
            }
        }
    });

    currentSelectedSubmission.engineerGrade = totalTaskGrade;
    currentSelectedSubmission.engineerNotes = combinedNotes.join('\n\n');
    currentSelectedSubmission.status = 'graded';

    // 1. Update in Firebase Realtime Database
    if (db) {
        db.ref('submissions/' + currentSelectedSubmission.id).set(currentSelectedSubmission)
          .then(() => console.log("Firebase updated successfully!"))
          .catch(err => console.error("Firebase update error:", err));
    }

    // 2. Update in LocalStorage Hybrid Adapter
    const index = currentSubmissions.findIndex(s => s.id === currentSelectedSubmission.id);
    if (index !== -1) {
        currentSubmissions[index] = currentSelectedSubmission;
        localStorage.setItem('megaminds_submissions', JSON.stringify(currentSubmissions));
    }

    alert('💾 تم حفظ تقييمك وملاحظاتك بنجاح في قاعدة البيانات السحابية والمحلية! ✅');
    showView(viewDashboard);
}

// ==========================================
// CERTIFICATE PREVIEW & PRINTING LOGIC
// ==========================================

window.previewCertificate = function() {
    if (!currentSelectedSubmission) return;
    const percentage = calculateSubmissionPercentage(currentSelectedSubmission);
    if (percentage <= 85) {
        alert(`⚠️ عذراً يا مهندسنا، طباعة الشهادة الرسمية تتاح فقط للأبطال الحاصلين على أكثر من 85% (النسبة الحالية للطالب: ${percentage.toFixed(1)}%).`);
        return;
    }

    // Populate Certificate DOM
    const certStudentNameEl = document.getElementById('certStudentName');
    const certCourseTitleEl = document.getElementById('certCourseTitle');
    const certScorePercentEl = document.getElementById('certScorePercent');
    const certDateValueEl = document.getElementById('certDateValue');
    const certTeacherNameEl = document.getElementById('certTeacherName');

    if (certStudentNameEl) certStudentNameEl.textContent = currentSelectedSubmission.studentName || 'بطل غير مسجل';
    if (certCourseTitleEl) certCourseTitleEl.textContent = currentSelectedSubmission.course || 'مسار البرمجة والذكاء الاصطناعي';
    if (certScorePercentEl) certScorePercentEl.textContent = `${percentage.toFixed(1)}%`;
    
    const dateObj = new Date(currentSelectedSubmission.timestamp);
    const dateValueStr = dateObj.toLocaleDateString('ar-EG', { year: 'numeric', month: 'long', day: 'numeric' });
    if (certDateValueEl) certDateValueEl.textContent = dateValueStr;
    if (certTeacherNameEl) certTeacherNameEl.textContent = currentSelectedSubmission.teacherName || 'المهندس المشرف';

    // Show Certificate Modal
    const certContainer = document.getElementById('certificateContainer');
    if (certContainer) certContainer.style.display = 'flex';
};

window.closeCertificatePreview = function() {
    const certContainer = document.getElementById('certificateContainer');
    if (certContainer) certContainer.style.display = 'none';
};

window.printCertificateOnly = function() {
    document.body.classList.add('print-mode-certificate');
    setTimeout(() => {
        window.print();
        setTimeout(() => {
            document.body.classList.remove('print-mode-certificate');
        }, 500);
    }, 150);
};

// Overwrite default print button for Evaluation Report
const btnPrintEval = document.getElementById('btnPrintEvalReport');
if (btnPrintEval) {
    btnPrintEval.onclick = function(e) {
        e.preventDefault();
        document.body.className = 'print-mode-report';
        window.print();
        document.body.className = '';
    };
}
