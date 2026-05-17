// ============================================================================
// CURRICULUM.JS - Interactive Python Curriculum & Custom Simulator
// ============================================================================

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
// CURRICULUM DATABASE (6 INTERACTIVE STATIONS)
// ============================================================================
const stationsData = {
    1: {
        id: 1,
        title: "المحطة 1: صندوق المتغيرات السحري",
        story: "أهلاً بك يا بطل المستقبل في جزيرة بايثون! لغة بايثون ذكية جداً، وتستطيع التحدث وتخزين الكلمات والأرقام في صناديق سحرية نسميها (Variables). لكي تجعل بايثون يطبع كلاماً على الشاشة، نستخدم الكلمة السحرية <code>print</code>.",
        simple: "تخيل أن المتغير (Variable) مثل كرتونة ألعابك! تكتب عليها من الخارج (لعبتي) وتضع بداخلها سيارة أو كرة. وعندما تريد أن تريها لأصدقائك تقول لبايثون <code>print(لعبتي)</code> فيخرجها فوراً!",
        hint: "اكتب السطر السحري التالي في المحرر: <code>print(\"أنا بطل ميجامايندز\")</code> ثم اضغط تشغيل!",
        challenge: "قم بطباعة الجملة السحرية <code>أنا بطل ميجامايندز</code> على الشاشة باستخدام أمر الطباعة print.",
        starter_code: "# اكتب كود الطباعة هنا يا بطل:\n",
        pills: [
            { label: "طباعة عبارة التحدي", code: 'print("أنا بطل ميجامايندز")' },
            { label: "إنشاء متغير وطباعته", code: 'hero_name = "أحمد"\nprint(hero_name)' }
        ],
        validator: (output, canvasUsed) => {
            return output.includes("أنا بطل ميجامايندز");
        }
    },
    2: {
        id: 2,
        title: "المحطة 2: آلة الحساب الذكية",
        story: "بايثون يعشق الأرقام والرياضيات! يستطيع جمع وطرح وضرب وقسمة أرقام ضخمة جداً في جزء من الثانية دون أي خطأ. نستخدم علامة <code>+</code> للجمع، و <code>*</code> للضرب.",
        simple: "بايثون عامل زي الكاشير السوبر مان! بتديه رقمين وتقوله اضربهم في بعض بيطلع الناتج في ثانية من غير ما يتعب ولا يحتاج آلة حاسبة!",
        hint: "اكتب في المحرر: <code>result = 50 * 20</code> وفي السطر التالي <code>print(result)</code>.",
        challenge: "قم بضرب الرقمين 50 في 20 واطبع الناتج النهائي (1000) على الشاشة باستخدام أمر print.",
        starter_code: "# احسب حاصل ضرب 50 في 20 واطبع الناتج:\n",
        pills: [
            { label: "حساب مباشر للضرب", code: 'print(50 * 20)' },
            { label: "استخدام المتغيرات للحساب", code: 'x = 50\ny = 20\nprint(x * y)' }
        ],
        validator: (output, canvasUsed) => {
            return output.includes("1000");
        }
    },
    3: {
        id: 3,
        title: "المحطة 3: حارس بوابة الشروط",
        story: "لكي نصنع برامج وألعاب ذكية، يجب أن نجعل بايثون يتخذ قرارات بنفسه! نستخدم قاعدة الشروط <code>if / else</code>. إذا كانت كلمة السر صحيحة (if) افتح البوابة، وإلا (else) أغلق البوابة!",
        simple: "زي شرطي المرور بالضبط! لو الإشارة خضراء (if) عدي بسلام، لو الإشارة حمراء (else) اقف مكانك فوراً!",
        hint: "اكتب <code>score = 100</code> ثم في السطر التالي <code>if score == 100:</code> وتحته بمسافة <code>print(\"بطل خارق\")</code>.",
        challenge: "قم بإنشاء متغير <code>score = 100</code> واستخدم شرط <code>if score == 100:</code> لطباعة عبارة <code>بطل خارق</code>.",
        starter_code: "# أنشئ المتغير واكتب شرط التحقق:\nscore = 100\n",
        pills: [
            { label: "شرط التحقق من الدرجة", code: 'score = 100\nif score == 100:\n    print("بطل خارق")' },
            { label: "شرط مع Else", code: 'score = 100\nif score > 50:\n    print("بطل خارق")\nelse:\n    print("حاول ثانية")' }
        ],
        validator: (output, canvasUsed) => {
            return output.includes("بطل خارق");
        }
    },
    4: {
        id: 4,
        title: "المحطة 4: دوامة التكرار العجيبة",
        story: "المبرمج الذكي لا يكرر كتابة الأكواد! بدلاً من كتابة أمر الطباعة 5 مرات متتالية، نأمر بايثون بتكرار الأمر 5 مرات بجملة سحرية واحدة: <code>for i in range(5):</code>.",
        simple: "زي المروحة الكهربائية! بدل ما تلف ريشة ريشة بإيدك، بتضغط على الزرار وهي بتلف لوحدها 500 مرة بدون توقف!",
        hint: "اكتب <code>for i in range(5):</code> وتحتها بمسافة <code>print(\"ميجامايندز\")</code>.",
        challenge: "استخدم حلقة التكرار <code>for i in range(5):</code> لطباعة كلمة <code>ميجامايندز</code> 5 مرات متتالية على الشاشة.",
        starter_code: "# استخدم حلقة for لطباعة الكلمة 5 مرات:\n",
        pills: [
            { label: "حلقة تكرار for", code: 'for i in range(5):\n    print("ميجامايندز")' },
            { label: "طباعة أرقام الحلقة", code: 'for i in range(5):\n    print(i)' }
        ],
        validator: (output, canvasUsed) => {
            const matches = output.match(/ميجامايندز/g);
            return matches && matches.length >= 5;
        }
    },
    5: {
        id: 5,
        title: "المحطة 5: فنان السلحفاة الذكي",
        story: "وصلنا لأمتع محطة فنية! سلحفاة بايثون السحرية (Turtle Graphics). يمكنك توجيه السلحفاة بالأوامر لترسم أشكالاً هندسية وفنية مذهلة بالألوان. نستخدم <code>import turtle</code> ثم أوامر الحركة والرسم.",
        simple: "تخيل سلحفاة آلية صغيرة تمشي على ورقة ومربوط في ذيلها قلم ألوان! كلما قلت لها تقدمي للأمام (forward) أو استديري (right) تترك خطاً ملوناً وراءها!",
        hint: "اكتب <code>import turtle</code> ثم <code>turtle.color(\"green\")</code> ثم <code>turtle.circle(60)</code>.",
        challenge: "قم باستدعاء السلحفاة <code>import turtle</code> واجعلها ترسم دائرة خضراء باستخدام <code>turtle.color(\"green\")</code> و <code>turtle.circle(60)</code>.",
        starter_code: "# استدعِ السلحفاة وارسم دائرة خضراء:\nimport turtle\n",
        pills: [
            { label: "رسم دائرة خضراء", code: 'import turtle\nturtle.color("green")\nturtle.circle(60)' },
            { label: "رسم مربع أحمر", code: 'import turtle\nturtle.color("red")\nfor i in range(4):\n    turtle.forward(100)\n    turtle.right(90)' }
        ],
        validator: (output, canvasUsed) => {
            return canvasUsed && (output.includes("circle") || output.includes("دائرة") || output.includes("رسم"));
        }
    },
    6: {
        id: 6,
        title: "المحطة 6: مبرمج الألعاب الخارق",
        story: "المحطة الختامية الكبرى في جزيرة بايثون! سنقوم بمحاكاة برمجة منطق لعبة كرة الطاولة الشهيرة (Ping Pong). سنحدد سرعة الكرة، موقع المضرب، ونحاكي اصطدام الكرة لتحقيق النصر!",
        simple: "زي لعبة التنس في الملاهي! بنبرمج الكورة لما تخبط في المضرب ترجع تاني، ولما تعدي نحسب نقطة للبطل!",
        hint: "اكتب <code>ball_speed = 10</code> و <code>paddle_pos = 50</code> ثم الجملة السحرية <code>print(\"تم تشغيل لعبة Ping Pong بنجاح!\")</code>.",
        challenge: "قم بتهيئة متغيرات اللعبة <code>ball_speed = 10</code> و <code>paddle_pos = 50</code> واطبع العبارة الختامية <code>تم تشغيل لعبة Ping Pong بنجاح!</code> لمشاهدة المحاكاة!",
        starter_code: "# تهيئة اللعبة وتشغيل المحاكاة:\nball_speed = 10\npaddle_pos = 50\n",
        pills: [
            { label: "تشغيل محاكاة اللعبة", code: 'ball_speed = 10\npaddle_pos = 50\nprint("تم تشغيل لعبة Ping Pong بنجاح!")' }
        ],
        validator: (output, canvasUsed) => {
            return output.includes("تم تشغيل لعبة Ping Pong بنجاح!");
        }
    }
};

// ============================================================================
// STATE MANAGEMENT & LOCAL STORAGE
// ============================================================================
let currentStationId = 1;
let studentProgress = {
    xp: 0,
    completedStations: []
};

// Load progress from localStorage
function loadProgress() {
    const saved = localStorage.getItem('megaminds_python_progress');
    if (saved) {
        try {
            studentProgress = JSON.parse(saved);
        } catch(e) { console.error("Error parsing progress", e); }
    }
    updateUIProgress();
}

// Save progress to localStorage
function saveProgress() {
    localStorage.setItem('megaminds_python_progress', JSON.stringify(studentProgress));
    updateUIProgress();
}

// Update UI elements based on progress state
function updateUIProgress() {
    const xpCountText = document.getElementById('xpCountText');
    const xpProgressBar = document.getElementById('xpProgressBar');
    const btnClaimCert = document.getElementById('btnClaimCert');

    // Update XP text & bar
    if (xpCountText) xpCountText.textContent = `${studentProgress.xp} / 600 XP`;
    if (xpProgressBar) {
        const percentage = Math.min(100, (studentProgress.xp / 600) * 100);
        xpProgressBar.style.width = `${percentage}%`;
    }

    // Update Badges Showcase & Station Cards
    for (let i = 1; i <= 6; i++) {
        const badgeEl = document.getElementById(`badge_${i}`);
        const stationEl = document.getElementById(`station_${i}`);
        
        const isCompleted = studentProgress.completedStations.includes(i);
        const isUnlocked = isCompleted || (i === 1) || studentProgress.completedStations.includes(i - 1);

        // Badge update
        if (badgeEl) {
            if (isCompleted) {
                badgeEl.classList.add('earned');
            } else {
                badgeEl.classList.remove('earned');
            }
        }

        // Station card update
        if (stationEl) {
            stationEl.classList.remove('locked', 'active', 'completed');
            const badgeSpan = stationEl.querySelector('.station-badge');
            const btnSpan = stationEl.querySelector('.station-btn span');

            if (isCompleted) {
                stationEl.classList.add('completed');
                if (badgeSpan) badgeSpan.textContent = "مكتمل ✅";
                if (btnSpan) btnSpan.textContent = "مراجعة التحدي 🔄";
            } else if (isUnlocked) {
                stationEl.classList.add('active');
                if (badgeSpan) badgeSpan.textContent = "متاح الآن 🌟";
                if (btnSpan) btnSpan.textContent = "ابدأ المغامرة 🚀";
            } else {
                stationEl.classList.add('locked');
                if (badgeSpan) badgeSpan.textContent = "مغلق 🔒";
                if (btnSpan) btnSpan.textContent = "مغلق حالياً 🔒";
            }
        }
    }

    // Check if all 6 stations completed to show Claim Certificate button
    if (studentProgress.completedStations.length >= 6) {
        if (btnClaimCert) btnClaimCert.classList.add('active');
    } else {
        if (btnClaimCert) btnClaimCert.classList.remove('active');
    }
}

// ============================================================================
// CUSTOM PYTHON EDUCATIONAL SIMULATOR & INTERPRETER
// ============================================================================
function simulatePythonExecution(code, stationId) {
    const outputArea = document.getElementById('outputContentArea');
    const turtleCanvas = document.getElementById('turtleCanvas');
    let canvasUsed = false;

    if (!outputArea) return;
    outputArea.innerHTML = ''; // Clear previous output

    // Helper to log to simulated console
    function logOutput(text, type = 'success') {
        const div = document.createElement('div');
        div.className = `output-log ${type}`;
        div.textContent = text;
        outputArea.appendChild(div);
    }

    logOutput(">>> جاري تشغيل كود بايثون السحري...", "info");

    // Reset Canvas
    if (turtleCanvas) {
        const ctx = turtleCanvas.getContext('2d');
        ctx.clearRect(0, 0, turtleCanvas.width, turtleCanvas.height);
        turtleCanvas.classList.remove('active');
    }

    let simulatedStdout = [];
    let pyVariables = {};

    // Basic line-by-line simulation parser
    const lines = code.split('\n');
    let insideForLoop = false;
    let forLoopCount = 0;
    let forLoopBody = [];
    let forLoopVar = 'i';

    try {
        for (let i = 0; i < lines.length; i++) {
            let line = lines[i].trim();
            if (!line || line.startsWith('#')) continue; // Skip comments & empty lines

            // Check if inside for loop body (indented)
            if (insideForLoop) {
                if (lines[i].startsWith('    ') || lines[i].startsWith('\t')) {
                    forLoopBody.push(line);
                    if (i === lines.length - 1) {
                        // Execute loop body
                        executeForLoop(forLoopVar, forLoopCount, forLoopBody, pyVariables, simulatedStdout, logOutput);
                    }
                    continue;
                } else {
                    // Loop ended, execute it
                    executeForLoop(forLoopVar, forLoopCount, forLoopBody, pyVariables, simulatedStdout, logOutput);
                    insideForLoop = false;
                    forLoopBody = [];
                }
            }

            // 1. Variable Assignment (e.g. hero = "أحمد" or x = 50 * 20)
            if (line.includes('=') && !line.includes('==') && !line.startsWith('if') && !line.startsWith('for')) {
                const parts = line.split('=');
                const varName = parts[0].trim();
                let varVal = parts[1].trim();

                // Evaluate basic math if present
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

            // 2. Print Statement (e.g. print("Hello") or print(x))
            if (line.startsWith('print(') && line.endsWith(')')) {
                let content = line.slice(6, -1).trim();

                // Check math inside print
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

            // 3. If Statement (e.g. if score == 100:)
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

                // Check next line for if body
                if (i + 1 < lines.length && (lines[i+1].startsWith('    ') || lines[i+1].startsWith('\t'))) {
                    let nextLine = lines[i+1].trim();
                    if (isTrue) {
                        if (nextLine.startsWith('print(')) {
                            let content = nextLine.slice(6, -1).trim().replace(/["']/g, '');
                            simulatedStdout.push(content);
                            logOutput(content, "success");
                        }
                    }
                    i++; // skip if body line
                    // check for else
                    if (i + 1 < lines.length && lines[i+1].trim() === 'else:') {
                        i++; // skip else line
                        if (i + 1 < lines.length && (lines[i+1].startsWith('    ') || lines[i+1].startsWith('\t'))) {
                            let elseLine = lines[i+1].trim();
                            if (!isTrue) {
                                if (elseLine.startsWith('print(')) {
                                    let content = elseLine.slice(6, -1).trim().replace(/["']/g, '');
                                    simulatedStdout.push(content);
                                    logOutput(content, "success");
                                }
                            }
                            i++; // skip else body line
                        }
                    }
                }
                continue;
            }

            // 4. For Loop Statement (e.g. for i in range(5):)
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

    // Helper to execute for loop body in simulator
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

    // Check station validation
    const station = stationsData[stationId];
    const fullOutputText = simulatedStdout.join(' ') + ' ' + outputArea.textContent;
    const isCorrect = station.validator(fullOutputText, canvasUsed);

    if (isCorrect) {
        logOutput("\n✨ إجابة عبقرية! لقد نجحت في تحقيق التحدي المطلوب! ✨", "success");
        playSuccessFanfare();
        triggerConfetti();

        // Award XP & unlock next
        if (!studentProgress.completedStations.includes(stationId)) {
            studentProgress.completedStations.push(stationId);
            studentProgress.xp += 100;
            saveProgress();
        }

        // Show celebration modal
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
    loadProgress();

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

    // Open Studio Helper
    function openStudioForStation(stId) {
        currentStationId = stId;
        const station = stationsData[stId];

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

        // Hide hint box initially
        if (hintDisplayBox) hintDisplayBox.classList.remove('active');

        // Clear output
        const outputArea = document.getElementById('outputContentArea');
        if (outputArea) outputArea.innerHTML = '<div class="output-log info"># شاشة المخرجات جاهزة. اضغط على "تشغيل الكود السحري" لرؤية النتيجة!</div>';

        // Hide turtle canvas
        const turtleCanvas = document.getElementById('turtleCanvas');
        if (turtleCanvas) turtleCanvas.classList.remove('active');

        // Show Studio & Scroll
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
            if (hintDisplayBox) {
                hintTitleText.textContent = "💡 التبسيط العامي (بسطها لي):";
                hintContentText.innerHTML = stationsData[currentStationId].simple;
                hintDisplayBox.classList.add('active');
                playHappyChime();
            }
        });
    }

    // 6. Magic Hint Button
    if (btnMagicHint) {
        btnMagicHint.addEventListener('click', () => {
            if (hintDisplayBox) {
                hintTitleText.textContent = "✨ تلميح سحري للمساعدة:";
                hintContentText.innerHTML = stationsData[currentStationId].hint;
                hintDisplayBox.classList.add('active');
                playHappyChime();
            }
        });
    }

    // 7. Celebration Next Button
    if (btnCelebrationNext) {
        btnCelebrationNext.addEventListener('click', () => {
            if (celebrationModal) celebrationModal.classList.remove('active');
            if (currentStationId < 6) {
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
            
            // Try to get student name from localStorage if registered in quiz
            const regData = localStorage.getItem('megaminds_student_reg');
            if (regData) {
                try {
                    const parsed = JSON.parse(regData);
                    if (parsed.studentName && studentNameDisplay) {
                        studentNameDisplay.textContent = parsed.studentName;
                    }
                } catch(e){}
            }

            // Set current date
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
