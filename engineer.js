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

    // Check Login State
    const isLoggedIn = sessionStorage.getItem('engineer_logged_in') === 'true';
    if (isLoggedIn) {
        showView(viewDashboard);
        loadSubmissions();
    } else {
        showView(viewLogin);
    }
});

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
