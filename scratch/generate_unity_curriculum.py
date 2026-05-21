import json
import os

recap_path = r"c:\Users\rowan\Desktop\ev\evaluate\database\senior_unity\recap.json"
games_path = r"c:\Users\rowan\Desktop\ev\evaluate\database\senior_unity\games.json"

# Define the 24 sessions details
sessions_data = [
    {
        "id": 1,
        "badge_icon": "🕹️",
        "badge_title": "Unity Beginner Medal",
        "title_en": "Session 1: Introduction to Games & Unity",
        "title_ar": "الحصة 1: مقدمة الألعاب ومحرك يونيتي السحري",
        "desc_en": "Introduction to game components, why Unity, C# intro, and Unity hub setup.",
        "desc_ar": "مقدمة لمكونات الألعاب، لماذا نختار يونيتي، لمحة عن لغة C# وإعداد البرنامج.",
        "story_ar": """<h3>👋 مرحباً بك يا بطل المستقبل في عالم يونيتي السحري!</h3>اليوم سنبدأ رحلة تصميم الألعاب الاحترافية! سنتعلم كيف يعمل محرك الألعاب <b>Unity</b> وكيف يقوم المبرمجون بصنع ألعابهم المفضلة.<br><br><b>🎯 المبادئ الأساسية التي سنتعلمها اليوم:</b><ul><li>🕹️ <b>مكونات اللعبة (Game Components):</b> اللاعب، محرك اللعبة، وصانع اللعبة.</li><li>💻 <b>لغة C# (سي شارب):</b> اللغة السحرية التي نستخدمها لإعطاء أوامر ليونيتي.</li><li>⚙️ <b>إعداد محرك يونيتي (Setup Unity):</b> كيف نفتح أول مشروع ثنائي الأبعاد (2D) وثلاثي الأبعاد (3D).</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> إنشاء أول مشروع وتحديد القالب السحري (Template)!</div><br><h4>💻 نموذج كود سي شارب السحري (C# Template):</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
// أول سكربت في عالم يونيتي للأبطال!
public class MyFirstGame : MonoBehaviour {
    void Start() {
        Debug.Log("مرحباً بك يا بطل في عالم يونيتي!");
    }
}</code></pre><br><p>دعنا نشغل الكود التالي لتفعيل محطة المغامرة الأولى! 🌟🚀</p>""",
        "story_en": """<h3>👋 Welcome, future legend, to the magic of Unity!</h3>Today we embark on an epic journey to design professional games! We will learn how <b>Unity</b> works and how game developers build our favorite digital worlds.<br><br><b>🎯 Core Concepts We'll Master Today:</b><ul><li>🕹️ <b>Game Components:</b> Player, Game Engine, and Game Creator roles.</li><li>💻 <b>C# Introduction:</b> The magic language we use to code behaviors in Unity.</li><li>⚙️ <b>Setup Unity:</b> Installing Unity Hub and choosing 2D or 3D templates.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Setting up your very first Unity template!</div><br><h4>💻 C# Magic Starter Code:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class MyFirstGame : MonoBehaviour {
    void Start() {
        Debug.Log("Welcome to the Unity universe, Hero!");
    }
}</code></pre><br><p>Let's run the validator script below to activate this amazing station! 🌟🚀</p>""",
        "simple_en": "Imagine that Unity is like a digital LEGO box where you can build anything, and C# is the magic spell that makes your toys come to life!",
        "simple_ar": "تخيل أن محرك يونيتي هو مثل صندوق ليغو رقمي عملاق تبني فيه ما تشاء، ولغة السي شارب هي العصا السحرية التي تجعل المكعبات تتحرك وتتكلم!",
        "hint_en": "Type: <code>print('Unity initialized successfully!')</code> and hit Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Unity initialized successfully!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact message: <code>Unity initialized successfully!</code>",
        "challenge_ar": "اطبع العبارة التالية تماماً: <code>Unity initialized successfully!</code>",
        "starter_code": "# اكتب كود تفعيل محرك يونيتي الأول هنا يا بطل:\n",
        "pills": [
            {
                "label": "تفعيل يونيتي / Activate Unity",
                "code": "print('Unity initialized successfully!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Unity initialized successfully!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: إعداد مشروع يونيتي",
        "homework_title_en": "🏠 Magic Home Challenge: Unity Project Architect",
        "homework_desc_ar": "يا بطل! قم بمحاكاة تفعيل مشروع يونيتي جديد باسم 'MySuperGame' في الكود بالأسفل وطباعة رسالة نجاح الإعداد!",
        "homework_desc_en": "Awesome work! Simulate launching a new Unity project named 'MySuperGame' and print a setup success message using Python!",
        "homework_starter_code": "# تحدي المنزل: اكتب محاكاة إعداد مشروع MySuperGame واطبع تم الإعداد بنجاح!\n"
    },
    {
        "id": 2,
        "badge_icon": "🖥️",
        "badge_title": "Interface Explorer Medal",
        "title_en": "Session 2: Unity Interface & Asset Store",
        "title_ar": "الحصة 2: واجهة يونيتي السحرية ومتجر الأصول",
        "desc_en": "Exploring Hierarchy, Project, Console, Scene & Game views, and the Asset Store.",
        "desc_ar": "استكشاف النوافذ الأساسية (التسلسل الهرمي، المشروع، الكونسول، المشهد) وطريقة استخدام متجر الأصول.",
        "story_ar": """<h3>🖥️ استكشاف لوحة التحكم السحرية في يونيتي!</h3>لتصميم أروع الألعاب، يجب أن نتعرف على النوافذ السحرية التي يوفرها لنا محرك يونيتي وكيف نتحكم بها.<br><br><b>🎯 النوافذ السحرية الأساسية:</b><ul><li>📂 <b>نافذة التسلسل الهرمي (Hierarchy):</b> التي تحتوي على كل العناصر الموجودة حالياً في اللعبة (كائنات اللعبة).</li><li>📦 <b>نافذة المشروع (Project):</b> التي تشبه الملفات على حاسوبك وبها كل الملفات والأصوات والصور.</li><li>🎮 <b>نافذة المشهد واللعب (Scene & Game Views):</b> حيث نقوم برسم وتحريك وتجربة لعبتنا كأننا لاعبين حقيقيين!</li><li>🏪 <b>متجر أصول يونيتي (Asset Store):</b> المكان السحري الذي نحصل منه على شخصيات ثلاثية الأبعاد ومجسمات جاهزة مجاناً!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> تصميم مشهد بسيط باستخدام مجسمات ثلاثية الأبعاد مجانية من المتجر!</div><br><h4>💻 نموذج كود سي شارب لتأكيد ربط الأصول باللعبة:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class AssetVerifier : MonoBehaviour {
    void Start() {
        Debug.Log("تم استيراد شخصيات متجر الأصول بنجاح! 🦊🌟");
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لاختبار نافذة الكونسول السحرية لدينا! 🌟🚀</p>""",
        "story_en": """<h3>🖥️ Exploring the Unity Control Deck!</h3>To build spectacular games, we must learn the tools of the trade inside the Unity editor interface.<br><br><b>🎯 The Essential Windows:</b><ul><li>📂 <b>Hierarchy Window:</b> Lists all elements (GameObjects) currently active in your scene.</li><li>📦 <b>Project Window:</b> Your folder system containing all graphics, sounds, and scripts.</li><li>🎮 <b>Scene & Game Views:</b> Where you build and play-test your worlds like a real developer!</li><li>🏪 <b>Unity Asset Store:</b> A magic store where you can download free 3D models and character sprites!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Designing your level layout with assets imported from the store!</div><br><h4>💻 C# Asset Checker Code:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class AssetVerifier : MonoBehaviour {
    void Start() {
        Debug.Log("Assets imported from the Store successfully! 🦊🌟");
    }
}</code></pre><br><p>Let's run the code below to test our simulator console! 🌟🚀</p>""",
        "simple_en": "Imagine that the Unity interface is like an artist's canvas: the Hierarchy lists your brushes, the Project window holds your paint tubes, and the Scene view is where you draw your world!",
        "simple_ar": "تخيل أن واجهة يونيتي هي مثل مرسم الفنان: التسلسل الهرمي يضم قائمة فراشيك، ونافذة المشروع تحتوي على أنابيب الألوان، ونافذة المشهد هي اللوحة التي ترسم عليها عالمك المذهل!",
        "hint_en": "Type: <code>print('Console Window Activated!')</code> and hit Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Console Window Activated!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Console Window Activated!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Console Window Activated!</code>",
        "starter_code": "# اكتب كود تفعيل لوحة الكونسول هنا:\n",
        "pills": [
            {
                "label": "تفعيل الكونسول / Activate Console",
                "code": "print('Console Window Activated!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Console Window Activated!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: تصميم واجهة اللعبة",
        "homework_title_en": "🏠 Magic Home Challenge: Scene Layout Simulator",
        "homework_desc_ar": "قم بكتابة كود يعلن عن تفعيل الكائنات الثلاثة الأساسية في مشهدك: 'Player', 'Ground', 'Mascot' باستخدام جمل الطباعة!",
        "homework_desc_en": "Write a script that announces the loading of three essential GameObjects in your scene: 'Player', 'Ground', and 'Mascot' using prints!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود يعلن تحميل الكائنات الثلاثة هنا:\n"
    },
    {
        "id": 3,
        "badge_icon": "🧩",
        "badge_title": "Visual Scripting Badge",
        "title_en": "Session 3: Visual Scripting with Bolt",
        "title_ar": "الحصة 3: البرمجة المرئية السحرية باستخدام Bolt",
        "desc_en": "Introduction to Bolt visual scripting nodes, setup, and flow variables.",
        "desc_ar": "مقدمة لنظام البرمجة المرئية Bolt، توصيل العقد التفاعلية وتوصيل المتغيرات بدون كتابة كود معقد.",
        "story_ar": """<h3>🧩 البرمجة بالبلوكات والخطوط السحرية (Bolt)!</h3>هل تعلم أن بإمكاننا إعطاء أوامر وحل مشكلات برمجية بالكامل دون كتابة أي نص معقد؟ نعم! باستخدام أداة البرمجة المرئية <b>Bolt</b>.<br><br><b>🎯 المبادئ التي سنتعلمها اليوم:</b><ul><li>🔗 <b>عقد البرمجة (Bolt Nodes):</b> كتل برمجية تفاعلية تمثل أوامر ووظائف مختلفة.</li><li>⚙️ <b>آلة التدفق (Flow Machine):</b> المخطط الذي يحتوي على العقد ويوصل بينها بخطوط سحرية ليعمل منطق اللعبة.</li><li>📍 <b>العقد والأحداث (Events & Actions):</b> مثل عقدة البداية (Start Event) وعقدة التحديث (Update Event).</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> توصيل البلوكات البرمجية لجعل شخصيتك تتحرك في شاشة اللعبة!</div><br><h4>💻 كيف يترجم Bolt التدفق البرمجي؟</h4><p>في Bolt، نقوم بتوصيل العقد كالتالي: <br><code>[Update Event] ---> [Translate Node] ---> (Direction: Vector3.right * speed)</code></p><br><p>دعنا نختبر تدفق برمجتنا المرئية بتشغيل محاكاة Bolt في المحاكي السحري بالأسفل! 🌟🚀</p>""",
        "story_en": """<h3>🧩 Visual Scripting with Bolt!</h3>Did you know you can script game behaviors without writing complex code syntax? Yes! With Unity's visual scripting tool called <b>Bolt</b>.<br><br><b>🎯 Core Concepts We'll Master Today:</b><ul><li>🔗 <b>Bolt Nodes:</b> Interactive blocks representing logic functions and arithmetic.</li><li>⚙️ <b>Flow Machine:</b> The main canvas where we connect nodes with visual logic flow lines.</li><li>📍 <b>Events and Actions:</b> Essential event nodes like 'On Start' and 'On Update' that drive your game loops.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Wiring up your very first visual script to move a character!</div><br><h4>💻 How Bolt Visual Flow Works:</h4><p>We connect the flow logic visually: <br><code>[Update Event] ---> [Translate Node] ---> (Direction: Vector3.right * speed)</code></p><br><p>Let's run the script below to verify our visual flow engine! 🌟🚀</p>""",
        "simple_en": "Imagine that Bolt visual scripting is like building a pipeline for water: each node is a pipe section, and the flow line determines which way the water (data and logic) runs!",
        "simple_ar": "تخيل أن برمجة Bolt المرئية هي مثل بناء شبكة أنابيب مياه تفاعلية: كل عقدة هي أنبوب، والخطوط الواصلة بينها تحدد كيف يجري تيار الأفكار والمنطق!",
        "hint_en": "Type: <code>print('Bolt Engine Setup Completed!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Bolt Engine Setup Completed!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Bolt Engine Setup Completed!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Bolt Engine Setup Completed!</code>",
        "starter_code": "# اكتب كود تشغيل محرك Bolt التفاعلي هنا:\n",
        "pills": [
            {
                "label": "تفعيل محرك Bolt / Start Bolt",
                "code": "print('Bolt Engine Setup Completed!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Bolt Engine Setup Completed!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكاة عقد Bolt",
        "homework_title_en": "🏠 Magic Home Challenge: Bolt Flow Architect",
        "homework_desc_ar": "قم بكتابة سكربت يقوم بطباعة اسم الحدث 'On Update Event' ثم طباعة اسم الفعل 'Translate Object' لمحاكاة تدفق برمجة الحركة المرئية!",
        "homework_desc_en": "Write a script that prints 'On Update Event' followed by 'Translate Object' to simulate a basic visual movement flow logic!",
        "homework_starter_code": "# تحدي المنزل: اكتب محاكاة تدفق الحركة التفاعلية هنا:\n"
    },
    {
        "id": 4,
        "badge_icon": "🔄",
        "badge_title": "Rotation Master Medal",
        "title_en": "Session 4: Bolt scripting - Rotating Object",
        "title_ar": "الحصة 4: البرمجة المرئية - تدوير الكواكب والمجسمات",
        "desc_en": "Creating a visual script with Bolt to rotate 3D GameObjects in Unity.",
        "desc_ar": "تصميم أول سكربت مرئي تفاعلي متكامل لتدوير الكائنات والمجسمات ثلاثية الأبعاد بذكاء.",
        "story_ar": """<h3>🔄 تدوير الكائنات السحرية بلمستك الخاصة!</h3>اليوم سنقوم بصنع شيء فائق الروعة: سنقوم ببرمجة مجسم ثلاثي الأبعاد ليدور حول نفسه باستمرار كأننا نصنع كوكباً يدور في الفضاء السحيق!<br><br><b>🎯 المبادئ التفاعلية لدرس اليوم:</b><ul><li>📂 <b>استيراد الأصول (Import Asset):</b> إضافة أشكال ثلاثية الأبعاد جميلة إلى لعبتنا.</li><li>🔄 <b>عقدة الدوران (Rotate Node):</b> عقدة سحرية تأخذ قيم ثلاثية الأبعاد وتطبق دوران مستمر.</li><li>⏱️ <b>الزمن الحقيقي (Time.deltaTime):</b> لضمان أن يدور الكوب بنفس السرعة السلسة على جميع الحواسيب!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> بناء مشهد فضائي وبرمجة كواكب تدور بسرعات متغيرة وجميلة!</div><br><h4>💻 كيف نحدد قيم الدوران في الفضاء ثلاثي الأبعاد؟</h4><p>نستخدم متجه الدوران <b>Vector3</b> لتحديد المحور (X, Y, Z):<br><code>Rotation: Vector3(0, 45f * Time.deltaTime, 0)</code></p><br><p>دعنا نشغل الكود التالي لمحاكاة عملية الدوران بمعدل إطار تلو الآخر! 🌟🚀</p>""",
        "story_en": """<h3>🔄 Spin the World with Your Code!</h3>Today we are building something truly magical: we will script a 3D GameObject to spin continuously around itself, like a mysterious planet orbiting in outer space!<br><br><b>🎯 Interactive Concepts We'll Learn:</b><ul><li>📂 <b>Importing Assets:</b> Bringing cool 3D items into our scene hierarchy.</li><li>🔄 <b>Rotate Node:</b> The specific Bolt node that applies rotation over time.</li><li>⏱️ <b>Time.deltaTime:</b> The magic scale that ensures your objects rotate at the exact same speed on every computer!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Creating a space nebula scene where planets rotate at dynamic speeds!</div><br><h4>💻 Rotation Logic in 3D Space:</h4><p>We configure rotation using a <b>Vector3</b> vector on the Y axis:<br><code>Rotation: Vector3(0, 45f * Time.deltaTime, 0)</code></p><br><p>Let's run the code below to simulate frame-by-frame 3D rotation! 🌟🚀</p>""",
        "simple_en": "Imagine a spinning top: you spin it once and it turns around. In Bolt, we tell Unity to 'flick' the top slightly on every single frame so it never stops spinning!",
        "simple_ar": "تخيل النحلة الدوارة (البلبل): تقوم بتدويرها مرة فتدور حول نفسها. في يونيتي، نحن نأمر اللعبة بنقش المجسم نقشاً خفيفاً in كل إطار لكي يستمر بالدوران دون توقف!",
        "hint_en": "Type: <code>print('Planet Rotating around Y-Axis!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Planet Rotating around Y-Axis!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Planet Rotating around Y-Axis!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Planet Rotating around Y-Axis!</code>",
        "starter_code": "# اكتب كود محاكاة دوران الكوكب ثلاثي الأبعاد هنا:\n",
        "pills": [
            {
                "label": "تدوير الكوكب / Rotate Planet",
                "code": "print('Planet Rotating around Y-Axis!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Planet Rotating around Y-Axis!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: تدوير النجمة السحرية",
        "homework_title_en": "🏠 Magic Home Challenge: Star Rotation Simulator",
        "homework_desc_ar": "قم بكتابة كود يقوم بحساب زاوية الدوران باستخدام حلقة تكرار بسيطة تطبع زاوية الدوران من 10 درجات وتزيد بمقدار 10 حتى تصل لـ 50 درجة تفاعلياً!",
        "homework_desc_en": "Write a script that calculates star rotation step-by-step: print the rotation angle starting from 10 degrees, increasing by 10 in a loop until it reaches 50 degrees!",
        "homework_starter_code": "# تحدي المنزل: اكتب حلقة حساب زوايا الدوران هنا:\n"
    },
    {
        "id": 5,
        "badge_icon": "🐦",
        "badge_title": "Flappy Physics Medal",
        "title_en": "Session 5: Flappy Bird 1: Game Layout & Jump",
        "title_ar": "الحصة 5: لعبة الطائر الغاضب 1: الجاذبية وقفزة الطائر",
        "desc_en": "Setting up Flappy Bird layout and programming the bird jump using Rigidbody2D forces.",
        "desc_ar": "تصميم هيكل لعبة الطائر الغاضب بالكامل، وإعطاء الطائر ميزة القفز والتأثر بالجاذبية الأرضية.",
        "story_ar": """<h3>🐦 مرحباً بك في مشروع لعبة الطائر الغاضب (Flappy Bird) الشهيرة!</h3>هل أنت مستعد لصنع لعبتك المفضلة بنفسك؟ اليوم سنقوم ببناء المشهد التفاعلي الأول للطائر وسنتحكم بقوانين الفيزياء والجاذبية الأرضية لنجعله يطير ويقفز عند الضغط!<br><br><b>🎯 المبادئ الفيزيائية التفاعلية:</b><ul><li>⚖️ <b>الجسيم الفيزيائي (Rigidbody2D):</b> المكون السحري الذي يعطي الطائر وزناً وجاذبية ليسقط للأسفل!</li><li>💥 <b>القوة الفيزيائية (AddForce):</b> دفع الطائر للأعلى بإعطائه دفعة قوة عمودية (Vector2.up).</li><li>🚧 <b>حركة الأنابيب (Translate):</b> جعل الأنابيب تتحرك من اليمين إلى اليسار لتبدو وكأن الطائر يتقدم للأمام!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة قفزة الطائر التفاعلية بالكامل باستخدام البرمجة المرئية!</div><br><h4>💻 كيف نبرمج قفزة الطائر في يونيتي؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>// عند الضغط على زر المسافة (Space)، نضيف قوة تفاعلية للأعلى!
if (Input.GetKeyDown(KeyCode.Space)) {
    GetComponent&lt;Rigidbody2D&gt;().velocity = Vector2.up * jumpForce;
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لمحاكاة دفعة قفزة الطائر الجميلة! 🌟🚀</p>""",
        "story_en": """<h3>🐦 Welcome to the Flappy Bird Odyssey!</h3>Are you ready to program your own version of the legendary Flappy Bird game? Today we lay down the game structure and configure the physics engine to make our bird fly and jump on command!<br><br><b>🎯 Interactive Physics Concepts:</b><ul><li>⚖️ <b>Rigidbody 2D:</b> The core physics component that adds mass and gravity to our bird.</li><li>💥 <b>Add Force / Jump Impulse:</b> Pushing the bird upwards by applying a velocity impulse (Vector2.up).</li><li>🚧 <b>Pipe Translation:</b> Moving obstacle pipes from right to left using Translate to simulate forward flight!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Wiring the bird's jump and gravity mechanics!</div><br><h4>💻 Jump Logic in C# Simulation:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>// When Space key is clicked, add dynamic upward velocity!
if (Input.GetKeyDown(KeyCode.Space)) {
    GetComponent&lt;Rigidbody2D&gt;().velocity = Vector2.up * jumpForce;
}</code></pre><br><p>Let's run the script below to simulate our flappy bird jump! 🌟🚀</p>""",
        "simple_en": "Imagine a paper airplane: if you don't throw it, gravity pulls it down. Pushing the Space key is like giving the paper airplane a little push upward with your hand to keep it flying!",
        "simple_ar": "تخيل طائرة ورقية: إن لم تدفعها للأعلى، ستسحبها الجاذبية وتسقط أرضاً. الضغط على زر المسافة هو بمثابة نفخة هواء سحرية تدفع الطائر للأعلى ليبقى طائراً في الهواء!",
        "hint_en": "Type: <code>print('Flappy Bird Jump Active!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Flappy Bird Jump Active!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Flappy Bird Jump Active!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Flappy Bird Jump Active!</code>",
        "starter_code": "# اكتب كود محاكاة قفزة الطائر التفاعلية هنا:\n",
        "pills": [
            {
                "label": "برمجة القفزة / Trigger Jump",
                "code": "print('Flappy Bird Jump Active!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Flappy Bird Jump Active!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكاة قفزات الطائر المتعددة",
        "homework_title_en": "🏠 Magic Home Challenge: Flappy Flight Log",
        "homework_desc_ar": "قم بكتابة كود يقوم بطباعة قيمة الارتفاع (Y-axis) للطائر وهي تزيد بمقدار 5 أمتار في كل مرة يضغط فيها مسافة حتى تصل لارتفاع 15 متر!",
        "homework_desc_en": "Write a script that tracks flappy bird's height: print the altitude starting from 0, increasing by 5 meters on each jump in a loop, up to 15 meters!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة الارتفاع المتتابع للطائر هنا:\n"
    },
    {
        "id": 6,
        "badge_icon": "🚧",
        "badge_title": "Prefab Spawner Medal",
        "title_en": "Session 6: Flappy Bird 2: Prefabs & Repeating Pipes",
        "title_ar": "الحصة 6: لعبة الطائر الغاضب 2: النماذج الجاهزة وتوليد الأنابيب",
        "desc_en": "Creating dynamic obstacles with Prefabs, spawning repeating pipes, and handling collision destruction.",
        "desc_ar": "تصميم الأنابيب المكررة تلقائياً باستخدام ميزة الـ Prefab السحرية، والتحكم بالاصطدامات لتدمير اللاعب.",
        "story_ar": """<h3>🚧 مصنع الأنابيب اللانهائي وتجنب الاصطدام!</h3>ألعابنا تحتاج إلى عقبات مثيرة! اليوم سنتعلم كيف نصنع أنابيب لا نهائية تظهر أمام الطائر بارتفاعات عشوائية وممتعة، وكيف نجعل اللعبة تنتهي عند اصطدام الطائر بالأنابيب!<br><br><b>🎯 المبادئ البرمجية التفاعلية:</b><ul><li>📦 <b>النماذج الجاهزة (Prefabs):</b> قالب جاهز للأنبوب نقوم بصناعته وتخزينه لنقوم بتكراره ملايين المرات!</li><li>🧬 <b>التوليد التلقائي (Instantiate):</b> استدعاء نسخة جديدة من الأنبوب السحري في أوقات محددة.</li><li>💥 <b>رصد الاصطدام (OnCollisionEnter2D):</b> معرفة متى يلمس الطائر الأنبوب فوراً لإنهاء اللعبة وتدميره!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة مصنع الأنابيب اللانهائي مع الاصطدامات الذكية!</div><br><h4>💻 كيف نبرمج اصطدام الطائر بالأنبوب بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>void OnCollisionEnter2D(Collision2D collision) {
    if (collision.gameObject.CompareTag("Pipe")) {
        Debug.Log("آخ! اصطدم الطائر بالأنبوب.. انتهت اللعبة! 💥☠️");
        Destroy(gameObject); // تدمير الطائر البطل
    }
}</code></pre><br><p>دعنا نشغل الكود التالي لتفعيل مصنع الأنابيب بنجاح! 🌟🚀</p>""",
        "story_en": """<h3>🚧 Infinite Obstacles & Collision Alert!</h3>Our game needs challenges! Today we learn to build an infinite pipe factory that spawns obstacles with randomized heights, and program the game to end instantly when the bird collides with them!<br><br><b>🎯 Interactive Coding Concepts:</b><ul><li>📦 <b>Prefabs:</b> Reusable game blueprints. We design the pipe once and duplicate it infinitely!</li><li>🧬 <b>Instantiate / Spawning:</b> Creating new copies of the pipe prefab dynamically in runtime.</li><li>💥 <b>Collision Detection (OnCollisionEnter 2D):</b> Real-time callback to know when the bird touches a pipe and trigger Game Over!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Coding a fully functional infinite prefab pipe spawner with collision damage!</div><br><h4>💻 C# Collision Handler Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>void OnCollisionEnter2D(Collision2D collision) {
    if (collision.gameObject.CompareTag("Pipe")) {
        Debug.Log("Boom! Bird collided with pipe.. Game Over! 💥☠️");
        Destroy(gameObject); // Destroy player object
    }
}</code></pre><br><p>Let's run the script below to activate our dynamic pipe factory! 🌟🚀</p>""",
        "simple_en": "Imagine a cookie cutter: the cutter is the Prefab, and each cookie stamped out onto the baking tray is a new spawned pipe in our game world!",
        "simple_ar": "تخيل قالب صنع البسكويت: قالب البسكويت هو الـ Prefab، وكل قطعة بسكويت دائرية ومكررة تضعها في الصينية هي أنبوب جديد يولد تلقائياً في لعبتنا الرائعة!",
        "hint_en": "Type: <code>print('Pipes Spawning & Colliders Loaded!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Pipes Spawning & Colliders Loaded!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Pipes Spawning & Colliders Loaded!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Pipes Spawning & Colliders Loaded!</code>",
        "starter_code": "# اكتب كود تفعيل مصنع الأنابيب ورصد الاصطدامات هنا:\n",
        "pills": [
            {
                "label": "تشغيل مصنع الأنابيب / Spawn Pipes",
                "code": "print('Pipes Spawning & Colliders Loaded!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Pipes Spawning & Colliders Loaded!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: عداد توليد الأنابيب التفاعلي",
        "homework_title_en": "🏠 Magic Home Challenge: Pipe Spawner Counter",
        "homework_desc_ar": "اكتب كوداً يحاكي توليد 4 أنابيب متتالية، بحيث يطبع رقم كل أنبوب مضاف في اللعبة مثل: 'Spawning Pipe #1', 'Spawning Pipe #2' وهكذا!",
        "homework_desc_en": "Write a script that simulates spawning 4 consecutive pipes: print 'Spawning Pipe #1', 'Spawning Pipe #2' up to pipe #4 using a loop!",
        "homework_starter_code": "# تحدي المنزل: اكتب محاكاة عداد توليد الأنابيب هنا:\n"
    },
    {
        "id": 7,
        "badge_icon": "🎬",
        "badge_title": "Scene Navigator Medal",
        "title_en": "Session 7: Flappy Bird 3: Scenes & UI Toolkit",
        "title_ar": "الحصة 7: لعبة الطائر الغاضب 3: الشاشات المتعددة وأدوات الواجهة UI",
        "desc_en": "Creating game scenes (start, end), introducing UI Toolkit buttons, and scripting scene transitions.",
        "desc_ar": "تصميم الشاشات المتعددة (شاشة البداية، شاشة النهاية)، تفعيل الأزرار والواجهات التفاعلية، والانتقال السلس بين الشاشات.",
        "story_ar": """<h3>🎬 تنظيم شاشات اللعبة والقوائم التفاعلية!</h3>ألعابنا الاحترافية لا تبدأ فوراً، بل يجب أن يكون لها شاشة بداية جميلة بها زر (ابدأ اللعب) وشاشة نهاية مبهجة عندما يخسر اللاعب!<br><br><b>🎯 المبادئ البرمجية لدرس اليوم:</b><ul><li>🎬 <b>إدارة الشاشات (Scenes):</b> تقسيم اللعبة إلى مشاهد مستقلة (شاشة البداية، شاشة اللعب، شاشة النهاية).</li><li>🔘 <b>أدوات الواجهة (UI Toolkit):</b> تصميم أزرار تفاعلية ونصوص ملونة مبهرة للأطفال.</li><li>🔄 <b>الانتقال بين الشاشات (SceneManager):</b> كتابة أوامر سحرية للانتقال فوراً عند الضغط على الأزرار!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> ربط القوائم التفاعلية والأزرار وتسهيل انتقال اللاعب بين شاشات اللعبة!</div><br><h4>💻 كيف نبرمج الانتقال إلى شاشة اللعب عند ضغط زر بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using UnityEngine.SceneManagement; // المكتبة السحرية للتحكم بالشاشات!

public class MainMenu : MonoBehaviour {
    public void StartGame() {
        SceneManager.LoadScene("GameScene"); // انتقال سحري فوراً!
    }
}</code></pre><br><p>دعنا نختبر الانتقال التفاعلي للشاشات بتشغيل الكود بالأسفل! 🌟🚀</p>""",
        "story_en": """<h3>🎬 Shaping Scenes & Interactive UI!</h3>Professional games don't just dump you in the action! They start with beautiful main menus and transition smoothly to gameover screens. Today we construct this workflow using the UI Toolkit!<br><br><b>🎯 Core Screen Concepts:</b><ul><li>🎬 <b>Scenes:</b> Designing independent worlds for your menus, gameplay, and gameover slides.</li><li>🔘 <b>UI Toolkit:</b> Building clickable buttons and vibrant graphic layouts.</li><li>🔄 <b>Scene Management (SceneManager):</b> Scripting fast transitions when the player clicks 'Start Game' or 'Try Again'!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Creating a full start menu and linking interactive buttons!</div><br><h4>💻 C# Scene Loading Logic:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using UnityEngine.SceneManagement;

public class MainMenu : MonoBehaviour {
    public void StartGame() {
        SceneManager.LoadScene("GameScene"); // Super fast loading!
    }
}</code></pre><br><p>Let's verify our scene manager configuration by running the code below! 🌟🚀</p>""",
        "simple_en": "Imagine a storybook: scenes are the pages. When you click the 'Start' button, it's like turning from the cover page to page 1 to start reading!",
        "simple_ar": "تخيل كتاب قصص تفاعلي: الشاشات أو المشاهد هي الصفحات. عندما تضغط على زر 'ابدأ'، فكأنك تقلب الغلاف لتدخل إلى الصفحة الأولى لتبدأ المغامرة السعيدة!",
        "hint_en": "Type: <code>print('Switching to GameScene...')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Switching to GameScene...')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Switching to GameScene...</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Switching to GameScene...</code>",
        "starter_code": "# اكتب كود محاكاة الانتقال إلى شاشة اللعب هنا:\n",
        "pills": [
            {
                "label": "الانتقال للمشهد / Load GameScene",
                "code": "print('Switching to GameScene...')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Switching to GameScene...",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: نظام انتقالات القائمة الكامل",
        "homework_title_en": "🏠 Magic Home Challenge: Menu Switch Log",
        "homework_desc_ar": "اكتب كوداً يحاكي تنقل اللاعب: اطبع أولاً 'Loading StartMenu...'، ثم 'Button Clicked!', ثم 'Loading GameScene!' لتجسيد العملية البرمجية بالكامل!",
        "homework_desc_en": "Write a script that simulates a complete transition log: print 'Loading StartMenu...', then 'Button Clicked!', and finally 'Loading GameScene!'!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة انتقالات الشاشة هنا:\n"
    },
    {
        "id": 8,
        "badge_icon": "🏆",
        "badge_title": "Game Publisher Medal",
        "title_en": "Session 8: Flappy Bird 4: Score & Game Build",
        "title_ar": "الحصة 8: لعبة الطائر الغاضب 4: حساب النقاط وبناء اللعبة النهائية",
        "desc_en": "Using triggers to score points, displaying points on UI text, and exporting the final desktop game build.",
        "desc_ar": "برمجة مناطق العبور الذكية لاحتساب النقاط، عرض مجموع النقاط على الشاشة، وتصدير اللعبة كملف تنفيذي (.exe).",
        "story_ar": """<h3>🏆 احتساب النقاط وبناء اللعبة النهائية للاستعراض!</h3>اليوم هو حفل التخرج للمشروع الأول! سنتعلم كيف نزيد النقاط تفاعلياً عندما يمر الطائر بسلام من بين الأنابيب، وسنقوم ببناء وتصدير اللعبة كبرنامج حقيقي لترسله لأصدقائك وتدهشهم بذكائك الفائق!<br><br><b>🎯 المبادئ الذهبية التي سنتعلمها اليوم:</b><ul><li>🎯 <b>منطقة العبور الحساسة (Is Trigger):</b> منطقة تصادم وهمية في الأنابيب لا تمنع حركة الطائر، لكنها تحتسب نقطة بمجرد لمسها!</li><li>📝 <b>متغيرات العداد (Variables Get & Set):</b> لتخزين وزيادة النقاط وعرضها تلقائياً.</li><li>🏗️ <b>بناء وتصدير اللعبة (Build Game):</b> تحويل المشروع بالكامل إلى برنامج سطح مكتب (.exe) أو صفحة ويب تفاعلية!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة عداد النقاط بالكامل وتصدير لعبتك Flappy Bird كنسخة حقيقية قابلة للعب!</div><br><h4>💻 كيف نبرمج زيادة النقاط عند عبور الأنبوب بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>void OnTriggerEnter2D(Collider2D other) {
    if (other.gameObject.CompareTag("Player")) {
        score += 1;
        scoreText.text = "Score: " + score; // تحديث واجهة المستخدم!
        Debug.Log("رائع! أحسنت يا بطل، النقاط الحالية: " + score);
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لنحاكي تجميع النقاط ونعلن انتصارنا الأكاديمي! 🌟🚀</p>""",
        "story_en": """<h3>🏆 Scoring Points & Final Game Build Export!</h3>Today is the graduation party of our first big project! We will program dynamic score counting whenever the bird glides safely between the pipes, and export the entire game into a standalone app to share with your friends and family!<br><br><b>🎯 Golden Game Concepts:</b><ul><li>🎯 <b>Is Trigger Colliders:</b> Phantom sensors inside pipes that trigger a point increment instead of blocking flight!</li><li>📝 <b>Variables (Get & Set):</b> Modifying data stores to keep track of current score and output onto the game screen.</li><li>🏗️ <b>Build Game (.exe):</b> Compiling your game assets and scripts into a playable desktop application!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Integrating the score counter system and exporting your Flappy Bird masterpiece!</div><br><h4>💻 C# Point Trigger Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>void OnTriggerEnter2D(Collider2D other) {
    if (other.gameObject.CompareTag("Player")) {
        score += 1;
        scoreText.text = "Score: " + score;
        Debug.Log("Bravo! Point earned. Current score: " + score);
    }
}</code></pre><br><p>Let's run the script below to simulate adding a point and compiling our project! 🌟🚀</p>""",
        "simple_en": "Imagine a soccer goal line: when the ball crosses the line, a sensor rings to declare a Goal! Is Trigger is exactly that line, and score is the referee's board showing points!",
        "simple_ar": "تخيل خط مرمى كرة القدم: عندما تعبر الكرة هذا الخط، يرن جرس سحري ليعلن عن هدف! منطقة (Is Trigger) هي ذلك الخط السري، والمتغير (Score) هو لوحة الملعب التي تظهر النتيجة للأبطال!",
        "hint_en": "Type: <code>print('Flappy Bird Game Build Successful!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Flappy Bird Game Build Successful!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Flappy Bird Game Build Successful!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Flappy Bird Game Build Successful!</code>",
        "starter_code": "# اكتب كود محاكاة تصدير وبناء اللعبة النهائية هنا:\n",
        "pills": [
            {
                "label": "بناء وتصدير اللعبة / Build Game",
                "code": "print('Flappy Bird Game Build Successful!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Flappy Bird Game Build Successful!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: عداد تجميع الجواهر والذهب",
        "homework_title_en": "🏠 Magic Home Challenge: Gem Collection Simulator",
        "homework_desc_ar": "قم بكتابة كود يعلن بدء اللعبة بنقاط صفر، ثم يزيد النقاط بمقدار 1 مع كل حلقة تكرار للمحاكاة حتى يصل لـ 3 نقاط كاملة تفاعلياً!",
        "homework_desc_en": "Write a script that starts with score 0, and increments score by 1 in each loop cycle, printing 'Score: X' until it reaches 3 points!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود زيادة مجموع النقاط التراكمي هنا:\n"
    },
    {
        "id": 9,
        "badge_icon": "💻",
        "badge_title": "C# Coder Badge",
        "title_en": "Session 9: Introduction to C# & First Project",
        "title_ar": "الحصة 9: مدخل إلى لغة C# وكتابة برنامجنا الأول",
        "desc_en": "Introducing C# syntax, writing output, reading user inputs, and adding comments.",
        "desc_ar": "التعرف على بناء جمل لغة C#، طباعة المخرجات على الشاشة، استقبال مدخلات المستخدم، وكتابة التعليقات.",
        "story_ar": """<h3>💻 التحدث بلغة المبرمجين الحقيقية (C#)!</h3>أهلاً بك يا بطل في مسار المحترفين! بعد أن استخدمنا البرمجة مرئية، اليوم سنتعلم كيف يكتب مهندسو البرمجيات الحقيقيون الأكواد النصية باستخدام لغة <b>C# (سي شارب)</b> الرائعة والمستخدمة في كبرى شركات الألعاب!<br><br><b>🎯 الأساسيات البرمجية النصية اليوم:</b><ul><li>🖥️ <b>طباعة المخرجات (Console.WriteLine):</b> كيف نجعل الحاسوب يتحدث ويعرض عبارات جميلة على شاشتنا السوداء.</li><li>👤 <b>مدخلات المستخدم (Console.ReadLine):</b> كيف نسأل الطالب عن اسمه ونستمع لإجابته بذكاء!</li><li>📝 <b>التعليقات (Comments):</b> ملاحظات سرية نكتبها في الكود لا يراها الحاسوب بل يراها المهندسون فقط (//).</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> إنشاء برنامج دردشة ذكي يتفاعل مع المستخدم ويرحب به باسمه!</div><br><h4>💻 كيف يبدو أول برنامج حقيقي بلغة سي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using System;

class Program {
    static void Main() {
        Console.WriteLine("مرحباً بك في عالم السي شارب!"); // طباعة
        Console.Write("اكتب اسمك يا بطل: ");
        string name = Console.ReadLine(); // استقبال الاسم
        Console.WriteLine("أهلاً بك يا عبقري: " + name);
    }
}</code></pre><br><p>دعنا نختبر مهارات البرمجة ونقوم بطباعة رسالتنا الترحيبية الأولى! 🌟🚀</p>""",
        "story_en": """<h3>💻 Speaking the Language of Pro Developers (C#)!</h3>Welcome, young legend, to the professional programming zone! Today we step up from visual blocks and learn how real game engineers type raw script using <b>C# (C-Sharp)</b> - the powerful language used globally to build top-tier games!<br><br><b>🎯 C# Core Concepts We'll Learn Today:</b><ul><li>🖥️ <b>Console Output (Console.WriteLine):</b> Making the computer talk by printing out messages on the screen.</li><li>👤 <b>User Input (Console.ReadLine):</b> Asking the user questions and listening to their reply in real-time!</li><li>📝 <b>Code Comments (//):</b> Writing private developer notes that the computer ignores but helps you stay organized!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Crafting a smart chatbot that talks to the player and welcomes them by name!</div><br><h4>💻 Your Very First C# Program Layout:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using System;

class Program {
    static void Main() {
        Console.WriteLine("Hello to the C# Universe!");
        Console.Write("Enter your hero name: ");
        string name = Console.ReadLine();
        Console.WriteLine("Greetings, Commander: " + name);
    }
}</code></pre><br><p>Let's run the code below to test our script output console! 🌟🚀</p>""",
        "simple_en": "Imagine that C# is like writing an email directly to the computer's brain: we have to spell the words exactly right, or the computer will get confused!",
        "simple_ar": "تخيل أن لغة C# هي مثل كتابة رسالة بريد إلكتروني مباشرة إلى عقل الحاسوب: يجب أن نكتب الكلمات والحروف بدقة متناهية، وإلا سيصاب الحاسوب بالحيرة الكبيرة ويرفض التشغيل!",
        "hint_en": "Type: <code>print('Hello World from C# Console!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Hello World from C# Console!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact greeting: <code>Hello World from C# Console!</code>",
        "challenge_ar": "اطبع الترحيب التالي تماماً: <code>Hello World from C# Console!</code>",
        "starter_code": "# اكتب كود طباعة رسالة الترحيب الأولى هنا:\n",
        "pills": [
            {
                "label": "طباعة الترحيب / Hello C#",
                "code": "print('Hello World from C# Console!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Hello World from C# Console!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: مصمم بطاقات الهوية الشخصية",
        "homework_title_en": "🏠 Magic Home Challenge: Profile Info Printer",
        "homework_desc_ar": "يا ذكي، اكتب كوداً يقوم بتعريف متغيرين: أحدهما لاسم البطل والآخر لعمره بالسنوات، ثم قم بطباعتهما معاً بشكل جميل وتفاعلي!",
        "homework_desc_en": "Write a script that defines two variables: one for the hero name, and one for their age. Print them together in a neat profile message!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود طباعة الهوية التفاعلية للبطل هنا:\n"
    },
    {
        "id": 10,
        "badge_icon": "🧮",
        "badge_title": "Operator Wizard Medal",
        "title_en": "Session 10: C# Variables & Operators",
        "title_ar": "الحصة 10: متغيرات لغة C# والعمليات الحسابية",
        "desc_en": "Creating C# variables, using constants, and learning arithmetic, comparison, and logical operators.",
        "desc_ar": "تصميم المتغيرات بأنواعها المختلفة، القيم الثابتة، واستخدام العمليات الرياضية والمقارنات المنطقية بذكاء.",
        "story_ar": """<h3>🧮 صناديق حفظ البيانات والعمليات الرياضية السحرية!</h3>كل الألعاب تحتاج لحساب نقاط اللاعبين، وحجم قوتهم، وسرعتهم. اليوم سنتعلم كيف نصنع صناديق سرية لتخزين البيانات تسمى **المتغيرات (Variables)** وكيف نجري العمليات الحسابية الفائقة!<br><br><b>🎯 المبادئ الحسابية التفاعلية:</b><ul><li>📦 <b>أنواع المتغيرات (Variable Types):</b> الأعداد الصحيحة (int)، الأعداد العشرية (float)، النصوص (string)، وحقائق الصواب والخطأ (bool).</li><li>🔒 <b>القيم الثابتة (Constants):</b> قيم لا تتغير أبداً مثل النسبة التقريبية أو الجاذبية.</li><li>⚡ <b>العوامل الرياضية والمنطقية (Operators):</b> الجمع والطرح والضرب والمقارنات الذكية مثل أكبر وأصغر (>, <).</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> تصميم آلة حاسبة برمجية خارقة تحسب درجات الطالب وتصنف أداءه!</div><br><h4>💻 كيف نعلن عن المتغيرات الحسابية بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>int score = 100;
float speed = 15.5f;
string heroName = "Megamind Coder";
bool isGameOver = false;

// عملية حسابية تفاعلية!
int newScore = score + 50; </code></pre><br><p>دعنا نجري حساباً سريعاً بتشغيل الكود بالأسفل في محاكي المتغيرات! 🌟🚀</p>""",
        "story_en": """<h3>🧮 Data Vaults & Computational Spells!</h3>Every video game needs to store player health, scores, speeds, and levels. Today we master **Variables** - our secret memory boxes inside C#, along with mathematical operators!<br><br><b>🎯 C# Math & Logic Concepts:</b><ul><li>📦 <b>Data Types:</b> Integers (int), decimals (float), text strings (string), and true/false switches (bool).</li><li>🔒 <b>Constants (const):</b> Fixed variables that can never be modified (like math values).</li><li>⚡ <b>Operators:</b> Arithmetic (+, -, *, /), comparison (>, <, ==), and logical gates (AND, OR).</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Coding a math calculator engine that computes combat power ratings!</div><br><h4>💻 Defining Typed Variables in C#:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>int score = 100;
float speed = 15.5f;
string heroName = "Megamind Coder";
bool isGameOver = false;

// Compute a dynamic bonus!
int totalScore = score + 50;</code></pre><br><p>Let's run the code below to test variables declaration! 🌟🚀</p>""",
        "simple_en": "Imagine a variable is like a labeled lunchbox: the 'int' box holds whole numbers like apples, the 'string' box holds written name tags, and the 'bool' box holds a simple on/off light switch!",
        "simple_ar": "تخيل أن المتغير هو صندوق طعام ملصق عليه اسم: الصندوق 'int' يحتوي على تفاح صحيح كامل (أرقام)، والصندوق 'string' يحتوي على كلمات الاسم، والصندوق 'bool' يحتوي فقط على مفتاح إضاءة (تشغيل/إطفاء)!",
        "hint_en": "Type: <code>print('Variable calculations are correct!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Variable calculations are correct!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>Variable calculations are correct!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>Variable calculations are correct!</code>",
        "starter_code": "# اكتب كود إجراء العمليات الحسابية الذكية هنا:\n",
        "pills": [
            {
                "label": "حساب المتغيرات / Calculate Variables",
                "code": "print('Variable calculations are correct!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Variable calculations are correct!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: حاسب نقاط الطاقة الخارقة",
        "homework_title_en": "🏠 Magic Home Challenge: XP Power Computator",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يحاكي حساب النقاط: أعلن عن متغير نقاط البداية 10 نقاط، واضربه في 5، ثم اطبع النتيجة النهائية بوضوح!",
        "homework_desc_en": "Write a script that simulates scoring: declare a startScore variable of 10, multiply it by 5, and print 'Final Score: X'!",
        "homework_starter_code": "# تحدي المنزل: اكتب معادلة حساب الطاقة وضاعفها 5 مرات هنا:\n"
    },
    {
        "id": 11,
        "badge_icon": "🔀",
        "badge_title": "Logic Gate Medal",
        "title_en": "Session 11: Conditions & Loops in C#",
        "title_ar": "الحصة 11: اتخاذ القرارات الذكية والتكرار (الشروط والحلقات)",
        "desc_en": "Working with C# conditions (if, else if, else) and control loops (while, for).",
        "desc_ar": "صنع القرارات باستخدام العبارات الشرطية، وتكرار الأوامر بذكاء تام باستخدام الحلقات التكرارية.",
        "story_ar": """<h3>🔀 جعل الحاسوب يفكر ويتخذ القرارات الذكية!</h3>اليوم سنعطي الحاسوب عقلاً يفكر به! سنتعلم كيف نجعله يقرر بنفسه متى يفوز اللاعب ومتى يخسر بناءً على نقاطه، وكيف يقوم بتكرار الأوامر ملايين المرات في أجزاء من الثانية دون كلل!<br><br><b>🎯 قواعد المنطق الذكي اليوم:</b><ul><li>🚦 <b>الجمل الشرطية (if, else if):</b> اتخاذ مسارات مختلفة بناءً على الشروط (مثل: إذا كانت النقاط أكبر من 50 -> فزت باللعبة!).</li><li>🔄 <b>حلقة التكرار (for loop):</b> تكرار أمر معين لعدد محدد من المرات (مثل توليد 10 نجوم ذهبية).</li><li>⏳ <b>حلقة التكرار المشروط (while loop):</b> تكرار العمل طالما أن الشرط لا يزال صحيحاً.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة لعبة تخمين الأرقام السرية التفاعلية مع البطل!</div><br><h4>💻 كيف نكتب الجمل الشرطية والتكرار بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>int health = 80;

// اتخاذ القرار تفاعلياً!
if (health &gt;= 50) {
    Debug.Log("البطل في حالة ممتازة ومتحمس! 💪");
} else {
    Debug.Log("احترس! طاقة البطل منخفضة جداً!");
}

// تكرار توليد 3 مكافآت!
for (int i = 1; i &lt;= 3; i++) {
    Debug.Log("توليد الجوهرة رقم: " + i);
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لمحاكاة الشروط التفاعلية بذكاء! 🌟🚀</p>""",
        "story_en": """<h3><span style="font-family: inherit;">🔀 Smart Decision Making & Turbo Loops!</span></h3>Today we give our computer a digital brain! We will learn how to make the computer decide when the player wins or loses based on rules, and repeat complicated commands millions of times in milliseconds without ever getting tired!<br><br><b>🎯 Logic & Control Flow Concepts:</b><ul><li>🚦 <b>Conditional Branching (if, else if):</b> Choosing paths depending on state checks (e.g., if score is greater than 50 -> declare Win!).</li><li>🔄 <b>For Loops:</b> Repeating a specific action for a fixed number of times (like spawning 10 gold gems).</li><li>⏳ <b>While Loops:</b> Running loops continuously as long as a criteria is active.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Programming an interactive guess-the-number game engine!</div><br><h4>💻 C# Decision & Loop Syntax:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>int health = 80;

// Conditional check
if (health &gt;= 50) {
    Debug.Log("Hero is fully charged and happy! 💪");
} else {
    Debug.Log("Warning! Low health alert!");
}

// Spawn 3 trophies in a row!
for (int i = 1; i &lt;= 3; i++) {
    Debug.Log("Spawning Trophy #" + i);
}</code></pre><br><p>Let's run the logic engine script below to verify! 🌟🚀</p>""",
        "simple_en": "Imagine a traffic light: IF the light is green, the car goes. ELSE IF the light is yellow, the car slows down. ELSE, the car stops! Loops are like windshield wipers that swing back and forth repeatedly!",
        "simple_ar": "تخيل إشارة المرور: إذا (IF) كانت الإشارة خضراء، تسير السيارة. وإلا إذا (ELSE IF) كانت صفراء، تهدئ السيارة. وإلا (ELSE)، تقف السيارة تماماً! أما الحلقات التكرارية فهي مثل مساحات الزجاج التي تتحرك ذهاباً وإياباً طالما أن المطر يتساقط!",
        "hint_en": "Type: <code>print('Logic & Loop Checks Passed!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Logic & Loop Checks Passed!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Logic & Loop Checks Passed!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Logic & Loop Checks Passed!</code>",
        "starter_code": "# اكتب كود محاكاة الشروط واتخاذ القرارات هنا:\n",
        "pills": [
            {
                "label": "تشغيل المنطق والشروط / Test Logic",
                "code": "print('Logic & Loop Checks Passed!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Logic & Loop Checks Passed!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: حلقة توليد طاقة الأبطال الخارقين",
        "homework_title_en": "🏠 Magic Home Challenge: Hero Power-Up Loop",
        "homework_desc_ar": "قم بكتابة كود حلقة تكرار بسيطة تطبع مستوى القوة للبطل بداية من المستوى 1 إلى المستوى 5 بعبارة: 'Hero Level: X'!",
        "homework_desc_en": "Write a script that prints a training simulator log: print 'Hero Level: X' for each level starting from 1 to 5 using a loop!",
        "homework_starter_code": "# تحدي المنزل: اكتب حلقة توليد المستويات الخمسة للأبطال هنا:\n"
    },
    {
        "id": 12,
        "badge_icon": "🏛️",
        "badge_title": "Class Architect Medal",
        "title_en": "Session 12: Methods, Classes & Objects",
        "title_ar": "الحصة 12: الدوال والفئات والكائنات البرمجية (OOP)",
        "desc_en": "Understanding C# functions/methods, class design, objects, and access modifiers.",
        "desc_ar": "التعرف على الدوال لتنظيم الأكواد، الفئات البرمجية كقوالب لتصميم الأبطال، وفلسفة الكائنات البرمجية.",
        "story_ar": """<h3>🏛️ مهندسو الفئات البرمجية وتصميم الكائنات!</h3>اليوم سنتعلم المبدأ السري الذي تستخدمه كبرى استوديوهات الألعاب في العالم لتصميم آلاف الشخصيات والأعداء بسهولة: **البرمجة كائنية التوجه (OOP)**! سنصنع قالب بطل خارق ثم نولد منه مئات الأبطال المميزين!<br><br><b>🎯 الأركان البرمجية التفاعلية لليوم:</b><ul><li>⚙️ <b>الدوال (Methods/Functions):</b> مجمعات أكواد سحرية تقوم بوظيفة محددة (مثل: القفز، إطلاق النار) ونستدعيها وقتما نشاء!</li><li>🏛️ <b>الفئات (Classes):</b> المخطط الهندسي السري للشخصية (الاسم، الصحة، اللون).</li><li>📦 <b>الكائنات (Objects):</b> الشخصيات الحقيقية والمولدة داخل لعبتنا بناءً على المخطط السري.</li><li>🔒 <b>محددات الوصول (Access Modifiers):</b> تحديد من يحق له تعديل البيانات (public vs private).</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> تصميم فئة البطل الخارق وتوليد البطل 'Sonic' والبطل 'Mario' بخصائص مذهلة ومتفاوتة!</div><br><h4>💻 كيف نكتب الفئات والدوال بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

// الفئة السحرية للبطل
public class Player {
    public string name;
    public int score;

    public void GainPoint() {
        score += 10;
        Debug.Log(name + " حصل على 10 نقاط طاقة! المجموع: " + score);
    }
}</code></pre><br><p>دعنا نشغل الكود التالي لتأكيد تشغيل الدوال البرمجية لدينا! 🌟🚀</p>""",
        "story_en": """<h3>🏛️ Class Blueprints & Generating Objects!</h3>Today we learn the industrial standard concept that major game studios use to manage thousands of complex game characters: **Object-Oriented Programming (OOP)**! We will design a master blueprint and stamp out dozens of heroes!<br><br><b>🎯 Core OOP Concepts:</b><ul><li>⚙️ <b>Methods (Functions):</b> Blocks of code that perform specific actions (like Shoot, Jump) that we run on demand!</li><li>🏛️ <b>Classes:</b> The structural blueprint detailing variables (name, HP, skin) and actions of an entity.</li><li>📦 <b>Objects:</b> The real, living instances spawned inside your game from the master class.</li><li>🔒 <b>Access Modifiers (public/private):</b> Restricting or allowing external classes to read your data fields.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Coding a Hero class and instantiating 'Sonic' and 'Mario' with custom stats!</div><br><h4>💻 Designing C# Classes and Methods:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class Player {
    public string name;
    public int score;

    public void GainPoint() {
        score += 10;
        Debug.Log(name + " got 10 energy points! Current score: " + score);
    }
}</code></pre><br><p>Let's run the code below to test class method execution! 🌟🚀</p>""",
        "simple_en": "Imagine a car factory: the blueprint drawing is the Class. The actual physical cars rolling out of the assembly line that you can drive are the Objects!",
        "simple_ar": "تخيل مصنع سيارات: الرسم التخطيطي الهندسي للسيارة هو الفئة (Class)، والسيارات الحقيقية والملموسة التي تخرج من المصنع وتستطيع ركوبها وقيادتها هي الكائنات (Objects)!",
        "hint_en": "Type: <code>print('Methods & Classes compiled successfully!')</code> and hit Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Methods & Classes compiled successfully!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>Methods & Classes compiled successfully!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>Methods & Classes compiled successfully!</code>",
        "starter_code": "# اكتب كود محاكاة استدعاء دالة البطل هنا:\n",
        "pills": [
            {
                "label": "تشغيل الكلاسات والدوال / Run Class Methods",
                "code": "print('Methods & Classes compiled successfully!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Methods & Classes compiled successfully!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: مصنع الأبطال الخارقين التفاعلي",
        "homework_title_en": "🏠 Magic Home Challenge: OOP Factory Stamp",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يعرف دالة باسم 'activate_hero' تطبع العبارة 'Hero Activated!' واستدعيها في نهاية الكود لتأكيد فهمك للدوال!",
        "homework_desc_en": "Write a script that defines a method named 'activate_hero' that prints 'Hero Activated!' and call it in your script to test!",
        "homework_starter_code": "# تحدي المنزل: اكتب تعريف دالة التفعيل واستدعيها هنا:\n"
    },
    {
        "id": 13,
        "badge_icon": "🗺️",
        "badge_title": "2D Tilemap Explorer Medal",
        "title_en": "Session 13: Sunny Land 1: Sprite & Tilemap",
        "title_ar": "الحصة 13: لعبة الأرض المشمسة 1: تصميم العالم وحركة الكيبورد",
        "desc_en": "Handling sprites, tile palettes, and tilemaps, and scripting player horizontal movement in 2D.",
        "desc_ar": "التحكم بالرسومات ثنائية الأبعاد، رسم التضاريس والخرائط باستخدام لوحة البلاطات، وبرمجة حركة اللاعب بالأزرار.",
        "story_ar": """<h3>🗺️ رسم وتصميم عالم مغامراتك ثنائي الأبعاد!</h3>اليوم سنبدأ مشروعاً عملاقاً وممتعاً: **لعبة مغامرات الأرض المشمسة (Sunny Land)**! سنتعلم كيف يرسم المطورون التضاريس والجبال والمنصات التفاعلية باستخدام الفرشاة السحرية، وكيف نجعل شخصيتنا تتحرك يميناً ويساراً بلوحة المفاتيح!<br><br><b>🎯 أساسيات تصميم الألعاب ثنائية الأبعاد:</b><ul><li>🖼️ <b>المجسم الرسومي (Sprite):</b> الصور المسطحة التي تمثل الشخصيات والأرضيات في عالمنا ثنائي الأبعاد.</li><li>🎨 <b>لوحة البلاطات (Tile Palette):</b> لوحة ألوان تحتوي على مربعات الأرض والعشب والمنصات الجاهزة للرسم بها.</li><li>🗺️ <b>خارطة البلاطات (Tilemap):</b> الشبكة السحرية التي نقوم بالرسم عليها لبناء مستويات اللعبة التفاعلية.</li><li>⌨️ <b>التحكم بلوحة المفاتيح (Keyboard Input):</b> استخدام الكود للتحكم بالحركة عند ضغط أزرار الحركة (A, D) أو الأسهم.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> بناء مستوى كامل ورسم منصات جميلة بيدك وبرمجة حركة بطلنا الثعلب فوقها!</div><br><h4>💻 كيف نبرمج حركة الثعلب بلوحة المفاتيح بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class FoxMove : MonoBehaviour {
    public float speed = 5f;

    void Update() {
        // استقبال المدخلات الأفقية (يمين / يسار)
        float moveInput = Input.GetAxis("Horizontal");
        transform.Translate(new Vector3(moveInput * speed * Time.deltaTime, 0, 0));
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لمحاكاة قراءة حركة أزرار الاتجاهات! 🌟🚀</p>""",
        "story_en": """<h3>🗺️ Painting Beautiful 2D Realms!</h3>Today we embark on an ambitious new project: **Sunny Land 2D Platformer Adventure**! We will learn how developers paint grasslands, caves, and floating islands using a digital brush, and code our character to run left and right using the keyboard!<br><br><b>🎯 2D Game Architecture Concepts:</b><ul><li>🖼️ <b>Sprites:</b> Flat 2D image sheets that define our player skins, obstacles, and backgrounds.</li><li>🎨 <b>Tile Palette:</b> A dynamic editor box filled with grass, rock, and bridge tiles ready to draw.</li><li>🗺️ <b>Tilemaps:</b> The grid component inside Unity where we layout our visual game platforms.</li><li>⌨️ <b>Keyboard Input:</b> Capturing horizontal button signals (A, D or Arrow keys) to translate our player transform.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Painting a gorgeous sky level and coding our cute fox hero to run!</div><br><h4>💻 C# 2D Keyboard Movement Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class FoxMove : MonoBehaviour {
    public float speed = 5f;

    void Update() {
        // Read input axis (A, D, Left, Right)
        float moveInput = Input.GetAxis("Horizontal");
        transform.Translate(new Vector3(moveInput * speed * Time.deltaTime, 0, 0));
    }
}</code></pre><br><p>Let's run the input verification script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine a checkerboard: Tilemap is the empty board, Tile Palette is your box of red and black square tokens, and you can paint them onto the grid to make any level shape you want!",
        "simple_ar": "تخيل رقعة الشطرنج: خارطة البلاطات (Tilemap) هي الرقعة الفارغة، ولوحة البلاطات (Tile Palette) هي علبة المكعبات والقطع الملونة، ويمكنك استخدامها لرسم وبناء أي قلعة ومنصة تشاء في لعبتك!",
        "hint_en": "Type: <code>print('Tilemap Ground Created & Fox Input Active!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Tilemap Ground Created & Fox Input Active!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>Tilemap Ground Created & Fox Input Active!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>Tilemap Ground Created & Fox Input Active!</code>",
        "starter_code": "# اكتب كود تفعيل حركة اللاعب ثنائي الأبعاد هنا:\n",
        "pills": [
            {
                "label": "تشغيل تضاريس اللعبة / Load Tilemap Platforms",
                "code": "print('Tilemap Ground Created & Fox Input Active!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Tilemap Ground Created & Fox Input Active!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكاة إحداثيات حركة اللاعب",
        "homework_title_en": "🏠 Magic Home Challenge: Horizontal Coordinate Tracker",
        "homework_desc_ar": "قم بكتابة كود يزيد موقع اللاعب الأفقي (X-coordinate) بمقدار 2 in كل خطوة حركة، واطبع الإحداثيات 5 مرات متتالية لمحاكاة الثعلب يجري للأمام!",
        "homework_desc_en": "Write a script that increments the player's X coordinate by 2 in each step, printing 'Fox Position X: Y' for 5 steps to simulate running!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود زيادة إحداثيات موقع الثعلب هنا:\n"
    },
    {
        "id": 14,
        "badge_icon": "⚖️",
        "badge_title": "2D Physics Master Badge",
        "title_en": "Session 14: Sunny Land 2: 2D Physics & Camera Follow",
        "title_ar": "الحصة 14: لعبة الأرض المشمسة 2: الفيزياء ثنائية الأبعاد ومتابعة الكاميرا",
        "desc_en": "Configuring 2D colliders, Rigidbodies, constraint freezing, and setup Cinemachine camera follow.",
        "desc_ar": "تأمين الجسيمات بالفيزياء ورصد الاصطدامات، تثبيت حركة اللاعب لمنع انقلابه، وجعل الكاميرا تتبع البطل بذكاء.",
        "story_ar": """<h3>⚖️ تفعيل الجاذبية الأرضية والكاميرا الذكية التي تلاحق البطل!</h3>عالمنا الرائع يحتاج لقوانين تحكمه! اليوم سنعطي الثعلب وزناً حقيقياً ليتأثر بالجاذبية ويسقط فوق المنصات دون أن يخترقها، وسنقوم ببرمجة الكاميرا لتتحرك وتلحق به أينما ذهب مثل مصوري السينما المحترفين!<br><br><b>🎯 مكونات المحاكاة الفيزيائية التفاعلية:</b><ul><li>🧱 <b>أدوات الاصطدام (Colliders 2D):</b> الدروع السحرية مثل BoxCollider2D و TilemapCollider2D التي تمنع الشخصيات من التداخل وتمنعها من السقوط اللانهائي!</li><li>⚓ <b>تثبيت الدوران (Freeze Rotation):</b> قفل محور الدوران Z لمنع الثعلب من الانقلاب على وجهه عند السقوط!</li><li>🎥 <b>كاميرا سينماشين (Cinemachine Camera):</b> الكاميرا الذكية التي نوجهها نحو الثعلب لتقوم بمتابعته بسلاسة وبأعلى دقة جمالية!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> ضبط فيزياء اللعبة ومنع اختراق الأرضيات وإعداد ملاحقة الكاميرا السحرية للبطل!</div><br><h4>💻 كيف نضبط سرعة البطل الفيزيائية بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class PhysicsFox : MonoBehaviour {
    private Rigidbody2D rb;
    public float moveSpeed = 5f;

    void Start() {
        rb = GetComponent&lt;Rigidbody2D&gt;();
        // تثبيت الدوران لكي لا ينقلب الثعلب!
        rb.freezeRotation = true; 
    }

    void FixedUpdate() {
        float xMove = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(xMove * moveSpeed, rb.velocity.y);
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لتفعيل محرك الجاذبية ومتابعة الكاميرا بنجاح! 🌟🚀</p>""",
        "story_en": """<h3>⚖️ Real 2D Physics & Dynamic Camera Tracking!</h3>Our game world needs rules! Today we give our fox real mass so they fall realistically under gravity and stand firm on grass platforms. Plus, we program a dynamic movie-style camera to follow our hero everywhere!<br><br><b>🎯 2D Physics & Camera Building Blocks:</b><ul><li>🧱 <b>2D Colliders:</b> BoxCollider2D and TilemapCollider2D shields that prevent GameObjects from falling through the floor!</li><li>⚓ <b>Freeze Rotation:</b> Locking the Z-rotation axis so our poor fox doesn't tip over and roll on their head when dropping!</li><li>🎥 <b>Cinemachine Camera:</b> The industry-standard tool to lock camera focus on your target and pan smoothly.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Rigging character physics, stopping boundary penetrations, and setting up Cinemachine tracking!</div><br><h4>💻 C# Rigidbody Velocity Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class PhysicsFox : MonoBehaviour {
    private Rigidbody2D rb;
    public float moveSpeed = 5f;

    void Start() {
        rb = GetComponent&lt;Rigidbody2D&gt;();
        rb.freezeRotation = true; // Lock Z rotation
    }

    void FixedUpdate() {
        float xMove = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(xMove * moveSpeed, rb.velocity.y);
    }
}</code></pre><br><p>Let's run the physics initializer script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine wearing a magic heavy suit: Rigidbody2D is that heavy suit that pulls you to the floor, and Colliders are like wooden shoes that stop you from sinking into the mud!",
        "simple_ar": "تخيل أنك ترتدي بدلة ثقيلة سحرية: الجسيم الفيزيائي (Rigidbody2D) هو هذه البدلة التي تشدك نحو الأرض بفعل الجاذبية، وأدوات الاصطدام (Colliders) هي حذاؤك الحديدي الذي يمنعك من الغوص داخل الطين أو اختراق الرصيف!",
        "hint_en": "Type: <code>print('Rigidbody2D and Cinemachine Follow Active!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Rigidbody2D and Cinemachine Follow Active!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>Rigidbody2D and Cinemachine Follow Active!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>Rigidbody2D and Cinemachine Follow Active!</code>",
        "starter_code": "# اكتب كود تفعيل المحاكاة الفيزيائية والكاميرا هنا:\n",
        "pills": [
            {
                "label": "تفعيل الجاذبية والكاميرا / Activate Physics",
                "code": "print('Rigidbody2D and Cinemachine Follow Active!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Rigidbody2D and Cinemachine Follow Active!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكي الجاذبية والسقوط الحر",
        "homework_title_en": "🏠 Magic Home Challenge: Gravity Drop Simulator",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يحاكي تراجع قيمة الارتفاع (Y-axis) للاعب بمقدار 3 in كل خطوة سقوط حاد، واطبع موقعه في 4 خطوات متتالية حتى يستقر على الأرض!",
        "homework_desc_en": "Write a script that simulates vertical gravity: decrease a Y position variable by 3 in each loop step, printing 'Fox Height: Y' until it reaches ground level!",
        "homework_starter_code": "# تحدي المنزل: اكتب محاكاة السقوط الحر للثعلب هنا:\n"
    },
    {
        "id": 15,
        "badge_icon": "💎",
        "badge_title": "Gem Collector Medal",
        "title_en": "Session 15: Sunny Land 3: Player Jump, Tags & Score",
        "title_ar": "الحصة 15: لعبة الأرض المشمسة 3: قفزة الثعلب، تصنيف الأهداف وتجميع الجواهر",
        "desc_en": "Programming 2D vertical jump, identifying game items with tags, and creating a gem collection system.",
        "desc_ar": "برمجة قفز اللاعب للأعلى بالفيزياء، تمييز الكائنات باستخدام العلامات (Tags)، وصنع نظام جمع وتخزين المجوهرات الملونة.",
        "story_ar": """<h3>💎 القفز وتجميع المجوهرات السحرية وبث الروح في اللعبة!</h3>الألعاب الرائعة تحتاج لأهداف! اليوم سنصنع هدفاً تفاعلياً رائعاً: سنقوم ببرمجة قفز الثعلب للأعلى بحركات بهلوانية جميلة لتفادي السقوط، وسنقوم بنشر مجوهرات لامعة في العالم ليقوم الثعلب بجمعها وربح النقاط الذهبية!<br><br><b>🎯 أركان لعبتنا اليوم:</b><ul><li>🦘 <b>القفز الفيزيائي (2D Jump):</b> إعطاء سرعة للأعلى في المحور Y لتخطي الحفر بنجاح.</li><li>🏷️ <b>العلامات السحرية (Tags):</b> كيفية تمييز الكائنات؛ مثلاً نضع علامة 'Gem' على الجواهر، لكي تفرق اللعبة بين لمس الأرض ولمس المكافأة!</li><li>💎 <b>نظام التجميع والتدمير (Collect & Destroy):</b> زيادة عداد المجوهرات بمقدار 1 وإخفاء المجوهرة المصطدم بها فوراً كأنها ابتلعت!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة قفز البطل والتقاط المجوهرات وزيادة العداد التفاعلي بنجاح!</div><br><h4>💻 كيف نبرمج التقاط المجوهرات بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class FoxInventory : MonoBehaviour {
    public int gemsCount = 0;

    void OnTriggerEnter2D(Collider2D other) {
        // التحقق من العلامة السحرية للمجوهرة!
        if (other.gameObject.CompareTag("Gem")) {
            gemsCount++;
            Debug.Log("مذهل! التقطت مجوهرة سحرية! المجموع الحالي: " + gemsCount);
            Destroy(other.gameObject); // إخفاء المجوهرة فوراً!
        }
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لتأكيد نظام التقاط المجوهرات الرائع! 🌟🚀</p>""",
        "story_en": """<h3>💎 Jump High & Collect Magical Gems!</h3>Great games need goals! Today we create an awesome gameplay mechanic: we script our fox to jump high in the air to avoid traps, and scatter beautiful glittering gems around the level for our player to collect and boost their score!<br><br><b>🎯 Essential Gameplay Elements:</b><ul><li>🦘 <b>2D Physics Jump:</b> Giving our Rigidbody an upward impulse on the Y axis to leap over deep pits.</li><li>🏷️ <b>Dynamic Tagging:</b> Marking objects with tags (e.g., 'Gem') so our player script knows exactly what it collided with!</li><li>💎 <b>Collect & Destroy Pattern:</b> Incrementing our gem count variable by 1 and destroying the collected gem game object on collision!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Implementing player jump controls and scripting a dynamic gem pickup inventory!</div><br><h4>💻 C# Gem Collection Trigger Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class FoxInventory : MonoBehaviour {
    public int gemsCount = 0;

    void OnTriggerEnter2D(Collider2D other) {
        // Verify target object tag!
        if (other.gameObject.CompareTag("Gem")) {
            gemsCount++;
            Debug.Log("Splendid! Gem collected. Total inventory: " + gemsCount);
            Destroy(other.gameObject); // Disappear gem!
        }
    }
}</code></pre><br><p>Let's run the collector script below to simulate picking up a magic gem! 🌟🚀</p>""",
        "simple_en": "Imagine walking in the dark with a scanner: your tag 'Gem' is like a scanner beacon that rings out 'Bonus!' only when you touch a gold coin, and stays silent when you step on grass!",
        "simple_ar": "تخيل أنك تمشي في الظلام ومعك جهاز كاشف سحري: العلامة (Tag) 'Gem' هي بمثابة رنين من الكاشف يصيح 'مكافأة!' فقط عندما تلمس مجوهرة ذهبية، ويبقى صامتاً عندما تلمس الأرضية العادية!",
        "hint_en": "Type: <code>print('Gem Pickup & Score Counting Activated!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Gem Pickup & Score Counting Activated!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>Gem Pickup & Score Counting Activated!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>Gem Pickup & Score Counting Activated!</code>",
        "starter_code": "# اكتب كود تفعيل جمع المجوهرات وحساب النقاط هنا:\n",
        "pills": [
            {
                "label": "تشغيل تجميع المجوهرات / Activate Gem Pickup",
                "code": "print('Gem Pickup & Score Counting Activated!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Gem Pickup & Score Counting Activated!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: حلقة جمع الكنز الأسطوري",
        "homework_title_en": "🏠 Magic Home Challenge: Treasure Chest Loot Log",
        "homework_desc_ar": "قم بكتابة كود يحاكي فتح صندوق كنز يحتوي على 3 جواهر سحرية: اطبع جمل تجميع متتالية متزايدة 'Gem #1 Collected!', 'Gem #2 Collected!' تفاعلياً!",
        "homework_desc_en": "Write a script that simulates looting a treasure chest with 3 gems: print consecutive collection statements 'Gem #1 Collected!' up to 'Gem #3 Collected!'!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة جمع صندوق الكنز هنا:\n"
    },
    {
        "id": 16,
        "badge_icon": "🐸",
        "badge_title": "Sunny Land Creator Medal",
        "title_en": "Session 16: Sunny Land 4: Enemy AI, Audio & Game Build",
        "title_ar": "الحصة 16: لعبة الأرض المشمسة 4: ذكاء الأعداء، الأصوات والمستويات النهائية",
        "desc_en": "Scripting enemy horizontal patrol, UI canvas score updates, 2D audio trigger, and WebGL publishing.",
        "desc_ar": "برمجة دورية حركة الأعداء الأذكياء، تحديث لوحة النقاط على الشاشة، تفعيل الأصوات التفاعلية، وتصدير اللعبة بنجاح.",
        "story_ar": """<h3>🐸 ذكاء الأعداء والمؤثرات الصوتية وتصدير المغامرة الكبرى!</h3>اليوم سنضع اللمسات السحرية النهائية على لعبتنا Sunny Land! سنجعل الضفادع والوحوش تتحرك في دوريات ذكية لحراسة المستويات، وسنضيف أصواتاً تفاعلية حماسية عند القفز والجمع، ونصدر لعبتنا للعالم!<br><br><b>🎯 الميزات السحرية النهائية لليوم:</b><ul><li>🤖 <b>ذكاء الأعداء (Enemy AI Patrol):</b> جعل العدو الضفدع يتحرك بين نقطتين ذهاباً وإياباً لحراسة الكنز بذكاء!</li><li>🔊 <b>الأصوات ثنائية الأبعاد (AudioSource):</b> تشغيل صوت بهيج ومرح عند التقاط الجواهر وصوت آخر عند القفز.</li><li>🖥️ <b>لوحة النقاط (UI Canvas):</b> عرض شريط الصحة وعدد الجواهر أمام اللاعب على الشاشة مباشرة.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة دورية حركة العدو وتفعيل الأصوات وتصدير لعبتنا كنسخة ويب تفاعلية بالكامل!</div><br><h4>💻 كيف نبرمج حركة العدو ذهاباً وإياباً بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class EnemyPatrol : MonoBehaviour {
    public float speed = 2f;
    private bool movingRight = true;

    void Update() {
        if (movingRight) {
            transform.Translate(Vector2.right * speed * Time.deltaTime);
        } else {
            transform.Translate(Vector2.left * speed * Time.deltaTime);
        }
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لتصدير لعبة الأرض المشمسة بنجاح ساحق! 🌟🚀</p>""",
        "story_en": """<h3>🐸 Enemy AI Patrol, Sound Effects & Victory Compilation!</h3>Today we add the final professional touches to our Sunny Land platformer! We will script wild frogs and opossums to patrol and guard their territories, play retro sound effects when jumping or collecting, and build our final package!<br><br><b>🎯 Advanced Game Mechanics:</b><ul><li>🤖 <b>Enemy AI Patrol:</b> Programming an enemy sprite to walk back and forth between two boundary nodes automatically.</li><li>🔊 <b>2D Sound Trigger (AudioSource.Play):</b> Triggering crystal-clear sound effects upon picking up gems or bouncing on a spring.</li><li>🖥️ <b>UI Screen Canvas:</b> Designing real-time HP bars and dynamic score text that updates on the player HUD.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Rigging enemy AI patrol systems, layering game audio, and building your final executable!</div><br><h4>💻 C# Enemy Patrol Logic:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class EnemyPatrol : MonoBehaviour {
    public float speed = 2f;
    private bool movingRight = true;

    void Update() {
        if (movingRight) {
            transform.Translate(Vector2.right * speed * Time.deltaTime);
        } else {
            transform.Translate(Vector2.left * speed * Time.deltaTime);
        }
    }
}</code></pre><br><p>Let's run the build script below to compile Sunny Land Game! 🌟🚀</p>""",
        "simple_en": "Imagine a security guard walking from the front gate to the back gate and then turning around to walk back. That's exactly how our AI Frog patrols the scene!",
        "simple_ar": "تخيل حارس أمن يسير من البوابة الأمامية إلى البوابة الخلفية، ثم يستدير ويسير عائداً للبداية. هذه هي طريقة حركة الضفدع الشرير لحراسة الجواهر بدقة تامة!",
        "hint_en": "Type: <code>print('Sunny Land Build Compiled & Audio Loaded!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Sunny Land Build Compiled & Audio Loaded!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Sunny Land Build Compiled & Audio Loaded!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Sunny Land Build Compiled & Audio Loaded!</code>",
        "starter_code": "# اكتب كود محاكاة تصدير وبناء لعبة الأرض المشمسة هنا:\n",
        "pills": [
            {
                "label": "تصدير وبناء اللعبة / Build 2D Game",
                "code": "print('Sunny Land Build Compiled & Audio Loaded!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Sunny Land Build Compiled & Audio Loaded!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكي دورية حارس الأمن",
        "homework_title_en": "🏠 Magic Home Challenge: Security Patrol Log",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يحاكي حركة الحارس: اطبع 'Guard moving Right...', ثم 'Patrol Limit reached!', ثم 'Guard moving Left!' لتجسيد المنطق الفيزيائي!",
        "homework_desc_en": "Write a script that simulates enemy patrol logs: print 'Guard moving Right...', then 'Patrol Limit reached!', and finally 'Guard moving Left!'!",
        "homework_starter_code": "# تحدي المنزل: اكتب محاكاة حركة دورية الحارس هنا:\n"
    },
    {
        "id": 17,
        "badge_icon": "🏰",
        "badge_title": "3D Architect Medal",
        "title_en": "Session 17: RPG 3D 1: 3D Objects & Materials",
        "title_ar": "الحصة 17: لعبة مغامرات 3D 1: الأشكال ثلاثية الأبعاد والمواد والألوان",
        "desc_en": "Creating 3D projects, handling primitives, importing RPG Poly Pack, materials, and Cinemachine tracking.",
        "desc_ar": "إنشاء أول لعبة ثلاثية الأبعاد، التلاعب بالمجسمات الفراغية، استيراد حزم الأصول وتلوينها، وإعداد كاميرا تتبع الأهداف.",
        "story_ar": """<h3>🏰 الولوج إلى البعد الثالث وبناء القلاع ثلاثية الأبعاد!</h3>تهانينا! لقد تخرجت رسمياً من ثنائي الأبعاد، والآن ندخل إلى عالم ألعاب المحترفين الأسطوري: **العوالم ثلاثية الأبعاد (3D Game Dev)**! سنصنع وادي القلاع الأسطوري ونلوّن الصخور والجبال بألوان خلابة!<br><br><b>🎯 أساسيات الأبعاد الثلاثية اليوم:</b><ul><li>🧱 <b>المجسمات الأساسية (3D Primitives):</b> المكعب، الكرة، والأسطوانة التي ندمجها لصناعة أي شيء فراغي!</li><li>🎨 <b>المواد والألوان (Materials & Shaders):</b> الأقمشة البرمجية التي نغطي بها الأشكال لنمنحها مظهر الخشب، أو الذهب اللامع، أو الحجر.</li><li>🎥 <b>كاميرا التتبع ثلاثية الأبعاد (Cinemachine 3D):</b> تتبع بطلنا بدقة فائقة من جميع الزوايا كأننا في فيلم سينمائي رائع!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> بناء وتلوين أول جزيرة عائمة ثلاثية الأبعاد وتوجيه الكاميرا الذكية نحوها!</div><br><h4>💻 كيف نضبط إعدادات كاميرا سينماشين بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using Cinemachine; // استدعاء حزمة الكاميرا السينمائية

public class CameraSetup : MonoBehaviour {
    public CinemachineFreeLook freeLookCamera;
    public Transform targetPlayer;

    void Start() {
        // جعل الكاميرا تركز وتتابع البطل تلقائياً في الفراغ ثلاثي الأبعاد!
        freeLookCamera.Follow = targetPlayer;
        freeLookCamera.LookAt = targetPlayer;
    }
}</code></pre><br><p>دعنا نشغل كود محاكاة إطلاق البعد الثالث ثلاثي الأبعاد بنجاح! 🌟🚀</p>""",
        "story_en": """<h3>🏰 Stepping into the 3D Realm & Castle Building!</h3>Congratulations, young wizard! You have officially graduated from flat 2D games, and today we enter the legendary universe of **3D Game Development**! We will construct a epic mountain valley and layer beautiful materials on terrain objects!<br><br><b>🎯 3D Architecture Core Concepts:</b><ul><li>🧱 <b>3D Primitives:</b> Cubes, spheres, and cylinders that you combine to build any structure.</li><li>🎨 <b>Materials & Shaders:</b> The digital fabrics we wrap around 3D meshes to make them look like shiny gold, solid rock, or polished wood.</li><li>🎥 <b>3D Cinemachine Camera:</b> Setting up a cinematic 3rd-person camera that orbits around our player dynamically!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Structuring your first floating 3D island, texturing it, and locking target camera orbits!</div><br><h4>💻 C# Cinemachine Setup Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using Cinemachine;

public class CameraSetup : MonoBehaviour {
    public CinemachineFreeLook freeLookCamera;
    public Transform targetPlayer;

    void Start() {
        // Set the camera to follow and look at the target player in 3D!
        freeLookCamera.Follow = targetPlayer;
        freeLookCamera.LookAt = targetPlayer;
    }
}</code></pre><br><p>Let's run the 3D setup script below to initialize our viewport! 🌟🚀</p>""",
        "simple_en": "Imagine 2D is like drawing a picture on a piece of paper, and 3D is like building a castle with actual physical wooden blocks that you can walk around and look at from behind!",
        "simple_ar": "تخيل أن البعد ثنائي الأبعاد (2D) هو مثل رسم صورة على ورقة مسطحة، والبعد ثلاثي الأبعاد (3D) هو بمثابة بناء قلعة حقيقية بمكعبات خشبية تستطيع المشي حولها والنظر إليها من الخلف واليمين واليسار!",
        "hint_en": "Type: <code>print('3D Primitives & Cinemachine Setup Completed!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('3D Primitives & Cinemachine Setup Completed!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>3D Primitives & Cinemachine Setup Completed!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>3D Primitives & Cinemachine Setup Completed!</code>",
        "starter_code": "# اكتب كود تفعيل البعد الثالث والكاميرا الذكية هنا:\n",
        "pills": [
            {
                "label": "تفعيل الأبعاد الثلاثية / Start 3D Game",
                "code": "print('3D Primitives & Cinemachine Setup Completed!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "3D Primitives & Cinemachine Setup Completed!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكي إحداثيات الفضاء ثلاثي الأبعاد",
        "homework_title_en": "🏠 Magic Home Challenge: 3D Vector Coordinate Logger",
        "homework_desc_ar": "يا ذكي، اكتب كوداً يعرف ثلاثة متغيرات تمثل محاور الفراغ (X, Y, Z)، واطبع موقع كائن يتحرك بمقدار خطوة واحدة في المحاور الثلاثة معاً بشكل تفاعلي ومبسط!",
        "homework_desc_en": "Write a script that defines three coordinate variables (X, Y, Z) starting at 0, increments them all by 1, and prints 'Player Pos: (1, 1, 1)' to simulate 3D space movement!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة إحداثيات الحركة ثلاثية الأبعاد هنا:\n"
    },
    {
        "id": 18,
        "badge_icon": "🏃",
        "badge_title": "3D Physics Explorer Medal",
        "title_en": "Session 18: RPG 3D 2: Character Controller & Physics",
        "title_ar": "الحصة 18: لعبة مغامرات 3D 2: حركة اللاعب والفيزياء المجسمة",
        "desc_en": "Implementing Mesh Colliders, Capsule Colliders, Character Controller movement, gravity, and jump in 3D.",
        "desc_ar": "تأمين الاصطدامات بالمجسمات المعقدة، استخدام متحكم الشخصية السلس للحركة، وتطبيق قوانين الجاذبية والقفز ثلاثي الأبعاد.",
        "story_ar": """<h3>🏃 حركة اللاعب السلسة والجاذبية في الأبعاد الثلاثية!</h3>عالمنا ثلاثي الأبعاد يحتاج لقوانين حركة غاية في السلاسة والدقة. اليوم سنتعلم كيف نحرك البطل باستخدام مكون احترافي يمنعه من التداخل مع الجدران والأرضيات ويعطيه سرعة وجاذبية وقفزاً مبهراً!<br><br><b>🎯 مكونات الحركة ثلاثية الأبعاد الاحترافية:</b><ul><li>🛡️ <b>أدوات اصطدام النماذج (Mesh Collider):</b> درع فيزيائي يلتف بدقة حول تصميم الجبال والقلاع ثلاثية الأبعاد المعقدة لكي لا نسقط داخلها.</li><li>🤖 <b>متحكم الشخصية (Character Controller):</b> المكون السوبر ذكي الذي يسهل حركة الشخصيات في الألعاب من منظور الشخص الثالث.</li><li>⚖️ <b>الجاذبية ثلاثية الأبعاد (3D Gravity):</b> محاكاة قوة سحب البطل للأسفل باستمرار عند تركه في الهواء.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة بطل يدور ويجري في جزيرتنا ثلاثية الأبعاد بسلاسة فائقة ويتأثر بالجاذبية!</div><br><h4>💻 كيف نبرمج حركة البطل بمتحكم الشخصية بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class RPGMove : MonoBehaviour {
    private CharacterController controller;
    public float speed = 6f;
    private float gravity = -9.81f;
    private Vector3 velocity;

    void Start() {
        controller = GetComponent&lt;CharacterController&gt;();
    }

    void Update() {
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");
        Vector3 move = transform.right * x + transform.forward * z;
        controller.Move(move * speed * Time.deltaTime);

        // تطبيق الجاذبية التفاعلية!
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}</code></pre><br><p>دعنا نشغل الكود لتفعيل متحكم الشخصية والجاذبية ثلاثية الأبعاد بنجاح! 🌟🚀</p>""",
        "story_en": """<h3>🏃 Fluid 3D Movement & Gravity Simulation!</h3>Our 3D fantasy world needs fluid movement rules. Today we program a high-precision component that handles running, turning, colliding, and jumping under 3D gravity conditions without sinking through surfaces!<br><br><b>🎯 3D Movement Dynamics:</b><ul><li>🛡️ <b>Mesh Colliders:</b> Advanced physics shields that wrap perfectly around custom 3D fortress models for high-fidelity collision.</li><li>🤖 <b>Character Controller:</b> A specialized Unity component designed for custom 3rd-person movement physics and step climbs.</li><li>⚖️ <b>3D Gravity Logic:</b> Computing real-world downward velocity pulls so your character stays grounded.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Scripting keyboard-based 3D character movements, gravity calculations, and jumps!</div><br><h4>💻 C# Character Controller Movement Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class RPGMove : MonoBehaviour {
    private CharacterController controller;
    public float speed = 6f;
    private float gravity = -9.81f;
    private Vector3 velocity;

    void Start() {
        controller = GetComponent&lt;CharacterController&gt;();
    }

    void Update() {
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");
        Vector3 move = transform.right * x + transform.forward * z;
        controller.Move(move * speed * Time.deltaTime);

        // Apply realistic gravity!
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }
}</code></pre><br><p>Let's run the physics movement validator script below! 🌟🚀</p>""",
        "simple_en": "Imagine you are driving a bumper car: Character Controller is the steering wheel and thick rubber edge that lets you steer easily and bounce off walls without flying away!",
        "simple_ar": "تخيل أنك تقود سيارة تصادم تفاعلية في الملاهي: متحكم الشخصية (Character Controller) هو مقود السيارة والمطاط المحيط بها الذي يسمح لك بالقيادة بسلاسة والارتداد عن الجدران دون حدوث مشكلات!",
        "hint_en": "Type: <code>print('Character Controller Movement & Gravity Active!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Character Controller Movement & Gravity Active!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Character Controller Movement & Gravity Active!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Character Controller Movement & Gravity Active!</code>",
        "starter_code": "# اكتب كود تفعيل متحكم الشخصية التفاعلي هنا:\n",
        "pills": [
            {
                "label": "تفعيل متحكم اللاعب / Start Character Controller",
                "code": "print('Character Controller Movement & Gravity Active!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Character Controller Movement & Gravity Active!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: حلقة رصد قوة الجاذبية ثلاثية الأبعاد",
        "homework_title_en": "🏠 Magic Home Challenge: Gravity Acceleration Log",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يزيد سرعة السقوط بمقدار 9.8 في كل خطوة محاكاة، واطبع قيمة سرعة الهبوط 3 مرات متتالية لمحاكاة تسارع الجاذبية في الفراغ!",
        "homework_desc_en": "Write a script that simulates gravitational acceleration: increase a fallSpeed variable by 9.8 in a loop, printing 'Velocity Y: X' for 3 steps!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود حساب تسارع الجاذبية التفاعلي هنا:\n"
    },
    {
        "id": 19,
        "badge_icon": "🏃",
        "badge_title": "Animation Master Medal",
        "title_en": "Session 19: RPG 3D 3: Running & Animation Settings",
        "title_ar": "الحصة 19: لعبة مغامرات 3D 3: الجري السريع والتحكم بالرسوم المتحركة",
        "desc_en": "Normalizing movement vectors, magnitude speed checks, and linking player velocity to dynamic animation states.",
        "desc_ar": "معايرة متجهات الحركة وسرعتها، ضبط لوحة الأنيميتور، وربط حركة اللاعب بالرسوم المتحركة للجري والمشي بذكاء.",
        "story_ar": """<h3>🏃 بث الروح في البطل عبر الرسوم المتحركة للجري!</h3>البطل لا يجب أن يتحرك متجمداً كالحجر! اليوم سنتعلم المبدأ السحري الفخم: كيف نجعل البطل يمشي عندما نحرك المقود برفق، ويجري بحماس كبير عند تحريكه بقوة، ويقف في مكانه مستريحاً (Idle animation) عند ترك الأزرار!<br><br><b>🎯 أركان برمجة الأنيميشن ثلاثية الأبعاد:</b><ul><li>⚖️ <b>معايرة الحركة (Vector Normalization):</b> ضبط متجهات الحركة لكي لا يتحرك البطل بسرعة مضاعفة عند الجري بزاوية مائلة!</li><li>🖼️ <b>منظم الرسوم (Animator Controller):</b> المخطط التفاعلي الذي يحتوي على مقاطع الحركة ويوصل بينها بشروط سحرية.</li><li>⚡ <b>قيم التمازج (Blend Trees):</b> ميزة يونيتي المدهشة التي تمزج بين حركة المشي وحركة الجري تلقائياً حسب سرعة اللاعب!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> ربط لوحة Animator بالبطل وجعله يمشي ويجري ويقفز بشكل غاية في الواقعية والجمال!</div><br><h4>💻 كيف نرسل السرعة إلى الأنيميتور بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class RPGAnim : MonoBehaviour {
    private Animator animator;
    private CharacterController controller;

    void Start() {
        animator = GetComponent&lt;Animator&gt;();
        controller = GetComponent&lt;CharacterController&gt;();
    }

    void Update() {
        // حساب سرعة اللاعب الفعلية ثلاثية الأبعاد!
        float speed = controller.velocity.magnitude;
        // إرسال السرعة للأنيميتور لتمزج بين المشي والجري تلقائياً!
        animator.SetFloat("Speed", speed); 
    }
}</code></pre><br><p>دعنا نشغل الكود التالي لتفعيل محاكي الرسوم المتحركة الذكي! 🌟🚀</p>""",
        "story_en": """<h3>🏃 Breathing Life into Your Hero with 3D Animations!</h3>A hero shouldn't slide around frozen like a statue! Today we learn a beautiful concept: how to play a relaxed 'Idle' animation when standing still, transition to a gentle 'Walk' on slight key presses, and trigger an energetic 'Run' at full velocity!<br><br><b>🎯 3D Animation Concepts:</b><ul><li>⚖️ <b>Vector Normalization:</b> Scaling movement vectors so diagonal running doesn't speed up our hero double time!</li><li>🖼️ <b>Animator Controller:</b> The state machine grid inside Unity that manages animation clip transitions.</li><li>⚡ <b>Blend Trees:</b> Unity's magical tool that blends walking and running frames dynamically based on character speed variables!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Constructing an Animator Controller and wiring up beautiful, fluid character run cycles!</div><br><h4>💻 C# Speed-to-Animator Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class RPGAnim : MonoBehaviour {
    private Animator animator;
    private CharacterController controller;

    void Start() {
        animator = GetComponent&lt;Animator&gt;();
        controller = GetComponent&lt;CharacterController&gt;();
    }

    void Update() {
        // Calculate 3D velocity magnitude!
        float speed = controller.velocity.magnitude;
        // Feed speed value into the Blend Tree!
        animator.SetFloat("Speed", speed);
    }
}</code></pre><br><p>Let's run the animation controller script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine a flipbook: when you flip the pages slowly, the stick figure walks. When you flip the pages super fast, the figure runs! Speed in C# tells the Animator how fast to flip the pages!",
        "simple_ar": "تخيل دفتر رسوم ورقي متحرك: عندما تقلب الأوراق ببطء، يبدو الرجل الورقي وهو يمشي. وعندما تقلبها بسرعة كبيرة، يبدو كأنه يجري بحماس! كود السي شارب يخبر المنظم (Animator) بمدى سرعة تقليب تلك الصفحات الفنية!",
        "hint_en": "Type: <code>print('Animator Blend Tree & Speed Parameter Connected!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Animator Blend Tree & Speed Parameter Connected!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>Animator Blend Tree & Speed Parameter Connected!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>Animator Blend Tree & Speed Parameter Connected!</code>",
        "starter_code": "# اكتب كود تفعيل منظم الحركة والأنيميتور التفاعلي هنا:\n",
        "pills": [
            {
                "label": "تشغيل الرسوم المتحركة / Load Animator Controller",
                "code": "print('Animator Blend Tree & Speed Parameter Connected!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Animator Blend Tree & Speed Parameter Connected!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكي تبديل حالات الرسوم المتحركة",
        "homework_title_en": "🏠 Magic Home Challenge: Animation State Switch Log",
        "homework_desc_ar": "قم بكتابة كود يعبر عن سرعات مختلفة للاعب: إذا كانت السرعة 0 اطبع 'Playing Idle...', وإذا كانت 5 اطبع 'Playing Walk!', وإذا كانت 10 اطبع 'Playing Run!' لمحاكاة شجرة التمازج!",
        "homework_desc_en": "Write a script that prints the animation state based on speed: if speed is 0 print 'Playing Idle...', if 5 print 'Playing Walk!', and if 10 print 'Playing Run!'!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة تبديل حالات الأنيميشن هنا:\n"
    },
    {
        "id": 20,
        "badge_icon": "🤖",
        "badge_title": "AI Master Medal",
        "title_en": "Session 20: RPG 3D 4: Enemy AI & NavMesh Pathfinding",
        "title_ar": "الحصة 20: لعبة مغامرات 3D 4: ذكاء الأعداء وملاحقة البطل (NavMesh)",
        "desc_en": "Implementing NavMesh pathfinding, setting up AI navigation agents, and scripting enemy follow behavior.",
        "desc_ar": "صنع شبكة الملاحة والذكاء الاصطناعي، استخدام وكيل الملاحة للأعداء، وكتابة أوامر ملاحقة البطل أينما ذهب وتفادي الحواجز.",
        "story_ar": """<h3>🤖 ذكاء الأعداء وملاحقة الأبطال عبر شبكة الملاحة ثلاثية الأبعاد!</h3>اليوم سنقوم بصنع شيء مذهل ومرعب! سنبرمج وحشاً يتحرك بالذكاء الاصطناعي (AI) أينما ذهبت! سيلاحقك ويتفادى الصخور والجدران بذكاء شديد وكأنه يفكر ويرسم خريطة طريق كاملة للقبض عليك!<br><br><b>🎯 مكونات الذكاء الاصطناعي في يونيتي:</b><ul><li>🕸️ <b>شبكة الملاحة (NavMesh):</b> خريطة رقمية سرية نقوم بخبزها (Baking) داخل عالم اللعبة تحدد للعدو أين يستطيع المشي وأين توجد الحوائط المغلقة.</li><li>🤖 <b>وكيل الملاحة (NavMeshAgent):</b> المكون السوبر ذكي الذي نضعه على العدو ليعطيه الذكاء لحساب أقصر طريق نحو الهدف!</li><li>🎯 <b>ملاحقة الهدف (SetDestination):</b> أمر برمجي بسيط نكتبه بالسي شارب ليقوم العدو بتحديث مساره نحو موقع البطل باستمرار.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> تفعيل ذكاء العدو بالكامل ومطاردته للبطل مع التجنب التلقائي للحواجز والصخور!</div><br><h4>💻 كيف نبرمج ملاحقة الذكاء الاصطناعي للبطل بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using UnityEngine.AI; // مكتبة الذكاء الاصطناعي والملاحة السحرية

public class EnemyAI : MonoBehaviour {
    private NavMeshAgent agent;
    public Transform targetPlayer;

    void Start() {
        agent = GetComponent&lt;NavMeshAgent&gt;();
    }

    void Update() {
        // مطاردة البطل أينما ذهب في الفراغ ثلاثي الأبعاد!
        agent.SetDestination(targetPlayer.position);
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لتفعيل شبكة ذكاء العدو التفاعلية! 🌟🚀</p>""",
        "story_en": """<h3>🤖 Dynamic AI Pathfinding & Enemy Tracker!</h3>Today we build something incredibly cool and slightly scary! We will script an AI enemy that chases you around the map. The enemy will dynamically avoid rocks, walls, and drops like a real thinking creature!<br><br><b>🎯 AI Pathfinding Architecture:</b><ul><li>🕸️ <b>Navigation Mesh (NavMesh):</b> The secret walkability blueprint we 'bake' into our level so the AI knows where it's safe to step and where walls are.</li><li>🤖 <b>NavMeshAgent:</b> The intelligent pathfinder component we attach to our enemy so they navigate easily.</li><li>🎯 <b>Target Tracking (SetDestination):</b> The simple C# function we run to update the enemy's path toward our player's live position!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Building walkable terrain maps and scripting a fully functional AI tracking enemy!</div><br><h4>💻 C# AI Tracking Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using UnityEngine.AI;

public class EnemyAI : MonoBehaviour {
    private NavMeshAgent agent;
    public Transform targetPlayer;

    void Start() {
        agent = GetComponent&lt;NavMeshAgent&gt;();
    }

    void Update() {
        // Track player coordinate continuously!
        agent.SetDestination(targetPlayer.position);
    }
}</code></pre><br><p>Let's run the AI pathfinding script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine using Google Maps: NavMesh is the road network, NavMeshAgent is your GPS, and SetDestination is typing in your friend's home address to find the fastest way to get there!",
        "simple_ar": "تخيل أنك تستخدم خرائط جوجل: شبكة الملاحة (NavMesh) هي شوارع المدينة، ووكيل الملاحة (NavMeshAgent) هو نظام الـ GPS، وأمر (SetDestination) هو كتابة عنوان صديقك ليجد الـ GPS أسرع طريق إليه تفاعلياً!",
        "hint_en": "Type: <code>print('NavMesh Baked & AI Pathfinding Active!')</code> and click Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('NavMesh Baked & AI Pathfinding Active!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>NavMesh Baked & AI Pathfinding Active!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>NavMesh Baked & AI Pathfinding Active!</code>",
        "starter_code": "# اكتب كود تفعيل شبكة ذكاء العدو الملاحي هنا:\n",
        "pills": [
            {
                "label": "تشغيل مطاردة الذكاء الاصطناعي / Start Enemy AI",
                "code": "print('NavMesh Baked & AI Pathfinding Active!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "NavMesh Baked & AI Pathfinding Active!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكي نظام رصد أهداف الذكاء الاصطناعي",
        "homework_title_en": "🏠 Magic Home Challenge: AI Distance Calculator",
        "homework_desc_ar": "اكتب كوداً يحاكي اقتراب العدو: اطبع المسافة بداية من 15 متر وتتناقص بمقدار 5 أمتار في كل خطوة حتى تصل لصفر واطبع 'Target in Attack Range!'!",
        "homework_desc_en": "Write a script that tracks AI distance to target: decrease distance from 15 meters by 5 in a loop, and print 'Target in Attack Range!' when it reaches 0!",
        "homework_starter_code": "# تحدي المنزل: اكتب محاكاة اقتراب الذكاء الاصطناعي هنا:\n"
    },
    {
        "id": 21,
        "badge_icon": "⚔️",
        "badge_title": "Sword Master Medal",
        "title_en": "Session 21: RPG 3D 5: Static Data & Sword Attack",
        "title_ar": "الحصة 21: لعبة مغامرات 3D 5: ضربات السيف السحرية وتأكيد الضرر",
        "desc_en": "Working with static variables, Awake method lifecycle, sword animation hit checks, and enemy damage.",
        "desc_ar": "استخدام المتغيرات المشتركة، دورة حياة الكائنات بـ Awake، تفعيل هجوم السيف ورصد الاصطدامات بالعدو لتخفيض صحته.",
        "story_ar": """<h3>⚔️ هجوم السيف الساحق ورصد إصابة الوحوش!</h3>الآن بدأت الإثارة الكبرى! سنتعلم كيف نبرمج بطلنا ليقوم بهزيمة الأعداء والوحوش عندما نضغط بزر الفأرة الأيسر ليقوم بضربهم بالسيف السحري، ورصد الاصطدامات لتخفيض صحتهم وتدميرهم!<br><br><b>🎯 الأركان البرمجية التفاعلية لليوم:</b><ul><li>🌀 <b>دالة اليقظة (Awake Method):</b> الدالة السوبر سريعة التي تعمل قبل Start لتجهيز الأسلحة والتروس البرمجية.</li><li>🔒 <b>البيانات الثابتة (Static Data):</b> المتغيرات المشتركة بين جميع الأكواد لتسهيل إرسال قوة الضربة من البطل للعدو.</li><li>💥 <b>تأكيد الضرر (Hit Detection & Damage):</b> رصد اصطدام السيف بالوحش لتخفيض صحته وتدميره باحترافية!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> برمجة حركة هجوم البطل بالسيف ورصد إصابة الوحوش وتدميرها فور نفاد طاقتها!</div><br><h4>💻 كيف نبرمج تخفيض صحة العدو عند إصابته بالسيف بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class EnemyHealth : MonoBehaviour {
    public int health = 100;

    public void TakeDamage(int damageAmount) {
        health -= damageAmount;
        Debug.Log("آخ! الوحش تلقى ضربة! الصحة المتبقية: " + health);

        if (health &lt;= 0) {
            Debug.Log("رائع! هُزم الوحش الشرير وتلاشى! 🏆🎉");
            Destroy(gameObject); // تدمير مجسم الوحش
        }
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لمحاكاة ضربات السيف السريعة بنجاح! 🌟🚀</p>""",
        "story_en": """<h3>⚔️ Sword Swing Action & Dynamic Hit Detection!</h3>Now the true battles begin! Today we script our hero to brandish a legendary sword when we left-click. We will code high-fidelity hit detection that lowers the enemy's HP and destroys them in a flurry of sparks!<br><br><b>🎯 Battle Code Concepts:</b><ul><li>🌀 <b>Awake Method:</b> The super-fast Unity lifecycle method that boots before 'Start' to prep inventory components.</li><li>🔒 <b>Static Variables:</b> Shared global variables that allow our player's attack to pass damage values instantly to the enemy.</li><li>💥 <b>Damage Mechanics:</b> Hooking triggers to subtract health and dispatching enemies when their health reaches 0!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Coding sword combat mechanics, hit colliders, and dynamic enemy health depletion!</div><br><h4>💻 C# Enemy Take Damage Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class EnemyHealth : MonoBehaviour {
    public int health = 100;

    public void TakeDamage(int damageAmount) {
        health -= damageAmount;
        Debug.Log("Ouch! Enemy took damage. HP left: " + health);

        if (health &lt;= 0) {
            Debug.Log("Hooray! The evil minion is defeated! 🏆🎉");
            Destroy(gameObject); // Disappear enemy
        }
    }
}</code></pre><br><p>Let's run the combat simulation script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine a balloon: it has air inside (health). When you poke it with a needle (sword hit), the balloon instantly pops (Destroy GameObject) because its air level hit 0!",
        "simple_ar": "تخيل بالوناً منفوخاً بالكامل بالهواء (يمثل صحة العدو). عندما تقوم بنخزه بدبوس صغير (يمثل ضربة السيف)، ينفجر البالون فوراً ويتلاشى (Destroy) لأن منسوب الهواء وصل إلى الصفر!",
        "hint_en": "Type: <code>print('Awake Called & Sword Collision Attack System Ready!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Awake Called & Sword Collision Attack System Ready!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>Awake Called & Sword Collision Attack System Ready!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>Awake Called & Sword Collision Attack System Ready!</code>",
        "starter_code": "# اكتب كود محاكاة هجوم السيف ورصد الاصطدام بالعدو هنا:\n",
        "pills": [
            {
                "label": "تشغيل ضربة السيف / Sword Swing Hit",
                "code": "print('Awake Called & Sword Collision Attack System Ready!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Awake Called & Sword Collision Attack System Ready!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: محاكي الصحة وسقوط الوحوش",
        "homework_title_en": "🏠 Magic Home Challenge: HP Depletion Tracker",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يعلن صحة وحش 60 نقطة، ويطرح منها 20 في كل ضربة، ويطبع الصحة المتبقية 3 مرات متتالية حتى يصبح 0 تماماً!",
        "homework_desc_en": "Write a script that tracks HP depletion: start with 60 HP, subtract 20 in a loop, and print 'Enemy HP: X' for 3 swings until it hits 0!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة هبوط نقاط صحة الوحش هنا:\n"
    },
    {
        "id": 22,
        "badge_icon": "❤️",
        "badge_title": "UI Health Bar Medal",
        "title_en": "Session 22: RPG 3D 6: Health UI & Floating Scrollbar",
        "title_ar": "الحصة 22: لعبة مغامرات 3D 6: شاشات الصحة وشريط الطاقة العائم",
        "desc_en": "Creating character health systems, implementing world-space canvas, and floating health UI scrollbars.",
        "desc_ar": "صنع نظام طاقة وصحة متكامل للاعبين، إعداد لوحة العرض في الفراغ ثلاثي الأبعاد، وعرض أشرطة الصحة العائمة فوق الشخصيات.",
        "story_ar": """<h3>❤️ شريط الصحة العائم فوق رأس البطل والوحوش!</h3>ألعابنا تحتاج إلى مؤشر بصري واضح يوضح الصحة والطاقة! اليوم سنتعلم كيف نصنع شريط طاقة أحمر جميل عائم فوق رأس اللاعب والوحوش يتحرك معهم في الفراغ ثلاثي الأبعاد ويتناقص عند تلقي الضربات بشكل مدهش وحماسي!<br><br><b>🎯 مبادئ واجهات الألعاب ثلاثية الأبعاد:</b><ul><li>❤️ <b>نظام الصحة (Health System):</b> دوال لزيادة الصحة عند التقاط التفاح والقلوب ونقصها عند الضرر.</li><li>🖥️ <b>لوحة الفضاء (World Space Canvas):</b> لوحة عرض مميزة لا تلتصق بالمتصفح، بل تطفو في الفضاء ثلاثي الأبعاد فوق رأس المجسمات!</li><li>📊 <b>أشرطة التمرير والمنزلقات (UI Sliders):</b> أشرطة مخصصة ترتبط تلقائياً بقيمة الصحة لتملأ باللون الأخضر أو تفرغ باللون الأحمر تفاعلياً.</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> تصميم وتفعيل شريط الصحة العائم فوق الأعداء وتعديل قيمته ديناميكياً!</div><br><h4>💻 كيف نربط صحة اللاعب بشريط التمرير بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using UnityEngine.UI; // استدعاء واجهات المستخدم السحرية

public class HealthBar : MonoBehaviour {
    public Slider healthSlider;
    public int maxHealth = 100;
    private int currentHealth;

    void Start() {
        currentHealth = maxHealth;
        healthSlider.maxValue = maxHealth;
        healthSlider.value = maxHealth; // ملء الشريط بالكامل!
    }

    public void ReduceHealth(int amount) {
        currentHealth -= amount;
        healthSlider.value = currentHealth; // تحديث الشريط بصرياً فوراً!
    }
}</code></pre><br><p>دعنا نشغل كود محاكاة تحديث شريط الصحة التفاعلي الممتع! 🌟🚀</p>""",
        "story_en": """<h3>❤️ Dynamic Floating Health Bars!</h3>Every high-quality game needs visual cues for HP! Today we learn to construct a beautiful crimson health bar that floats dynamically in 3D world space above our characters, rotating with them and updating dynamically on every damage tick!<br><br><b>🎯 3D UI & Health Concepts:</b><ul><li>❤️ <b>Health Logic:</b> Formulating heal methods for item pickups and damage callbacks for enemies.</li><li>🖥️ <b>World Space Canvas:</b> A specialized UI canvas that floats freely inside the 3D level geometry rather than locking flat on the screen!</li><li>📊 <b>UI Sliders & Scrollbars:</b> Standard value bars linked to character health values to show red/green gauges dynamically!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Placing dynamic floating health displays above enemies and updating their percentages!</div><br><h4>💻 C# UI Slider Health Connector:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;
using UnityEngine.UI;

public class HealthBar : MonoBehaviour {
    public Slider healthSlider;
    public int maxHealth = 100;
    private int currentHealth;

    void Start() {
        currentHealth = maxHealth;
        healthSlider.maxValue = maxHealth;
        healthSlider.value = maxHealth; // Fill to the brim!
    }

    public void ReduceHealth(int amount) {
        currentHealth -= amount;
        healthSlider.value = currentHealth; // Instantly shrink bar visually!
    }
}</code></pre><br><p>Let's run the health UI compiler script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine a phone battery bar: when you play heavy games, the green bar shrinks. Charging is like eating a golden apple - the bar fills back up. Floating UI is that battery bar floating directly above your character!",
        "simple_ar": "تخيل مؤشر شحن بطارية هاتفك: عند لعب ألعاب ثقيلة، يتقلص الشريط الأخضر تدريجياً. وشحن الهاتف هو بمثابة التقاط تفاحة ذهبية فيعيد ملء شريط البطارية بالكامل! شريط الصحة العائم يطفو تماماً فوق رأس شخصيتك المذهلة!",
        "hint_en": "Type: <code>print('World Space Canvas Loaded & Floating HP Bars Ready!')</code> and hit Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('World Space Canvas Loaded & Floating HP Bars Ready!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact phrase: <code>World Space Canvas Loaded & Floating HP Bars Ready!</code>",
        "challenge_ar": "اطبع الجملة التالية تماماً: <code>World Space Canvas Loaded & Floating HP Bars Ready!</code>",
        "starter_code": "# اكتب كود تفعيل لوحة أشرطة الصحة ثلاثية الأبعاد هنا:\n",
        "pills": [
            {
                "label": "تشغيل شريط الصحة / Load World HP UI",
                "code": "print('World Space Canvas Loaded & Floating HP Bars Ready!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "World Space Canvas Loaded & Floating HP Bars Ready!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: مؤشر الصحة البصري",
        "homework_title_en": "🏠 Magic Home Challenge: HP Visual Gauge Log",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يحاكي تحديث قيمة مؤشر الطاقة: اطبع 'HP: [█████] 100%'، ثم اطبع 'HP: [████░] 80%'، ثم 'HP: [███░░] 60%' لمحاكاة النقصان التدريجي للشريط!",
        "homework_desc_en": "Write a script that outputs a dynamic ASCII gauge: print 'HP: [█████] 100%', then 'HP: [████░] 80%', and finally 'HP: [███░░] 60%' to simulate UI depletion!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود رسم مؤشر الصحة التفاعلي هنا:\n"
    },
    {
        "id": 23,
        "badge_icon": "🪙",
        "badge_title": "Treasure Collector Medal",
        "title_en": "Session 23: RPG 3D 7: Collectibles & 3D Spatial Audio",
        "title_ar": "الحصة 23: جمع الكنوز وتفعيل المؤثرات الصوتية ثلاثية الأبعاد",
        "desc_en": "Coding 3D item collection triggers, adding spatial audio sources, and implementing 3D listener settings.",
        "desc_ar": "برمجة التقاط الكنوز والصناديق ثلاثية الأبعاد، تفعيل الأصوات الحية والواقعية، وإعداد مستمع الصوت المجسم.",
        "story_ar": """<h3>🪙 جمع الذهب وتأثيرات الصوت ثلاثية الأبعاد الحية!</h3>عالمنا ثلاثي الأبعاد يحتاج لأصوات واقعية! اليوم سنتعلم كيف نصنع صناديق كنز ذهبية لامعة في غابات لعبتنا، وكيف نجعل الصوت يبدو مجسماً (3D Spatial Audio): فإذا اقتربت من صندوق الكنز على اليمين تسمع صوته في سماعة اليمين، وإذا ابتعدت يتلاشى الصوت تدريجياً بشكل حقيقي فائق المتعة والجمال!<br><br><b>🎯 أساسيات هندسة الأصوات التفاعلية ثلاثية الأبعاد:</b><ul><li>🪙 <b>الكنوز التفاعلية (3D Collectibles):</b> تجميع القلوب والعملات الذهبية والمفاتيح لفتح البوابات الكبيرة.</li><li>🔊 <b>الصوت المجسم (3D Spatial Audio):</b> ضبط الصوت في الفراغ ثلاثي الأبعاد بحيث يرتفع وينخفض بناءً على قربك من المصدر.</li><li>🎧 <b>مصدر ومستمع الصوت (Audio Source & Audio Listener):</b> المصدر هو الكنز الذي يصدر اللحن، والمستمع يوضع على أذن بطلنا ليرصد الأصوات تلقائياً!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> نشر صناديق كنز ذهبية وتفعيل الصوت المجسم ثلاثي الأبعاد بجدارة!</div><br><h4>💻 كيف نبرمج تشغيل صوت جمع الكنز في الفراغ بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class CoinCollector : MonoBehaviour {
    public AudioClip coinSound;

    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Player")) {
            // تشغيل صوت جمع العملة المجسم ثلاثي الأبعاد في موقع الكنز بدقة!
            AudioSource.PlayClipAtPoint(coinSound, transform.position);
            Debug.Log("رائع! التقاط العملة الذهبية مع صوت تفاعلي مذهل! 🪙🔊");
            Destroy(gameObject);
        }
    }
}</code></pre><br><p>دعنا نشغل كود محاكاة الرنين التفاعلي للأصوات ثلاثية الأبعاد بنجاح! 🌟🚀</p>""",
        "story_en": """<h3>🪙 3D Treasure Hunts & Spatial Audio Spells!</h3>A premium 3D world needs lifelike, immersive sounds! Today we learn to place gold-gilded chests inside our wild forest, and implement **3D Spatial Audio** - where the audio physically gets louder in your right headphone speaker when you walk right, and fades beautifully as you sprint away!<br><br><b>🎯 Immersive Audio Concepts:</b><ul><li>🪙 <b>3D Collectibles:</b> Spawning golden coins and glowing keys to open secret dungeon chambers.</li><li>🔊 <b>3D Spatial Blending:</b> Tuning the 3D-spread engine in Unity so sounds dynamically morph depending on player coordinates.</li><li>🎧 <b>Source & Listener Pair:</b> Positioning an AudioSource component on the treasure chest and an AudioListener on our hero's ears!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Spawning magical chests, layering forest music loops, and rigging dynamic 3D sound effects!</div><br><h4>💻 C# 3D Sound Trigger Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class CoinCollector : MonoBehaviour {
    public AudioClip coinSound;

    void OnTriggerEnter(Collider other) {
        if (other.CompareTag("Player")) {
            // Play a gorgeous 3D spatial clip exactly at the coin's location!
            AudioSource.PlayClipAtPoint(coinSound, transform.position);
            Debug.Log("Jackpot! Gold coin acquired with immersive audio! 🪙🔊");
            Destroy(gameObject);
        }
    }
}</code></pre><br><p>Let's run the spatial sound simulator script below to test! 🌟🚀</p>""",
        "simple_en": "Imagine listening to a honeybee flying around you: you know where the bee is even with your eyes closed because your ears track the sound. 3D Spatial Audio does exactly that with your game treasures!",
        "simple_ar": "تخيل أنك تستمع لنحلة تطير حولك: ستعرف أين هي النحلة بدقة حتى وعيناك مغمضتان لأن أذنيك تلاحقان مصدر الصوت في الهواء. هندسة الأصوات ثلاثية الأبعاد تفعل ذلك تماماً مع كنوز ألعابنا!",
        "hint_en": "Type: <code>print('3D spatial audio & item collection active!')</code> and press Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('3D spatial audio & item collection active!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact confirmation: <code>3D spatial audio & item collection active!</code>",
        "challenge_ar": "اطبع التأكيد التالي تماماً: <code>3D spatial audio & item collection active!</code>",
        "starter_code": "# اكتب كود تفعيل تجميع الكنوز والأصوات المجسمة ثلاثية الأبعاد هنا:\n",
        "pills": [
            {
                "label": "تشغيل الكنوز والأصوات المجسمة / Start 3D Audio",
                "code": "print('3D spatial audio & item collection active!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "3D spatial audio & item collection active!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: رنين المؤثرات الصوتية ثلاثية الأبعاد",
        "homework_title_en": "🏠 Magic Home Challenge: 3D Spatial Sound Proximity Tracker",
        "homework_desc_ar": "اكتب كوداً تفاعلياً يحاكي علو الصوت عند الاقتراب: اطبع 'Volume: 10% (Far)', ثم 'Volume: 50% (Closer)', ثم 'Volume: 100% (Jackpot!)' لمحاكاة الاقتراب من الكنز!",
        "homework_desc_en": "Write a script that simulates spatial audio volume: print 'Volume: 10% (Far)', then 'Volume: 50% (Closer)', and finally 'Volume: 100% (Jackpot!)'!",
        "homework_starter_code": "# تحدي المنزل: اكتب كود محاكاة علو الصوت التفاعلي هنا:\n"
    },
    {
        "id": 24,
        "badge_icon": "🌎",
        "badge_title": "Game Producer Legend Medal",
        "title_en": "Session 24: RPG 3D 8: UI, WebGL & Publishing Game",
        "title_ar": "الحصة 24: لعبة مغامرات 3D 8: الواجهات النهائية، تصدير الويب ونشر لعبتك",
        "desc_en": "Designing final menus, exporting project as WebGL build, publishing to Itch.io, and final course wrap-up.",
        "desc_ar": "تصميم قائمة اللعب والبدء، تصدير المشروع ليعمل كصفحة ويب (WebGL)، نشر لعبتك على منصة Itch.io العالمية للاستعراض، وتخريج الأبطال.",
        "story_ar": """<h3>🌎 حفل التخريج الكبرى ونشر لعبتك ثلاثية الأبعاد للعالم!</h3>يا بطل الأبطال، اليوم هو يوم الانتصار والاحتفال الكبير! بعد أن بنينا وبرمجنا لعبتنا ثلاثية الأبعاد بالكامل، سنتعلم كيف نجعلها تعمل مباشرة على متصفح الويب (WebGL) لكي يستطيع أي شخص في العالم فتح رابط لعبتك ولعبها فوراً من هاتفه أو حاسوبه، ونشرها على منصة الألعاب العالمية **Itch.io**!<br><br><b>🎯 الخطوات الأسطورية لدرس اليوم:</b><ul><li>🖥️ <b>تصميم قائمة البداية (Main Menu):</b> واجهة رئيسية مبهجة وزر خروج وتشغيل للعبة باحترافية.</li><li>🌐 <b>تصدير الويب (WebGL Build):</b> تحويل اللعبة بالكامل لتشتغل مباشرة داخل متصفحات الويب كرابط سحري!</li><li>🚀 <b>النشر العالمي (Publishing on Itch.io):</b> رفع لعبتك على أشهر منصة ألعاب للمستقلين في العالم لتتلقى تشجيعاً مذهلاً!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>مشروع اليوم التطبيقي:</b> الانتهاء من الواجهات بالكامل وتصدير لعبتك ورفعها على Itch.io وتخريجك كمهندس ألعاب أسطوري!</div><br><h4>💻 كيف نبرمج زر الخروج من اللعبة بالسي شارب؟</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class MainMenuActions : MonoBehaviour {
    public void StartGame() {
        UnityEngine.SceneManagement.SceneManager.LoadScene(1);
    }

    public void QuitGame() {
        // إغلاق اللعبة تماماً عند البناء النهائي!
        Application.Quit(); 
        Debug.Log("تم الخروج من اللعبة بنجاح! نراكم لاحقاً يا أبطال 👋🌟");
    }
}</code></pre><br><p>دعنا نشغل الكود بالأسفل لإتمام الدورة وتصدير لعبتك النهائية بنجاح مطلق! 🌟🚀</p>""",
        "story_en": """<h3>🌎 The Grand Graduation & Publishing Your 3D Masterpiece!</h3>Champion of champions, today is the day of absolute victory and grand celebration! Having designed, coded, and polished your 3D RPG adventure, we master **WebGL Compilation** - turning your game into a instant web page so anyone can play it from their phone or browser, and publish it on the global gaming portal **Itch.io**!<br><br><b>🎯 Legendary Production Steps:</b><ul><li>🖥️ <b>Start Menu Screen:</b> Designing professional game hubs with 'Play' and 'Quit Game' logic.</li><li>🌐 <b>WebGL Compilation:</b> Transforming your game files into lightweight HTML5 codes that run instantly inside web browsers.</li><li>🚀 <b>Global Publishing (Itch.io):</b> Uploading your game onto Itch.io to show off your talent to the entire world!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 4px; margin-top: 10px;'>🚀 <b>Hands-on Project:</b> Finalizing game menus, compiling WebGL builds, and earning your Game Producer Graduation Certificate!</div><br><h4>💻 C# Quit Game Trigger Script:</h4><pre style='background: #1e1e2f; color: #f8f8f2; padding: 12px; border-radius: 8px; font-family: monospace; direction: ltr; text-align: left; overflow-x: auto;'><code>using UnityEngine;

public class MainMenuActions : MonoBehaviour {
    public void StartGame() {
        UnityEngine.SceneManagement.SceneManager.LoadScene(1);
    }

    public void QuitGame() {
        // Terminate application completely!
        Application.Quit();
        Debug.Log("Game exited successfully. Goodbye, Champions! 👋🌟");
    }
}</code></pre><br><p>Let's run the graduation compiler script below to compile your WebGL game! 🌟🚀</p>""",
        "simple_en": "Imagine baking a delicious cake: WebGL is like putting your cake inside a beautiful glass display case so that all visitors can easily look at it and eat it instantly with one spoon!",
        "simple_ar": "تخيل أنك صنعت كعكة عيد ميلاد فائقة اللذة: تصدير الويب (WebGL) هو بمثابة وضع الكعكة في واجهة زجاجية براقة في واجهة المحل لكي يستطيع كل الزوار والمارة تذوقها والاستمتاع بها بملعقة واحدة تفاعلياً وبسرعة!",
        "hint_en": "Type: <code>print('Congratulations! WebGL game compiled & published successfully!')</code> and hit Run!",
        "hint_ar": "اكتب في المحاكي: <code>print('Congratulations! WebGL game compiled & published successfully!')</code> واضغط تشغيل!",
        "challenge_en": "Print the exact graduation message: <code>Congratulations! WebGL game compiled & published successfully!</code>",
        "challenge_ar": "اطبع رسالة التخرج التالية تماماً: <code>Congratulations! WebGL game compiled & published successfully!</code>",
        "starter_code": "# اكتب كود إنهاء وتصدير اللعبة النهائية ونشرها هنا:\n",
        "pills": [
            {
                "label": "حفل التخريج الكبرى / Publish 3D Game",
                "code": "print('Congratulations! WebGL game compiled & published successfully!')"
            }
        ],
        "validation_rules": {
            "required_output_text": "Congratulations! WebGL game compiled & published successfully!",
            "required_canvas": False
        },
        "homework_title_ar": "🏠 تحدي الأبطال المنزلي: رسالة تخرج مهندس الألعاب الأسطوري",
        "homework_title_en": "🏠 Magic Home Challenge: Game Producer Legacy Note",
        "homework_desc_ar": "يا مهندس المستقبل الموهوب، اكتب كوداً تفاعلياً يطبع جملة فخر برمجية: 'I am a Certified Game Developer!' لتخليد اسمك في لوحة شرف الأكاديمية العظيمة!",
        "homework_desc_en": "Write a legacy script that prints your graduation statement: 'I am a Certified Game Developer!' to commemorate your wonderful effort!",
        "homework_starter_code": "# تحدي المنزل: اكتب عبارة فخر تخرجك هنا يا مهندس الألعاب الأسطوري:\n"
    }
]

# Generate recap.json structure
recap_json = {
    "course": "Unity Game Development",
    "course_title": "Unity Game Development",
    "recap_title_ar": "🎯 المراجعة التفاعلية السريعة: تطوير الألعاب بمحرك Unity",
    "recap_title_en": "🎯 Quick & Visual Recap: Unity Game Development",
    "recap_subtitle_ar": "مرحباً بك يا بطل المستقبل! هذه مراجعة تفاعلية سريعة ومبسطة مدعومة بأكواد حقيقية لتلخيص كل حصة تعلمتها في كورس يونيتي، وتجهيزك للاختبار السوبر وحصد شهادتك الأسطورية! 🚀🌟",
    "recap_subtitle_en": "Welcome, hero! This is a quick, child-friendly review supported by code examples and explanations for each session you learned in the Unity course to help you remember concepts and ace your super exam! 🚀🌟",
    "sessions": []
}

for sess in sessions_data:
    recap_sess = {
        "session_title": f"💡 Session {sess['id']}: {sess['title_en']}",
        "session_title_ar": f"💡 الحصة {sess['id']}: {sess['title_ar']}",
        "targets": [sess["title_en"], sess["desc_en"]],
        "blocks": ["GameObject", "MonoBehaviour", "C# Script", "Unity Engine"],
        "project": sess["title_en"] + " Sandbox",
        "points": [
            {
                "icon": sess["badge_icon"],
                "title": sess["title_en"],
                "title_ar": sess["title_ar"],
                "desc": sess["desc_en"] + " " + sess["simple_en"],
                "desc_ar": sess["desc_ar"] + " " + sess["simple_ar"],
                "code": "using UnityEngine;\n\npublic class SessionSimulator : MonoBehaviour {\n    void Start() {\n        Debug.Log(\"" + sess["title_en"] + " Completed successfully!\");\n    }\n}"
            }
        ]
    }
    recap_json["sessions"].append(recap_sess)

# Generate games.json structure
games_json = {
    "course_id": "senior_unity",
    "course_title": "Unity Game Development",
    "course_subtitle_ar": "مرحباً بك يا بطل المستقبل الخارق! استعد لمغامرة برمجية غاية في التشويق والدلع لتصميم وبرمجة ألعابك ثنائية وثلاثية الأبعاد بمحرك Unity وتصديرها للعالم كله! 🚀🌟",
    "course_subtitle": "Welcome, future legend! Embark on a spectacular coding adventure in Unity Game Development. Unlock custom medals, solve daily challenges, and program your own digital masterpieces!",
    "xp_total": 2400,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": []
}

for sess in sessions_data:
    station = {
        "id": sess["id"],
        "badge_icon": sess["badge_icon"],
        "badge_title": f"{sess['badge_title']} - {sess['title_en']}",
        "title": f"Station {sess['id']}: {sess['title_en']}",
        "title_ar": f"المحطة {sess['id']}: {sess['title_ar']}",
        "desc": sess["title_en"] + " Sandbox",
        "story_ar": sess["story_ar"],
        "story": sess["story_en"],
        "simple": sess["simple_en"],
        "simple_ar": sess["simple_ar"],
        "hint": sess["hint_en"],
        "hint_ar": sess["hint_ar"],
        "challenge": sess["challenge_en"],
        "challenge_ar": sess["challenge_ar"],
        "starter_code": sess["starter_code"],
        "pills": sess["pills"],
        "validation_rules": sess["validation_rules"],
        "homework": {
            "title": sess["homework_title_en"],
            "title_ar": sess["homework_title_ar"],
            "desc": sess["homework_desc_en"],
            "desc_ar": sess["homework_desc_ar"],
            "code": sess["homework_starter_code"],
            "starter_code": sess["homework_starter_code"]
        }
    }
    games_json["stations"].append(station)

# Write to files
with open(recap_path, "w", encoding="utf-8") as f:
    json.dump(recap_json, f, ensure_ascii=False, indent=2)
print("Successfully generated recap.json for Unity Game Development!")

with open(games_path, "w", encoding="utf-8") as f:
    json.dump(games_json, f, ensure_ascii=False, indent=2)
print("Successfully generated games.json for Unity Game Development!")
