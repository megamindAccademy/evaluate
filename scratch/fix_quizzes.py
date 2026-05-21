import json
import os

db_path = r'c:\Users\rowan\Desktop\ev\evaluate\database'
web_quizzes_path = os.path.join(db_path, 'senior_web_design', 'quizzes')
adv_quizzes_path = os.path.join(db_path, 'senior_web_design_advanced', 'quizzes')

if not os.path.exists(web_quizzes_path): os.makedirs(web_quizzes_path)
if not os.path.exists(adv_quizzes_path): os.makedirs(adv_quizzes_path)

# Define Web Design (HTML/CSS) Quizzes
web_quizzes = {
    "quiz1.json": {
        "quiz_title": "Web Design - Quiz 1: HTML Core & Formatting",
        "quiz_name": "Quiz 1: HTML Core & Formatting",
        "questions": [
            {
                "q": "Which tag defines the title of a web page displayed in the browser tab?",
                "opts": ["&lt;head&gt;", "&lt;title&gt;", "&lt;meta&gt;", "&lt;body&gt;"],
                "correct": 1,
                "exp": "The &lt;title&gt; tag inside the &lt;head&gt; section sets the title that appears in the browser's title bar or tab!"
            },
            {
                "q": "How many sizes of headings are available in HTML?",
                "opts": ["3 headings", "5 headings", "6 headings", "8 headings"],
                "correct": 2,
                "exp": "HTML has 6 standard heading tags from &lt;h1&gt; (largest) to &lt;h6&gt; (smallest)."
            },
            {
                "q": "What is the correct way to add a line break in HTML?",
                "opts": ["&lt;break&gt;", "&lt;lb&gt;", "&lt;br&gt;", "&lt;hr&gt;"],
                "correct": 2,
                "exp": "The &lt;br&gt; tag creates a line break, pushing content to a new line without adding space like a paragraph."
            },
            {
                "q": "Which attribute specifies the source path of an image?",
                "opts": ["href", "src", "alt", "link"],
                "correct": 1,
                "exp": "The 'src' (source) attribute contains the URL or file path of the image you want to embed."
            },
            {
                "q": "Which target value opens a hyperlink in a brand new tab?",
                "opts": ["target=\"_self\"", "target=\"_parent\"", "target=\"_blank\"", "target=\"_top\""],
                "correct": 2,
                "exp": "Using target=\"_blank\" tells the browser to open the link in a fresh, new tab!"
            }
        ],
        "tasks": [
            {"title": "Setup basic structure", "desc": "Write a clean HTML structure with a heading 1 and paragraph."},
            {"title": "Embed a thumbnail link", "desc": "Create a link opening in a new tab wrapping an image."}
        ]
    },
    "quiz2.json": {
        "quiz_title": "Web Design - Quiz 2: Media & Interactive Forms",
        "quiz_name": "Quiz 2: Media & Interactive Forms",
        "questions": [
            {
                "q": "Which attribute displays play/pause controls on a native HTML5 video player?",
                "opts": ["autoplay", "controls", "loop", "muted"],
                "correct": 1,
                "exp": "The 'controls' attribute adds play, pause, volume, and full-screen controls to the audio or video element!"
            },
            {
                "q": "Which input type displays a color picker widget on modern browsers?",
                "opts": ["type=\"text\"", "type=\"color\"", "type=\"palette\"", "type=\"range\""],
                "correct": 1,
                "exp": "Setting type=\"color\" creates a magic color wheel where users can pick colors!"
            },
            {
                "q": "Which element groups related fields inside a form with a nice visual border?",
                "opts": ["&lt;form&gt;", "&lt;legend&gt;", "&lt;fieldset&gt;", "&lt;label&gt;"],
                "correct": 2,
                "exp": "The &lt;fieldset&gt; element draws a box outline around inputs, while &lt;legend&gt; adds a title label!"
            },
            {
                "q": "What attribute makes a form input field mandatory to fill out?",
                "opts": ["required", "placeholder", "mandatory", "validate"],
                "correct": 0,
                "exp": "Adding the 'required' attribute prevents form submission until the user types inside that field!"
            },
            {
                "q": "Which tag creates a drop-down selection menu in HTML?",
                "opts": ["&lt;select&gt;", "&lt;option&gt;", "&lt;form&gt;", "&lt;list&gt;"],
                "correct": 0,
                "exp": "The &lt;select&gt; tag creates the drop-down menu container, which holds &lt;option&gt; tags!"
            }
        ],
        "tasks": [
            {"title": "Implement registration form", "desc": "Design a form with required name text field and email field."},
            {"title": "Embed a looping sound", "desc": "Create an audio player that starts automatically and loops."}
        ]
    },
    "quiz3.json": {
        "quiz_title": "Web Design - Quiz 3: Containers & CSS Selectors",
        "quiz_name": "Quiz 3: Containers & CSS Selectors",
        "questions": [
            {
                "q": "What is the difference between a &lt;div&gt; and a &lt;span&gt;?",
                "opts": [
                    "Div is inline, span is block",
                    "Div is block-level, span is inline",
                    "Div is only for images, span for text",
                    "There is no difference"
                ],
                "correct": 1,
                "exp": "Div starts on a new line (block), whereas span stays inline on the same line to style words."
            },
            {
                "q": "How do you select a class named 'header' in CSS?",
                "opts": ["#header", ".header", "header", "*header"],
                "correct": 1,
                "exp": "In CSS, class selectors start with a dot (.), e.g. .header, while ID selectors start with a hash (#)."
            },
            {
                "q": "Where in an HTML document is the best place to link an external CSS stylesheet?",
                "opts": ["At the bottom of the &lt;body&gt;", "Inside the &lt;head&gt; section", "Inside the &lt;title&gt;", "Directly in the HTML tag"],
                "correct": 1,
                "exp": "Linking stylesheet links in the &lt;head&gt; block ensures the styles load before the page renders, preventing lags!"
            },
            {
                "q": "What does the 'A' in RGBA color stand for?",
                "opts": ["Active", "Anchor", "Alpha (Opacity)", "Aesthetic"],
                "correct": 2,
                "exp": "The Alpha channel in RGBA controls the transparency/opacity of the color, ranging from 0.0 (clear) to 1.0 (solid)."
            },
            {
                "q": "How do you write a hex code for a pure white background color?",
                "opts": ["#000000", "#ffffff", "#ff0000", "#111111"],
                "correct": 1,
                "exp": "#ffffff represents pure white, while #000000 represents pure black."
            }
        ],
        "tasks": [
            {"title": "Link external style", "desc": "Write standard link tag to import 'Delicious.css'."},
            {"title": "Target unique elements", "desc": "Write ID CSS selector targeting #main-banner."}
        ]
    },
    "quiz4.json": {
        "quiz_title": "Web Design - Quiz 4: Backgrounds & Spacings",
        "quiz_name": "Quiz 4: Backgrounds & Spacings",
        "questions": [
            {
                "q": "Which property stretches background images to cover the container fully?",
                "opts": ["background-size: contain;", "background-size: cover;", "background-repeat: no-repeat;", "background-size: auto;"],
                "correct": 1,
                "exp": "background-size: cover; scales the background picture so it covers the entire box, cropping margins if needed!"
            },
            {
                "q": "In the CSS Box Model, what is the space OUTSIDE the border?",
                "opts": ["Padding", "Content", "Margin", "Outline"],
                "correct": 2,
                "exp": "Margin is the spacing outside elements, borders are boundary edges, and padding is spacing inside elements!"
            },
            {
                "q": "Which background attachment locks the image on screen so it does not move during scroll?",
                "opts": ["scroll", "fixed", "local", "static"],
                "correct": 1,
                "exp": "background-attachment: fixed; locks the background in place, creating a beautiful parallax scrolling effect!"
            },
            {
                "q": "If you write margin: 10px 20px 30px 40px; which value represents the LEFT margin?",
                "opts": ["10px", "20px", "30px", "40px"],
                "correct": 3,
                "exp": "CSS values follow a clockwise order: Top (10px), Right (20px), Bottom (30px), Left (40px)!"
            },
            {
                "q": "How do you set a solid, red border with a thickness of 3 pixels?",
                "opts": ["border: 3px solid red;", "border: solid red 3px;", "border-style: red solid 3px;", "border: 3px red;"],
                "correct": 0,
                "exp": "The shorthand 'border' accepts border-width (3px), border-style (solid), and border-color (red) in one neat line!"
            }
        ],
        "tasks": [
            {"title": "Center a Box", "desc": "Apply margin 'auto' and specify a percentage width on a div."},
            {"title": "Set Hero Background", "desc": "Set cover centered background image without repeating."}
        ]
    },
    "quiz5.json": {
        "quiz_title": "Web Design - Quiz 5: Typography & Advanced Layout",
        "quiz_name": "Quiz 5: Typography & Advanced Layout",
        "questions": [
            {
                "q": "Which typography property controls reading directions like right-to-left for Arabic?",
                "opts": ["text-align", "direction: rtl;", "text-transform", "letter-spacing"],
                "correct": 1,
                "exp": "direction: rtl; aligns reading structures from right-to-left, which is required for Arabic fonts!"
            },
            {
                "q": "What happens when you set text-transform to capitalize?",
                "opts": [
                    "All letters become uppercase",
                    "All letters become lowercase",
                    "The first letter of every word becomes uppercase",
                    "No changes occur"
                ],
                "correct": 2,
                "exp": "capitalize changes the first letter of each word to uppercase, while uppercase changes all letters!"
            },
            {
                "q": "Which property aligns elements left/right of their container and allows text wrapping?",
                "opts": ["clear", "overflow", "float", "display"],
                "correct": 2,
                "exp": "float allows elements (like images) to hug borders, letting textual paragraphs wrap smoothly around them!"
            },
            {
                "q": "Which overflow value adds scrollbars to a box ONLY when content exceeds size bounds?",
                "opts": ["visible", "hidden", "scroll", "auto"],
                "correct": 3,
                "exp": "overflow: auto; is smart! It only shows scrollbars if the text is too large to fit in the box."
            },
            {
                "q": "Which pseudo-class styles a hyperlink when the user's cursor hovering over it?",
                "opts": ["a:active", "a:visited", "a:hover", "a:focus"],
                "correct": 2,
                "exp": "a:hover activates styling rules the instant a student hovers their cursor over link buttons!"
            }
        ],
        "tasks": [
            {"title": "Style navigation items", "desc": "Design a block link element transforming color and decoration on hover."},
            {"title": "Adjust letter spacing", "desc": "Add letter spacing and bold font-weight to headers."}
        ]
    },
    "quiz6.json": {
        "quiz_title": "Web Design - Quiz 6: Positioning & Visual Animations",
        "quiz_name": "Quiz 6: Positioning & Visual Animations",
        "questions": [
            {
                "q": "Which position locks an element to a fixed spot relative to the viewport window?",
                "opts": ["static", "relative", "fixed", "absolute"],
                "correct": 2,
                "exp": "position: fixed; sticks elements (like sticky headers) to screen borders, ignoring page scroll moves!"
            },
            {
                "q": "What rule defines the visual states of a CSS animation at specific percentage timeline frames?",
                "opts": ["@animate", "@keyframes", "@transitions", "@pulse"],
                "correct": 1,
                "exp": "The @keyframes rule declares what elements look like at points along the timeline (e.g. 0%, 50%, 100%)!"
            },
            {
                "q": "How do you loop a CSS animation infinitely?",
                "opts": [
                    "animation-iteration-count: infinite;",
                    "animation-loop: true;",
                    "animation-repeat: forever;",
                    "animation-duration: infinite;"
                ],
                "correct": 0,
                "exp": "Setting animation-iteration-count: infinite; makes your graphic spin, pulse, or move forever!"
            },
            {
                "q": "What is the correct syntax for adding a drop-shadow glow to text?",
                "opts": ["box-shadow", "text-shadow: 2px 2px 5px red;", "text-glow: red;", "border-shadow"],
                "correct": 1,
                "exp": "text-shadow accepts horizontal offset (2px), vertical offset (2px), blur (5px), and color (red)!"
            },
            {
                "q": "How do you load Font Awesome icons into a web page?",
                "opts": [
                    "Using &lt;img&gt; elements",
                    "Linking the CDN inside &lt;head&gt; and using &lt;i&gt; class tags",
                    "Copy pasting the SVG files inside &lt;p&gt;",
                    "Icons load automatically in HTML"
                ],
                "correct": 1,
                "exp": "Link the CDN inside head, and use class tags like &lt;i class=\"fas fa-fire\"&gt;&lt;/i&gt;!"
            }
        ],
        "tasks": [
            {"title": "Implement pulse animation", "desc": "Write keyframes to scale element and assign to buttons infinitely."},
            {"title": "Design a shadow card", "desc": "Style a box with box-shadow offsets and relative position."}
        ]
    }
}

# Define Web Design Advanced (Bootstrap & JS) Quizzes
adv_quizzes = {
    "quiz1.json": {
        "quiz_title": "Web Design Advanced - Quiz 1: Bootstrap & CSS Flexbox",
        "quiz_name": "Quiz 1: Bootstrap & CSS Flexbox",
        "questions": [
            {
                "q": "What tag is used to link the Bootstrap CSS framework from a CDN?",
                "opts": ["&lt;script&gt;", "&lt;style&gt;", "&lt;link rel=\"stylesheet\" href=\"...\"&gt;", "&lt;meta&gt;"],
                "correct": 2,
                "exp": "To link Bootstrap CDN stylesheets, we use a link tag inside the &lt;head&gt; section!"
            },
            {
                "q": "Which parent display initializes the Flexbox layout system?",
                "opts": ["display: block;", "display: inline-block;", "display: flex;", "display: grid;"],
                "correct": 2,
                "exp": "display: flex; tells the browser to arrange all direct children of this container as flexible items."
            },
            {
                "q": "Which property wraps flex items onto a new line when they run out of space?",
                "opts": ["flex-direction", "flex-wrap: wrap;", "justify-content", "align-items"],
                "correct": 1,
                "exp": "flex-wrap: wrap; wraps child items to fresh rows dynamically as soon as container widths fill up!"
            },
            {
                "q": "Which justify-content value distributes space evenly, leaving equal gaps between and around boxes?",
                "opts": ["flex-start", "center", "space-between", "space-around"],
                "correct": 3,
                "exp": "space-around distributes items evenly, leaving standard spaces on both sides of each flex box!"
            },
            {
                "q": "If flex-direction is set to column, how do elements stack?",
                "opts": ["Horizontally", "Vertically on top of each other", "Flipped backward", "Diagonal layouts"],
                "correct": 1,
                "exp": "Setting column direction rotates axes, stacking boxes vertically like building blocks!"
            }
        ],
        "tasks": [
            {"title": "Link Bootstrap", "desc": "Write a clean Bootstrap link tag in head section."},
            {"title": "Center flex box", "desc": "Align elements centered horizontally and vertically using flex."}
        ]
    },
    "quiz2.json": {
        "quiz_title": "Web Design Advanced - Quiz 2: Utilities & Responsive Grids",
        "quiz_name": "Quiz 2: Utilities & Responsive Grids",
        "questions": [
            {
                "q": "What padding does the Bootstrap utility class 'p-3' represent?",
                "opts": ["Small padding", "Medium padding", "No padding", "Maximum padding"],
                "correct": 1,
                "exp": "Bootstrap spacing utilities scale from 1 (small) to 5 (large). p-3 provides nice medium spacing!"
            },
            {
                "q": "The powerful Bootstrap grid system is based on how many columns in a row?",
                "opts": ["6 columns", "10 columns", "12 columns", "16 columns"],
                "correct": 2,
                "exp": "The grid system divides screens into exactly 12 imaginary columns! You partition sizes to equal 12."
            },
            {
                "q": "Which class makes columns take exactly half the row width on mobile phones?",
                "opts": ["col-6", "col-md-6", "col-lg-6", "col-sm-6"],
                "correct": 0,
                "exp": "col-6 targets extra small mobile screen sizes by default, spanning half of the 12-column layout!"
            },
            {
                "q": "Which breakpoint class targets medium tablet screen sizes?",
                "opts": ["sm-", "md-", "lg-", "xl-"],
                "correct": 1,
                "exp": "md- stands for medium screens (like tablets) starting from 768px wide!"
            },
            {
                "q": "Which utility class curves element corners into a perfect circle in Bootstrap?",
                "opts": ["rounded", "rounded-pill", "rounded-circle", "circle"],
                "correct": 2,
                "exp": "rounded-circle appliesborder-radius 50%, transforming cards or profile photos into elegant circles!"
            }
        ],
        "tasks": [
            {"title": "Responsive card row", "desc": "Create grid system rows wrapping cards taking col-12 on mobile and col-md-4 on desktop."},
            {"title": "Spacing adjustments", "desc": "Style divisions with Bootstrap utilities setting margins and border classes."}
        ]
    },
    "quiz3.json": {
        "quiz_title": "Web Design Advanced - Quiz 3: JS Basics & Data Outputs",
        "quiz_name": "Quiz 3: JS Basics & Data Outputs",
        "questions": [
            {
                "q": "Which HTML element is used to house JavaScript scripts?",
                "opts": ["&lt;js&gt;", "&lt;javascript&gt;", "&lt;script&gt;", "&lt;code&gt;"],
                "correct": 2,
                "exp": "We insert Javascript code internally inside standard &lt;script&gt; tags, or link external files."
            },
            {
                "q": "Which data type stores true or false values in JavaScript?",
                "opts": ["String", "Number", "Boolean", "Null"],
                "correct": 2,
                "exp": "Booleans represent conditional logical binary variables: true or false!"
            },
            {
                "q": "Which output method logs diagnostic texts silently inside console inspectors?",
                "opts": ["window.alert()", "console.log()", "document.write()", "innerHTML"],
                "correct": 1,
                "exp": "console.log() prints messages to browser inspector logs, ideal for testing without interrupting users!"
            },
            {
                "q": "How do you trigger a pop-up alert dialog window in JavaScript?",
                "opts": ["window.alert()", "console.log()", "document.alert()", "prompt()"],
                "correct": 0,
                "exp": "window.alert() stops browser scripts, showing a warning box with text and an OK button!"
            },
            {
                "q": "Which DOM property changes the HTML content inside selected tags?",
                "opts": ["textContent", "innerHTML", "className", "style"],
                "correct": 1,
                "exp": "innerHTML lets you get or set the actual markup text nested inside HTML elements dynamically!"
            }
        ],
        "tasks": [
            {"title": "Declare student variables", "desc": "Write scripts declaring strings and printing greetings in console."},
            {"title": "Inject headings", "desc": "Target element and set innerHTML with custom tag content."}
        ]
    },
    "quiz4.json": {
        "quiz_title": "Web Design Advanced - Quiz 4: JS Operators & Control Flow",
        "quiz_name": "Quiz 4: JS Operators & Control Flow",
        "questions": [
            {
                "q": "Which operator checks if two values are equal in JavaScript?",
                "opts": ["=", "==", "===", "match"],
                "correct": 1,
                "exp": "The double equals (==) operator compares two values to see if they are equal!"
            },
            {
                "q": "Which logical operator represents AND, requiring BOTH sides to be true?",
                "opts": ["||", "&&", "!", "++"],
                "correct": 1,
                "exp": "&& (AND) evaluates true ONLY if both left and right conditional criteria evaluate true!"
            },
            {
                "q": "Which conditional block handles options if an IF statement evaluates false?",
                "opts": ["else if", "else", "switch", "fallback"],
                "correct": 1,
                "exp": "The 'else' block holds fallback code triggered when the parent IF condition fails."
            },
            {
                "q": "Which loop always executes its code block at least ONCE before validating parameters?",
                "opts": ["for loop", "while loop", "do-while loop", "infinite loop"],
                "correct": 2,
                "exp": "do-while loops run the block first, then check conditions at the bottom of the loop!"
            },
            {
                "q": "How do you increment a counter variable 'i' by 1 in loop syntax?",
                "opts": ["i =+ 1", "i++", "i+1", "i = 1"],
                "correct": 1,
                "exp": "The increment operator i++ adds exactly 1 to variables, commonly used in loop counters!"
            }
        ],
        "tasks": [
            {"title": "Write pass/fail logic", "desc": "Create an IF statement logging grades based on scoring values."},
            {"title": "Create a counter", "desc": "Write a loop repeating console logs exactly 5 times."}
        ]
    },
    "quiz5.json": {
        "quiz_title": "Web Design Advanced - Quiz 5: JS Arrays & Functions",
        "quiz_name": "Quiz 5: JS Arrays & Functions",
        "questions": [
            {
                "q": "What is the index position of the very first item in a JavaScript array?",
                "opts": ["1", "0", "-1", "Index A"],
                "correct": 1,
                "exp": "JavaScript arrays are zero-indexed! The first list item sits at colors[0]."
            },
            {
                "q": "Which array method adds a new element to the END of the list?",
                "opts": ["pop()", "push()", "shift()", "add()"],
                "correct": 1,
                "exp": "push() appends items to list ends, while pop() removes the last element!"
            },
            {
                "q": "How do you check how many items live inside an array named 'hobbies'?",
                "opts": ["hobbies.count", "hobbies.size", "hobbies.length", "hobbies.index"],
                "correct": 2,
                "exp": "The 'length' property returns the count of items currently stored inside arrays."
            },
            {
                "q": "What keyword outputs values from a function back to the caller?",
                "opts": ["send", "output", "return", "export"],
                "correct": 2,
                "exp": "The 'return' keyword halts functions and outputs calculations back to calls!"
            },
            {
                "q": "Which property gets the text currently typed inside an input text box?",
                "opts": ["text", "value", "innerHTML", "content"],
                "correct": 1,
                "exp": "The '.value' property gets or sets current text strings typed in interactive inputs!"
            }
        ],
        "tasks": [
            {"title": "Push names", "desc": "Write scripts initializing arrays and pushing new student strings."},
            {"title": "Calculate sum", "desc": "Define functions with variables returning multiplier math."}
        ]
    },
    "quiz6.json": {
        "quiz_title": "Web Design Advanced - Quiz 6: DOM Manipulation & BOM",
        "quiz_name": "Quiz 6: DOM Manipulation & BOM",
        "questions": [
            {
                "q": "Which DOM selector accesses tags using CSS styles (like dots for classes)?",
                "opts": ["getElementById", "querySelector", "getElementsByTagName", "select"],
                "correct": 1,
                "exp": "querySelector('selector') selects the first matching tag using CSS class or ID styles!"
            },
            {
                "q": "Which event triggers when a student clicks on a button?",
                "opts": ["onchange", "onmouseover", "onclick", "onkeypress"],
                "correct": 2,
                "exp": "onclick registers user mouse clicks, instantly triggering assigned script actions!"
            },
            {
                "q": "Which window property gets the viewport width of browser screens?",
                "opts": ["screen.width", "window.innerWidth", "window.outerWidth", "viewport.width"],
                "correct": 1,
                "exp": "window.innerWidth returns live widths of browser viewports, which is essential for BOM sizing!"
            },
            {
                "q": "How do you save persistent local data that survives browser page refreshes?",
                "opts": ["localStorage.setItem('key', 'val')", "sessionStorage.save()", "window.save()", "document.cookie()"],
                "correct": 0,
                "exp": "localStorage.setItem() saves key-value string files persistently inside the user's browser!"
            },
            {
                "q": "What is the difference between ES6 'let' and 'const' variables?",
                "opts": [
                    "Let can be reassigned, Const cannot",
                    "Const can be reassigned, Let cannot",
                    "There is no difference",
                    "Let is global, Const is block"
                ],
                "correct": 0,
                "exp": "let declares variables that can change values, while const declares final fixed constants!"
            }
        ],
        "tasks": [
            {"title": "Interactive toggler", "desc": "Write onclick event handles changing body colors to dark backgrounds."},
            {"title": "Persistent login", "desc": "Save student usernames persistently in local storage items."}
        ]
    }
}

# Write senior_web_design Quizzes
for name, content in web_quizzes.items():
    with open(os.path.join(web_quizzes_path, name), 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

# Write senior_web_design_advanced Quizzes
for name, content in adv_quizzes.items():
    with open(os.path.join(adv_quizzes_path, name), 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=2)

print("Quiz JSON files successfully generated for both courses!")
