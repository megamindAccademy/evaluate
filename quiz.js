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

function playGentleBeep() {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(330, now); // E4
    osc.frequency.exponentialRampToValueAtTime(220, now + 0.2); // A3
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.4, now + 0.05);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.35);
}

// Lightweight Custom Confetti Animation
function triggerConfetti(duration = 5000) {
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

        if (activePieces > 0 && Date.now() - startTime < duration) {
            requestAnimationFrame(animate);
        } else {
            if (canvas.parentNode) document.body.removeChild(canvas);
        }
    }
    animate();
}

// Quiz Management Variables
let manifestData = null;
let recapData = null;
let currentQuizData = null;
let currentQuestionIndex = 0;
let score = 0;
let mcqCount = 0;
let isQuestionAnswered = false;
let currentCourse = 'python';

// Student & Evaluation Tracking
let studentInfo = { name: '', group: '', teacher: '' };
let studentAnswers = []; // Stores { questionId, type: 'mcq'|'task', question, answer/selectedText, isCorrect, correctText }

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
        console.log("Firebase Realtime Database initialized successfully in quiz.js!");
    }
} catch (e) {
    console.error("Firebase initialization error:", e);
}

// DOM Elements
let viewRegistration, viewRecap, viewQuestion, viewResult;
let regFormEl, studentNameInputEl, groupNameInputEl, teacherNameInputEl;
let quizCourseTitleEl, recapTitleEl, recapSubtitleEl, recapCardsGridEl;
let progressTextEl, progressBarEl, questionTextEl, optionsGridEl;
let taskEditorContainerEl, editorLangTitleEl, taskHintTextEl, taskEditorTextareaEl, btnSubmitTaskBtnEl;
let feedbackContainerEl, feedbackTitleEl, feedbackDescEl, btnNextQuestionEl;
let resultScoreNumEl, resultMsgEl, engineerPortalContainerEl, btnPrintReportEl, btnRetryEl;

document.addEventListener('DOMContentLoaded', () => {
    // Initialize DOM Elements
    viewRegistration = document.getElementById('viewRegistration');
    viewRecap = document.getElementById('viewRecap');
    viewQuestion = document.getElementById('viewQuestion');
    viewResult = document.getElementById('viewResult');

    regFormEl = document.getElementById('regForm');
    studentNameInputEl = document.getElementById('studentNameInput');
    groupNameInputEl = document.getElementById('groupNameInput');
    teacherNameInputEl = document.getElementById('teacherNameInput');

    quizCourseTitleEl = document.getElementById('quizCourseTitle');
    recapTitleEl = document.getElementById('recapTitle');
    recapSubtitleEl = document.getElementById('recapSubtitle');
    recapCardsGridEl = document.getElementById('recapCardsGrid');

    progressTextEl = document.getElementById('progressText');
    progressBarEl = document.getElementById('progressBar');
    questionTextEl = document.getElementById('questionText');
    optionsGridEl = document.getElementById('optionsGrid');

    taskEditorContainerEl = document.getElementById('taskEditorContainer');
    editorLangTitleEl = document.getElementById('editorLangTitle');
    taskHintTextEl = document.getElementById('taskHintText');
    taskEditorTextareaEl = document.getElementById('taskEditorTextarea');
    btnSubmitTaskBtnEl = document.getElementById('btnSubmitTaskBtn');

    feedbackContainerEl = document.getElementById('feedbackContainer');
    feedbackTitleEl = document.getElementById('feedbackTitle');
    feedbackDescEl = document.getElementById('feedbackDesc');
    btnNextQuestionEl = document.getElementById('btnNextQuestion');

    resultScoreNumEl = document.getElementById('resultScoreNum');
    resultMsgEl = document.getElementById('resultMsg');
    engineerPortalContainerEl = document.getElementById('engineerPortalContainer');
    btnPrintReportEl = document.getElementById('btnPrintReport');
    btnRetryEl = document.getElementById('btnRetry');

    // Event Listeners
    if (regFormEl) {
        regFormEl.addEventListener('submit', handleRegistrationSubmit);
    }

    const btnStartQuiz = document.getElementById('btnStartQuiz');
    if (btnStartQuiz) {
        btnStartQuiz.addEventListener('click', startRandomQuiz);
    }

    if (btnSubmitTaskBtnEl) {
        btnSubmitTaskBtnEl.addEventListener('click', handleTaskSubmission);
    }

    if (btnNextQuestionEl) {
        btnNextQuestionEl.addEventListener('click', handleNextQuestion);
    }

    if (btnPrintReportEl) {
        btnPrintReportEl.addEventListener('click', () => window.print());
    }

    if (btnRetryEl) {
        btnRetryEl.addEventListener('click', restartQuizFlow);
    }

    // Determine course from URL parameter
    const urlParams = new URLSearchParams(window.location.search);
    currentCourse = urlParams.get('course') || 'python';

    // Fetch Course Manifest from Database
    fetch(`./database/${currentCourse}/manifest.json`)
        .then(response => {
            if (!response.ok) throw new Error(`Manifest not found for course: ${currentCourse}`);
            return response.json();
        })
        .then(manifest => {
            manifestData = manifest;
            if (quizCourseTitleEl) quizCourseTitleEl.textContent = manifest.course_title;
            return fetch(`./database/${currentCourse}/${manifest.recap_file}`);
        })
        .then(response => {
            if (!response.ok) throw new Error(`Recap file not found`);
            return response.json();
        })
        .then(recap => {
            recapData = recap;
            // Initially show registration screen
            showView(viewRegistration);
        })
        .catch(error => {
            console.error('Error loading database JSON:', error);
            if (quizCourseTitleEl) {
                quizCourseTitleEl.textContent = 'خطأ في تحميل بيانات الاختبار';
            }
        });
});

// Switch Active View Helper
function showView(viewEl) {
    [viewRegistration, viewRecap, viewQuestion, viewResult].forEach(v => {
        if (v) v.classList.remove('active');
    });
    if (viewEl) viewEl.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

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

// Helper to detect if text is predominantly English (LTR) or Arabic (RTL)
function getTextDirection(text) {
    if (!text) return 'rtl';
    const cleaned = text.replace(/[\u1F600-\u1F64F\u1F300-\u1F5FF\u1F680-\u1F6FF\u1F700-\u1F77F\u1F780-\u1F7FF\u1F800-\u1F8FF\u2600-\u26FF\u2700-\u27BF\u0020-\u003F\u00A0-\u00BF]/g, '').trim();
    if (!cleaned) return 'rtl';
    const firstChar = cleaned.charAt(0);
    if (/[\u0600-\u06FF]/.test(firstChar)) {
        return 'rtl';
    } else {
        return 'ltr';
    }
}

// 0. Handle Registration Submit
function handleRegistrationSubmit(e) {
    e.preventDefault();
    studentInfo.name = studentNameInputEl.value.trim();
    studentInfo.group = groupNameInputEl.value.trim();
    studentInfo.teacher = teacherNameInputEl.value.trim();

    playHappyChime();
    initRecapScreen();
}

// 1. Initialize Recap Screen (Grouped by Sessions)
function initRecapScreen() {
    if (!recapData) return;

    const titleDir = getTextDirection(recapData.recap_title);
    if (recapTitleEl) {
        recapTitleEl.textContent = recapData.recap_title;
        recapTitleEl.setAttribute('dir', titleDir);
        recapTitleEl.style.textAlign = titleDir === 'ltr' ? 'left' : 'right';
    }

    const subText = `أهلاً بك يا بطل ${studentInfo.name} (مجموعة: ${studentInfo.group} مع المهندس ${studentInfo.teacher})! ${recapData.recap_subtitle}`;
    const subDir = getTextDirection(recapData.recap_subtitle);
    if (recapSubtitleEl) {
        recapSubtitleEl.textContent = subText;
        recapSubtitleEl.setAttribute('dir', subDir);
        recapSubtitleEl.style.textAlign = subDir === 'ltr' ? 'left' : 'right';
    }

    // Populate Recap Cards Grouped by Sessions
    if (recapCardsGridEl) {
        recapCardsGridEl.innerHTML = '';
        
        recapData.sessions.forEach(session => {
            const sessionGroup = document.createElement('div');
            sessionGroup.className = 'recap-session-group';
            sessionGroup.style.width = '100%';
            sessionGroup.style.marginTop = '35px';
            sessionGroup.style.marginBottom = '20px';

            const sessDir = getTextDirection(session.session_title);
            const sessionHeader = document.createElement('h3');
            sessionHeader.className = 'recap-session-title';
            sessionHeader.setAttribute('dir', sessDir);
            sessionHeader.style.textAlign = sessDir === 'ltr' ? 'left' : 'right';
            sessionHeader.style.fontSize = '2.2rem';
            sessionHeader.style.fontWeight = '900';
            sessionHeader.style.color = 'var(--tertiary-dark)';
            sessionHeader.style.borderBottom = '4px solid var(--secondary)';
            sessionHeader.style.paddingBottom = '12px';
            sessionHeader.textContent = session.session_title;
            sessionGroup.appendChild(sessionHeader);
            
            recapCardsGridEl.appendChild(sessionGroup);

            session.points.forEach(point => {
                const cardDir = getTextDirection(point.desc);
                const card = document.createElement('div');
                card.className = 'recap-card';
                card.setAttribute('dir', cardDir);
                card.style.textAlign = cardDir === 'ltr' ? 'left' : 'right';

                card.innerHTML = `
                    <div class="recap-card-icon">${point.icon}</div>
                    <div class="recap-card-content">
                        <h4 style="text-align: ${cardDir === 'ltr' ? 'left' : 'right'};">${point.title}</h4>
                        <p style="text-align: ${cardDir === 'ltr' ? 'left' : 'right'};">${cleanBiDiText(point.desc)}</p>
                    </div>
                `;
                recapCardsGridEl.appendChild(card);
            });
        });
    }

    showView(viewRecap);
}

// 2. Start Random Quiz from Manifest Quizzes List
function startRandomQuiz() {
    if (!manifestData || !manifestData.quizzes || manifestData.quizzes.length === 0) {
        alert('لا توجد اختبارات متاحة حالياً لهذا المسار.');
        return;
    }

    const randomIndex = Math.floor(Math.random() * manifestData.quizzes.length);
    const randomQuizFileName = manifestData.quizzes[randomIndex];

    fetch(`./database/${currentCourse}/quizzes/${randomQuizFileName}`)
        .then(response => {
            if (!response.ok) throw new Error(`Quiz file ${randomQuizFileName} not found`);
            return response.json();
        })
        .then(quiz => {
            currentQuizData = quiz;
            currentQuestionIndex = 0;
            score = 0;
            mcqCount = 0;
            studentAnswers = [];
            playHappyChime();
            renderCurrentQuestion();
            showView(viewQuestion);
        })
        .catch(error => {
            console.error('Error loading random quiz:', error);
            alert('حدث خطأ أثناء تحميل الاختبار العشوائي.');
        });
}

// Render Current Question
function renderCurrentQuestion() {
    if (!currentQuizData || !currentQuizData.questions) return;

    isQuestionAnswered = false;
    const currentQ = currentQuizData.questions[currentQuestionIndex];
    const totalQ = currentQuizData.questions.length;

    // Update Progress Bar
    if (progressTextEl) progressTextEl.textContent = `السؤال ${currentQuestionIndex + 1} من ${totalQ}`;
    if (progressBarEl) {
        const progressPercent = ((currentQuestionIndex + 1) / totalQ) * 100;
        progressBarEl.style.width = `${progressPercent}%`;
    }

    // Update Question Text with BiDi formatting
    if (questionTextEl) questionTextEl.innerHTML = cleanBiDiText(currentQ.question);

    // Hide Feedback Box & Next Button
    if (feedbackContainerEl) feedbackContainerEl.classList.remove('active');
    if (btnNextQuestionEl) btnNextQuestionEl.classList.remove('active');

    // Handle Question Type: Task vs MCQ
    if (currentQ.type === 'task') {
        // Show Task Editor Container, Hide Options Grid
        if (optionsGridEl) optionsGridEl.style.display = 'none';
        if (taskEditorContainerEl) taskEditorContainerEl.style.display = 'block';
        
        if (editorLangTitleEl) editorLangTitleEl.textContent = `💻 محرر الأكواد والمهام (${manifestData.course_title})`;
        if (taskHintTextEl) {
            taskHintTextEl.style.display = 'none';
            taskHintTextEl.innerHTML = cleanBiDiText(currentQ.task_hint || 'اكتب إجابتك أو كودك بتركيز وإبداع يا بطل!');
        }
        if (taskEditorTextareaEl) {
            taskEditorTextareaEl.value = '';
            taskEditorTextareaEl.disabled = false;
        }
        if (btnSubmitTaskBtnEl) btnSubmitTaskBtnEl.style.display = 'inline-flex';
    } else {
        // Show Options Grid, Hide Task Editor Container
        if (optionsGridEl) optionsGridEl.style.display = 'grid';
        if (taskEditorContainerEl) taskEditorContainerEl.style.display = 'none';

        optionsGridEl.innerHTML = '';
        currentQ.options.forEach((optionText, index) => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.innerHTML = `<span class="option-text-span" dir="auto" style="unicode-bidi: plaintext; text-align: right; width: 100%; display: inline-block;">${cleanBiDiText(optionText)}</span> <span class="option-indicator">👈</span>`;
            btn.addEventListener('click', () => handleOptionClick(index, btn));
            optionsGridEl.appendChild(btn);
        });
    }
}

// Handle Task Submission
function handleTaskSubmission() {
    if (isQuestionAnswered || !currentQuizData) return;

    const answerText = taskEditorTextareaEl ? taskEditorTextareaEl.value.trim() : '';
    if (!answerText) {
        alert('من فضلك اكتب إجابتك أو الكود الخاص بك أولاً يا بطل!');
        return;
    }

    isQuestionAnswered = true;
    const currentQ = currentQuizData.questions[currentQuestionIndex];

    // Disable textarea and submit button
    if (taskEditorTextareaEl) taskEditorTextareaEl.disabled = true;
    if (btnSubmitTaskBtnEl) btnSubmitTaskBtnEl.style.display = 'none';

    // Store Student Answer for Engineer Evaluation
    studentAnswers.push({
        questionId: currentQ.id,
        type: 'task',
        question: currentQ.question,
        answer: answerText,
        isCorrect: null, // To be graded by engineer
        correctText: currentQ.explanation || 'سيقوم المهندس المشرف بمراجعة الكود وتقييمه قريباً.'
    });

    playHappyChime();
    triggerConfetti(3000);

    feedbackTitleEl.textContent = '🚀 تم حفظ إجابتك السحرية بنجاح!';
    feedbackTitleEl.className = 'feedback-title correct';
    if (feedbackDescEl) feedbackDescEl.innerHTML = cleanBiDiText(currentQ.explanation || 'تم تسجيل الكود الخاص بك في التقرير ليقوم المهندس بمراجعته وتقييمه.');
    if (feedbackContainerEl) feedbackContainerEl.classList.add('active');

    // Show Next Button
    if (btnNextQuestionEl) {
        const isLastQuestion = (currentQuestionIndex === currentQuizData.questions.length - 1);
        btnNextQuestionEl.innerHTML = isLastQuestion ? '<span>عرض النتيجة والتقرير 🏆</span>' : '<span>السؤال التالي 🚀</span>';
        btnNextQuestionEl.classList.add('active');
    }
}

// Handle Option Click (For MCQ)
function handleOptionClick(selectedIndex, clickedBtn) {
    if (isQuestionAnswered || !currentQuizData) return;
    isQuestionAnswered = true;
    mcqCount++;

    const currentQ = currentQuizData.questions[currentQuestionIndex];
    const isCorrect = (selectedIndex === currentQ.correct);

    const allOptionBtns = optionsGridEl.querySelectorAll('.option-btn');
    allOptionBtns.forEach((btn, idx) => {
        btn.classList.add('disabled');
        if (idx === currentQ.correct) {
            btn.classList.add('correct');
            btn.querySelector('.option-indicator').textContent = '✅';
        } else if (idx === selectedIndex && !isCorrect) {
            btn.classList.add('incorrect');
            btn.querySelector('.option-indicator').textContent = '❌';
        }
    });

    // Store Student Answer for Engineer Evaluation
    studentAnswers.push({
        questionId: currentQ.id,
        type: 'mcq',
        question: currentQ.question,
        answer: currentQ.options[selectedIndex],
        isCorrect: isCorrect,
        correctText: currentQ.options[currentQ.correct]
    });

    if (isCorrect) {
        score++;
        playHappyChime();
        triggerConfetti(3000);
        feedbackTitleEl.textContent = '🎉 إجابة صحيحة، عبقري!';
        feedbackTitleEl.className = 'feedback-title correct';
    } else {
        playGentleBeep();
        feedbackTitleEl.textContent = '💡 محاولة جيدة يا بطل!';
        feedbackTitleEl.className = 'feedback-title incorrect';
    }

    if (feedbackDescEl) feedbackDescEl.textContent = currentQ.explanation;
    if (feedbackContainerEl) feedbackContainerEl.classList.add('active');

    if (btnNextQuestionEl) {
        const isLastQuestion = (currentQuestionIndex === currentQuizData.questions.length - 1);
        btnNextQuestionEl.innerHTML = isLastQuestion ? '<span>عرض النتيجة والتقرير 🏆</span>' : '<span>السؤال التالي 🚀</span>';
        btnNextQuestionEl.classList.add('active');
    }
}

// Handle Next Question Click
function handleNextQuestion() {
    if (!currentQuizData) return;

    if (currentQuestionIndex < currentQuizData.questions.length - 1) {
        currentQuestionIndex++;
        renderCurrentQuestion();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
        showResultScreen();
    }
}

// 3. Show Result Screen & Save Submission to Storage Adapter
function showResultScreen() {
    if (!currentQuizData) return;

    // Save Submission to Storage Adapter (LocalStorage/Firebase Hybrid)
    const submissionData = {
        id: 'sub_' + Date.now(),
        timestamp: new Date().toISOString(),
        studentName: studentInfo.name || 'طالب غير مسجل',
        groupName: studentInfo.group || 'مجموعة غير مسجلة',
        teacherName: studentInfo.teacher || 'مهندس غير مسجل',
        course: manifestData ? manifestData.course_title : currentCourse,
        mcqScore: score,
        mcqTotal: mcqCount,
        status: 'pending', // 'pending' | 'graded'
        engineerNotes: '',
        engineerGrade: null,
        answers: studentAnswers
    };

    // 1. Save to Firebase Realtime Database
    if (db) {
        try {
            db.ref('submissions/' + submissionData.id).set(submissionData)
              .then(() => console.log("Submission saved to Firebase successfully!"))
              .catch(err => console.error("Firebase save error:", err));
        } catch(err) {
            console.error("Firebase ref error:", err);
        }
    }

    // 2. Save to LocalStorage as Hybrid Fallback
    let submissions = JSON.parse(localStorage.getItem('megaminds_submissions') || '[]');
    submissions.push(submissionData);
    localStorage.setItem('megaminds_submissions', JSON.stringify(submissions));

    // Hide score number, score box, engineer portal container, retry button, and print button
    if (resultScoreNumEl) resultScoreNumEl.style.display = 'none';
    const scoreBoxEl = document.querySelector('.result-score-box');
    if (scoreBoxEl) scoreBoxEl.style.display = 'none';
    if (engineerPortalContainerEl) engineerPortalContainerEl.style.display = 'none';
    if (btnPrintReportEl) btnPrintReportEl.style.display = 'none';
    if (btnRetryEl) btnRetryEl.style.display = 'none';

    // Display beautiful celebratory pampering message telling student their teacher will review
    if (resultMsgEl) {
        resultMsgEl.innerHTML = `
            <div class="success-banner" style="font-size: 2.6rem; color: var(--primary); margin-bottom: 25px;">
                🎉 تم إرسال إجاباتك ومهامك السحرية بنجاح يا بطل! 🎉
            </div>
            <div class="teacher-notice" style="font-size: 1.8rem; color: var(--tertiary-dark); background: var(--bg-gradient-2); padding: 30px; border-radius: var(--radius-md); border: 3px solid var(--tertiary); margin-bottom: 30px; line-height: 1.8;">
                سيقوم المهندس المشرف <strong>${studentInfo.teacher || 'الخاص بك'}</strong> بمراجعة وتقييم إجاباتك وإبداعاتك البرمجية وإبلاغك بالنتيجة النهائية قريباً في مجموعة <strong>${studentInfo.group || 'الكورس'}</strong>!
            </div>
            <div class="praise-text" style="font-size: 2rem; color: var(--purple); font-weight: 900;">
                أنت فخر أكاديمية ميجامايندز ومستقبلك عظيم جداً! 🚀🌟
            </div>
        `;
        triggerConfetti(8000);
        playHappyChime();
    }

    showView(viewResult);
}

// Restart Quiz Flow (Goes back to Registration/Recap)
function restartQuizFlow() {
    showView(viewRegistration);
}
