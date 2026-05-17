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

    // Auto-discover Teaching Aids
    const teachingAidsContainer = document.getElementById('teachingAidsContainer');
    if (teachingAidsContainer) {
        fetch('./database/courses_index.json')
            .then(res => res.json())
            .then(coursesList => {
                coursesList.forEach(courseId => {
                    fetch(`./database/${courseId}/teaching_aids.json`)
                        .then(r => {
                            if (!r.ok) throw new Error('No teaching aids');
                            return r.json();
                        })
                        .then(aidsData => {
                            renderTeachingAidsGroup(aidsData, teachingAidsContainer);
                        })
                        .catch(e => {}); // Silent catch for courses without aids
                });
            })
            .catch(err => console.error('Error loading courses index for aids:', err));
    }

    // Check Login State
    const isLoggedIn = sessionStorage.getItem('engineer_logged_in') === 'true';
    if (isLoggedIn) {
        showView(viewDashboard);
        loadSubmissions();
    } else {
        showView(viewLogin);
    }
});

// Render Discovered Teaching Aids Group Helper
function renderTeachingAidsGroup(data, containerEl) {
    const groupEl = document.createElement('div');
    groupEl.className = 'teaching-aid-group';
    groupEl.style.cssText = 'background: rgba(255,255,255,0.95); border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.06); border: 2px solid #edf2f7;';

    groupEl.innerHTML = `
        <h4 style="font-size: 2rem; color: #8338ec; margin-bottom: 25px; border-bottom: 2px dashed #e0cffc; padding-bottom: 10px;">
            ${data.course_title}
        </h4>
        <div class="aids-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px;"></div>
    `;

    const gridEl = groupEl.querySelector('.aids-grid');

    data.aids.forEach(aid => {
        const card = document.createElement('div');
        card.className = 'aid-card';
        card.style.cssText = 'background: #fff; border-radius: 16px; padding: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.05); border: 2px solid #edf2f7; display: flex; flex-direction: column; justify-content: space-between;';

        let interactiveArea = '';

        if (aid.type === 'variable_box') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #fff9f2; border-radius: 16px; border: 3px dashed #ff7b00; text-align: center;">
                    <div style="font-size: 1.6rem; margin-bottom: 15px;">📦 الصندوق السحري (المتغير x): <strong id="varBoxVal_${aid.id}" style="color: #ff7b00; font-size: 2rem; background: #fff; padding: 5px 15px; border-radius: 10px; border: 2px solid #ff7b00;">${aid.init_val || 'فارغ'}</strong></div>
                    <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                        ${(aid.options || []).map((opt, i) => `<button class="btn-var-opt" onclick="document.getElementById('varBoxVal_${aid.id}').textContent = '${opt}'; if(typeof playPopupSound === 'function') playPopupSound(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 8px 16px; font-size: 1.3rem; font-weight: bold; border-radius: 12px; background: #ffb703; color: #023047; border: none; cursor: pointer; box-shadow: 0 4px 10px rgba(255,183,3,0.3); transition: transform 0.2s;">اسحب: ${opt}</button>`).join('')}
                    </div>
                </div>
            `;
        } else if (aid.type === 'traffic_light') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #e2f8fa; border-radius: 16px; border: 3px dashed #219ebc; text-align: center;">
                    <div style="display: flex; justify-content: center; gap: 15px; margin-bottom: 20px;">
                        <div id="lightRed_${aid.id}" style="width: 50px; height: 50px; border-radius: 50%; background: #ff006e; opacity: 0.3; box-shadow: 0 0 15px #ff006e; border: 3px solid #023047;"></div>
                        <div id="lightGreen_${aid.id}" style="width: 50px; height: 50px; border-radius: 50%; background: #06d6a0; opacity: 1; box-shadow: 0 0 15px #06d6a0; border: 3px solid #023047;"></div>
                    </div>
                    <div id="carStatus_${aid.id}" style="font-size: 1.8rem; font-weight: bold; color: #06d6a0; margin-bottom: 15px;">🚗 الإشارة خضراء (else: go) - السيارة تنطلق بسلام!</div>
                    <div style="display: flex; gap: 15px; justify-content: center;">
                        <button onclick="document.getElementById('lightRed_${aid.id}').style.opacity = '1'; document.getElementById('lightGreen_${aid.id}').style.opacity = '0.3'; document.getElementById('carStatus_${aid.id}').textContent = '🛑 الإشارة حمراء (if red: stop) - السيارة تتوقف!'; document.getElementById('carStatus_${aid.id}').style.color = '#ff006e'; if(typeof playPopupSound === 'function') playPopupSound();" style="padding: 10px 20px; font-size: 1.4rem; font-weight: bold; border-radius: 12px; background: #ff006e; color: #fff; border: none; cursor: pointer;">أحمر (قف 🛑)</button>
                        <button onclick="document.getElementById('lightGreen_${aid.id}').style.opacity = '1'; document.getElementById('lightRed_${aid.id}').style.opacity = '0.3'; document.getElementById('carStatus_${aid.id}').textContent = '🚗 الإشارة خضراء (else: go) - السيارة تنطلق بسلام!'; document.getElementById('carStatus_${aid.id}').style.color = '#06d6a0'; if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 10px 20px; font-size: 1.4rem; font-weight: bold; border-radius: 12px; background: #06d6a0; color: #023047; border: none; cursor: pointer;">أخضر (انطلق 🚗)</button>
                    </div>
                </div>
            `;
        } else if (aid.type === 'loop_factory') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #f5f3ff; border-radius: 16px; border: 3px dashed #8338ec; text-align: center;">
                    <div style="font-size: 1.6rem; margin-bottom: 15px;">📦 الهدايا المغلفة: <strong id="loopCount_${aid.id}" style="color: #8338ec; font-size: 2.2rem;">0 / 5</strong></div>
                    <div id="loopBar_${aid.id}" style="width: 100%; height: 20px; background: #edf2f7; border-radius: 10px; overflow: hidden; margin-bottom: 20px;">
                        <div id="loopProgress_${aid.id}" style="width: 0%; height: 100%; background: linear-gradient(45deg, #8338ec, #ff006e); transition: width 0.3s;"></div>
                    </div>
                    <button onclick="let c = 0; let int = setInterval(() => { c++; document.getElementById('loopCount_${aid.id}').textContent = c + ' / 5'; document.getElementById('loopProgress_${aid.id}').style.width = (c*20) + '%'; if(typeof playPopupSound === 'function') playPopupSound(); if(c === 5) { clearInterval(int); if(typeof triggerConfetti === 'function') triggerConfetti(); if(typeof playHappyChime === 'function') playHappyChime(); } }, 800);" style="padding: 12px 30px; font-size: 1.4rem; font-weight: bold; border-radius: 12px; background: #8338ec; color: #fff; border: none; cursor: pointer; box-shadow: 0 6px 15px rgba(131,56,236,0.4);">🚀 تشغيل حلقة التكرار for i in range(5)</button>
                </div>
            `;
        } else if (aid.type === 'block_train') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #fff9f2; border-radius: 16px; border: 3px dashed #ffb703; text-align: center;">
                    <div id="trainArea_${aid.id}" style="display: flex; gap: 10px; justify-content: center; margin-bottom: 20px; min-height: 60px; align-items: center; background: #fff; padding: 15px; border-radius: 12px; border: 2px solid #ffb703;">
                        <span style="color: #888; font-size: 1.3rem;">اسحب وركب البلوكات هنا بالترتيب لتشغيل القطار...</span>
                    </div>
                    <div style="display: flex; gap: 10px; justify-content: center; flex-wrap: wrap;">
                        <button onclick="document.getElementById('trainArea_${aid.id}').innerHTML = '<div style=\\'background:#ffb703; padding:8px 15px; border-radius:10px; font-weight:bold; color:#023047;\\'>🟡 عند النقر على العلم</div>'; if(typeof playPopupSound === 'function') playPopupSound();" style="padding: 8px 15px; background: #ffb703; color: #023047; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">1. حدث النقر 🟡</button>
                        <button onclick="document.getElementById('trainArea_${aid.id}').innerHTML += '<div style=\\'background:#219ebc; padding:8px 15px; border-radius:10px; font-weight:bold; color:#fff;\\'>🔵 تحرك 10 خطوات</div>'; if(typeof playPopupSound === 'function') playPopupSound();" style="padding: 8px 15px; background: #219ebc; color: #fff; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">2. الحركة 🔵</button>
                        <button onclick="document.getElementById('trainArea_${aid.id}').innerHTML += '<div style=\\'background:#8338ec; padding:8px 15px; border-radius:10px; font-weight:bold; color:#fff;\\'>🟣 قل مرحباً</div>'; if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 8px 15px; background: #8338ec; color: #fff; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">3. الهيئة 🟣</button>
                    </div>
                </div>
            `;
        } else if (aid.type === 'xy_hunt') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #f0f8ff; border-radius: 16px; border: 3px dashed #219ebc; text-align: center;">
                    <div style="position: relative; width: 100%; height: 160px; background: #e2f8fa; border-radius: 12px; border: 2px solid #219ebc; overflow: hidden; margin-bottom: 20px;">
                        <div style="position: absolute; top: 50%; left: 0; width: 100%; height: 2px; background: #023047; opacity: 0.3;"></div>
                        <div style="position: absolute; top: 0; left: 50%; width: 2px; height: 100%; background: #023047; opacity: 0.3;"></div>
                        <div id="catSprite_${aid.id}" style="position: absolute; top: 70px; left: 140px; font-size: 2.5rem; transition: all 0.5s;">🐱</div>
                        <div id="treasure_${aid.id}" style="position: absolute; top: 20px; left: 240px; font-size: 2.2rem;">💎</div>
                    </div>
                    <button onclick="document.getElementById('catSprite_${aid.id}').style.top = '20px'; document.getElementById('catSprite_${aid.id}').style.left = '240px'; if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 10px 25px; font-size: 1.4rem; font-weight: bold; border-radius: 12px; background: #219ebc; color: #fff; border: none; cursor: pointer;">اذهب إلى الكنز (X: 100, Y: 50) 🚀</button>
                </div>
            `;
        } else if (aid.type === 'ai_trainer') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #fef6fb; border-radius: 16px; border: 3px dashed #ff006e; text-align: center;">
                    <div style="font-size: 1.5rem; margin-bottom: 15px;">📊 بيانات التدريب: تفاح (<strong id="appleCnt_${aid.id}">0</strong>) | موز (<strong id="bananaCnt_${aid.id}">0</strong>)</div>
                    <div style="display: flex; gap: 15px; justify-content: center; margin-bottom: 20px;">
                        <button onclick="let c = parseInt(document.getElementById('appleCnt_${aid.id}').textContent)+1; document.getElementById('appleCnt_${aid.id}').textContent = c; if(typeof playPopupSound === 'function') playPopupSound();" style="padding: 10px 20px; font-size: 1.5rem; background: #ff006e; color: #fff; border: none; border-radius: 12px; cursor: pointer;">🍎 إضافة تفاح</button>
                        <button onclick="let c = parseInt(document.getElementById('bananaCnt_${aid.id}').textContent)+1; document.getElementById('bananaCnt_${aid.id}').textContent = c; if(typeof playPopupSound === 'function') playPopupSound();" style="padding: 10px 20px; font-size: 1.5rem; background: #ffb703; color: #023047; border: none; border-radius: 12px; cursor: pointer;">🍌 إضافة موز</button>
                    </div>
                    <button onclick="if(parseInt(document.getElementById('appleCnt_${aid.id}').textContent) > 0 && parseInt(document.getElementById('bananaCnt_${aid.id}').textContent) > 0) { alert('🤖 الروبوت: لقد تعلمت بنجاح! هذه الصورة الجديدة هي: تفاحة 🍎 (بنسبة ثقة 98%)'); if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti(); } else { alert('⚠️ الروبوت: من فضلك قم بتزويدي بصور التفاح والموز أولاً لأتعلم!'); }" style="padding: 12px 30px; font-size: 1.4rem; font-weight: bold; background: #8338ec; color: #fff; border: none; border-radius: 12px; cursor: pointer;">🧪 اختبار الروبوت بصورة جديدة 🚀</button>
                </div>
            `;
        } else if (aid.type === 'face_landmarks') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #f5f3ff; border-radius: 16px; border: 3px dashed #8338ec; text-align: center;">
                    <div style="position: relative; width: 140px; height: 140px; margin: 0 auto 20px; background: #edf2f7; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 5rem; border: 3px solid #8338ec;">
                        🙂
                        <div id="glasses_${aid.id}" style="position: absolute; top: 35px; left: 15px; font-size: 4rem; display: none;">🕶️</div>
                        <div id="hat_${aid.id}" style="position: absolute; top: -35px; left: 25px; font-size: 4.5rem; display: none;">🎩</div>
                    </div>
                    <div style="display: flex; gap: 15px; justify-content: center;">
                        <button onclick="document.getElementById('glasses_${aid.id}').style.display = 'block'; if(typeof playPopupSound === 'function') playPopupSound();" style="padding: 10px 20px; font-size: 1.3rem; font-weight: bold; background: #219ebc; color: #fff; border: none; border-radius: 12px; cursor: pointer;">تحديد العينين (🕶️)</button>
                        <button onclick="document.getElementById('hat_${aid.id}').style.display = 'block'; if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 10px 20px; font-size: 1.3rem; font-weight: bold; background: #ff006e; color: #fff; border: none; border-radius: 12px; cursor: pointer;">تحديد الرأس (🎩)</button>
                    </div>
                </div>
            `;
        } else if (aid.type === 'circuit_builder') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #fff9f2; border-radius: 16px; border: 3px dashed #ffb703; text-align: center;">
                    <div style="display: flex; justify-content: center; align-items: center; gap: 20px; margin-bottom: 20px; font-size: 3rem;">
                        🔋 <span id="wire_${aid.id}" style="color: #ff006e;">--/--</span> <span id="led_${aid.id}" style="filter: grayscale(1);">💡</span>
                    </div>
                    <button onclick="document.getElementById('wire_${aid.id}').textContent = '-----'; document.getElementById('led_${aid.id}').style.filter = 'grayscale(0) drop-shadow(0 0 15px #ffb703)'; if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 12px 30px; font-size: 1.4rem; font-weight: bold; background: #ffb703; color: #023047; border: none; border-radius: 12px; cursor: pointer; box-shadow: 0 6px 15px rgba(255,183,3,0.4);">🔌 إغلاق الدائرة الكهربائية ⚡</button>
                </div>
            `;
        } else if (aid.type === 'ultrasonic_radar') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #e2f8fa; border-radius: 16px; border: 3px dashed #219ebc; text-align: center;">
                    <div style="position: relative; width: 100%; height: 80px; background: #edf2f7; border-radius: 12px; overflow: hidden; margin-bottom: 20px; display: flex; align-items: center;">
                        <div id="carRadar_${aid.id}" style="position: absolute; left: 10px; font-size: 3rem; transition: left 1s;">🚗</div>
                        <div style="position: absolute; right: 10px; font-size: 3rem; border-right: 5px solid #ff006e; padding-right: 10px;">🧱</div>
                    </div>
                    <button onclick="document.getElementById('carRadar_${aid.id}').style.left = 'calc(100% - 90px)'; setTimeout(() => { alert('🚨 الرادار: تحذير! تم اكتشاف جدار على مسافة 10 سم. التوقف التلقائي مفعل!'); if(typeof playPopupSound === 'function') playPopupSound(); if(typeof triggerConfetti === 'function') triggerConfetti(); }, 1000);" style="padding: 12px 30px; font-size: 1.4rem; font-weight: bold; background: #219ebc; color: #fff; border: none; border-radius: 12px; cursor: pointer; box-shadow: 0 6px 15px rgba(33,158,188,0.4);">📡 تشغيل رادار السيارة والاقتراب 🚀</button>
                </div>
            `;
        } else if (aid.type === 'pet_snap') {
            interactiveArea = `
                <div class="aid-interactive-box" style="margin: 20px 0; padding: 20px; background: #fff9f2; border-radius: 16px; border: 3px dashed #ff7b00; text-align: center;">
                    <div style="display: flex; justify-content: center; align-items: center; gap: 30px; margin-bottom: 20px;">
                        <div style="background: #ff7b00; color: #fff; padding: 15px 25px; border-radius: 16px; font-size: 1.6rem; font-weight: bold;">🍖 بلوك: أطعم الكلب</div>
                        <div id="dogPet_${aid.id}" style="font-size: 4.5rem; transition: transform 0.3s;">🐶 💤</div>
                    </div>
                    <button onclick="document.getElementById('dogPet_${aid.id}').textContent = '🐶 🍖 (يهز ذيله فرحاً!)'; document.getElementById('dogPet_${aid.id}').style.transform = 'scale(1.2)'; if(typeof playHappyChime === 'function') playHappyChime(); if(typeof triggerConfetti === 'function') triggerConfetti();" style="padding: 12px 30px; font-size: 1.4rem; font-weight: bold; background: #ffb703; color: #023047; border: none; border-radius: 12px; cursor: pointer; box-shadow: 0 6px 15px rgba(255,183,3,0.4);">تشغيل قصة إطعام الكلب 🚀</button>
                </div>
            `;
        }

        card.innerHTML = `
            <div>
                <h5 style="font-size: 1.7rem; color: #023047; margin-bottom: 10px;">${aid.title}</h5>
                <p style="font-size: 1.3rem; color: #5c677d; line-height: 1.6;">${aid.desc}</p>
                ${interactiveArea}
            </div>
            <div style="text-align: left; margin-top: 15px;">
                <span style="font-size: 1.1rem; background: #edf2f7; color: #5c677d; padding: 4px 12px; border-radius: 8px; font-weight: bold;">جاهز للتشغيل في الحصة 🌟</span>
            </div>
        `;
        gridEl.appendChild(card);
    });

    containerEl.appendChild(groupEl);
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
