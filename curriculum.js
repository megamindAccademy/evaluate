// ============================================================================
// CURRICULUM.JS - Dynamic Interactive Curriculum & Games Engine
// ============================================================================

// Initialize Firebase Analytics if available
try {
    if (typeof firebase !== 'undefined' && firebase.analytics) {
        firebase.analytics();
        console.log("Firebase Analytics initialized successfully in curriculum.js!");
    }
} catch (e) {
    console.error("Firebase Analytics initialization error:", e);
}

// Web Audio API for synthesized cheerful sound effects
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playHappyChime() {
    if (audioCtx.state === 'suspended') audioCtx.resume();
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

function playSuccessFanfare() {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const now = audioCtx.currentTime;
    const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51];
    notes.forEach((freq, index) => {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'triangle';
        osc.frequency.value = freq;
        gain.gain.setValueAtTime(0, now + index * 0.15);
        gain.gain.linearRampToValueAtTime(0.4, now + index * 0.15 + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, now + index * 0.15 + 0.6);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start(now + index * 0.15);
        osc.stop(now + index * 0.15 + 0.65);
    });
}

function playBeepSound() {
    if (audioCtx.state === 'suspended') audioCtx.resume();
    const now = audioCtx.currentTime;
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(300, now);
    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.2, now + 0.02);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(now);
    osc.stop(now + 0.25);
}

// Custom Confetti Animation
function triggerConfetti() {
    const canvas = document.createElement('canvas');
    canvas.style.position = 'fixed';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    canvas.style.pointerEvents = 'none';
    canvas.style.zIndex = '99999';
    document.body.appendChild(canvas);

    const ctx = canvas.getContext('2d');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const pieces = [];
    const numberOfPieces = 200;
    const colors = ['#ff7b00', '#ffb703', '#219ebc', '#8338ec', '#06d6a0', '#ff006e', '#ffd166'];

    for (let i = 0; i < numberOfPieces; i++) {
        pieces.push({
            x: canvas.width * Math.random(),
            y: canvas.height * Math.random() - canvas.height,
            rotation: Math.random() * 360,
            rotationSpeed: (Math.random() - 0.5) * 12,
            size: Math.random() * 15 + 8,
            speedY: Math.random() * 6 + 4,
            speedX: (Math.random() - 0.5) * 5,
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

        if (activePieces > 0 && Date.now() - startTime < 6000) {
            requestAnimationFrame(animate);
        } else {
            if (canvas.parentNode) document.body.removeChild(canvas);
        }
    }
    animate();
}

// ============================================================================
// DYNAMIC STATE & JSON FETCHING
// ============================================================================
let currentCourseId = 'python';
let currentCourseData = null;
let currentStationId = 1;
let studentProgress = {
    xp: 0,
    completedStations: []
};

// Check URL param for initial course selection
function getUrlCourseParam() {
    const params = new URLSearchParams(window.location.search);
    return params.get('course') || 'python';
}

// Load progress from localStorage for current course
function loadProgress() {
    const storageKey = `megaminds_progress_${currentCourseId}`;
    const saved = localStorage.getItem(storageKey);
    if (saved) {
        try {
            studentProgress = JSON.parse(saved);
        } catch(e) {
            studentProgress = { xp: 0, completedStations: [] };
        }
    } else {
        studentProgress = { xp: 0, completedStations: [] };
    }
    updateUIProgress();
}

// Save progress to localStorage
function saveProgress() {
    const storageKey = `megaminds_progress_${currentCourseId}`;
    localStorage.setItem(storageKey, JSON.stringify(studentProgress));
    updateUIProgress();
}

// Fetch Course Games JSON dynamically
function fetchCourseGames(courseId) {
    currentCourseId = courseId;
    loadProgress();

    // Update active tab button styling
    document.querySelectorAll('.course-tab-btn').forEach(btn => {
        if (btn.getAttribute('data-course') === courseId) {
            btn.classList.add('active');
            btn.style.background = '#ffb703';
            btn.style.color = '#023047';
        } else {
            btn.classList.remove('active');
            btn.style.background = '#023047';
            btn.style.color = '#ffffff';
        }
    });

    // Hide studio section when switching courses
    const studioSection = document.getElementById('studioSection');
    if (studioSection) studioSection.classList.remove('active');

    // Fetch JSON file
    fetch(`./database/${courseId}/games.json?v=` + Date.now())
        .then(response => {
            if (!response.ok) throw new Error("Games file not found");
            return response.json();
        })
        .then(data => {
            currentCourseData = data;
            renderCourseContent();
        })
        .catch(err => {
            console.error(`Error loading games for ${courseId}:`, err);
            alert("عذراً يا بطل! جاري تجهيز ألعاب وتحديات هذا المسار قريباً جداً.");
        });
}

// Render dynamic course data into HTML
function renderCourseContent() {
    if (!currentCourseData) return;

    // 1. Update Hero Banner
    const heroTitle = document.querySelector('.curriculum-hero .curriculum-title');
    const heroDesc = document.querySelector('.curriculum-hero .curriculum-desc');
    const heroMascot = document.querySelector('.curriculum-hero .curriculum-hero-mascot');
    
    if (heroTitle) heroTitle.textContent = currentCourseData.course_title;
    if (heroDesc) heroDesc.textContent = currentCourseData.course_subtitle;
    if (heroMascot && currentCourseData.mascot_img) heroMascot.src = currentCourseData.mascot_img;

    // 2. Update Journey Header
    const journeyTitle = document.querySelector('.journey-section .journey-title');
    if (journeyTitle) journeyTitle.textContent = `🗺️ خريطة محطات ${currentCourseData.course_title}`;

    // 3. Render Badges Showcase
    const badgesShowcase = document.getElementById('badgesShowcase');
    if (badgesShowcase) {
        badgesShowcase.innerHTML = '';
        currentCourseData.stations.forEach(station => {
            const badgeEl = document.createElement('div');
            badgeEl.className = `badge-item ${studentProgress.completedStations.includes(station.id) ? 'earned' : ''}`;
            badgeEl.id = `badge_${station.id}`;
            badgeEl.setAttribute('title', station.badge_title);
            badgeEl.textContent = station.badge_icon;
            badgesShowcase.appendChild(badgeEl);
        });
    }

    // 4. Render Journey Grid Cards
    const journeyGrid = document.getElementById('journeyGrid');
    if (journeyGrid) {
        journeyGrid.innerHTML = '';
        currentCourseData.stations.forEach(station => {
            const isCompleted = studentProgress.completedStations.includes(station.id);
            const isUnlocked = isCompleted || (station.id === 1) || studentProgress.completedStations.includes(station.id - 1);

            let cardClass = isCompleted ? 'completed' : (isUnlocked ? 'active' : 'locked');
            let badgeText = isCompleted ? 'مكتمل ✅' : (isUnlocked ? 'متاح الآن 🌟' : 'مغلق 🔒');
            let btnText = isCompleted ? 'مراجعة التحدي 🔄' : (isUnlocked ? 'ابدأ المغامرة 🚀' : 'مغلق حالياً 🔒');

            const article = document.createElement('article');
            article.className = `station-card ${cardClass}`;
            article.id = `station_${station.id}`;
            article.setAttribute('data-station', station.id);

            article.innerHTML = `
                <span class="station-badge">${badgeText}</span>
                <div class="station-number-icon">${station.badge_icon}</div>
                <h3 class="station-title">${station.title}</h3>
                <p class="station-desc">${station.desc}</p>
                <button class="station-btn"><span>${btnText}</span></button>
            `;

            journeyGrid.appendChild(article);
        });
    }

    updateUIProgress();
}

// Update UI elements based on progress state
function updateUIProgress() {
    if (!currentCourseData) return;

    const xpCountText = document.getElementById('xpCountText');
    const xpProgressBar = document.getElementById('xpProgressBar');
    const btnClaimCert = document.getElementById('btnClaimCert');

    const totalXp = currentCourseData.xp_total || 600;

    // Update XP text & bar
    if (xpCountText) xpCountText.textContent = `${studentProgress.xp} / ${totalXp} XP`;
    if (xpProgressBar) {
        const percentage = Math.min(100, (studentProgress.xp / totalXp) * 100);
        xpProgressBar.style.width = `${percentage}%`;
    }

    // Update Badges Showcase & Station Cards dynamically
    currentCourseData.stations.forEach(station => {
        const badgeEl = document.getElementById(`badge_${station.id}`);
        const stationEl = document.getElementById(`station_${station.id}`);
        
        const isCompleted = studentProgress.completedStations.includes(station.id);
        const isUnlocked = isCompleted || (station.id === 1) || studentProgress.completedStations.includes(station.id - 1);

        if (badgeEl) {
            if (isCompleted) badgeEl.classList.add('earned');
            else badgeEl.classList.remove('earned');
        }

        if (stationEl) {
            stationEl.className = `station-card ${isCompleted ? 'completed' : (isUnlocked ? 'active' : 'locked')}`;
            const badgeSpan = stationEl.querySelector('.station-badge');
            const btnSpan = stationEl.querySelector('.station-btn span');

            if (isCompleted) {
                if (badgeSpan) badgeSpan.textContent = "مكتمل ✅";
                if (btnSpan) btnSpan.textContent = "مراجعة التحدي 🔄";
            } else if (isUnlocked) {
                if (badgeSpan) badgeSpan.textContent = "متاح الآن 🌟";
                if (btnSpan) btnSpan.textContent = "ابدأ المغامرة 🚀";
            } else {
                if (badgeSpan) badgeSpan.textContent = "مغلق 🔒";
                if (btnSpan) btnSpan.textContent = "مغلق حالياً 🔒";
            }
        }
    });

    // Check if all stations completed to show Claim Certificate button
    if (studentProgress.completedStations.length >= currentCourseData.stations.length) {
        if (btnClaimCert) btnClaimCert.classList.add('active');
    } else {
        if (btnClaimCert) btnClaimCert.classList.remove('active');
    }
}

// ============================================================================
// CUSTOM SIMULATOR & JSON RULES VALIDATOR
// ============================================================================
function simulatePythonExecution(code, stationId) {
    if (!currentCourseData) return;

    const outputArea = document.getElementById('outputContentArea');
    const turtleCanvas = document.getElementById('turtleCanvas');
    let canvasUsed = false;

    if (!outputArea) return;
    outputArea.innerHTML = ''; // Clear previous output

    function logOutput(text, type = 'success') {
        const div = document.createElement('div');
        div.className = `output-log ${type}`;
        div.textContent = text;
        outputArea.appendChild(div);
    }

    logOutput(`>>> جاري تشغيل كود ${currentCourseData.course_title} السحري...`, "info");

    // Reset Canvas
    if (turtleCanvas) {
        const ctx = turtleCanvas.getContext('2d');
        ctx.clearRect(0, 0, turtleCanvas.width, turtleCanvas.height);
        turtleCanvas.classList.remove('active');
    }

    let simulatedStdout = [];
    let pyVariables = {};

    const lines = code.split('\n');
    let insideForLoop = false;
    let forLoopCount = 0;
    let forLoopBody = [];
    let forLoopVar = 'i';

    try {
        for (let i = 0; i < lines.length; i++) {
            let line = lines[i].trim();
            if (!line || line.startsWith('#')) continue;

            if (insideForLoop) {
                if (lines[i].startsWith('    ') || lines[i].startsWith('\t')) {
                    forLoopBody.push(line);
                    if (i === lines.length - 1) {
                        executeForLoop(forLoopVar, forLoopCount, forLoopBody, pyVariables, simulatedStdout, logOutput);
                    }
                    continue;
                } else {
                    executeForLoop(forLoopVar, forLoopCount, forLoopBody, pyVariables, simulatedStdout, logOutput);
                    insideForLoop = false;
                    forLoopBody = [];
                }
            }

            // 1. Variable Assignment
            if (line.includes('=') && !line.includes('==') && !line.startsWith('if') && !line.startsWith('for')) {
                const parts = line.split('=');
                const varName = parts[0].trim();
                let varVal = parts[1].trim();

                if (varVal.includes('*')) {
                    const mathParts = varVal.split('*');
                    const n1 = isNaN(mathParts[0].trim()) ? pyVariables[mathParts[0].trim()] : parseFloat(mathParts[0].trim());
                    const n2 = isNaN(mathParts[1].trim()) ? pyVariables[mathParts[1].trim()] : parseFloat(mathParts[1].trim());
                    varVal = n1 * n2;
                } else if (varVal.includes('+')) {
                    const mathParts = varVal.split('+');
                    const n1 = isNaN(mathParts[0].trim()) ? pyVariables[mathParts[0].trim()] : parseFloat(mathParts[0].trim());
                    const n2 = isNaN(mathParts[1].trim()) ? pyVariables[mathParts[1].trim()] : parseFloat(mathParts[1].trim());
                    varVal = n1 + n2;
                } else if (varVal.startsWith('"') && varVal.endsWith('"')) {
                    varVal = varVal.slice(1, -1);
                } else if (varVal.startsWith("'") && varVal.endsWith("'")) {
                    varVal = varVal.slice(1, -1);
                } else if (!isNaN(varVal)) {
                    varVal = parseFloat(varVal);
                }

                pyVariables[varName] = varVal;
                logOutput(`# تم حفظ المتغير: ${varName} = ${varVal}`, "info");
                continue;
            }

            // 2. Print Statement
            if (line.startsWith('print(') && line.endsWith(')')) {
                let content = line.slice(6, -1).trim();

                if (content.includes('*')) {
                    const mathParts = content.split('*');
                    const n1 = isNaN(mathParts[0].trim()) ? pyVariables[mathParts[0].trim()] : parseFloat(mathParts[0].trim());
                    const n2 = isNaN(mathParts[1].trim()) ? pyVariables[mathParts[1].trim()] : parseFloat(mathParts[1].trim());
                    content = n1 * n2;
                } else if (content.startsWith('"') && content.endsWith('"')) {
                    content = content.slice(1, -1);
                } else if (content.startsWith("'") && content.endsWith("'")) {
                    content = content.slice(1, -1);
                } else if (pyVariables[content] !== undefined) {
                    content = pyVariables[content];
                }

                simulatedStdout.push(content);
                logOutput(content, "success");
                continue;
            }

            // 3. If Statement
            if (line.startsWith('if ') && line.endsWith(':')) {
                let condition = line.slice(3, -1).trim();
                let isTrue = false;

                if (condition.includes('==')) {
                    const cParts = condition.split('==');
                    const left = pyVariables[cParts[0].trim()] !== undefined ? pyVariables[cParts[0].trim()] : cParts[0].trim();
                    let right = cParts[1].trim();
                    if (!isNaN(right)) right = parseFloat(right);
                    isTrue = (left === right);
                } else if (condition.includes('>')) {
                    const cParts = condition.split('>');
                    const left = pyVariables[cParts[0].trim()] !== undefined ? pyVariables[cParts[0].trim()] : parseFloat(cParts[0].trim());
                    const right = parseFloat(cParts[1].trim());
                    isTrue = (left > right);
                }

                if (i + 1 < lines.length && (lines[i+1].startsWith('    ') || lines[i+1].startsWith('\t'))) {
                    let nextLine = lines[i+1].trim();
                    if (isTrue) {
                        if (nextLine.startsWith('print(')) {
                            let content = nextLine.slice(6, -1).trim().replace(/["']/g, '');
                            simulatedStdout.push(content);
                            logOutput(content, "success");
                        }
                    }
                    i++;
                    if (i + 1 < lines.length && lines[i+1].trim() === 'else:') {
                        i++;
                        if (i + 1 < lines.length && (lines[i+1].startsWith('    ') || lines[i+1].startsWith('\t'))) {
                            let elseLine = lines[i+1].trim();
                            if (!isTrue) {
                                if (elseLine.startsWith('print(')) {
                                    let content = elseLine.slice(6, -1).trim().replace(/["']/g, '');
                                    simulatedStdout.push(content);
                                    logOutput(content, "success");
                                }
                            }
                            i++;
                        }
                    }
                }
                continue;
            }

            // 4. For Loop Statement
            if (line.startsWith('for ') && line.includes(' in range(') && line.endsWith('):')) {
                const match = line.match(/for\s+(\w+)\s+in\s+range\((\d+)\):/);
                if (match) {
                    forLoopVar = match[1];
                    forLoopCount = parseInt(match[2]);
                    insideForLoop = true;
                    forLoopBody = [];
                }
                continue;
            }

            // 5. Turtle Graphics Simulation
            if (line === 'import turtle') {
                canvasUsed = true;
                if (turtleCanvas) turtleCanvas.classList.add('active');
                logOutput("# تم استدعاء السلحفاة بنجاح وتجهيز شاشة الرسم!", "info");
                continue;
            }

            if (line.startsWith('turtle.')) {
                canvasUsed = true;
                if (turtleCanvas) turtleCanvas.classList.add('active');
                const ctx = turtleCanvas.getContext('2d');
                
                if (line.startsWith('turtle.color(')) {
                    let col = line.slice(13, -1).trim().replace(/["']/g, '');
                    ctx.strokeStyle = col;
                    ctx.fillStyle = col;
                    logOutput(`# تغيير لون السلحفاة إلى: ${col}`, "info");
                } else if (line.startsWith('turtle.circle(')) {
                    let r = parseFloat(line.slice(14, -1).trim());
                    ctx.beginPath();
                    ctx.arc(turtleCanvas.width / 2, turtleCanvas.height / 2, r, 0, Math.PI * 2);
                    ctx.stroke();
                    logOutput(`# السلحفاة رسمت دائرة بنصف قطر ${r}`, "success");
                    simulatedStdout.push("رسم دائرة");
                } else if (line.startsWith('turtle.forward(')) {
                    let dist = parseFloat(line.slice(15, -1).trim());
                    ctx.beginPath();
                    ctx.moveTo(turtleCanvas.width / 2 - dist/2, turtleCanvas.height / 2);
                    ctx.lineTo(turtleCanvas.width / 2 + dist/2, turtleCanvas.height / 2);
                    ctx.stroke();
                    logOutput(`# السلحفاة تحركت للأمام مسافة ${dist}`, "success");
                }
                continue;
            }
        }
    } catch (err) {
        logOutput(`عذراً يا بطل، هناك خطأ في الكود: ${err.message}`, "error");
    }

    function executeForLoop(varName, count, bodyLines, vars, stdoutEl, logEl) {
        logEl(`# جاري تكرار الأوامر ${count} مرات...`, "info");
        for (let c = 0; c < count; c++) {
            vars[varName] = c;
            bodyLines.forEach(bLine => {
                if (bLine.startsWith('print(')) {
                    let content = bLine.slice(6, -1).trim().replace(/["']/g, '');
                    if (vars[content] !== undefined) content = vars[content];
                    stdoutEl.push(content);
                    logEl(`${content}`, "success");
                }
            });
        }
    }

    // Evaluate JSON Validation Rules
    const station = currentCourseData.stations.find(s => s.id === stationId);
    if (!station) return;

    const fullOutputText = simulatedStdout.join(' ') + ' ' + outputArea.textContent;
    const rules = station.validation_rules || {};
    let isCorrect = true;

    if (rules.required_output_text && !fullOutputText.includes(rules.required_output_text)) {
        isCorrect = false;
    }
    if (rules.required_keywords) {
        rules.required_keywords.forEach(kw => {
            if (!fullOutputText.includes(kw)) isCorrect = false;
        });
    }
    if (rules.required_canvas && !canvasUsed) {
        isCorrect = false;
    }

    if (isCorrect) {
        logOutput("\n✨ إجابة عبقرية! لقد نجحت في تحقيق التحدي المطلوب! ✨", "success");
        playSuccessFanfare();
        triggerConfetti();

        if (!studentProgress.completedStations.includes(stationId)) {
            studentProgress.completedStations.push(stationId);
            studentProgress.xp += 100;
            saveProgress();
        }

        setTimeout(() => {
            const modal = document.getElementById('celebrationModal');
            const cTitle = document.getElementById('celebrationTitle');
            const cText = document.getElementById('celebrationText');
            if (modal) {
                if (cTitle) cTitle.textContent = `إجابة عبقرية في ${station.title}!`;
                if (cText) cText.textContent = `لقد نجحت بجدارة واكتسبت 100 نقطة طاقة ووساماً جديداً ينير ملفك!`;
                modal.classList.add('active');
            }
        }, 1200);

    } else {
        logOutput("\n⚠️ النتيجة لم تطابق التحدي المطلوب بعد. جرب استخدام التلميح السحري أو الأكواد المساعدة يا بطل!", "error");
        playBeepSound();
    }
}

// ============================================================================
// DOM SETUP & EVENT LISTENERS
// ============================================================================
document.addEventListener('DOMContentLoaded', () => {
    // Initialize course from URL or default
    const initialCourse = getUrlCourseParam();
    fetchCourseGames(initialCourse);

    const journeyGrid = document.getElementById('journeyGrid');
    const studioSection = document.getElementById('studioSection');
    const journeySection = document.getElementById('journeySection');
    const btnExitStudio = document.getElementById('btnExitStudio');
    const btnRunStudioCode = document.getElementById('btnRunStudioCode');
    const btnClearOutput = document.getElementById('btnClearOutput');
    const btnExplainSimple = document.getElementById('btnExplainSimple');
    const btnMagicHint = document.getElementById('btnMagicHint');
    const hintDisplayBox = document.getElementById('hintDisplayBox');
    const hintTitleText = document.getElementById('hintTitleText');
    const hintContentText = document.getElementById('hintContentText');
    const celebrationModal = document.getElementById('celebrationModal');
    const btnCelebrationNext = document.getElementById('btnCelebrationNext');
    const btnClaimCert = document.getElementById('btnClaimCert');
    const certModal = document.getElementById('certModal');
    const btnModalCloseCert = document.getElementById('btnModalCloseCert');
    const btnModalPrintCert = document.getElementById('btnModalPrintCert');

    // Tab Bar Clicks
    document.querySelectorAll('.course-tab-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            const selectedCourse = e.target.getAttribute('data-course');
            fetchCourseGames(selectedCourse);
            playHappyChime();
        });
    });

    // 1. Station Card Click -> Open Studio Workspace
    if (journeyGrid) {
        journeyGrid.addEventListener('click', (e) => {
            const card = e.target.closest('.station-card');
            if (!card) return;

            if (card.classList.contains('locked')) {
                playBeepSound();
                alert("عذراً يا بطل! هذه المحطة مغلقة. عليك إنجاز المحطة السابقة أولاً لفتحها!");
                return;
            }

            const stId = parseInt(card.getAttribute('data-station'));
            openStudioForStation(stId);
        });
    }

    function openStudioForStation(stId) {
        if (!currentCourseData) return;
        currentStationId = stId;
        const station = currentCourseData.stations.find(s => s.id === stId);
        if (!station) return;

        // Populate Studio Titles & Texts
        document.getElementById('studioTitleText').textContent = station.title;
        document.getElementById('coachLessonText').innerHTML = station.story;
        document.getElementById('challengeDescText').innerHTML = station.challenge;
        document.getElementById('curriculumEditorTextarea').value = station.starter_code;

        // Populate Helper Pills
        const pillsContainer = document.getElementById('editorPillsContainer');
        if (pillsContainer) {
            pillsContainer.innerHTML = '<div class="editor-pills-label">✨ اضغط على أي كود مساعد لإضافته فوراً للمحرر:</div>';
            station.pills.forEach(pill => {
                const pEl = document.createElement('div');
                pEl.className = 'snippet-pill';
                pEl.textContent = pill.label;
                pEl.addEventListener('click', () => {
                    const textarea = document.getElementById('curriculumEditorTextarea');
                    textarea.value += (textarea.value.endsWith('\n') ? '' : '\n') + pill.code + '\n';
                    playHappyChime();
                });
                pillsContainer.appendChild(pEl);
            });
        }

        if (hintDisplayBox) hintDisplayBox.classList.remove('active');

        const outputArea = document.getElementById('outputContentArea');
        if (outputArea) outputArea.innerHTML = `<div class="output-log info"># شاشة المخرجات جاهزة. اضغط على "تشغيل الكود السحري" لرؤية النتيجة!</div>`;

        const turtleCanvas = document.getElementById('turtleCanvas');
        if (turtleCanvas) turtleCanvas.classList.remove('active');

        if (studioSection) {
            studioSection.classList.add('active');
            studioSection.scrollIntoView({ behavior: 'smooth' });
        }
        playHappyChime();
    }

    // 2. Exit Studio Button
    if (btnExitStudio) {
        btnExitStudio.addEventListener('click', () => {
            if (studioSection) studioSection.classList.remove('active');
            if (journeySection) journeySection.scrollIntoView({ behavior: 'smooth' });
            playBeepSound();
        });
    }

    // 3. Run Code Button
    if (btnRunStudioCode) {
        btnRunStudioCode.addEventListener('click', () => {
            const textarea = document.getElementById('curriculumEditorTextarea');
            simulatePythonExecution(textarea.value, currentStationId);
        });
    }

    // 4. Clear Output Button
    if (btnClearOutput) {
        btnClearOutput.addEventListener('click', () => {
            const outputArea = document.getElementById('outputContentArea');
            if (outputArea) outputArea.innerHTML = '<div class="output-log info"># تم تنظيف الشاشة بنجاح.</div>';
            const turtleCanvas = document.getElementById('turtleCanvas');
            if (turtleCanvas) turtleCanvas.classList.remove('active');
            playBeepSound();
        });
    }

    // 5. Explain Simple Button
    if (btnExplainSimple) {
        btnExplainSimple.addEventListener('click', () => {
            if (!currentCourseData) return;
            const station = currentCourseData.stations.find(s => s.id === currentStationId);
            if (hintDisplayBox && station) {
                hintTitleText.textContent = "💡 التبسيط العامي (بسطها لي):";
                hintContentText.innerHTML = station.simple;
                hintDisplayBox.classList.add('active');
                playHappyChime();
            }
        });
    }

    // 6. Magic Hint Button
    if (btnMagicHint) {
        btnMagicHint.addEventListener('click', () => {
            if (!currentCourseData) return;
            const station = currentCourseData.stations.find(s => s.id === currentStationId);
            if (hintDisplayBox && station) {
                hintTitleText.textContent = "✨ تلميح سحري للمساعدة:";
                hintContentText.innerHTML = station.hint;
                hintDisplayBox.classList.add('active');
                playHappyChime();
            }
        });
    }

    // 7. Celebration Next Button
    if (btnCelebrationNext) {
        btnCelebrationNext.addEventListener('click', () => {
            if (celebrationModal) celebrationModal.classList.remove('active');
            if (!currentCourseData) return;
            if (currentStationId < currentCourseData.stations.length) {
                openStudioForStation(currentStationId + 1);
            } else {
                if (studioSection) studioSection.classList.remove('active');
                if (journeySection) journeySection.scrollIntoView({ behavior: 'smooth' });
                if (btnClaimCert) btnClaimCert.classList.add('active');
            }
        });
    }

    // 8. Certificate Modal Buttons
    if (btnClaimCert) {
        btnClaimCert.addEventListener('click', () => {
            const studentNameDisplay = document.getElementById('certStudentNameDisplay');
            const certDateDisplay = document.getElementById('certDateDisplay');
            const certCourseTitle = document.querySelector('.cert-course-title');
            
            const regData = localStorage.getItem('megaminds_student_reg');
            if (regData) {
                try {
                    const parsed = JSON.parse(regData);
                    if (parsed.studentName && studentNameDisplay) {
                        studentNameDisplay.textContent = parsed.studentName;
                    }
                } catch(e){}
            }

            if (certCourseTitle && currentCourseData) {
                certCourseTitle.textContent = currentCourseData.course_title;
            }

            if (certDateDisplay) {
                const options = { year: 'numeric', month: 'long', day: 'numeric' };
                certDateDisplay.textContent = new Date().toLocaleDateString('ar-EG', options);
            }

            if (certModal) certModal.classList.add('active');
            playSuccessFanfare();
            triggerConfetti();
        });
    }

    if (btnModalCloseCert) {
        btnModalCloseCert.addEventListener('click', () => {
            if (certModal) certModal.classList.remove('active');
        });
    }

    if (btnModalPrintCert) {
        btnModalPrintCert.addEventListener('click', () => {
            document.body.classList.add('print-mode-certificate');
            window.print();
            setTimeout(() => {
                document.body.classList.remove('print-mode-certificate');
            }, 1000);
        });
    }
});
