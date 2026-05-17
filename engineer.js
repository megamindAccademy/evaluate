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
        title: "مقدمة البايثون ودالة print والمتغيرات 🧱",
        badge: "المستوى 1 🐍 الجلسة 1",
        desc: "اكتشف تاريخ لغة بايثون الرائعة، وتعلم دالة الطباعة وقواعد تسمية المتغيرات كالمحترفين!",
        concepts: [
            { title: "ما هي لغة بايثون؟ 🤔", desc: "بايثون هي لغة برمجة قوية وسهلة الفهم للغاية! إنها لغة عالية المستوى (High-level)، مفسرة (Interpreted)، وتعتمد على الكائنات (Object-oriented) والجميل أنها تبدو مثل اللغة الإنجليزية تماماً! تمتاز بايثون بمكتبتها القياسية الضخمة وسهولة كتابتها وتصحيحها.", icon: "🐍" },
            { title: "أين تُسخدم بايثون؟ 🚀", desc: "تُستخدم في مجالات مذهلة:\n1. استخراج البيانات من الويب (Web Scraping) باستخدام الروبوتات.\n2. الذكاء الاصطناعي وتعلم الآلة (Machine Learning & AI) لبناء نماذج تفكر كالبشر.\n3. تطوير الألعاب (Game Development).\n4. الأتمتة (Automation) لتحويل المهام اليدوية لآلية.\n5. الاختراق والأمن السيبراني (Hacking).\n6. تطوير مواقع الويب.", icon: "🤖" },
            { title: "دالة الطباعة print() 📢", desc: "نستخدم دالة print() لعرض النصوص والأرقام على الشاشة. تذكر وضع النصوص بين علامات تنصيص \" \" ليتمكن بايثون من قراءتها كنص!", code: "print(\"مرحباً بكم في أكاديمية ميجامايندز! 🚀\")\nprint(5 + 10)", icon: "📢" },
            { title: "المتغيرات وقواعد التسمية 📦", desc: "المتغير هو صندوق سحري نخزن فيه البيانات. قواعد تسمية الصناديق:\n- يجب أن يبدأ الاسم بحرف فقط (مثل name1 وليس 1name).\n- لا نستخدم كلمات برمجية محجوزة (مثل int, if, function).\n- استخدام أسماء معبرة (مثل length وليس x).\n- طريقة سنام الجمل Camel Case (مثل firstName) أو Pascal Case (مثل CallYourMother).\n- بايثون حساس لحالة الأحرف (name تختلف تماماً عن Name).\n- نربط المتغير بالنصوص باستخدام علامة الجمع (+).", code: "hero_name = \"سوبر بايثون\"\nmessage = \"بطلنا العظيم\"\nprint(message + \": \" + hero_name)", icon: "📦" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. قم بكتابة برنامج بلغة بايثون يستخدم دالة print() لطباعة جملة قصيرة ومفيدة مكونة من 3 كلمات.\n2. قم بإنشاء متغير (Variable) باسم message، وعين له القيمة النصية \"hello world\"، ثم قم بطباعة هذا المتغير على الشاشة لتتأكد من عمله!",
            code: "# 1. اكتب دالة الطباعة هنا لجملة من 3 كلمات\nprint(\"...\")\n\n# 2. أنشئ المتغير واطبعه هنا\nmessage = \"hello world\"\nprint(...)"
        }
    },
    {
        id: "lvl1_s2", level: 1, sessionNum: 2,
        title: "أنواع البيانات ودالة المدخلات والقوائم 🧪",
        badge: "المستوى 1 🐍 الجلسة 2",
        desc: "تعلم أنواع البيانات البرمجية، واستقبل مدخلات المستخدمين، وتحكم في القوائم السحرية!",
        concepts: [
            { title: "أنواع البيانات المضمنة 📊", desc: "بايثون يصنف البيانات ليفهمها:\n- النصوص (String - str): مثل \"Alice\".\n- الأعداد (Integer - int): أرقام صحيحة مثل 15.\n- الأرقام العشرية (Float): أرقام بكسور مثل 3.14.\n- المنطقي (Boolean - bool): نعم أو لا (True أو False).\nيمكننا معرفة نوع أي متغير باستخدام دالة type().", code: "age = 15\nprint(type(age)) # سيطبع <class 'int'>", icon: "🧪" },
            { title: "استخدام الأقواس في البرمجة 🔮", desc: "- الأقواس الدائرية (): لتمرير البيانات الإضافية أو الدوال.\n- الأقواس المربعة []: لتعريف وإعلان القوائم (Lists).\n- الأقواس المتعرجة {}: لإدخال قيم القواميس (Key-Value Dictionaries) أو التنسيقات.", icon: "🔮" },
            { title: "دالة المدخلات input() 📥", desc: "تُستخدم لاستقبل الكتابة من المستخدم. يستقبلها بايثون كـ String دائماً، ولإجراء حسابات عليها يجب تحويلها باستخدام int() أو float().", code: "name = input(\"ما اسمك؟ \")\nage = int(input(\"كم عمرك؟ \"))", icon: "📥" },
            { title: "القوائم السحرية (Lists) 🎒", desc: "حقيبة لتخزين عناصر متعددة بترتيب معين. تبدأ الفهرسة (Index) من 0.\nأهم عمليات القوائم:\n- الإضافة في النهاية: append()\n- إضافة قائمة أخرى: extend()\n- الإدخال في مكان محدد: insert()\n- الترتيب تصاعدياً: sort()\n- الترتيب تنازلياً: sort(reverse=True)\n- الحذف: remove() أو clear()", code: "bag = [5, 9, 6]\nbag.append(7)\nbag.insert(1, 2)\nbag.sort()\nprint(bag)", icon: "🎒" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. قم بإنشاء متغير باسم name وضعي فيه اسمكِ، ثم استخدم دالة type() لمعرفة ونوع المتغير وطباعته.\n2. قم بإنشاء قائمة تحتوي على الأرقام: [5, 9, 6, 7, 2, 5, 4] ثم قم بالعمليات التالية:\n- الوصول لعنصر وطباعته.\n- تعديل قيمة أحد العناصر.\n- إضافة رقم جديد في نهاية القائمة باستخدام append().\n- إدراج رقم جديد في فهرس محدد باستخدام insert().",
            code: "# 1. معرفة نوع المتغير\nname = \"yourName\"\nprint(...)\n\n# 2. عمليات القائمة السحرية\nnums = [5, 9, 6, 7, 2, 5, 4]\n# اكتب عمليات القوائم هنا"
        }
    },
    {
        id: "lvl1_s3", level: 1, sessionNum: 3,
        title: "العمليات الحسابية والمنطقية وتصميم الدوال ➕",
        badge: "المستوى 1 🐍 الجلسة 3",
        desc: "تعلم استخدام المعاملات الحسابية والمنطقية وتعرف على النصوص كقوائم والدوال البرمجية!",
        concepts: [
            { title: "المعاملات البرمجية (Operators) ➕", desc: "المعاملات هي رموز نستخدمها للعمليات:\n1. الحسابية: الجمع (+), الطرح (-), الضرب (*), القسمة (/).\n2. التعيين: التساوي (=), وزيادة القيمة (+=).\n3. المقارنة: التساوي (==), عدم التساوي (!=), أكبر من (>), أصغر من (<).\n4. المنطقية: (and) يجب تحقق الشرطين، (or) تحقق أحدهما، (not) عكس الشرط.", icon: "➕" },
            { title: "الأنواع العددية والتحويلات 🔢", desc: "الأرقام في بايثون إما عدد صحيح (int)، عشري (float)، أو مركب (complex). يمكننا التحويل بينهم هكذا:", code: "x = 10\ny = float(x)\nz = complex(x)\nprint(y, z)", icon: "🔢" },
            { title: "النصوص كقوائم من الحروف 📝", desc: "يعتبر بايثون النصوص مثل قائمة من الحروف، حيث يتم حساب المسافات كحروف وتملك فهارس تبدأ من 0.", code: "text = \"Python\"\nprint(text[0]) # سيطبع P", icon: "📝" },
            { title: "مفهوم الدوال (Functions) ⚙️", desc: "الدالة هي كتلة برمجية منظمة وقابلة لإعادة الاستخدام، تقوم بتأدية عمل محدد بمجرد استدعائها وتمنع تكرار الكود.", icon: "⚙️" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. استخدم دالة input() لاستقبال اسم المستخدم وطباعة رسالة ترحيبية مخصصة له.\n2. إذا كان لديك NUM1 = 5 و NUM2 = 10، قم بكتابة برنامج يوضح أمثلة على:\n- العمليات الحسابية (+, -, *, /)\n- عمليات التعيين (=, +=)\n- عمليات المقارنة (==, !=, >, <)\n- العمليات المنطقية (and, or, not)",
            code: "# 1. الترحيب بالمستخدم\nuser_name = input(\"...\")\nprint(...)\n\n# 2. تطبيق المعاملات البرمجية\nNUM1 = 5\nNUM2 = 10\n# اكتب مقارناتك الحسابية والمنطقية هنا"
        }
    },
    {
        id: "lvl1_s4", level: 1, sessionNum: 4,
        title: "الصف الثابت والقواميس البرمجية 🔒📖",
        badge: "المستوى 1 🐍 الجلسة 4",
        desc: "اكتشف الفروق الجوهرية بين القوائم والصفوف الثابتة (Tuples) والقواميس (Dictionaries) المخزنة بالمفاتيح!",
        concepts: [
            { title: "الصف الثابت (Tuple) 🔒", desc: "هو هيكل بيانات لتخزين عناصر متعددة. مميزاته:\n- مرتب (Ordered).\n- غير قابل للتعديل أو التغيير (Unchangeable/Immutable).\n- يسمح بتكرار العناصر.\n- يكتب بالأقواس الدائرية ().\nلتعديله: نحوله إلى قائمة، نعدله، ثم نعيده كصف ثابت!", code: "fruits = (\"تفاح\", \"موز\")\n# fruits[0] = \"خوخ\" # خطأ! غير قابل للتعديل", icon: "🔒" },
            { title: "القاموس (Dictionary) 📖", desc: "مخزن رائع يعتمد على المفتاح والقيمة (Key:Value). مميزاته:\n- مرتب (Ordered).\n- قابل للتعديل والتغيير (Changeable).\n- لا يسمح بتكرار المفاتيح أبداً.\n- يكتب بالأقواس المتعرجة {}.", code: "student = {\"name\": \"سيف\", \"grade\": 95}\nprint(student[\"name\"]) # يطبع سيف\nstudent[\"grade\"] = 98 # تحديث القيمة", icon: "📖" },
            { title: "المقارنة الكبرى ⚖️", desc: "- القائمة (List): مرتبة، قابلة للتعديل، تسمح بالتكرار []\n- الصف الثابت (Tuple): مرتب، غير قابل للتعديل، يسمح بالتكرار ()\n- القاموس (Dictionary): مرتب، قابل للتعديل، لا يسمح بتكرار المفاتيح {}", icon: "⚖️" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. تحدي التعديل على Tuple: لديك صف ثابت يحتوي على أسماء. قم بتحويله إلى قائمة، ثم أضف اسماً جديداً وقم بتعديل اسم موجود بالفعل، ثم أعد القائمة إلى صف ثابت واطبعه.\n2. قاموس درجات الطلاب: أنشئ قاموساً يحتوي على 3 طلاب ودرجاتهم. قم بطباعته. ثم قم بإضافة طالب جديد وتحديث درجة طالب آخر واطبع القاموس المحدث.",
            code: "# 1. التعديل على الصف الثابت\nnames_tuple = (\"أحمد\", \"سارة\", \"يوسف\")\nnames_list = list(names_tuple)\n# أضف وعدل هنا...\n\n# 2. قاموس درجات الطلاب\nscores = {\"أحمد\": 90, \"سارة\": 95, \"يوسف\": 88}\n# اكتب عمليات الإضافة والتحديث هنا"
        }
    },

    // LEVEL 2: Data Structures & Functions
    {
        id: "lvl2_s1", level: 2, sessionNum: 5,
        title: "الشروط البرمجية وحلقات التكرار While 🚦🔄",
        badge: "المستوى 2 🐍 الجلسة 5",
        desc: "اجعل كودك ذكياً يتخذ القرارات البرمجية، وتعلم كيفية تكرار الأكواد باستخدام حلقة While!",
        concepts: [
            { title: "الشروط البرمجية (If/Elif/Else) 🚦", desc: "يستخدم بايثون الشروط لاتخاذ القرارات بناءً على مقارنات منطقية. الجملة Elif تعني (إذا لم يتحقق السابق واختبر هذا)، والـ Else تلتقط كل ما لم تشمله الشروط السابقة.", code: "x = 20\nif x > 30:\n    print(\"كبير\")\nelif x > 15:\n    print(\"متوسط\")\nelse:\n    print(\"صغير\")", icon: "🚦" },
            { title: "الشروط المختصرة (Short Hand) ⚡", desc: "إذا كان لديك سطر كود واحد، يمكنك كتابة جملة If بأكملها في سطر واحد لتوفير المساحة وجعل الكود رشيقاً!", code: "if a > b: print(\"a أكبر\")\nprint(\"A\") if a > b else print(\"B\")", icon: "⚡" },
            { title: "حلقة التكرار While Loop 🔄", desc: "تقوم حلقة While بتكرار الكود طالما أن الشرط صحيح. تذكر دائماً وضع متغير البداية وتحديثه (Increment) حتى لا تدخل في حلقة تكرار لا نهائية تسبّب تعليق الجهاز!", code: "i = 1\nwhile i <= 5:\n    print(i)\n    i += 1", icon: "🔄" },
            { title: "معاملات التحكم (Break & Continue) 🛑", desc: "- Break: تنهي وتوقف حلقة التكرار تماماً حتى لو كان الشرط لا يزال صحيحاً.\n- Continue: توقف الدورة الحالية فقط وتنتقل فوراً للدورة التالية.\n- Else في While: سطر كود يتم تنفيذه مرة واحدة فقط عندما يصبح شرط While خاطئاً.", icon: "🛑" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. قم بإنشاء متغير age = 25. اكتب برنامجاً باستخدام If و Elif و Else يفحص الآتي:\n- إذا كان العمر أصغر من 0، يطبع \"Invalid age\".\n- إذا كان العمر أصغر من 18، يطبع \"child\".\n- إذا كان العمر أصغر من 65، يطبع \"Adult\".\n- غير ذلك، يطبع \"Senior\".\n2. قم بإنشاء قائمة تحتوي على أرقام، واستخدم حلقة While للمرور على عناصر القائمة وطباعة كل رقم على حدة.",
            code: "# 1. فحص فئات العمر\nage = 25\n# اكتب جمل الشرط هنا\n\n# 2. التكرار بـ While على قائمة\nnumbers = [10, 20, 30, 40]\n# اكتب حلقة التكرار هنا"
        }
    },
    {
        id: "lvl2_s2", level: 2, sessionNum: 6,
        title: "حلقات التكرار For والدوال المتداخلة 🔄🌀",
        badge: "المستوى 2 🐍 الجلسة 6",
        desc: "تعلم التكرار على القوائم والنصوص، دالة range() السحرية، وتصميم حلقات تكرار متداخلة!",
        concepts: [
            { title: "حلقة التكرار For Loop 🔄", desc: "تُسخدم للمرور والتكرار على سلسلة معينة (قائمة، نص، أو نطاق رقمي). يمكن استخدامها لطباعة عناصر قائمة فواكه أو أرقام بسهولة.", code: "for x in [\"تفاح\", \"موز\"]:\n    print(x)", icon: "🔄" },
            { title: "التكرار على النصوص ودالة range() 🔤", desc: "الحروف والنصوص تعتبر متسلسلات قابلة للتكرار! دالة range() تتيح لنا تكرار الكود لعدد محدد ومحدد مسبقاً من المرات.", code: "for letter in \"banana\":\n    print(letter)\n\nfor i in range(1, 6):\n    print(i) # يطبع من 1 لـ 5", icon: "🔤" },
            { title: "التحكم بالتكرار والـ Else 🛑", desc: "- يمكن استخدام Break و Continue داخل For تماماً مثل While.\n- كلمة Else في حلقة For تحدد كوداً يتم تشغيله فور انتهاء الحلقة بالكامل بسلام ودون انقطاع بـ Break.", icon: "🛑" },
            { title: "الحلقات المتداخلة (Nested Loops) 🌀", desc: "حلقة تكرار داخل حلقة تكرار أخرى. يتم تنفيذ الحلقة الداخلية بالكامل (من البداية للنهاية) في كل دورة واحدة من دورات الحلقة الخارجية.", code: "adj = [\"لذيذ\", \"كبير\"]\nfruits = [\"تفاح\", \"خوخ\"]\nfor a in adj:\n    for f in fruits:\n        print(a, f)", icon: "🌀" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "اكتب برنامجاً بلغة بايثون يستخدم حلقة تكرار For لطباعة الأرقام من 1 إلى 10، واستخدم دالة range() لإنشاء هذه الأرقام وتوليدها تلقائياً.",
            code: "# اكتب حلقة For مع دالة range هنا لطباعة الأرقام من 1 لـ 10\nfor i in range(1, 11):\n    print(...)"
        }
    },
    {
        id: "lvl2_s3", level: 2, sessionNum: 7,
        title: "بناء وتصميم الدوال البرمجية (Functions) 🧪",
        badge: "المستوى 2 🐍 الجلسة 7",
        desc: "تعلم إنشاء الآلات البرمجية الخاصة بك باستخدام def، واستدعائها وتمرير المعاملات البرمجية!",
        concepts: [
            { title: "ما هي الدالة (Function)؟ ⚙️", desc: "الدالة هي كتلة برمجية لا تعمل إلا عند استدعائها. نمرر إليها بيانات تسمى معاملات (Parameters)، وتستطيع إرجاع بيانات كناتج باستخدام الكلمة المفتاحية return.", icon: "⚙️" },
            { title: "إنشاء واستدعاء الدالة والمسافات 💻", desc: "نعرف الدالة باستخدام def ونضع اسماً وقوسين. تذكر دائماً ترك مسافة بادئة (Indentation) لتحديد نطاق الكود داخل الدالة!", code: "def my_greeting():\n    print(\"مرحباً بك يا بطل! 🌟\")\n\n# الاستدعاء\nmy_greeting()", icon: "💻" },
            { title: "المعاملات البرمجية والوسائط 📊", desc: "- المعامل (Parameter): هو المتغير المكتوب داخل القوسين عند تعريف الدالة.\n- الوسيط (Argument): هو القيمة الفعلية التي نرسلها للدالة عند استدعائها.", code: "def add_nums(num1, num2):\n    return num1 + num2\n\nprint(add_nums(10, 2)) # يطبع 12", icon: "📊" },
            { title: "الوسائط العشوائية والقيم الافتراضية 🔮", desc: "- الوسائط العشوائية (*args): نضع نجمة * قبل الاسم إذا لم نكن نعرف عدد الوسائط الممررة.\n- القيمة الافتراضية (Default Value): نحدد قيمة افتراضية للمعامل في حال تم استدعاء الدالة بدون وسيط.", code: "def greet_hero(name=\"بطل ميجامايندز\"):\n    print(\"أهلاً \" + name)\n\ngreet_hero() # سيستخدم الافتراضي", icon: "🔮" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. استخدم دالة input() لاستقبال اسم المستخدم، ثم اكتب دالة تقوم بطباعة رسالة ترحيبية مخصصة تحتوي على هذا الاسم.\n2. اكتب دالة باسم check_number تستقبل رقماً كمعامل، وتفحص ما إذا كان الرقم زوجياً (Even) أو فردياً (Odd) وترجع الإجابة.",
            code: "# 1. دالة الترحيب بالاسم المكتوب\ndef greet_user(name):\n    # اكتب كود الترحيب هنا\n    pass\n\n# 2. دالة فحص الرقم زوجي أم فردي\ndef check_number(num):\n    # اكتب كود الفحص والإرجاع هنا\n    pass"
        }
    },
    {
        id: "lvl2_s4", level: 2, sessionNum: 8,
        title: "مكتبات بايثون ورسوم السلحفاة التفاعلية 🐢🎨",
        badge: "المستوى 2 🐍 الجلسة 8",
        desc: "تعلم تثبيت المكتبات الخارجية والتحكم بالسلحفاة البرمجية لترسم لوحات فنية وتصميمات خلابة!",
        concepts: [
            { title: "ما هي مكتبات بايثون؟ 📚", desc: "المكتبة هي مجموعة من الأكواد والدوال الجاهزة التي كتبها مبرمجون آخرون لنستخدمها مباشرة في مشاريعنا دون إعادة اختراع العجلة!", icon: "📚" },
            { title: "تثبيت المكتبات باستخدام PIP ⚙", desc: "1. اذهب لموقع pypi.org وابحث عن المكتبة.\n2. افتح نافذة Anaconda Prompt وتأكد من وجود pip عبر الكود: python -m ensurepip\n3. الصق أمر التثبيت مثل: pip install library_name", icon: "⚙" },
            { title: "رسومات السلحفاة Turtle 🐢", desc: "السلحفاة هي لوحة رسم تفاعلية رائعة نتحكم فيها برمجياً للتحرك والرسم. أهم الدوال:\n- forward(distance): تحرك للأمام\n- backward(distance): تحرك للخلف\n- left(angle) / right(angle): دوران بالزوايا\n- color(c) / width(w) / shape(s): تغيير الشكل واللون والسمك\n- exitonclick(): إبقاء النافذة مفتوحة حتى نضغط عليها.", code: "import turtle\nt = turtle.Turtle()\nt.color(\"red\")\nt.forward(100)\nt.left(90)", icon: "🐢" },
            { title: "محاور الرسم والتحويل لملف تنفيذي 📐", desc: "- نملك محورين (x, y) و 4 أرباع لرسم الأشكال.\n- يمكننا تحويل الكود لملف تنفيذي (.exe) يفتح مباشرة على أي جهاز بدون بايثون باستخدام أداة auto-py-to-exe المذهلة!", code: "pip install auto-py-to-exe\npython -m auto_py_to_exe", icon: "📐" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "قم بكتابة برنامج متكامل يستخدم مكتبة السلحفاة Turtle لإنشاء كائن سلحفاة جديد، واستخدم الأوامر والدوران التكراري لرسم مربع كامل، وتأكد من إغلاق نافذة الرسم عند الضغط عليها بالماوس.",
            code: "import turtle\nt = turtle.Turtle()\n# 1. ارسم المربع باستخدام حلقة تكرار أو الأوامر المتتالية\n\n# 2. اجعل النافذة تقفل عند الضغط عليها\nturtle.exitonclick()"
        }
    },

    // LEVEL 3: Advanced Challenges & Projects
    {
        id: "lvl3_s1", level: 3, sessionNum: 9,
        title: "البرمجة كائنية التوجه وبناء الكلاسات (OOP Classes) 🧬",
        badge: "المستوى 3 🐍 الجلسة 9",
        desc: "تعلم كيف تصبح مهندساً معمارياً برمجياً! صمم قوالب البناء (Classes) وتفريخ كائنات حقيقية!",
        concepts: [
            { title: "البرمجة كائنية التوجه (OOP) 🧬", desc: "أسلوب برمجي متطور ينظم الكود على شكل كائنات (Objects) تشبه العالم الحقيقي. على سبيل المثال، يمكننا تمثيل الشخص (Person) ككائن يملك خصائص (الاسم، العمر) وأفعال يقوم بها (Greeting).", icon: "🧬" },
            { title: "الفئة والكائن (Class & Object) 🧱", desc: "- الفئة (Class): هي المخطط أو القالب الهندسي لإنشاء الكائنات.\n- الكائن (Object): هو النسخة الحقيقية والواقعية التي ننشئها ونفرخها من هذا القالب.", icon: "🧱" },
            { title: "الكلمة السحرية (self) 🔮", desc: "تعتبر self وسيطاً إجبارياً وأساسياً في أي دالة نكتبها داخل الكلاس. هي تشير وتشير إلى الكائن الحالي الذي نعمل عليه الآن (مثل pointer أو this في اللغات الأخرى) لنتمكن من مناداة وتغيير خصائصه.", icon: "🔮" },
            { title: "دالة البناء __init__ وتنسيق النصوص 🛠️", desc: "- دالة البناء __init__: هي أول دالة يتم مناداتها وتشغيلها تلقائياً بمجرد إنشاء الكائن لنعطيه خصائصه الأساسية.\n- لتنسيق النصوص وطباعة خصائص الكائن بسهولة، نستخدم f-string مع الأقواس المتعرجة {self.parameter}.", code: "class Hero:\n    def __init__(self, name, power):\n        self.name = name\n        self.power = power\n    def show(self):\n        print(f\"البطل {self.name} قوته {self.power}!\")\n\nhero1 = Hero(\"فلاش\", \"السرعة\")\nhero1.show()", icon: "🛠️" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "1. قم بتعريف كلاس يسمى Person يمثل شخصاً حقيقياً. يجب أن يملك الكلاس خاصيتين هما: name و age، ويتم تهيئتهما داخل دالة البناء __init__().\n2. أضف دالة داخل الكلاس تسمى greet() تقوم بطباعة رسالة ترحيبية تحتوي على اسم الشخص وعمره بتنسيق جميل.\n3. قم بإنشاء كائن جديد باسم person1 ومرر له اسماً وعمراً، ثم استدعِ دالة greet() لتتأكد من ظهور التحية المخصصة في الشاشة.",
            code: "class Person:\n    # 1. اكتب دالة البناء __init__ هنا\n    \n    # 2. اكتب دالة greet هنا\n    pass\n\n# 3. أنشئ الكائن person1 واستدعِ دالة greet()"
        }
    },
    {
        id: "lvl3_s2", level: 3, sessionNum: 10,
        title: "معمل اختراق الويب وحماية الخوادم (Cyber Hacking Lab) 💻🔒",
        badge: "المستوى 3 🐍 الجلسة 10",
        desc: "تعلم كيف تعمل هجمات التخمين Brute-Force وحماية خوادم Flask البرمجية!",
        concepts: [
            { title: "هجوم التخمين Brute-Force والقاموس 💣", desc: "- هجوم التخمين (Brute-Force): تقنية اختراق يقوم فيها المهاجم بتجربة كل تركيبات الأرقام والحروف المحتملة بشكل آلي حتى يجد كلمة المرور الصحيحة.\n- هجوم القاموس (Dictionary Attack): فكرة أذكى لتوفير الوقت تقوم بتجربة قائمة من الكلمات الشائعة (مثل كلمة مرور 123456).", icon: "💣" },
            { title: "مكتبة Requests ومكتبة Sys 🌐", desc: "- مكتبة requests: مكتبة قوية لإرسال طلبات الويب (GET/POST) والتحكم بالمواقع وتخمين كلمات المرور تلقائياً.\n- مكتبة sys: تتيح التفاعل مع بيئة تشغيل بايثون والتحكم في معاملات سطر الأوامر والخروج الفوري من الأكواد.", code: "import requests\nimport sys\n# إرسال طلب للموقع\nres = requests.get(\"https://google.com\")\nprint(res.status_code)", icon: "🌐" },
            { title: "خوادم الويب وإطار Flask 🧪", desc: "خادم الويب هو البرنامج الذي يستقبل الطلبات ويرد بالصفحات. إطار Flask هو مكتبة بايثون خفيفة وقوية تتيح لنا بناء مواقع ويب وخوادم متكاملة وتوجيه الروابط (Routes).", code: "from flask import Flask\napp = Flask(__name__)\n@app.route(\"/\")\ndef home():\n    return \"خادم محمي بكلمة مرور!\"\n# app.run()", icon: "🧪" },
            { title: "معمل الاختراق العملي 🔬", desc: "مكونات معملنا:\n- كود الواجهة (Front-End)\n- كود الخادم (Back-End) في server.py بكلمة مرور حقيقية\n- قائمة كلمات السر الشائعة (top-100.txt)\n- سكربت الهجوم (hack.py) الذي يرسل طلبات متكررة حتى ينجح!", icon: "🔬" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "قم بمحاكاة وتعديل معمل الاختراق في حاسوبك:\n1. قم بتغيير اسم المستخدم وكلمة المرور الحقيقية داخل كود server.py.\n2. قم بتعديل وإضافة كلمة مرورك الجديدة داخل ملف القاموس (wordlist.txt أو top-100.txt).\n3. قم بتشغيل سكربت الهجوم hack.py لتشاهد كيف يقوم بايثون باختراق الخادم تلقائياً وتخمين الباسورد الجديد.\n4. التقط لقطة شاشة (Screenshot) لنجاح الهجوم وظهور الباسورد المخترق وأرسلها لمهندسك!",
            code: "# 1. كود الخادم server.py\n# admin_user = \"new_admin\"\n# admin_pass = \"your_secret_pass\"\n\n# 2. كود الهجوم hack.py\n# قم بتشغيل السكربت لتخمين كلمة السر بنجاح!"
        }
    },
    {
        id: "lvl3_s3", level: 3, sessionNum: 11,
        title: "بناء لعبة البنج بونج - الجزء الأول 🏓",
        badge: "المستوى 3 🐍 الجلسة 11",
        desc: "صمم شاشة اللعبة السحرية وهيئ الكرة والمضارب وأزرار التحكم باستخدام مكتبة السلحفاة!",
        concepts: [
            { title: "تهيئة شاشة اللعبة ودورة التحديثات 📺", desc: "نستخدم كائن الشاشة في مكتبة السلحفاة، ونضبط العنوان والخلفية السوداء الرائعة، والأبعاد المناسبة للعب، ونلغي التحديث التلقائي ليكون الرسم فائق السرعة عبر دالة tracer(0).", icon: "📺" },
            { title: "إعداد الكرة والمضارب السحرية 🏓", desc: "نقوم بإنشاء المضربين والكرة ككائنات سلحفاة مستقلة، ونحدد شكلها وسرعة حركتها ولونها الأبيض، ونرفع القلم حتى لا تترك خطوطاً خلفها عند الحركة.", icon: "🏓" },
            { title: "محاور الحركة dx و dy 📏", desc: "نجعل الكرة تتحرك في بعدين عن طريق تزويدها بخاصيتين (dx و dy) وهما يعبران عن مقدار التغيير في إحداثيات الكرة في محوري السينات والصادات في كل دورة.", icon: "📏" },
            { title: "ربط أزرار لوحة المفاتيح 🎹", desc: "نكتب دالتين برمجيتين لتحريك المضرب للأعلى أو للأسفل (عن طريق زيادة أو نقصان إحداثي y للمضرب بمقدار 20 بكسل)، ثم نربطهما بمفاتيح الكيبورد باستخدام listen() و onkeypress().", icon: "🎹" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "قم بتثبيت وتجربة مكتبة الألعاب الكلاسيكية الجاهزة freegames عن طريق كتابة الأمر التالي في محطة الأوامر:\npip install freegames\nثم قم بتشغيل إحدى الألعاب المضمنة مثل لعبة الثعبان (snake) أو البونج (pong) للتسلية والتعلم، واكتشف كيف تمت كتابتها!",
            code: "# 1. افتح محطة الأوامر (CMD) وثبت المكتبة:\n# pip install freegames\n\n# 2. قم بتشغيل لعبة الثعبان البرمجية للمتعة والتجربة:\n# python -m freegames.snake"
        }
    },
    {
        id: "lvl3_s4", level: 3, sessionNum: 12,
        title: "بناء لعبة البنج بونج - الجزء الثاني 🏓🏆",
        badge: "المستوى 3 🐍 الجلسة 12",
        desc: "أكمل فيزياء اللعبة وحركة الكرة واصطدامات المضارب لتخرج بلعبة بنج بونج متكاملة وممتعة!",
        concepts: [
            { title: "دورة تحديثات اللعبة (Game Loop) 🔄", desc: "ننشئ حلقة تكرار While لا نهائية، ونقوم بتحديث الشاشة يدوياً فيها عبر screen.update() لنضمن أن الحركة فائقة السلاسة ودون تقطيع.", icon: "🔄" },
            { title: "حركة الكرة والارتداد من الجدران ⚽", desc: "- حركة الكرة: نزيد إحداثيات الكرة (x و y) بقيم dx و dy باستمرار.\n- اصطدام الجدران: عندما تصل الكرة لأعلى أو أسفل الشاشة، نقوم بعكس اتجاه حركتها الرأسية بضرب dy في -1 لترتد فوراً!", icon: "⚽" },
            { title: "الاصطدام بالمضارب 🏓", desc: "نقوم بفحص إحداثيات الكرة، فإذا اقتربت من مضرب اللاعب الأول أو الثاني وكانت تقع ضمن النطاق الرأسي للمضرب، نقوم بعكس اتجاه حركتها الأفقية بضرب dx في -1 لتطير للاتجاه المقابل!", icon: "🏓" },
            { title: "حساب النقاط وإعادة ضبط الشاشة 🎯", desc: "إذا مرت الكرة بجانب المضرب وخسرت، تزداد نقاط اللاعب المنافس، ونقوم بإعادة الكرة إلى مركز الشاشة بالضبط وعكس اتجاه حركتها لتبدأ دورة لعب جديدة، ثم نقوم بتحديث نص النتيجة المكتوب على الشاشة.", icon: "🎯" }
        ],
        homework: {
            title: "📝 التحدي المنزلي السحري (Homework)",
            desc: "تهانينا يا بطلنا العظيم! لقد أتممت مسار بايثون للتأسيس بنجاح مبهر! واجبك الأخير الممتع:\n1. قم بتجميع وتجميع وتعبئة لعبة البنج بونج الكاملة الخاصة بك إلى ملف تنفيذي (.exe) مستقل باستخدام أداة auto-py-to-exe.\n2. أرسل الملف التنفيذي لعائلتك وأصدقائك ليلعبوا لعبتك البرمجية المذهلة ويشهدوا على عبقريتك التكنولوجية!\n3. احصل على نسختك من شهادتك الرسمية من بوابة المهندس!",
            code: "# 1. للتعبئة لـ exe:\n# pip install auto-py-to-exe\n# python -m auto_py_to_exe\n\n# 2. شارك اللعبة مع أصدقائك واحتفل بنجاحك الرائع! 🎉"
        }
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
        this.renderExplanations(session.concepts, session.homework);

        // Update progress inside modal
        this.updateModalProgress();

        // Load interactive game
        this.loadSessionGame(session.id);
    }

    renderExplanations(concepts, homework) {
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

        // Appending the beautiful Homework Card
        if (homework) {
            const hwCard = document.createElement('div');
            hwCard.className = 'concept-card-premium homework-card-gold';
            hwCard.style.border = '3px solid #ffb703';
            hwCard.style.background = 'rgba(255, 183, 3, 0.08)';
            hwCard.style.boxShadow = '0 8px 24px rgba(255, 183, 3, 0.15)';
            hwCard.style.borderRadius = '20px';
            hwCard.style.padding = '20px';
            hwCard.style.marginTop = '20px';
            
            let codeMarkup = '';
            if (homework.code) {
                codeMarkup = `<pre class="concept-code-box" style="border-left-color: #ffb703; background: #023047; color: #fff;" dir="ltr">${homework.code}</pre>`;
            }

            hwCard.innerHTML = `
                <div class="concept-card-header" style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                    <span class="concept-card-icon" style="background: #ffb703; color: #023047; box-shadow: 0 4px 10px rgba(255,183,3,0.3); width: 35px; height: 35px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-size: 1.4rem;">📝</span>
                    <h5 class="concept-card-title" style="color: #ffb703; font-weight: 800; font-size: 1.6rem; margin: 0;">${homework.title}</h5>
                </div>
                <p class="concept-card-desc" style="color: #023047; font-weight: 700; line-height: 1.8; font-size: 1.35rem; margin-bottom: 15px;">${homework.desc.replace(/\n/g, '<br>')}</p>
                ${codeMarkup}
                <div style="margin-top: 15px; padding: 12px; background: rgba(6, 214, 160, 0.1); border: 2px dashed #06d6a0; border-radius: 12px; font-size: 1.25rem; color: #06d6a0; font-weight: bold; text-align: center;">
                    💡 تذكر يا بطل إرسال الواجب فور انتهائك منه لتقييمه والحصول على نقاط تفوق إضافية! 🌟
                </div>
            `;
            container.appendChild(hwCard);
        }
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
                titleEl.textContent = "🎮 محاكي سطر الأوامر: جرب دالة الطباعة والمتغيرات";
                this.initTerminalGame(container);
                break;
            case 'lvl1_s2':
                titleEl.textContent = "🎮 تصنيف البيانات: فرز الصناديق والقوائم السحرية";
                this.initDataSortingGame(container);
                break;
            case 'lvl1_s3':
                titleEl.textContent = "🎮 إشارة المرور الذكية: تحدي العمليات الحسابية والمقارنة";
                this.initTrafficLightGame(container);
                break;
            case 'lvl1_s4':
                titleEl.textContent = "🎮 قاعدة بيانات العميل السري: تحدي القواميس Dictionaries";
                this.initSpyDatabaseGame(container);
                break;
            case 'lvl2_s1':
                titleEl.textContent = "🎮 مصنع الكعك: تشغيل حلقة التكرار While Loop والشرط";
                this.initConveyorCakeGame(container);
                break;
            case 'lvl2_s2':
                titleEl.textContent = "🎮 الرسام المتنقل: تشغيل الحلقات المتداخلة والأبعاد";
                this.initNestedLoopsGame(container);
                break;
            case 'lvl2_s3':
                titleEl.textContent = "🎮 مرجل الساحر: تركيب الجرعة باستدعاء الدوال def";
                this.initPotionBrewingGame(container);
                break;
            case 'lvl2_s4':
                titleEl.textContent = "🎮 لوحة رسم السلحفاة: مغامرة Turtle Graphics الرائعة";
                this.initTurtleGraphicsGame(container);
                break;
            case 'lvl3_s1':
                titleEl.textContent = "🎮 مصنع تفريخ الكائنات: بناء بطل خارق Object من الـ Class";
                this.initHeroSpawnerGame(container);
                break;
            case 'lvl3_s2':
                titleEl.textContent = "🎮 معمل الاختراق الإلكتروني: محاكاة خوادم Flask والطلب";
                this.initFlaskServerGame(container);
                break;
            case 'lvl3_s3':
                titleEl.textContent = "🎮 لعبة البونج 🏓 الجزء 1: تهيئة شاشة الرسم وحركة المضربين";
                this.initPingPongPart1Game(container);
                break;
            case 'lvl3_s4':
                titleEl.textContent = "🎮 لعبة البونج 🏓 الجزء 2: الفيزياء الكاملة والتحدي المكتمل";
                this.initPingPongPart2Game(container);
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

    // GAME 11: Ping Pong Part 1 (Session 11)
    initPingPongPart1Game(container) {
        container.innerHTML = `
            <div class="pingpong-sandbox">
                <canvas id="pongPart1Canvas" width="320" height="180" style="background:#023047; border-radius:12px; border:3px solid #ffb703; display:block; margin:0 auto;"></canvas>
                <div class="pingpong-controls" style="margin-top:10px; display:flex; gap:10px; justify-content:center;">
                    <button class="btn-game-option" id="btnTestP1" style="background:#219ebc; color:#fff;">🎮 حركة المضرب الأيسر (W / S)</button>
                    <button class="btn-game-option" id="btnTestP2" style="background:#fb8500; color:#fff;">🎮 حركة المضرب الأيمن (Up / Down)</button>
                </div>
                <div style="margin-top:12px; padding:10px; background:rgba(33, 158, 188, 0.1); border-radius:8px; font-size:1.15rem; color:#219ebc; font-weight:bold; text-align:center;" id="pongPart1Status">
                    💡 انقر على الأزرار أعلاه أو اضغط على لوحة المفاتيح لتجربة تحريك المضارب برمجياً!
                </div>
            </div>
        `;

        setTimeout(() => {
            const canvas = document.getElementById('pongPart1Canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            // Game objects state
            let p1Y = 65;
            let p2Y = 65;
            const pHeight = 50;
            const pWidth = 10;
            const ballX = 160;
            const ballY = 90;

            const draw = () => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                
                // Draw dashed line
                ctx.strokeStyle = "rgba(255,255,255,0.2)";
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(160, 0);
                ctx.lineTo(160, 180);
                ctx.stroke();
                ctx.setLineDash([]);

                // Draw paddles
                ctx.fillStyle = "#219ebc"; // Player 1
                ctx.fillRect(15, p1Y, pWidth, pHeight);

                ctx.fillStyle = "#fb8500"; // Player 2
                ctx.fillRect(canvas.width - 25, p2Y, pWidth, pHeight);

                // Draw ball
                ctx.fillStyle = "#ffb703";
                ctx.beginPath();
                ctx.arc(ballX, ballY, 6, 0, Math.PI * 2);
                ctx.fill();
            };

            draw();

            const status = document.getElementById('pongPart1Status');
            let movedP1 = false;
            let movedP2 = false;

            const testP1 = () => {
                p1Y = p1Y === 65 ? 30 : 65;
                draw();
                playPopupSound();
                movedP1 = true;
                status.textContent = "✅ تحرك المضرب الأيسر (W/S) بنجاح!";
                checkProgress();
            };

            const testP2 = () => {
                p2Y = p2Y === 65 ? 100 : 65;
                draw();
                playPopupSound();
                movedP2 = true;
                status.textContent = "✅ تحرك المضرب الأيمن (Up/Down) بنجاح!";
                checkProgress();
            };

            document.getElementById('btnTestP1').onclick = testP1;
            document.getElementById('btnTestP2').onclick = testP2;

            // Optional keyboard listeners
            canvas.tabIndex = 1;
            canvas.style.outline = 'none';
            canvas.onkeydown = (e) => {
                e.preventDefault();
                if (e.key === 'w' || e.key === 'W') {
                    p1Y = Math.max(10, p1Y - 15);
                    movedP1 = true;
                    status.textContent = "🎹 تحريك يدوي: المضرب الأيسر للأعلى!";
                } else if (e.key === 's' || e.key === 'S') {
                    p1Y = Math.min(canvas.height - pHeight - 10, p1Y + 15);
                    movedP1 = true;
                    status.textContent = "🎹 تحريك يدوي: المضرب الأيسر للأسفل!";
                } else if (e.key === 'ArrowUp') {
                    p2Y = Math.max(10, p2Y - 15);
                    movedP2 = true;
                    status.textContent = "🎹 تحريك يدوي: المضرب الأيمن للأعلى!";
                } else if (e.key === 'ArrowDown') {
                    p2Y = Math.min(canvas.height - pHeight - 10, p2Y + 15);
                    movedP2 = true;
                    status.textContent = "🎹 تحريك يدوي: المضرب الأيمن للأسفل!";
                }
                draw();
                playPopupSound();
                checkProgress();
            };

            const checkProgress = () => {
                if (movedP1 && movedP2) {
                    status.style.color = '#06d6a0';
                    status.style.background = 'rgba(6,214,160,0.1)';
                    status.textContent = "🏆 رائع! لقد نجحت في تهيئة وتجربة حركة مضارب البونج بالكامل! (+100 XP)";
                    this.addXp(100);
                }
            };
        }, 50);
    }

    // GAME 12: Ping Pong Part 2 (Session 12)
    initPingPongPart2Game(container) {
        container.innerHTML = `
            <div class="pingpong-game-full">
                <div style="display:flex; justify-content:space-between; margin-bottom:8px; font-weight:bold; font-size:1.2rem; color:#023047;">
                    <span style="color:#219ebc;">اللاعب 1: <span id="p1Score">0</span></span>
                    <span style="color:#ffb703;" id="pongRoundStatus">العب بنج بونج! 🏓</span>
                    <span style="color:#fb8500;">الحاسوب: <span id="p2Score">0</span></span>
                </div>
                <canvas id="pongPart2Canvas" width="320" height="180" style="background:#023047; border-radius:12px; border:3px solid #ffb703; display:block; margin:0 auto; cursor:pointer;"></canvas>
                <div style="margin-top:10px; display:flex; justify-content:center; gap:10px;">
                    <button class="btn-game-option" id="btnStartPongGame" style="background:#06d6a0; color:#fff; font-weight:bold;">🚀 انقر لبدء اللعبة</button>
                </div>
                <p style="text-align:center; font-size:1rem; color:#5c677d; margin-top:8px;">💡 تحكم بمضربك الأيسر باستخدام الماوس (تحريك للأعلى والأسفل) وتغلب على الذكاء الاصطناعي لتفوز بـ XP!</p>
            </div>
        `;

        setTimeout(() => {
            const canvas = document.getElementById('pongPart2Canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');

            // Game logic vars
            let ballX = 160;
            let ballY = 90;
            let ballSpeedX = 2.5;
            let ballSpeedY = 1.5;

            let p1Y = 65;
            let p2Y = 65;
            const pHeight = 45;
            const pWidth = 8;
            let p1Score = 0;
            let p2Score = 0;
            let gameRunning = false;
            let gameInterval = null;

            const p1ScoreEl = document.getElementById('p1Score');
            const p2ScoreEl = document.getElementById('p2Score');
            const roundStatusEl = document.getElementById('pongRoundStatus');
            const startBtn = document.getElementById('btnStartPongGame');

            const resetBall = () => {
                ballX = 160;
                ballY = 90;
                ballSpeedX = -ballSpeedX > 0 ? 2.5 : -2.5;
                ballSpeedY = (Math.random() * 2 - 1) * 2;
            };

            const draw = () => {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                // Dashed line
                ctx.strokeStyle = "rgba(255,255,255,0.15)";
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(160, 0);
                ctx.lineTo(160, 180);
                ctx.stroke();
                ctx.setLineDash([]);

                // Paddles
                ctx.fillStyle = "#219ebc"; // P1
                ctx.fillRect(10, p1Y, pWidth, pHeight);

                ctx.fillStyle = "#fb8500"; // P2 (AI)
                ctx.fillRect(canvas.width - 18, p2Y, pWidth, pHeight);

                // Ball
                ctx.fillStyle = "#ffb703";
                ctx.beginPath();
                ctx.arc(ballX, ballY, 6, 0, Math.PI * 2);
                ctx.fill();
            };

            const update = () => {
                if (!gameRunning) return;

                // Move ball
                ballX += ballSpeedX;
                ballY += ballSpeedY;

                // Simple AI for P2
                const p2Center = p2Y + pHeight / 2;
                if (p2Center < ballY - 10) {
                    p2Y = Math.min(canvas.height - pHeight - 5, p2Y + 2.2);
                } else if (p2Center > ballY + 10) {
                    p2Y = Math.max(5, p2Y - 2.2);
                }

                // Top/Bottom bounce
                if (ballY <= 6 || ballY >= canvas.height - 6) {
                    ballSpeedY = -ballSpeedY;
                    playPopupSound();
                }

                // Paddle 1 (Left Player) collision
                if (ballX <= 22 && ballX >= 10) {
                    if (ballY >= p1Y && ballY <= p1Y + pHeight) {
                        ballSpeedX = -ballSpeedX * 1.08; // slightly speed up
                        ballX = 23; // prevent stuck
                        playPopupSound();
                    }
                }

                // Paddle 2 (Right AI) collision
                if (ballX >= canvas.width - 22 && ballX <= canvas.width - 10) {
                    if (ballY >= p2Y && ballY <= p2Y + pHeight) {
                        ballSpeedX = -ballSpeedX * 1.08;
                        ballX = canvas.width - 23;
                        playPopupSound();
                    }
                }

                // Out of bounds (Score points)
                if (ballX < 0) {
                    p2Score++;
                    p2ScoreEl.textContent = p2Score;
                    playPopupSound();
                    resetBall();
                    checkWin();
                } else if (ballX > canvas.width) {
                    p1Score++;
                    p1ScoreEl.textContent = p1Score;
                    playHappyChime();
                    resetBall();
                    checkWin();
                }

                draw();
            };

            const checkWin = () => {
                if (p1Score >= 2) {
                    gameRunning = false;
                    clearInterval(gameInterval);
                    roundStatusEl.textContent = "🏆 لقد فزت بالمباراة! 🎉";
                    roundStatusEl.style.color = "#06d6a0";
                    triggerConfetti();
                    playHappyChime();
                    this.addXp(100);
                    startBtn.disabled = false;
                    startBtn.textContent = "🔄 العب مجدداً";
                } else if (p2Score >= 2) {
                    gameRunning = false;
                    clearInterval(gameInterval);
                    roundStatusEl.textContent = "👾 فاز الكمبيوتر! حاول ثانية.";
                    roundStatusEl.style.color = "#ef4444";
                    startBtn.disabled = false;
                    startBtn.textContent = "🔄 إعادة المحاولة";
                }
            };

            // Mouse control for left paddle
            canvas.onmousemove = (e) => {
                const rect = canvas.getBoundingClientRect();
                const relativeY = e.clientY - rect.top;
                p1Y = Math.max(5, Math.min(canvas.height - pHeight - 5, relativeY - pHeight / 2));
                if (!gameRunning) draw();
            };

            startBtn.onclick = () => {
                playPopupSound();
                p1Score = 0;
                p2Score = 0;
                p1ScoreEl.textContent = "0";
                p2ScoreEl.textContent = "0";
                roundStatusEl.textContent = "مباراة حماسية! 🔥";
                roundStatusEl.style.color = "#ffb703";
                resetBall();
                gameRunning = true;
                startBtn.disabled = true;

                if (gameInterval) clearInterval(gameInterval);
                gameInterval = setInterval(update, 1000 / 60); // 60 FPS
            };

            draw();
        }, 50);
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
