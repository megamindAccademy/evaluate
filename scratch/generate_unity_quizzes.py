import json
import os

quizzes_dir = r"c:\Users\rowan\Desktop\ev\evaluate\database\senior_unity\quizzes"

# Define the 6 quizzes data
quizzes_data = {
    "quiz1.json": {
        "quiz_id": "unity_quiz_1",
        "quiz_title": "Quiz 1: Introduction to Unity & Bolt Scripting",
        "questions": [
            {
                "id": 1,
                "question": "What are the three main parts of any game, and which one is Unity? / ما هي المكونات الثلاثة الأساسية لأي لعبة، وأيها هو محرك يونيتي؟",
                "options": [
                    "Player, Level, and Unity (the game engine) / اللاعب، المستوى، ومحرك يونيتي (محرك اللعبة)",
                    "Console, Assets, and Hub / شاشة المخرجات، الملفات، وموزع المشروعات",
                    "Aesthetic, Graphic, and Code / الشكل الجمالي، الرسوميات، والأكواد",
                    "Compiler, Variables, and Classes / المترجم، المتغيرات، والفئات البرمجية"
                ],
                "correct": 0,
                "explanation": "Excellent! Every game has a Player who plays, a Creator who designs, and a Game Engine (Unity) that runs everything! / رائع! كل لعبة لها لاعب يلعب، وصانع يصمم، ومحرك ألعاب (يونيتي) يشغل كل شيء!"
            },
            {
                "id": 2,
                "question": "Which C# function displays messages on our Console screen when the game starts? / أي دالة بلغة C# تستخدم لطباعة رسالة في لوحة الكونسول بمجرد بدء اللعبة؟",
                "options": [
                    "Console.ReadLine()",
                    "Debug.Log()",
                    "GetComponent()",
                    "Destroy()"
                ],
                "correct": 1,
                "explanation": "Correct! We use Debug.Log('message') in Unity scripts to print info onto our Console window. / صحيح! نستخدم Debug.Log لطباعة الرسائل والمعلومات في لوحة الكونسول البرمجية!"
            },
            {
                "id": 3,
                "question": "Which Unity editor window contains all elements (GameObjects) currently active inside your scene? / أي نافذة في محرر يونيتي تحتوي على جميع الكائنات الموجودة حالياً داخل المشهد؟",
                "options": [
                    "Project Window / نافذة المشروع",
                    "Hierarchy Window / نافذة التسلسل الهرمي",
                    "Console Window / نافذة الكونسول",
                    "Asset Store / متجر الأصول"
                ],
                "correct": 1,
                "explanation": "Perfect! The Hierarchy lists every active GameObject in the current open scene. / ممتاز! نافذة التسلسل الهرمي (Hierarchy) تسرد كل الكائنات النشطة في المشهد الحالي!"
            },
            {
                "id": 4,
                "question": "What is the Unity Asset Store used for? / في ماذا نستخدم متجر أصول يونيتي (Asset Store) الساحر؟",
                "options": [
                    "To buy hardware for your PC / لشراء قطع غيار جديدة للحاسوب",
                    "To download characters, 3D models, textures, and sounds / لتحميل شخصيات، مجسمات، ألوان وأصوات جاهزة ومجانية",
                    "To write C# scripts / لكتابة السكربتات البرمجية",
                    "To build game executables / لتصدير اللعبة النهائية"
                ],
                "correct": 1,
                "explanation": "Bravo! The Asset Store is like a magic shop to import 3D models and character sprites. / رائع! متجر الأصول هو مثل متجر سحري للحصول على مجسمات وأشكال وشخصيات مذهلة!"
            },
            {
                "id": 5,
                "question": "What does Bolt visual scripting allow you to do? / ماذا يتيح لنا نظام البرمجة المرئية Bolt في يونيتي؟",
                "options": [
                    "Create games without writing text code by connecting visual nodes / برمجة منطق اللعبة بالكامل عبر توصيل البلوكات والعقد التفاعلية بدون أكواد نصية معقدة",
                    "Make the computer faster / جعل الحاسوب يعمل بسرعة خارقة",
                    "Delete Unity scripts automatically / حذف الأكواد والملفات تلقائياً",
                    "Draw 3D characters / رسم وتصميم الشخصيات ثلاثية الأبعاد"
                ],
                "correct": 0,
                "explanation": "Splendid! Bolt lets you program by linking visual nodes with line flows instead of writing raw text. / مذهل! يتيح Bolt البرمجة المرئية عبر توصيل الصناديق والخطوط لتبسيط الأفكار للأبطال!"
            },
            {
                "id": 6,
                "question": "Which Bolt node represents an action that happens once at the very start of the game? / أي عقدة في Bolt تمثل أمراً يحدث مرة واحدة فقط عند بدء تشغيل اللعبة مباشرة؟",
                "options": [
                    "On Update Event / عقدة التحديث المستمر",
                    "On Start Event / عقدة البداية الأولى",
                    "Rotate Node / عقدة الدوران",
                    "Translate Node / عقدة الحركة"
                ],
                "correct": 1,
                "explanation": "Great! The On Start event node triggers its flow lines once when the GameObject is initialized. / رائع! عقدة Start تفعل التدفق مرة واحدة فقط عند تشغيل اللعبة لأول مرة!"
            },
            {
                "id": 7,
                "question": "To rotate a planet around its vertical axis (Up/Down) in Unity, which axis of the Vector3 do we rotate? / لتدوير كوكب حول محوره الرأسي (أعلى/أسفل) في الفضاء، أي محور في المتجه Vector3 نقوم بتدويره؟",
                "options": [
                    "X axis / المحور الأفقي X",
                    "Y axis / المحور الرأسي Y",
                    "Z axis / المحور العميق Z",
                    "W axis / المحور الرابع W"
                ],
                "correct": 1,
                "explanation": "Superb! The Y-axis represents the vertical axis; rotating it makes objects spin like a top! / عبقري! المحور Y هو المحور الرأسي، وتدويره يجعل المجسمات تدور حول نفسها كالنحلة الدوارة!"
            },
            {
                "id": 8,
                "question": "Why do we multiply movement or rotation speed by 'Time.deltaTime' in Unity? / لماذا نضرب قيم الحركة والدوران في 'Time.deltaTime' في يونيتي؟",
                "options": [
                    "To make the game looks beautiful / لجعل شكل اللعبة جميلاً فقط",
                    "To ensure consistent speed on all computers, regardless of frame rates / لضمان حركة سلسة وبنفس السرعة على جميع الأجهزة مهما كانت سرعة معالجاتها",
                    "To pause the game / لإيقاف اللعبة مؤقتاً",
                    "To double the player's health / لمضاعفة صحة وطاقة اللاعب"
                ],
                "correct": 1,
                "explanation": "Outstanding! Time.deltaTime adjusts movement based on real seconds, making speed independent of frame rates. / ممتاز! يضمن Time.deltaTime تحرك الأشياء بسرعة موحدة وسلسة على كل الأجهزة!"
            },
            {
                "id": 9,
                "type": "task",
                "question": "Simple Coding Task: Write a C# script template that prints 'Greetings Hero' using Debug.Log inside the Start function. / مهمة برمجية: اكتب جملة طباعة Debug.Log لطباعة 'Greetings Hero'!",
                "task_hint": "Write: Debug.Log(\"Greetings Hero\");",
                "explanation": "Perfect! In C# we write Debug.Log() with a semicolon at the end of the statement! / مذهل! في لغة C# ننهي السطور دائماً بالفصلة المنقوطة Semicolon (;)!"
            },
            {
                "id": 10,
                "type": "task",
                "question": "Visual Flow Task: Describe how to connect a custom visual flow in Bolt to move a player: On Update Event connects to what node? / مهمة التدفق: حدد العقدة التي نصلها بعقدة On Update لتحريك كائن؟",
                "task_hint": "Connect 'On Update Event' to 'Translate' or 'Rotate' node",
                "explanation": "Spot on! Connecting the flow output of 'On Update Event' to a 'Translate' node applies movement frame-by-frame. / رائع! ربط حدث التحديث بعقدة الحركة (Translate) يجعل الحركة مستمرة مع كل إطار!"
            }
        ]
    },
    "quiz2.json": {
        "quiz_id": "unity_quiz_2",
        "quiz_title": "Quiz 2: Flappy Bird Game Mechanics",
        "questions": [
            {
                "id": 1,
                "question": "Which Unity component must be added to a GameObject to give it weight and gravity? / أي مكون في يونيتي يجب إضافته للكائنات لمنحها وزناً فيزيائياً وتأثراً بالجاذبية؟",
                "options": [
                    "Box Collider 2D / صندوق اصطدام",
                    "Rigidbody 2D / الجسيم الفيزيائي",
                    "Animator / منظم الحركة والأنيميشن",
                    "Sprite Renderer / مظهر الصورة"
                ],
                "correct": 1,
                "explanation": "Correct! Rigidbody 2D is the core component that brings physics and gravity to 2D sprites. / صحيح! الجسيم الفيزيائي Rigidbody 2D هو المسؤول عن الجاذبية والفيزياء في ثنائي الأبعاد!"
            },
            {
                "id": 2,
                "question": "How do we program the bird to jump upwards when the jump key is pressed? / كيف نجعل الطائر يقفز للأعلى في الكود عند ضغط زر القفز؟",
                "options": [
                    "By adding a velocity impulse upwards to its Rigidbody / بإعطاء دفعة سرعة للأعلى لجسيم Rigidbody",
                    "By destroying the bird / بتدمير الطائر وحذفه",
                    "By scaling the camera / بتكبير وتصغير حجم الكاميرا",
                    "By changing its color / بتغيير ألوان الطائر"
                ],
                "correct": 0,
                "explanation": "Excellent! Setting velocity = Vector2.up * jumpForce applies an instant upward impulse to make the bird hop! / رائع! إعطاء سرعة للأعلى هو ما يدفع الطائر ليقفز فوراً بالفيزياء!"
            },
            {
                "id": 3,
                "question": "What is a 'Prefab' in Unity, and what is its kitchen analogy? / ما هو الـ Prefab في يونيتي، وماذا يشبه في المطبخ الحقيقي؟",
                "options": [
                    "It is like a cookie cutter - a reusable template to stamp out copies of GameObjects / هو مثل قالب الكعك، قالب جاهز نستخدمه لتوليد وتكرار الكائنات اللانهائية",
                    "It is an oven to cook graphics / هو مثل الفرن لطهي وتلوين الرسوميات",
                    "It is a plate to display the game / هو الطبق الذي نقدم عليه اللعبة للجمهور",
                    "It is a custom sound effect / هو ملف مؤثرات صوتية مخصصة"
                ],
                "correct": 0,
                "explanation": "Bravo! Prefabs are reusable templates stored in your files, allowing you to instantiate copies anywhere. / ممتاز! الـ Prefab هو قالب سحري لصنع وتوليد مجسمات مكررة مثل الأنابيب اللانهائية!"
            },
            {
                "id": 4,
                "question": "Which C# built-in method is used to dynamically spawn a new instance of a Prefab in runtime? / أي دالة في يونيتي تستخدم لتوليد واستدعاء نسخة جديدة من الـ Prefab أثناء اللعب؟",
                "options": [
                    "Destroy()",
                    "Instantiate()",
                    "GetComponent()",
                    "Debug.Log()"
                ],
                "correct": 1,
                "explanation": "Splendid! Instantiate(prefab, position, rotation) generates a live copy of a prefab dynamically. / مذهل! دالة Instantiate هي مصنع التوليد التلقائي للنماذج الجاهزة أثناء تشغيل اللعبة!"
            },
            {
                "id": 5,
                "question": "Which physics collision method triggers when our player physically crashes into a solid pipe obstacle? / أي دالة اصطدام في يونيتي تعمل فوراً عندما يصطدم الطائر بجدار الأنبوب الصلب؟",
                "options": [
                    "OnTriggerEnter2D()",
                    "OnCollisionEnter2D()",
                    "OnStartEvent()",
                    "OnUpdate()"
                ],
                "correct": 1,
                "explanation": "Superb! OnCollisionEnter2D fires when solid colliders bump into each other. / عبقري! دالة OnCollisionEnter2D تفعل فوراً عند حدوث تصادم صلب وحقيقي بين الكائنات!"
            },
            {
                "id": 6,
                "question": "How do we split a complete game in Unity, such as having a main menu and a gameplay scene? / كيف نقسم لعبتنا في يونيتي ليكون لها شاشة بداية وشاشة لعب مستقلة؟",
                "options": [
                    "By creating separate Scenes / بإنشاء مشاهد وشاشات مستقلة (Scenes)",
                    "By coding multiple classes in one file / بكتابة مئات الأكواد في ملف واحد",
                    "By buying multiple computers / بشراء عدة حواسيب لكل شاشة",
                    "By using different camera models / باستخدام أنواع كاميرات مختلفة"
                ],
                "correct": 0,
                "explanation": "Perfect! Scenes in Unity act as separate levels or pages of your complete game universe. / ممتاز! المشاهد Scenes هي بمثابة صفحات الكتاب أو مستويات اللعبة التي ننتقل بينها!"
            },
            {
                "id": 7,
                "question": "Which namespace and class must be called in C# to load or switch between different game levels? / أي مكتبة وفئة برمجية نستدعيها في C# للانتقال والتحكم في مشاهد اللعبة؟",
                "options": [
                    "UnityEngine.UI",
                    "UnityEngine.SceneManagement.SceneManager",
                    "System.Collections.Generic",
                    "UnityEngine.Audio"
                ],
                "correct": 1,
                "explanation": "Bravo! SceneManager.LoadScene() is the magic command to switch between start menus and game levels! / رائع! نستخدم مكتبة SceneManager وأمر LoadScene للانتقال بين القوائم والمستويات!"
            },
            {
                "id": 8,
                "question": "How do we make a collider act as a 'score sensor' that triggers a point without physically stopping the bird? / كيف نجعل صندوق الاصطدام يعمل كمستشعر نقاط يعبر منه اللاعب دون أن يعيقه فيزيائياً؟",
                "options": [
                    "By making it smaller / بجعله صغير الحجم جداً",
                    "By checking the 'Is Trigger' checkbox in the Collider / بتفعيل خيار 'Is Trigger' في مكون الاصطدام",
                    "By removing the Rigidbody / بحذف الجسيم الفيزيائي بالكامل",
                    "By setting its scale to zero / بجعل مقياس الحجم صفراً"
                ],
                "correct": 1,
                "explanation": "Outstanding! checking 'Is Trigger' lets objects pass through while still firing OnTriggerEnter events. / ممتاز! تفعيل Is Trigger يحول درع الاصطدام لمستشعر غير مرئي يسجل العبور والنقاط!"
            },
            {
                "id": 9,
                "type": "task",
                "question": "Simple Coding Task: Write a line of code to destroy the GameObject this script is attached to. / مهمة برمجية: اكتب سطراً برمجياً يقوم بتدمير الكائن الحالي (gameObject) عند الاصطدام!",
                "task_hint": "Write: Destroy(gameObject);",
                "explanation": "Great job! Destroy(gameObject) deletes the specified object from memory instantly! / أحسنت! دالة Destroy تمسح الكائن المحدد من شاشة اللعبة ومن الذاكرة تماماً!"
            },
            {
                "id": 10,
                "type": "task",
                "question": "Physics Task: Write a C# velocity assignment statement to move the Rigidbody (rb) upward by jumpForce. / مهمة فيزيائية: اكتب جملة إعطاء سرعة للأعلى لجسيم Rigidbody باسم rb!",
                "task_hint": "Write: rb.velocity = Vector2.up * jumpForce;",
                "explanation": "Superb! Mutating Rigidbody velocity offers precise, responsive jump physics control. / عبقري! تعديل سرعة rb.velocity مباشرة يعطي قفزات تفاعلية وسريعة الاستجابة!"
            }
        ]
    },
    "quiz3.json": {
        "quiz_id": "unity_quiz_3",
        "quiz_title": "Quiz 3: C# Programming Fundamentals",
        "questions": [
            {
                "id": 1,
                "question": "What character must be placed at the end of almost every statement in C#? / ما هي العلامة السحرية التي يجب وضعها في نهاية كل جملة برمجية في لغة C#؟",
                "options": [
                    "Colon (:) / النقطتان",
                    "Semicolon (;) / الفصلة المنقوطة",
                    "Period (.) / النقطة",
                    "Hashtag (#) / علامة الهاشتاج"
                ],
                "correct": 1,
                "explanation": "Correct! C# statement lines must always end with a semicolon (;) to compile properly. / صحيح! لغة C# تشترط إنهاء الجمل البرمجية بالفصلة المنقوطة لكي يفهمها الحاسوب!"
            },
            {
                "id": 2,
                "question": "Which C# standard method reads user keystrokes from the terminal window? / أي دالة في C# تستخدم لاستقبال وقراءة الكلمات التي يكتبها المستخدم في شاشة المخرجات؟",
                "options": [
                    "Console.WriteLine()",
                    "Console.ReadLine()",
                    "Console.Clear()",
                    "Console.Play()"
                ],
                "correct": 1,
                "explanation": "Excellent! Console.ReadLine() pauses execution and listens to keyboard inputs typed by the user. / رائع! دالة Console.ReadLine تنتظر وتستمع لمدخلات المستخدم النصية بدقة!"
            },
            {
                "id": 3,
                "question": "Which C# data type is specifically designed to store true or false logic values? / ما هو نوع البيانات في C# المصمم خصيصاً لتخزين قيم الصواب والخطأ المنطقية؟",
                "options": [
                    "int / الأعداد الصحيحة",
                    "float / الأعداد العشرية",
                    "string / النصوص",
                    "bool / القيم المنطقية"
                ],
                "correct": 3,
                "explanation": "Perfect! A boolean (bool) type variable can only hold 'true' or 'false' logic values. / ممتاز! المتغير من نوع bool (بولين) لا يقبل سوى قيمتين فقط: true (صح) أو false (خطأ)!"
            },
            {
                "id": 4,
                "question": "What is the result of (10 > 5) && (3 == 3) in programming logic? / ما هي نتيجة العملية المنطقية التالية: (10 أكبر من 5) و (3 تساوي 3)؟",
                "options": [
                    "true",
                    "false",
                    "error / خطأ برمي",
                    "0"
                ],
                "correct": 0,
                "explanation": "Splendid! Both conditions are true, and the AND operator (&&) returns true only if both sides are true! / مذهل! كلا الشرطين صحيحان، والعامل && يعطي true لأن كلا الطرفين محققان!"
            },
            {
                "id": 5,
                "question": "Which statement is used to execute a block of code only if a specific condition is met? / ما هي الأداة البرمجية المستخدمة لتشغيل أكواد معينة فقط في حال تحقق شرط محدد؟",
                "options": [
                    "for loop",
                    "if statement",
                    "while loop",
                    "class blueprint"
                ],
                "correct": 1,
                "explanation": "Superb! If statements check conditions and divert logic flow dynamically. / عبقري! جملة if الشرطية تسمح للحاسوب باتخاذ القرارات الذكية بناءً على الشروط!"
            },
            {
                "id": 6,
                "question": "Which loop structure is best suited when you know the exact number of repetitions beforehand? / أي حلقة تكرار هي الأنسب عندما نكون على علم مسبق بالعدد الدقيق لمرات التكرار؟",
                "options": [
                    "while loop / حلقة وايل",
                    "for loop / حلقة فور",
                    "if block / جملة إف",
                    "class template / قالب الفئة"
                ],
                "correct": 1,
                "explanation": "Perfect! A for loop includes initializer, condition, and incrementor in one clean line, best for set ranges. / ممتاز! حلقة for هي الأروع لتكرار الأوامر بعدد محدد ومعلوم مسبقاً!"
            },
            {
                "id": 7,
                "question": "What is the difference between a Class and an Object in OOP? / ما هو الفرق الأساسي بين الفئة البرمجية (Class) والكائن (Object) في البرمجة؟",
                "options": [
                    "Class is the blueprint; Object is the real instance built from that blueprint / الفئة هي المخطط الهندسي، والكائن هو المجسم الحقيقي الذي بنيناه من هذا المخطط",
                    "Class is a sound file; Object is a picture / الفئة هي ملف صوتي والكائن هو صورة",
                    "Object is the code; Class is the user / الكائن هو الكود والفئة هي المستخدم",
                    "There is no difference / لا يوجد أي فرق بينهما"
                ],
                "correct": 0,
                "explanation": "Bravo! A Class defines the variables and methods; Objects are individual instances rolling off that blueprint. / رائع! الفئة هي الرسم التخطيطي للسيارات، والكائنات هي السيارات الملموسة في الشارع!"
            },
            {
                "id": 8,
                "question": "Which keyword makes variables or methods accessible by other scripts outside their own Class? / ما هي الكلمة المفتاحية التي تجعل المتغيرات والدوال قابلة للقراءة والاستدعاء من خارج فئتها البرمجية؟",
                "options": [
                    "private",
                    "public",
                    "static",
                    "void"
                ],
                "correct": 1,
                "explanation": "Outstanding! Declaring properties public exposes them to other Unity components and scripts. / ممتاز! كلمة public هي جواز السفر الذي يتيح تبادل البيانات واستدعاء الدوال بين السكربتات!"
            },
            {
                "id": 9,
                "type": "task",
                "question": "Simple Coding Task: Write a C# variable declaration for an integer named 'gems' assigned with the value 5. / مهمة برمجية: اكتب إعلان متغير من نوع رقم صحيح (int) باسم 'gems' ويحمل قيمة 5!",
                "task_hint": "Write: int gems = 5;",
                "explanation": "Awesome work! In C# we strongly type variables by writing the type (int) followed by name and assignment! / أحسنت! في C# يجب تحديد نوع المتغير أولاً مثل int ثم الاسم والقيمة!"
            },
            {
                "id": 10,
                "type": "task",
                "question": "OOP Method Task: Design a void method named 'Jump' in C# that takes no arguments. / مهمة برمجية: اكتب هيكل دالة فارغة (void) باسم 'Jump' لا تأخذ أي معطيات!",
                "task_hint": "Write: void Jump() { }",
                "explanation": "Spot on! Void methods execute actions without returning any output data values. / رائع! الدوال من نوع void تقوم بتنفيذ الأوامر والحركات دون الحاجة لإرجاع قيمة حسابية!"
            }
        ]
    },
    "quiz4.json": {
        "quiz_id": "unity_quiz_4",
        "quiz_title": "Quiz 4: Sunny Land 2D Platformer Adventure",
        "questions": [
            {
                "id": 1,
                "question": "Which component allows us to draw ground, grass, and brick layers directly onto a grid layout? / أي مكون في يونيتي 2D يتيح لنا رسم الأرضيات والعشب والمنصات مباشرة فوق المشهد؟",
                "options": [
                    "Sprite Renderer / مظهر المجسمات",
                    "Tilemap / خارطة البلاطات",
                    "Rigidbody 2D / الجسيم الفيزيائي",
                    "Cinemachine virtual camera / الكاميرا الافتراضية"
                ],
                "correct": 1,
                "explanation": "Correct! Tilemaps let you paint levels using blocks from your Tile Palette onto a grid canvas. / صحيح! خارطة البلاطات Tilemap هي الشبكة التي نرسم عليها تضاريس اللعبة!"
            },
            {
                "id": 2,
                "question": "Which Input method captures horizontal arrow keys or 'A/D' signals to move a player left/right? / ما هي الدالة البرمجية المستخدمة لرصد ضغط أزرار الاتجاهات الأفقية أو أزرار A/D لتحريك اللاعب؟",
                "options": [
                    "Input.GetAxis(\"Horizontal\")",
                    "Input.GetKeyDown(KeyCode.Space)",
                    "Input.mousePosition",
                    "Input.touchCount"
                ],
                "correct": 0,
                "explanation": "Excellent! Input.GetAxis('Horizontal') returns a value from -1 to 1 depending on keys pressed. / رائع! دالة GetAxis('Horizontal') ترصد اتجاه حركتنا الأفقية بدقة!"
            },
            {
                "id": 3,
                "question": "Why do we add a BoxCollider2D or CapsuleCollider2D to our player character? / لماذا نضيف كبسولة اصطدام (CapsuleCollider2D) لشخصية اللاعب الثعلب؟",
                "options": [
                    "To draw the player sprite / لرسم صورة اللاعب",
                    "To prevent the player from passing through floor platforms and detect boundaries / لمنع اللاعب من اختراق الأرضيات ولرصد الحدود والاصطدامات",
                    "To play footstep sound loops / لتشغيل أصوات المشي",
                    "To increase player jumping speed / لزيادة سرعة القفز"
                ],
                "correct": 1,
                "explanation": "Perfect! Colliders define the physical boundary shields that stop objects from sinking into floors. / ممتاز! أجهزة الاصطدام هي الدروع غير المرئية التي تجعل اللاعب يقف بثبات على الأرض!"
            },
            {
                "id": 4,
                "question": "Which Rigidbody2D constraint should be turned ON to prevent our platformer player from tipping over and rolling? / أي خيار في جسيم Rigidbody 2D يجب تفعيله لمنع بطلنا الثعلب من الانقلاب والدوران على وجهه؟",
                "options": [
                    "Freeze Position X / تثبيت الموقع الأفقي",
                    "Freeze Rotation Z / تثبيت الدوران Z",
                    "Use Gravity / تفعيل الجاذبية",
                    "Is Trigger / تحويله لمستشعر"
                ],
                "correct": 1,
                "explanation": "Splendid! Freezing the Z rotation locks the player upright so they slide and jump perfectly stable. / مذهل! خيار Freeze Rotation Z يحافظ على توازن الثعلب واقفاً للأبد دون انقلاب!"
            },
            {
                "id": 5,
                "question": "What is Cinemachine Virtual Camera mostly used for in platformer games? / في ماذا نستخدم كاميرات Cinemachine الذكية في ألعاب المغامرات ثنائية الأبعاد؟",
                "options": [
                    "To compile scripts / لترجمة الأكواد",
                    "To automatically follow the player smoothly / لملاحقة الكاميرا للاعب تلقائياً وبأقصى سلاسة وحركة جمالية",
                    "To record gameplay clips / لتسجيل مقاطع لعب تفاعلية",
                    "To change level dimensions / لتعديل أبعاد المستوى"
                ],
                "correct": 1,
                "explanation": "Superb! Cinemachine virtual cameras follow target objects smoothly with beautiful damping controls. / عبقري! كاميرا Cinemachine تضمن بقاء بطلنا في منتصف الشاشة وتلاحقه بسلاسة فائقة!"
            },
            {
                "id": 6,
                "question": "How do we distinguish between touching the ground floor and touching a collectible jewel? / كيف نفرق في الكود بين اصطدام اللاعب بالأرض العادية وبين لمسه لمجوهرة سحرية لجمعها؟",
                "options": [
                    "By looking at their colors / بالنظر لألوان المجسمات",
                    "By comparing their custom Unity Tags (like \"Gem\") / بمقارنة علامات التمييز السحرية الخاصة بها (Tags) مثل علامة Gem",
                    "By calculating camera positions / بحساب موقع الكاميرا",
                    "By running loops / بتشغيل حلقات تكرارية"
                ],
                "correct": 1,
                "explanation": "Perfect! Tags let developers categorize GameObjects so scripts can execute specific logic. / ممتاز! العلامات (Tags) هي الطريقة السحرية لتصنيف الكائنات؛ فنقول: إذا لمسنا 'Gem' اجمعها!"
            },
            {
                "id": 7,
                "question": "What is the standard 'Collect & Destroy' code pattern when a player triggers a gem? / ما هو النمط البرمجي المتبع لجمع المجوهرة وإخفائها من الشاشة عند لمسها؟",
                "options": [
                    "Subtract points and spawn new gem / نطرح نقاطاً ونولد مجوهرة جديدة",
                    "Add 1 to count, play audio, and call Destroy(gem) / نزيد عداد النقاط، نشغل الصوت، ونستدعي دالة تدمير المجوهرة",
                    "End the game immediately / ننهي اللعبة فوراً",
                    "Restart the current level / نعيد تشغيل المستوى الحالي"
                ],
                "correct": 1,
                "explanation": "Bravo! Incrementing score and deleting the triggered asset gives a rewarding collect feedback. / رائع! زيادة العداد متبوعاً بحذف المجوهرة (Destroy) يعطي شعوراً حقيقياً بالجمع والتقاط الكنوز!"
            },
            {
                "id": 8,
                "question": "How do we program a 2D AI enemy frog to patrol back and forth between two platforms? / كيف نبرمج ضفدع العدو ليقوم بدوريات حراسة ويتحرك ذهاباً وإياباً؟",
                "options": [
                    "By changing its gravity / بتغيير جاذبيته الأرضية",
                    "By switching its movement direction variable (Right/Left) once it hits boundaries / بعكس متغير اتجاه الحركة (يمين/يسار) بمجرد وصوله لنقطة الحدود",
                    "By locking its camera focus / بقفل تركيز كاميرا اللعب",
                    "By spawing repeating prefabs / بتوليد أنابيب جديدة"
                ],
                "correct": 1,
                "explanation": "Outstanding! Toggling a boolean variable direction on boundary collisions keeps the AI patrolling smoothly. / ممتاز! عكس اتجاه الحركة عند الحدود يجعل الذكاء الاصطناعي يتحرك في حراسة مستمرة!"
            },
            {
                "id": 9,
                "type": "task",
                "question": "Simple Coding Task: Write a tag comparison check in C# to see if 'other' GameObject has the tag 'Gem'. / مهمة برمجية: اكتب شرط التحقق if للتأكد أن كائن other لديه علامة التمييز 'Gem'!",
                "task_hint": "Write: if (other.gameObject.CompareTag(\"Gem\"))",
                "explanation": "Great! CompareTag() is highly optimized in Unity to compare object categories safely. / أحسنت! دالة CompareTag هي الأسرع والأفضل لمقارنة وتحديد أصناف كائنات يونيتي!"
            },
            {
                "id": 10,
                "type": "task",
                "question": "Movement Task: Write a translation code block to move a sprite along the horizontal X-axis by speed and delta time. / مهمة برمجية: اكتب كود حركة أفقية في المحور X باستخدام سرعة speed وزمن deltaTime!",
                "task_hint": "Write: transform.Translate(Vector3.right * speed * Time.deltaTime);",
                "explanation": "Superb! Multipling movement translations by Time.deltaTime ensures frame-rate independence. / عبقري! ضرب الحركة بـ deltaTime يجعل بطلنا يتحرك بنفس السرعة على كل الحواسيب!"
            }
        ]
    },
    "quiz5.json": {
        "quiz_id": "unity_quiz_5",
        "quiz_title": "Quiz 5: RPG 3D Game Design & Physics",
        "questions": [
            {
                "id": 1,
                "question": "What coordinate axes define a location in a 3D Unity project? / ما هي محاور الإحداثيات الثلاثية التي تحدد موقع الكائنات في فضاء يونيتي ثلاثي الأبعاد؟",
                "options": [
                    "X and Y only / المحور الأفقي والعمودي فقط",
                    "X, Y, and Z axes / المحور الأفقي X، المحور الرأسي Y، ومحور العمق Z",
                    "Z and W axes / محاور العمق والبعد الرابع",
                    "Horizontal axis only / المحور الأفقي فقط"
                ],
                "correct": 1,
                "explanation": "Correct! 3D space introduces the Z-axis representing depth, alongside width (X) and height (Y). / صحيح! الفضاء ثلاثي الأبعاد يضيف محور العمق Z بجانب العرض X والارتفاع Y!"
            },
            {
                "id": 2,
                "question": "What is the difference between a Texture and a Material in 3D game design? / ما هو الفرق الأساسي بين التكستشر (Texture) والماتريال (Material) في ألعاب 3D؟",
                "options": [
                    "Texture is the raw 2D image; Material is the wrapper setting light, shine, and color reflections / التكستشر هي الصورة المسطحة، والماتريال هي الغلاف الذكي الذي يحدد اللمعان والانعكاس والألوان",
                    "Material is a script; Texture is an audio / الماتريال هي كود والتكستشر هي صوت",
                    "They are identical / لا يوجد فرق بينهما على الإطلاق",
                    "Texture is a physics collider / التكستشر هي درع اصطدام فيزيائي"
                ],
                "correct": 0,
                "explanation": "Excellent! Materials act as fabrics wrapping 3D models, utilizing textures to determine visual look. / رائع! الماتريال هي بمثابة المادة البرمجية التي تكسو المجسمات وتحدد مدى لمعانها وانعكاس الضوء عليها!"
            },
            {
                "id": 3,
                "question": "Why do we use a CapsuleCollider instead of a complex MeshCollider for our moving 3D player? / لماذا نفضل استخدام كبسولة اصطدام بسيطة (CapsuleCollider) لشخصيتنا بدلاً من دروع MeshCollider المعقدة؟",
                "options": [
                    "To draw player face details / لرسم تفاصيل وجه اللاعب",
                    "Mesh colliders are extremely slow to calculate, while capsule colliders are fast and slip over steps / لأن حسابات كبسولة الاصطدام سريعة جداً وتسهل صعود السلالم، عكس Mesh المعقدة والبطيئة",
                    "Capsule colliders can play audio / لأن الكبسولة تشغل الأصوات الحماسية",
                    "Capsule colliders contain C# variables / لأن الكبسولات تحتوي على متغيرات"
                ],
                "correct": 1,
                "explanation": "Perfect! Simplified primitives like CapsuleCollider speed up collision calculations immensely in real-time. / ممتاز! استخدام الأشكال البسيطة كالكبسولة يمنع اللعبة من البطء والتعليق ويسهل حركة البطل!"
            },
            {
                "id": 4,
                "question": "What is the benefit of the Character Controller component compared to a standard Rigidbody in 3D? / ما هي الفائدة القصوى لاستخدام متحكم الشخصية (Character Controller) بدلاً من Rigidbody في ألعاب 3D؟",
                "options": [
                    "It automatically applies high graphics / يحسن جودة الرسوميات تلقائياً",
                    "It offers custom, fluid 3rd-person movement controls that ignore raw rigid physics and climb steps smoothly / يوفر حركة مخصصة وسلسة من منظور الشخص الثالث مع صعود الدرج تلقائياً وتجاوز الفيزياء الصعبة",
                    "It writes scripts for you / يقوم بكتابة الأكواد بالنيابة عنك",
                    "It plays particle effects / يطلق تأثيرات انفجارية"
                ],
                "correct": 1,
                "explanation": "Splendid! Character Controller gives developers complete direct command over movements without fighting physical forces. / مذهل! يمنح متحكم الشخصية المطورين قيادة مباشرة لحركة اللاعب دون التعارض مع قوانين الفيزياء المعقدة!"
            },
            {
                "id": 5,
                "question": "How do we simulate gravity on a Character Controller? / كيف نقوم ببرمجة ومحاكاة الجاذبية الأرضية عند استخدام متحكم الشخصية في الكود؟",
                "options": [
                    "By scaling the character / بتكبير حجم البطل",
                    "By continuously decreasing the Y velocity over time and calling controller.Move() / بالتقليل المستمر لقيمة السرعة الرأسية Y باستمرار وتمريرها لأمر الحركة controller.Move",
                    "By changing player animations / بتغيير الحركات التعبيرية",
                    "It works automatically / الجاذبية تعمل تلقائياً بدون كود"
                ],
                "correct": 1,
                "explanation": "Superb! We must manually calculate downward gravity acceleration and apply it via controller.Move() on every frame. / عبقري! يجب حساب تسارع الجاذبية يدوياً في الكود وتطبيق السحب للأسفل بشكل مستمر وسلس!"
            },
            {
                "id": 6,
                "question": "Why is it important to normalize movement input vectors (Vector3.Normalize) in 3D? / لماذا يُعد معايرة متجهات الحركة (Normalization) أمراً بالغ الأهمية في الألعاب ثلاثية الأبعاد؟",
                "options": [
                    "To prevent characters from running twice as fast when moving diagonally / لمنع البطل من الجري بسرعة مضاعفة عند المشي بزاوية مائلة أو قطرية",
                    "To change player health / لتغيير طاقة وصحة اللاعب",
                    "To activate camera rotation / لتفعيل دوران الكاميرا",
                    "To import textures / لاستيراد صور وتكستشرز جديدة"
                ],
                "correct": 0,
                "explanation": "Outstanding! Normalization sets the vector length to 1, ensuring diagonal movement speed matches axial speed. / ممتاز! المعايرة تضبط طول ناقل الحركة ليكون 1، مما يمنع زيادة سرعة البطل عند الجري المائل!"
            },
            {
                "id": 7,
                "question": "What is a Blend Tree in Unity Animator? / ما هو منظم التمازج (Blend Tree) السحري في لوحة الحركة والأنيميتور بيونيتي؟",
                "options": [
                    "A tool to grow trees in level / أداة لزراعة الغابات الكثيفة",
                    "An animator state that smoothly blends multiple animations (like Idle, Walk, and Run) based on speed / حالة أنيميشن تمزج وتدمج بين عدة حركات (الوقوف، المشي، الجري) بسلاسة فائقة حسب السرعة",
                    "A variable storing scores / متغير برمي لحساب مجموع النقاط",
                    "A physics collider / درع اصطدام فيزيائي"
                ],
                "correct": 1,
                "explanation": "Bravo! Blend Trees use speed float parameters to seamlessly blend from slow walks to full sprint cycles. / رائع! يمزج منظم التمازج بين المشي والجري تلقائياً وبأقصى واقعية بناءً على سرعة البطل الحالية!"
            },
            {
                "id": 8,
                "question": "What is NavMesh pathfinding, and what does 'Baking' a navigation mesh mean? / ما هو نظام الملاحة NavMesh، وماذا يعني 'خبز خريطة الملاحة' (Baking)؟",
                "options": [
                    "Baking is heating up the PC / الخبز هو تسخين الحاسوب ليعمل بسرعة",
                    "Baking calculates walkable and obstacle areas on the map, generating a secret navigation grid for AI agents / الخبز هو حساب وتحديد المناطق الصالحة للمشي والعوائق لبناء شبكة تنقل سرية للذكاء الاصطناعي",
                    "A script to play spatial music / كود لتشغيل الموسيقى الحية",
                    "A 3D character controller / متحكم حركة ثلاثي الأبعاد"
                ],
                "correct": 1,
                "explanation": "Outstanding! Baking pre-calculates the walkable level geometry so AI agents can navigate paths without hitting obstacles. / ممتاز! عملية الخبز pre-calculates ترسم خريطة الممرات الآمنة للذكاء الاصطناعي ليتفادى الصخور والجدران!"
            },
            {
                "id": 9,
                "type": "task",
                "question": "Simple Coding Task: Write a C# command to set a NavMeshAgent (named 'agent') target destination to player's position. / مهمة برمجية: اكتب أمراً برمجياً يوجه وكيل الملاحة 'agent' نحو موقع اللاعب player.position!",
                "task_hint": "Write: agent.SetDestination(player.position);",
                "explanation": "Perfect! SetDestination updates the pathfinding calculations live to chase target coordinates. / مذهل! دالة SetDestination تجعل الذكاء الاصطناعي يطارد البطل باستمرار أينما ذهب!"
            },
            {
                "id": 10,
                "type": "task",
                "question": "Physics Task: Write a C# script declaration referencing a Character Controller named 'myController'. / مهمة برمجية: أعلن عن متغير مرجعي من نوع CharacterController باسم 'myController'!",
                "task_hint": "Write: CharacterController myController;",
                "explanation": "Superb! Strongly-typed variables allow us to store and manipulate controller movements on update ticks. / عبقري! الإعلان عن myController يتيح لنا استدعاء وظائف الحركة والجاذبية في كل إطار!"
            }
        ]
    },
    "quiz6.json": {
        "quiz_id": "unity_quiz_6",
        "quiz_title": "Quiz 6: RPG 3D Combat, Audio & Publishing",
        "questions": [
            {
                "id": 1,
                "question": "What is the key difference between the 'Awake' and 'Start' event lifecycle methods in Unity? / ما هو الفرق الزمني والمفهومي الجوهري بين دالتي Awake و Start في دورة حياة كائنات يونيتي؟",
                "options": [
                    "Awake is called once during loading, even if the script component is disabled, while Start is called right before the first frame update / دالة Awake تفعل فوراً أثناء التحميل حتى وإن كان السكربت معطلاً، بينما Start تفعل مباشرة قبل أول إطار حركة",
                    "Start is faster than Awake / دالة Start أسرع وأسبق من Awake",
                    "Awake is only for audio files / دالة Awake مخصصة للمؤثرات الصوتية فقط",
                    "There is no difference / لا يوجد أي فرق بينهما"
                ],
                "correct": 0,
                "explanation": "Correct! Awake is ideal for initializing references, while Start handles game setup actions once the script is active. / صحيح! دالة Awake هي الأسبق وتستخدم لتجهيز التروس والربط، وتليها دالة Start لبدء الأفعال!"
            },
            {
                "id": 2,
                "question": "What is a 'static' variable in C# programming? / ما هو المتغير الساكن أو المشترك (static variable) في لغة C#؟",
                "options": [
                    "A variable that changes color / متغير يقوم بتغيير ألوان اللعبة",
                    "A shared variable that belongs to the Class itself, meaning all object instances share the exact same value / متغير مشترك ينتمي للفئة نفسها، مما يعني أن جميع الكائنات تشترك وتتحكم في نفس القيمة الموحدة",
                    "A variable that cannot be read / متغير سري لا يمكن قراءته",
                    "A physics collider / درع اصطدام فيزيائي"
                ],
                "correct": 1,
                "explanation": "Excellent! Static fields are class-level, making them great for global settings like HighScores or shared damages. / رائع! المتغيرات المشتركة static تسهل الوصول للقيم العامة من أي مكان مثل نقاط النصر أو قوة الضربات!"
            },
            {
                "id": 3,
                "question": "How do we code hit registers so our hero's sword inflicts damage on enemies? / كيف نقوم ببرمجة ضربات السيف لرصد إصابة الأعداء وإنقاص صحتهم؟",
                "options": [
                    "By using Trigger Colliders on the sword and calling the enemy's TakeDamage() method on collision / بوضع مناطق تصادم (Trigger) على السيف واستدعاء دالة TakeDamage للعدو عند لمسه",
                    "By restarting the game / بإعادة تشغيل اللعبة بأكملها",
                    "By changing materials dynamically / بتعديل ألوان الماتريال",
                    "By deleting audio sources / بحذف مكبرات الصوت"
                ],
                "correct": 0,
                "explanation": "Perfect! When the sword collider triggers the enemy tag, invoking their custom health method depletes their HP. / ممتاز! عندما يلمس درع السيف العدو، نستدعي دالة الخصم TakeDamage لإنقاص عداد صحته بصورة تفاعلية!"
            },
            {
                "id": 4,
                "question": "What is the difference between Screen Space and World Space Canvas in Unity UI design? / ما هو الفرق الأساسي بين واجهات الشاشة (Screen Space) والواجهات العائمة (World Space Canvas)؟",
                "options": [
                    "Screen Space canvas is flat on your screen; World Space canvas floats in the 3D game level (like a signpost over an enemy) / واجهات الشاشة مسطحة تماماً أمام عين اللاعب، والواجهات العائمة تطفو وتتحرك داخل الفراغ ثلاثي الأبعاد فوق رأس الشخصية",
                    "Screen Space is in Arabic, World Space is in English / واجهات الشاشة بالعربية والواجهات العائمة بالإنجليزية",
                    "World Space canvas is only for textures / الواجهات العائمة مخصصة للصور فقط",
                    "They are exactly the same / هما متطابقان تماماً"
                ],
                "correct": 0,
                "explanation": "Splendid! World Space canvases let developers construct floating UI indicators (like health bars) that follow 3D GameObjects. / مذهل! الواجهات العائمة (World Space) تتيح لنا تزيين اللعبة بأشرطة صحة مبهرة تطفو وتتحرك فوق رؤوس الأبطال والوحوش!"
            },
            {
                "id": 5,
                "question": "Which Unity UI component is best suited to display health bars visually? / ما هو أفضل مكون واجهة مستخدم (UI) في يونيتي لتمثيل وعرض أشرطة الصحة والطاقة؟",
                "options": [
                    "Text element / عنصر النص",
                    "Slider component / مكون شريط التمرير (Slider)",
                    "Button component / الأزرار التفاعلية",
                    "Audio Listener / مستمع الأصوات"
                ],
                "correct": 1,
                "explanation": "Superb! A UI Slider can be locked to min/max health values and shrinks visually when damage is applied. / عبقري! منزلق التمرير (Slider) مثالي؛ فهو يقل ويكبر تلقائياً ليمثل منسوب الحياة المتبقي للأبطال!"
            },
            {
                "id": 6,
                "question": "What is the difference between an AudioSource and an AudioListener in Unity? / ما هو الفرق الهندسي والبرمي بين مصدر الصوت (AudioSource) ومستمع الصوت (AudioListener)؟",
                "options": [
                    "AudioSource is the speaker playing sounds; AudioListener is the virtual ear (usually on the camera) that hears them / مصدر الصوت هو مكبر الصوت الذي يطلق الأصوات، والمستمع هو الأذن الافتراضية (توضع على الكاميرا) لترصد الترددات",
                    "AudioListener is a microphone / المستمع هو ميكروفون لتسجيل الصوت",
                    "AudioSource makes objects jump / المصدر يجعل المجسمات تقفز",
                    "They do the same thing / هما يقومان بنفس العمل تماماً"
                ],
                "correct": 0,
                "explanation": "Outstanding! AudioSources play the sound assets, while the single AudioListener acts as the player's microphone ears. / ممتاز! المصدر هو الراديو الذي يغني، والمستمع هو أذن بطلنا الذكي التي تلتقط الأنغام ثلاثية الأبعاد بوضوح!"
            },
            {
                "id": 7,
                "question": "What is the primary benefit of compiling your final game as a 'WebGL' build? / ما هي الفائدة العظمى والأكثر تميزاً لتصدير لعبتك النهائية كنسخة ويب (WebGL)؟",
                "options": [
                    "It doubles the PC processing power / يضاعف سرعة تشغيل الحاسوب",
                    "It converts the game into HTML5 so players can play it instantly inside any web browser via a simple link / يحول اللعبة بالكامل لتعمل داخل المتصفحات كرابط سحري تفاعلي بدون الحاجة لتحميل وتسطيب برامج معقدة",
                    "It deletes all enemy AI paths / يقوم بحذف شبكات ذكاء الأعداء",
                    "It removes sounds to save disk space / يحذف الأصوات لتوفير المساحة"
                ],
                "correct": 1,
                "explanation": "Superb! WebGL compiles games into light scripts that render directly on standard browsers, making sharing effortless. / عبقري! تصدير الويب WebGL يحول لعبتك لصفحة ويب تفاعلية تفتح بلمسة واحدة من الهواتف والحواسيب!"
            },
            {
                "id": 8,
                "question": "What is Itch.io in the game developer community? / ما هي منصة Itch.io الشهيرة في أوساط صانعي ومطوري الألعاب؟",
                "options": [
                    "A platform to publish independent games, host WebGL builds, and share creations with the world / موقع عالمي لنشر ألعاب المطورين المستقلين، استضافة ألعاب الويب، واستعراض الإبداعات للجمهور مجاناً",
                    "A tool to fix coding errors / أداة برمجية لإصلاح عيوب الأكواد",
                    "An editor to design textures / برنامج لتلوين وتكستشرز المجسمات",
                    "A programming language / لغة برمجية جديدة"
                ],
                "correct": 0,
                "explanation": "Bravo! Itch.io is the absolute best portal for independent creators to upload, test, and host their custom creations. / رائع! منصة Itch.io هي شاشة العرض العالمية لنشر ألعابك وتلقي تصفيق وتشجيع زملائك المبرمجين الأبطال!"
            },
            {
                "id": 9,
                "type": "task",
                "question": "Simple Coding Task: Write a C# void statement that quits and shuts down the final game application. / مهمة برمجية: اكتب سطراً برمجياً بلغة C# لإغلاق وإنهاء تطبيق اللعبة النهائية بالكامل!",
                "task_hint": "Write: Application.Quit();",
                "explanation": "Outstanding! Application.Quit() exits the compiled standalone application smoothly in play mode. / ممتاز! أمر Application.Quit يغلق اللعبة تماماً عند البناء والتصدير النهائي لراحة اللاعبين!"
            },
            {
                "id": 10,
                "type": "task",
                "question": "Awake vs Start Task: Which method is called first when a script starts up, Awake or Start? Type the name of the method. / مهمة سريعة: أي دالة تعمل أولاً وتسبق الأخرى عند بدء السكربت، Awake أم Start؟ اكتب اسم الدالة فقط!",
                "task_hint": "Type: Awake",
                "explanation": "Awesome! Awake is ALWAYS called before Start, making it the supreme choice for initial component hookups. / أحسنت! دالة Awake تعمل دوماً قبل Start لضمان ترابط أجهزة اللعبة قبل بدء المغامرة!"
            }
        ]
    }
}

# Write each quiz to file
for filename, quiz_content in quizzes_data.items():
    file_path = os.path.join(quizzes_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(quiz_content, f, ensure_ascii=False, indent=2)
    print(f"Successfully generated {filename} with bilingual questions!")

print("All 6 Unity quizzes generated successfully!")
