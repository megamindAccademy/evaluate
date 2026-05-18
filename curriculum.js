// ============================================================================
// CURRICULUM.JS - Dynamic Interactive Curriculum & Games Engine
// ============================================================================

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
            console.log("Firebase Analytics initialized successfully in curriculum.js!");
        }
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
let currentCourseId = 'senior_python';
let currentCourseData = null;
let currentStationId = 1;
let studentProgress = {
    xp: 0,
    completedStations: []
};

// Check URL param for initial course selection
function getUrlCourseParam() {
    const params = new URLSearchParams(window.location.search);
    return params.get('course') || 'senior_python';
}

// Check URL param for initial station selection
function getUrlStationParam() {
    const params = new URLSearchParams(window.location.search);
    const stParam = params.get('station');
    return stParam ? parseInt(stParam) : null;
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
    // Safety check: Redirect deprecated or cached 'python' requests to 'senior_python'
    if (courseId === 'python') {
        courseId = 'senior_python';
    }
    
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
            
            // Check if there is an initial station to autoload
            const initStation = getUrlStationParam();
            if (initStation && initStation > 0 && initStation <= currentCourseData.stations.length) {
                setTimeout(() => {
                    openStudioForStation(initStation);
                }, 300);
            }
        })
        .catch(err => {
            console.error(`Error loading games for ${courseId}:`, err);
            currentCourseData = {
                course_title: "قريباً جداً! ⏳",
                course_subtitle: "جاري تجهيز ألعاب وتحديات هذا المسار السحرية في مختبراتنا...",
                mascot_img: "./assets/megaminds_mascot.png",
                stations: []
            };
            renderCourseContent();
            
            const journeyGrid = document.getElementById('journeyGrid');
            if (journeyGrid) {
                journeyGrid.innerHTML = `
                    <div style="grid-column: 1 / -1; text-align: center; padding: 50px; background: #023047; border-radius: 20px; border: 2px dashed #ffb703; margin-top: 20px;">
                        <div style="font-size: 4rem; margin-bottom: 20px;">🚧🛠️🚀</div>
                        <h2 style="color: #ffb703; font-size: 2rem; margin-bottom: 15px;">الألعاب تحت الإنشاء!</h2>
                        <p style="color: #ffffff; font-size: 1.2rem; line-height: 1.6;">
                            عذراً يا بطل، محطات وألعاب هذا المسار يتم تجهيزها حالياً بكل حب.<br>
                            عد قريباً لتكتشف المغامرات الجديدة!
                        </p>
                    </div>
                `;
            }
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

    // Copy direct session link to clipboard
    const btnCopySessionLink = document.getElementById('btnCopySessionLink');
    if (btnCopySessionLink) {
        btnCopySessionLink.addEventListener('click', () => {
            const sessionUrl = `${window.location.origin}${window.location.pathname}?course=${currentCourseId}&station=${currentStationId}`;
            
            navigator.clipboard.writeText(sessionUrl).then(() => {
                playHappyChime();
                const originalText = btnCopySessionLink.innerHTML;
                btnCopySessionLink.innerHTML = '<span>✅ تم نسخ الرابط السحري!</span>';
                btnCopySessionLink.style.background = 'linear-gradient(135deg, #06d6a0, #4cc9f0)';
                btnCopySessionLink.style.color = '#ffffff';
                btnCopySessionLink.style.border = '3px solid #ffffff';
                
                setTimeout(() => {
                    btnCopySessionLink.innerHTML = originalText;
                    btnCopySessionLink.style.background = 'linear-gradient(135deg, #fb8500, #ffb703)';
                    btnCopySessionLink.style.color = '#023047';
                    btnCopySessionLink.style.border = '3px solid #023047';
                }, 2000);
            }).catch(err => {
                console.error("Failed to copy direct link:", err);
                alert("رابط الحصة المباشر هو:\n" + sessionUrl);
            });
        });
    }

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

    function applyAutoDirection(containerId) {
        const container = document.getElementById(containerId);
        if (!container) return;
        const elements = container.querySelectorAll('ol, ul, li, p, h3, h4, div');
        elements.forEach(el => {
            el.setAttribute('dir', 'auto');
        });
        container.setAttribute('dir', 'auto');
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

        applyAutoDirection('coachLessonText');
        applyAutoDirection('challengeDescText');

        // Reset and set active tab to Story & Challenge
        document.querySelectorAll('.studio-tab-btn').forEach(b => {
            if (b.getAttribute('data-tab') === 'tab-story') b.classList.add('active');
            else b.classList.remove('active');
        });
        document.querySelectorAll('.studio-tab-content').forEach(c => {
            if (c.id === 'tab-story') c.classList.add('active');
            else c.classList.remove('active');
        });

        // Load dynamic interactive game
        loadInteractiveGame(stId);

        // Populate Homework Details
        const homework = station.homework;
        if (homework) {
            document.getElementById('studioHomeworkTitle').textContent = homework.title;
            document.getElementById('studioHomeworkDesc').innerHTML = homework.desc;
            applyAutoDirection('studioHomeworkDesc');
            
            const codeBox = document.getElementById('studioHomeworkCodeBox');
            if (codeBox) {
                const hwCode = homework.code || homework.starter_code || '';
                codeBox.innerHTML = `
                    <div style="position:relative; margin-top:10px;">
                        <pre style="background:#023047; color:#06d6a0; padding:15px; border-radius:10px; font-family:monospace; direction:ltr; text-align:left; overflow-x:auto; font-size:1.1rem; line-height:1.5;"><code>${hwCode.replace(/</g, "&lt;").replace(/>/g, "&gt;")}</code></pre>
                        <button class="btn-copy-hw-code" style="position:absolute; top:10px; left:10px; background:#ffb703; color:#023047; border:none; padding:6px 12px; border-radius:6px; font-size:0.95rem; font-weight:800; cursor:pointer; transition:all 0.2s;">
                            📋 نسخ كود البداية للمحرر
                        </button>
                    </div>
                `;
                
                // Copy homework code to main editor textarea
                codeBox.querySelector('.btn-copy-hw-code').addEventListener('click', () => {
                    const textarea = document.getElementById('curriculumEditorTextarea');
                    if (textarea) {
                        textarea.value = hwCode;
                        playHappyChime();
                        alert("🎉 تم نسخ كود البداية إلى محرر الأكواد السحري بنجاح! اذهب لعلامة '📘 الشرح والتحدي' للبدء في حله.");
                    }
                });
            }
        }

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
                applyAutoDirection('hintContentText');
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
                applyAutoDirection('hintContentText');
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

    // Initialize Studio Tab Switchers
    setupStudioTabs();
});

// Setup Studio Tab Listeners
function setupStudioTabs() {
    const tabButtons = document.querySelectorAll('.studio-tab-btn');
    const tabContents = document.querySelectorAll('.studio-tab-content');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const targetTab = btn.getAttribute('data-tab');
            
            // Toggle active buttons
            tabButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Toggle active content divs
            tabContents.forEach(c => {
                if (c.id === targetTab) {
                    c.classList.add('active');
                } else {
                    c.classList.remove('active');
                }
            });

            playHappyChime();
        });
    });
}

// Dynamic Gamified Station Activities (12 Interactive Games!)
function loadInteractiveGame(stationId) {
    const gamePlayArea = document.getElementById('studioGamePlayArea');
    const gameXpProgress = document.getElementById('studioGameXpProgress');
    const gameXpText = document.getElementById('studioGameXpText');

    if (!gamePlayArea) return;

    // Reset game XP bar
    if (gameXpProgress) gameXpProgress.style.width = '0%';
    if (gameXpText) gameXpText.textContent = '0 / 100 XP';

    // Clear previous game play area
    gamePlayArea.innerHTML = '';

    // Create container
    const container = document.createElement('div');
    container.style.width = '100%';
    container.style.display = 'flex';
    container.style.flexDirection = 'column';
    container.style.gap = '15px';
    container.style.alignItems = 'center';
    gamePlayArea.appendChild(container);

    const checkComplete = (points) => {
        if (gameXpProgress) gameXpProgress.style.width = `${points}%`;
        if (gameXpText) gameXpText.textContent = `${points} / 100 XP`;
        if (points >= 100) {
            if (gameXpText) gameXpText.textContent = '100 / 100 XP (مكتمل! 🎉)';
            playSuccessFanfare();
            triggerConfetti();
        } else {
            playHappyChime();
        }
    };

    switch (stationId) {
        case 1: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 لعبة ترتيب صناديق الذاكرة: انقر على الأسماء البرمجية لتصنيفها في الصندوق الصحيح!
                </p>
                <div style="display:flex; gap:20px; width:100%; justify-content:space-around; margin-top:10px;">
                    <div id="valid-box" style="flex:1; border:3px solid #06d6a0; background:rgba(6,214,160,0.05); border-radius:12px; padding:15px; min-height:100px; text-align:center;">
                        <h4 style="color:#06d6a0; margin-bottom:10px;">📦 أسماء صحيحة (Valid)</h4>
                        <div class="box-items" style="display:flex; flex-direction:column; gap:6px;"></div>
                    </div>
                    <div id="invalid-box" style="flex:1; border:3px solid #ff006e; background:rgba(255,0,110,0.05); border-radius:12px; padding:15px; min-height:100px; text-align:center;">
                        <h4 style="color:#ff006e; margin-bottom:10px;">❌ أسماء خاطئة (Invalid)</h4>
                        <div class="box-items" style="display:flex; flex-direction:column; gap:6px;"></div>
                    </div>
                </div>
                <div id="items-pool" style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center; margin-top:15px;"></div>
            `;

            const items = [
                { name: 'name1', valid: true },
                { name: '1name', valid: false },
                { name: 'print', valid: false },
                { name: 'first_name', valid: true },
                { name: 'my-name', valid: false },
                { name: 'Age', valid: true }
            ];

            let score = 0;
            const validBox = container.querySelector('#valid-box .box-items');
            const invalidBox = container.querySelector('#invalid-box .box-items');
            const itemsPool = container.querySelector('#items-pool');

            items.forEach(item => {
                const btn = document.createElement('button');
                btn.className = 'btn-game-option';
                btn.textContent = item.name;
                btn.addEventListener('click', () => {
                    if (item.valid) {
                        validBox.appendChild(btn);
                        btn.disabled = true;
                        btn.style.background = '#e6fffa';
                        btn.style.borderColor = '#06d6a0';
                    } else {
                        invalidBox.appendChild(btn);
                        btn.disabled = true;
                        btn.style.background = '#fff0f6';
                        btn.style.borderColor = '#ff006e';
                    }
                    score += 17;
                    if (score > 100) score = 100;
                    checkComplete(score);
                });
                itemsPool.appendChild(btn);
            });
            break;
        }
        case 2: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;" id="type-quest">
                    🎯 كاشف نوع العنصر: ما هو نوع العنصر التالي؟
                </p>
                <div id="type-element-display" style="background:#023047; color:#ffd166; padding:15px; border-radius:12px; font-family:monospace; font-size:1.4rem; font-weight:bold; width:200px; text-align:center; margin:10px 0;">[5, 9, 6]</div>
                <div style="display:flex; gap:10px; flex-wrap:wrap; justify-content:center;">
                    <button class="btn-game-option" data-type="list">List</button>
                    <button class="btn-game-option" data-type="str">String</button>
                    <button class="btn-game-option" data-type="int">Integer</button>
                    <button class="btn-game-option" data-type="bool">Boolean</button>
                </div>
            `;

            const quests = [
                { val: '[5, 9, 6]', ans: 'list' },
                { val: '"ميجامايندز"', ans: 'str' },
                { val: '42', ans: 'int' },
                { val: 'True', ans: 'bool' },
                { val: '3.14', ans: 'int' }
            ];

            let qIdx = 0;
            let score = 0;

            const buttons = container.querySelectorAll('.btn-game-option');
            buttons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const chosen = btn.getAttribute('data-type');
                    if (chosen === quests[qIdx].ans) {
                        score += 25;
                        if (score > 100) score = 100;
                        checkComplete(score);
                    } else {
                        playBeepSound();
                    }
                    qIdx = (qIdx + 1) % quests.length;
                    container.querySelector('#type-element-display').textContent = quests[qIdx].val;
                });
            });
            break;
        }
        case 3: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;" id="op-quest">
                    🎯 بازل الرموز: ما هو المعامل الحسابي الصحيح لإتمام العملية؟
                </p>
                <div style="font-size:1.5rem; font-weight:bold; color:#023047; margin:15px 0; direction:ltr;">
                    10 <span id="op-placeholder" style="border-bottom:3px dashed #ffb703; padding:0 15px; color:#ffb703;">?</span> 2 = 20
                </div>
                <div style="display:flex; gap:10px;">
                    <button class="btn-game-option" data-op="*">*</button>
                    <button class="btn-game-option" data-op="+">+</button>
                    <button class="btn-game-option" data-op="-">-</button>
                    <button class="btn-game-option" data-op="/">/</button>
                </div>
            `;

            const quests = [
                { exp: '10 ? 2 = 20', ans: '*' },
                { exp: '15 ? 5 = 20', ans: '+' },
                { exp: '30 ? 10 = 3', ans: '/' },
                { exp: '25 ? 5 = 20', ans: '-' }
            ];

            let qIdx = 0;
            let score = 0;

            const buttons = container.querySelectorAll('.btn-game-option');
            buttons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const chosen = btn.getAttribute('data-op');
                    if (chosen === quests[qIdx].ans) {
                        score += 25;
                        if (score > 100) score = 100;
                        checkComplete(score);
                    } else {
                        playBeepSound();
                    }
                    qIdx = (qIdx + 1) % quests.length;
                    const q = quests[qIdx];
                    container.querySelector('#op-quest').nextElementSibling.innerHTML = q.exp.replace('?', `<span style="border-bottom:3px dashed #ffb703; padding:0 15px; color:#ffb703;">?</span>`);
                });
            });
            break;
        }
        case 4: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 فرز كروت الخزائن: صنف العنصر التالي في الصندوق الصحيح!
                </p>
                <div id="structure-display" style="background:#edf2f7; border:3px solid #cbd5e1; padding:15px; border-radius:12px; font-family:monospace; font-size:1.35rem; font-weight:bold; margin:10px 0;">{"name": "Falcon"}</div>
                <div style="display:flex; gap:10px;">
                    <button class="btn-game-option" data-struct="dict">Dictionary (قاموس)</button>
                    <button class="btn-game-option" data-struct="tuple">Tuple (صف ثابت)</button>
                </div>
            `;

            const quests = [
                { val: '{"name": "Falcon"}', ans: 'dict' },
                { val: '("تفاح", "موز")', ans: 'tuple' },
                { val: '{"age": 12, "hero": "Flash"}', ans: 'dict' },
                { val: '(10, 20, 30)', ans: 'tuple' }
            ];

            let qIdx = 0;
            let score = 0;

            const buttons = container.querySelectorAll('.btn-game-option');
            buttons.forEach(btn => {
                btn.addEventListener('click', () => {
                    const chosen = btn.getAttribute('data-struct');
                    if (chosen === quests[qIdx].ans) {
                        score += 25;
                        if (score > 100) score = 100;
                        checkComplete(score);
                    } else {
                        playBeepSound();
                    }
                    qIdx = (qIdx + 1) % quests.length;
                    container.querySelector('#structure-display').textContent = quests[qIdx].val;
                });
            });
            break;
        }
        case 5: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 حارس الإشارة الذكي: انقر لزيادة العداد (i += 1) لتفادي الحلقة اللانهائية وإطلاق السيارة!
                </p>
                <div style="display:flex; gap:20px; align-items:center; margin:15px 0;">
                    <div id="while-car" style="font-size:3rem; transition:transform 0.4s ease; transform:translateX(0px);">🚗</div>
                    <div style="background:#023047; color:#06d6a0; padding:10px 15px; border-radius:10px; font-family:monospace; font-size:1.15rem;">
                        i = <span id="while-counter" style="color:#ffb703; font-weight:bold;">1</span><br>
                        while i <= 5:<br>
                        &nbsp;&nbsp;drive()<br>
                        &nbsp;&nbsp;<span style="color:#ffd166;">i += 1</span>
                    </div>
                </div>
                <button class="btn-game-option" id="btn-increment-while" style="background:#ffb703; color:#023047; font-size:1.3rem;">⚡ زيادة العداد i += 1</button>
            `;

            let i = 1;
            const car = container.querySelector('#while-car');
            const counter = container.querySelector('#while-counter');
            const btn = container.querySelector('#btn-increment-while');

            btn.addEventListener('click', () => {
                if (i < 5) {
                    i++;
                    counter.textContent = i;
                    car.style.transform = `translateX(-${(i-1)*40}px)`;
                    checkComplete(i * 20);
                } else if (i === 5) {
                    i++;
                    counter.textContent = i;
                    car.style.transform = `translateX(-220px)`;
                    btn.disabled = true;
                    btn.textContent = "🚗 انطلقت السيارة بنجاح!";
                    checkComplete(100);
                }
            });
            break;
        }
        case 6: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 قطاف تفاح For Loop: الحلقة تطبع range(5). اقطف 5 تفاحات حمراء ناضجة!
                </p>
                <div id="apple-orchard" style="display:flex; gap:10px; margin:15px 0; min-height:50px;"></div>
                <button class="btn-game-option" id="btn-harvest-apple" style="background:#ff006e; color:#ffffff; font-size:1.3rem;">🍎 اقطف تفاحة</button>
            `;

            let apples = 0;
            const orchard = container.querySelector('#apple-orchard');
            const btn = container.querySelector('#btn-harvest-apple');

            btn.addEventListener('click', () => {
                if (apples < 5) {
                    apples++;
                    const app = document.createElement('span');
                    app.textContent = '🍎';
                    app.style.fontSize = '2.5rem';
                    orchard.appendChild(app);
                    checkComplete(apples * 20);
                    if (apples === 5) {
                        btn.disabled = true;
                        btn.textContent = "🏆 تم جمع المحصول بنجاح!";
                    }
                }
            });
            break;
        }
        case 7: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 مصنع الحلوى البرمجية: رتب خطوات دالة الحلوى البرمجية make_candy!
                </p>
                <div id="candy-steps-pool" style="display:flex; flex-direction:column; gap:6px; margin:10px 0; width:100%;"></div>
                <div id="candy-maker-result" style="font-size:3rem; margin-top:10px; min-height:50px;"></div>
            `;

            const steps = [
                { text: '1. def make_candy(flavor, size):', order: 1 },
                { text: '2.     candy = flavor + size', order: 2 },
                { text: '3.     return candy', order: 3 },
                { text: '4. print(make_candy("فراولة", "كبير"))', order: 4 }
            ];

            let expectedOrder = 1;
            const pool = container.querySelector('#candy-steps-pool');
            const result = container.querySelector('#candy-maker-result');

            steps.sort(() => Math.random() - 0.5).forEach(step => {
                const btn = document.createElement('button');
                btn.className = 'btn-game-option';
                btn.textContent = step.text;
                btn.style.width = '100%';
                btn.addEventListener('click', () => {
                    if (step.order === expectedOrder) {
                        btn.disabled = true;
                        btn.style.background = '#e6fffa';
                        btn.style.borderColor = '#06d6a0';
                        expectedOrder++;
                        checkComplete((expectedOrder - 1) * 25);
                        if (expectedOrder > 4) {
                            result.textContent = '🍭🌟🍬';
                        }
                    } else {
                        playBeepSound();
                    }
                });
                pool.appendChild(btn);
            });
            break;
        }
        case 8: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 متاهة السلحفاة Turtle: وجّه السلحفاة نحو النجمة السحرية ⭐!
                </p>
                <div style="position:relative; width:200px; height:200px; background:#e2e8f0; border-radius:12px; border:3px solid #219ebc; overflow:hidden;">
                    <div id="maze-turtle" style="position:absolute; top:150px; left:20px; font-size:2rem; transition:all 0.3s ease; transform:rotate(0deg);">🐢</div>
                    <div id="maze-star" style="position:absolute; top:20px; left:140px; font-size:2rem;">⭐</div>
                </div>
                <div style="display:flex; gap:10px; margin-top:10px;">
                    <button class="btn-game-option" id="turtle-up">⬆️ forward(50)</button>
                    <button class="btn-game-option" id="turtle-right">↪️ right(90)</button>
                </div>
            `;

            let x = 20;
            let y = 150;
            let angle = 0;
            const t = container.querySelector('#maze-turtle');
            const up = container.querySelector('#turtle-up');
            const right = container.querySelector('#turtle-right');

            right.addEventListener('click', () => {
                angle = (angle + 90) % 360;
                t.style.transform = `rotate(-${angle}deg)`;
                playHappyChime();
            });

            up.addEventListener('click', () => {
                if (angle === 90) {
                    y -= 50;
                } else if (angle === 0) {
                    x += 50;
                } else {
                    playBeepSound();
                    return;
                }
                if (x > 180) x = 180;
                if (y < 0) y = 0;

                t.style.left = `${x}px`;
                t.style.top = `${y}px`;

                let dist = Math.abs(x - 140) + Math.abs(y - 20);
                if (dist < 40) {
                    checkComplete(100);
                    up.disabled = true;
                    right.disabled = true;
                    t.textContent = '🐢🎉';
                } else {
                    checkComplete(50);
                }
            });
            break;
        }
        case 9: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 مصنع أبطال الكلاسات: فرّخ بطلاً خارقاً عن طريق إدخال القوى السحرية!
                </p>
                <div style="display:flex; flex-direction:column; gap:10px; width:100%; max-width:250px;">
                    <input type="text" id="hero-name-input" placeholder="اسم البطل الخارق..." style="padding:8px 12px; border-radius:8px; border:2px solid #cbd5e1; font-size:1.1rem; text-align:center;">
                    <select id="hero-power-select" style="padding:8px 12px; border-radius:8px; border:2px solid #cbd5e1; font-size:1.1rem; text-align:center;">
                        <option value="⚡ البرق السريع">⚡ البرق السريع</option>
                        <option value="🔥 اللهب الحارق">🔥 اللهب الحارق</option>
                        <option value="❄️ الجليد المجمد">❄️ الجليد المجمد</option>
                    </select>
                    <button class="btn-game-option" id="btn-spawn-hero" style="background:#219ebc; color:#ffffff; font-size:1.2rem;">🦸‍♂️ فرّخ البطل الخارق!</button>
                </div>
                <div id="spawn-result-card" style="margin-top:15px; width:100%;"></div>
            `;

            const btn = container.querySelector('#btn-spawn-hero');
            const nameIn = container.querySelector('#hero-name-input');
            const powerSel = container.querySelector('#hero-power-select');
            const resultCard = container.querySelector('#spawn-result-card');

            btn.addEventListener('click', () => {
                const name = nameIn.value.trim() || 'بطل ميجامايندز';
                const power = powerSel.value;

                resultCard.innerHTML = `
                    <div class="homework-card-gold" style="border-color:#219ebc; background:rgba(33,158,188,0.05); text-align:center; padding:15px; border-radius:12px;">
                        <span style="font-size:3rem;">🦸‍♂️</span>
                        <h4 style="color:#023047; font-size:1.4rem; margin:8px 0;">الكائن (Object) تم تفريخه!</h4>
                        <p style="font-size:1.2rem; font-weight:bold; color:#219ebc;">البطل: ${name}</p>
                        <p style="font-size:1.1rem; color:#475569;">القوة السحرية: ${power}</p>
                    </div>
                `;
                checkComplete(100);
                btn.disabled = true;
            });
            break;
        }
        case 10: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 معمل التخمين Brute-Force: اضغط على زر الهجمات لفك تشفير كلمة سر خادم Flask!
                </p>
                <button class="btn-game-option" id="btn-brute-attack" style="background:#ffb703; color:#023047; font-size:1.3rem; font-weight:bold;">⚡ ابدأ هجوم التخمين البرق</button>
                <div id="brute-terminal" style="width:100%; min-height:100px; background:#023047; color:#06d6a0; font-family:monospace; padding:15px; border-radius:10px; margin-top:10px; font-size:1.05rem; overflow-y:auto; text-align:left; direction:ltr;">
                    [System] Press button to inject dictionary...
                </div>
            `;

            const btn = container.querySelector('#btn-brute-attack');
            const term = container.querySelector('#brute-terminal');
            const passwords = ['123456', 'password', 'admin', 'megaminds123', 'admin_pass'];

            btn.addEventListener('click', () => {
                btn.disabled = true;
                term.innerHTML = '';
                let idx = 0;

                const interval = setInterval(() => {
                    if (idx < passwords.length - 1) {
                        const div = document.createElement('div');
                        div.textContent = `[Trying] dict_word = "${passwords[idx]}" -> [401 Unauthorized]`;
                        term.appendChild(div);
                        idx++;
                        checkComplete(idx * 20);
                    } else {
                        clearInterval(interval);
                        const div = document.createElement('div');
                        div.style.color = '#ffd166';
                        div.style.fontWeight = 'bold';
                        div.textContent = `[Success] dict_word = "${passwords[idx]}" -> [200 OK Access Granted!] 🎉`;
                        term.appendChild(div);
                        checkComplete(100);
                    }
                    term.scrollTop = term.scrollHeight;
                }, 500);
            });
            break;
        }
        case 11: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 تدريب المضارب: ارتد الكرة بمضرب التنس 3 مرات للفوز!
                </p>
                <div style="position:relative; width:100%; max-width:280px; height:180px; background:#023047; border-radius:12px; overflow:hidden; margin:0 auto;">
                    <div id="pong-pad" style="position:absolute; bottom:10px; left:110px; width:60px; height:12px; background:#ffb703; border-radius:6px;"></div>
                    <div id="pong-ball" style="position:absolute; top:20px; left:130px; width:15px; height:15px; background:#06d6a0; border-radius:50%;"></div>
                </div>
                <div style="display:flex; gap:10px; margin-top:10px;">
                    <button class="btn-game-option" id="btn-pong-left">⬅️ حرك يساراً</button>
                    <button class="btn-game-option" id="btn-pong-right">حرك يميناً ➡️</button>
                </div>
            `;

            let padX = 110;
            let ballX = 130;
            let ballY = 20;
            let speedX = 6;
            let speedY = 5;
            let bounces = 0;

            const pad = container.querySelector('#pong-pad');
            const ball = container.querySelector('#pong-ball');
            const left = container.querySelector('#btn-pong-left');
            const right = container.querySelector('#btn-pong-right');

            left.addEventListener('click', () => {
                padX -= 30;
                if (padX < 10) padX = 10;
                pad.style.left = `${padX}px`;
            });

            right.addEventListener('click', () => {
                padX += 30;
                if (padX > 210) padX = 210;
                pad.style.left = `${padX}px`;
            });

            const gameLoop = setInterval(() => {
                ballX += speedX;
                ballY += speedY;

                if (ballX < 10 || ballX > 255) speedX = -speedX;
                if (ballY < 10) speedY = -speedY;

                if (ballY >= 148 && ballY <= 160) {
                    if (ballX >= padX - 15 && ballX <= padX + 75) {
                        speedY = -speedY;
                        bounces++;
                        checkComplete(Math.min(100, bounces * 34));
                        if (bounces >= 3) {
                            clearInterval(gameLoop);
                            checkComplete(100);
                        }
                    } else {
                        ballY = 20;
                        ballX = 130;
                    }
                }

                ball.style.left = `${ballX}px`;
                ball.style.top = `${ballY}px`;
            }, 100);

            // Safety clear
            const checkExist = setInterval(() => {
                if (!document.body.contains(container)) {
                    clearInterval(gameLoop);
                    clearInterval(checkExist);
                }
            }, 1000);
            break;
        }
        case 12: {
            container.innerHTML = `
                <p style="font-size:1.15rem; font-weight:700; color:#023047; text-align:center;">
                    🎯 مباراة الذكاء الاصطناعي الكبرى: العب ضد بايثون-كوتش! أول من يحرز هدفين يفوز!
                </p>
                <div style="display:flex; justify-content:space-around; font-size:1.2rem; font-weight:bold; color:#023047; width:100%; margin-bottom:5px;">
                    <div>البطل: <span id="p1-score" style="color:#06d6a0;">0</span></div>
                    <div>الروبوت: <span id="p2-score" style="color:#ff006e;">0</span></div>
                </div>
                <div style="position:relative; width:100%; max-width:280px; height:180px; background:#023047; border-radius:12px; overflow:hidden; margin:0 auto;">
                    <div id="pong-p1" style="position:absolute; left:10px; top:70px; width:10px; height:45px; background:#06d6a0; border-radius:4px;"></div>
                    <div id="pong-p2" style="position:absolute; right:10px; top:70px; width:10px; height:45px; background:#ff006e; border-radius:4px;"></div>
                    <div id="pong-b1" style="position:absolute; top:80px; left:135px; width:12px; height:12px; background:#ffd166; border-radius:50%;"></div>
                </div>
                <div style="display:flex; gap:10px; margin-top:10px;">
                    <button class="btn-game-option" id="btn-p1-up">⬆️ تحرك لأعلى</button>
                    <button class="btn-game-option" id="btn-p1-down">تحرك لأسفل ⬇️</button>
                </div>
            `;

            let p1Y = 70;
            let p2Y = 70;
            let bX = 135;
            let bY = 80;
            let dx = 8;
            let dy = 6;
            let p1Score = 0;
            let p2Score = 0;

            const p1 = container.querySelector('#pong-p1');
            const p2 = container.querySelector('#pong-p2');
            const b = container.querySelector('#pong-b1');
            const up = container.querySelector('#btn-p1-up');
            const down = container.querySelector('#btn-p1-down');
            const score1 = container.querySelector('#p1-score');
            const score2 = container.querySelector('#p2-score');

            up.addEventListener('click', () => {
                p1Y -= 25;
                if (p1Y < 10) p1Y = 10;
                p1.style.top = `${p1Y}px`;
            });

            down.addEventListener('click', () => {
                p1Y += 25;
                if (p1Y > 125) p1Y = 125;
                p1.style.top = `${p1Y}px`;
            });

            const matchLoop = setInterval(() => {
                bX += dx;
                bY += dy;

                if (bY < 10 || bY > 158) dy = -dy;

                if (bX <= 24) {
                    if (bY >= p1Y - 10 && bY <= p1Y + 55) {
                        dx = -dx;
                        playHappyChime();
                    } else {
                        p2Score++;
                        score2.textContent = p2Score;
                        bX = 135; bY = 80;
                        dx = -dx;
                        if (p2Score >= 2) {
                            clearInterval(matchLoop);
                            playBeepSound();
                            alert("🤖 لقد فاز الروبوت هذه المرة! حاول مجدداً يا بطل!");
                            loadInteractiveGame(12);
                        }
                    }
                }

                if (bX >= 244) {
                    if (bY >= p2Y - 10 && bY <= p2Y + 55) {
                        dx = -dx;
                        playHappyChime();
                    } else {
                        p1Score++;
                        score1.textContent = p1Score;
                        bX = 135; bY = 80;
                        dx = -dx;
                        checkComplete(p1Score * 50);
                        if (p1Score >= 2) {
                            clearInterval(matchLoop);
                            checkComplete(100);
                        }
                    }
                }

                if (bY > p2Y + 20) p2Y += 5;
                else if (bY < p2Y + 20) p2Y -= 5;
                if (p2Y < 10) p2Y = 10;
                if (p2Y > 125) p2Y = 125;
                p2.style.top = `${p2Y}px`;

                b.style.left = `${bX}px`;
                b.style.top = `${bY}px`;
            }, 100);

            // Safety clear
            const checkExist = setInterval(() => {
                if (!document.body.contains(container)) {
                    clearInterval(matchLoop);
                    clearInterval(checkExist);
                }
            }, 1000);
            break;
        }
    }
}
