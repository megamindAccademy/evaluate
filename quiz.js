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
let isQuestionAnswered = false;
let currentCourse = 'python';

// DOM Elements
let viewRecap, viewQuestion, viewResult;
let quizCourseTitleEl, recapTitleEl, recapSubtitleEl, recapCardsGridEl;
let progressTextEl, progressBarEl, questionTextEl, optionsGridEl;
let feedbackContainerEl, feedbackTitleEl, feedbackDescEl, btnNextQuestionEl;
let resultScoreNumEl, resultMsgEl, btnRetryEl;

document.addEventListener('DOMContentLoaded', () => {
    // Initialize DOM Elements
    viewRecap = document.getElementById('viewRecap');
    viewQuestion = document.getElementById('viewQuestion');
    viewResult = document.getElementById('viewResult');

    quizCourseTitleEl = document.getElementById('quizCourseTitle');
    recapTitleEl = document.getElementById('recapTitle');
    recapSubtitleEl = document.getElementById('recapSubtitle');
    recapCardsGridEl = document.getElementById('recapCardsGrid');

    progressTextEl = document.getElementById('progressText');
    progressBarEl = document.getElementById('progressBar');
    questionTextEl = document.getElementById('questionText');
    optionsGridEl = document.getElementById('optionsGrid');

    feedbackContainerEl = document.getElementById('feedbackContainer');
    feedbackTitleEl = document.getElementById('feedbackTitle');
    feedbackDescEl = document.getElementById('feedbackDesc');
    btnNextQuestionEl = document.getElementById('btnNextQuestion');

    resultScoreNumEl = document.getElementById('resultScoreNum');
    resultMsgEl = document.getElementById('resultMsg');
    btnRetryEl = document.getElementById('btnRetry');

    const btnStartQuiz = document.getElementById('btnStartQuiz');
    if (btnStartQuiz) {
        btnStartQuiz.addEventListener('click', startRandomQuiz);
    }

    if (btnNextQuestionEl) {
        btnNextQuestionEl.addEventListener('click', handleNextQuestion);
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
            initRecapScreen();
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
    [viewRecap, viewQuestion, viewResult].forEach(v => {
        if (v) v.classList.remove('active');
    });
    if (viewEl) viewEl.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// 1. Initialize Recap Screen (Grouped by Sessions)
function initRecapScreen() {
    if (!recapData) return;

    if (recapTitleEl) recapTitleEl.textContent = recapData.recap_title;
    if (recapSubtitleEl) recapSubtitleEl.textContent = recapData.recap_subtitle;

    // Populate Recap Cards Grouped by Sessions
    if (recapCardsGridEl) {
        recapCardsGridEl.innerHTML = '';
        
        recapData.sessions.forEach(session => {
            // Create Session Section Wrapper
            const sessionGroup = document.createElement('div');
            sessionGroup.className = 'recap-session-group';
            sessionGroup.style.gridColumn = '1 / -1';
            sessionGroup.style.marginTop = '25px';
            sessionGroup.style.marginBottom = '15px';

            const sessionHeader = document.createElement('h3');
            sessionHeader.className = 'recap-session-title';
            sessionHeader.style.fontSize = '1.8rem';
            sessionHeader.style.color = 'var(--tertiary-dark)';
            sessionHeader.style.borderBottom = '3px solid var(--secondary)';
            sessionHeader.style.paddingBottom = '10px';
            sessionHeader.textContent = session.session_title;
            sessionGroup.appendChild(sessionHeader);
            
            recapCardsGridEl.appendChild(sessionGroup);

            // Create Cards for Session Points
            session.points.forEach(point => {
                const card = document.createElement('div');
                card.className = 'recap-card';
                card.innerHTML = `
                    <div class="recap-card-icon">${point.icon}</div>
                    <div class="recap-card-content">
                        <h4>${point.title}</h4>
                        <p>${point.desc}</p>
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

    // Pick a random quiz file name from manifest list
    const randomIndex = Math.floor(Math.random() * manifestData.quizzes.length);
    const randomQuizFileName = manifestData.quizzes[randomIndex];

    // Fetch the random quiz JSON
    fetch(`./database/${currentCourse}/quizzes/${randomQuizFileName}`)
        .then(response => {
            if (!response.ok) throw new Error(`Quiz file ${randomQuizFileName} not found`);
            return response.json();
        })
        .then(quiz => {
            currentQuizData = quiz;
            currentQuestionIndex = 0;
            score = 0;
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

    // Update Question Text
    if (questionTextEl) questionTextEl.textContent = currentQ.question;

    // Hide Feedback Box & Next Button
    if (feedbackContainerEl) feedbackContainerEl.classList.remove('active');
    if (btnNextQuestionEl) btnNextQuestionEl.classList.remove('active');

    // Render Options
    if (optionsGridEl) {
        optionsGridEl.innerHTML = '';
        currentQ.options.forEach((optionText, index) => {
            const btn = document.createElement('button');
            btn.className = 'option-btn';
            btn.innerHTML = `<span>${optionText}</span> <span class="option-indicator">👈</span>`;
            btn.addEventListener('click', () => handleOptionClick(index, btn));
            optionsGridEl.appendChild(btn);
        });
    }
}

// Handle Option Click
function handleOptionClick(selectedIndex, clickedBtn) {
    if (isQuestionAnswered || !currentQuizData) return;
    isQuestionAnswered = true;

    const currentQ = currentQuizData.questions[currentQuestionIndex];
    const isCorrect = (selectedIndex === currentQ.correct);

    // Disable all option buttons
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

    // Handle Correct / Incorrect Actions
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

    // Show Explanation
    if (feedbackDescEl) feedbackDescEl.textContent = currentQ.explanation;
    if (feedbackContainerEl) feedbackContainerEl.classList.add('active');

    // Show Next Button
    if (btnNextQuestionEl) {
        const isLastQuestion = (currentQuestionIndex === currentQuizData.questions.length - 1);
        btnNextQuestionEl.innerHTML = isLastQuestion ? '<span>عرض النتيجة النهائية 🏆</span>' : '<span>السؤال التالي 🚀</span>';
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

// 3. Show Result Screen
function showResultScreen() {
    if (!currentQuizData) return;
    const totalQ = currentQuizData.questions.length;

    if (resultScoreNumEl) resultScoreNumEl.textContent = `${score} / ${totalQ}`;

    // Personalized pampering message based on score
    if (resultMsgEl) {
        const percentage = (score / totalQ) * 100;
        if (percentage === 100) {
            resultMsgEl.textContent = "🏆 عبقري بايثون الأول! إجاباتك كلها صحيحة 100%، أنت فخر أكاديمية ميجامايند ومستقبلك عظيم جداً!";
            triggerConfetti(8000);
            playHappyChime();
        } else if (percentage >= 80) {
            resultMsgEl.textContent = "🌟 رائع جداً يا بطل! نتيجتك مذهلة واقتربت جداً من العلامة الكاملة، واصل إبداعك وتألقك!";
            triggerConfetti(5000);
            playHappyChime();
        } else if (percentage >= 50) {
            resultMsgEl.textContent = "👍 بطل حقيقي! لقد بذلت جهداً رائعاً اليوم. تذكر أن المبرمجين الخارقين يتعلمون من المحاولة، جرب مرة أخرى لتصل للقمة!";
            triggerConfetti(3000);
        } else {
            resultMsgEl.textContent = "💪 لا تستسلم يا بطل! البرمجة تحتاج إلى تدريب ومحاولة. راجع الملخص السريع وجرب التحدي مرة أخرى، نحن واثقون من قدراتك!";
        }
    }

    showView(viewResult);
}

// Restart Quiz Flow (Goes back to Recap)
function restartQuizFlow() {
    initRecapScreen();
}
