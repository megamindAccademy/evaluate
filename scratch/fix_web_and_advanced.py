import json
import os

# Paths
db_path = r'c:\Users\rowan\Desktop\ev\evaluate\database'
web_path = os.path.join(db_path, 'senior_web_design')
adv_path = os.path.join(db_path, 'senior_web_design_advanced')

# ----------------- SENIOR WEB DESIGN (HTML/CSS) - 16 SESSIONS -----------------
web_stations = [
    {
        "id": 1,
        "badge_icon": "🦕",
        "badge_title": "HTML Structure Medal",
        "title": "Station 1: HTML Structure & Basic Elements",
        "desc": "Build the skeleton of your web page using core HTML tags!",
        "story": "<h3>👋 Welcome, future Web Designer!</h3>"
                 "Let's learn how to build the skeleton of a web page using <b>HTML</b>!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>&lt;!DOCTYPE html&gt;</code>: Tells the browser this is a modern HTML5 document.</li>"
                 "<li><code>&lt;html&gt;</code>: The root element of our page.</li>"
                 "<li><code>&lt;head&gt;</code>: Contains meta-info like <code>&lt;title&gt;</code>.</li>"
                 "<li><code>&lt;body&gt;</code>: Where the visible content lives.</li>"
                 "<li><code>&lt;h1&gt;</code> to <code>&lt;h6&gt;</code>: Six sizes of headers (h1 is the biggest!).</li>"
                 "<li><code>&lt;p&gt;</code>: The paragraph tag.</li>"
                 "<li><code>&lt;br&gt;</code> & <code>&lt;hr&gt;</code>: Line break and horizontal thematic dividers!</li>"
                 "</ul>",
        "simple": "Think of HTML as the building blocks of a house. The body is the room, and the tags are the furniture!",
        "hint": "Use <code>&lt;h1&gt;Welcome&lt;/h1&gt;</code> and <code>&lt;p&gt;Hello World&lt;/p&gt;</code> to complete the text challenge.",
        "challenge": "Write a clean HTML structure with a heading <code>&lt;h1&gt;Welcome to Megaminds!&lt;/h1&gt;</code> and a paragraph <code>&lt;p&gt;Coding is magical.&lt;/p&gt;</code>.",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <title>My First Website</title>\n</head>\n<body>\n    <!-- Write your heading and paragraph below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Heading 1", "code": "<h1>Welcome to Megaminds!</h1>"},
            {"label": "Add Paragraph", "code": "<p>Coding is magical.</p>"},
            {"label": "Add Divider", "code": "<hr>"}
        ],
        "validation_rules": {
            "required_output_text": "Megaminds",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: My Profile Page",
            "desc": "Create a profile page at home using a main heading <code>&lt;h1&gt;</code>, a short paragraph description about yourself <code>&lt;p&gt;</code>, and separate the sections with a horizontal rule <code>&lt;hr&gt;</code>!",
            "code": "<!DOCTYPE html>\n<html>\n<body>\n    <h1>All About Me!</h1>\n    <hr>\n    <p>My name is Rowan and I love coding beautiful web pages!</p>\n</body>\n</html>",
            "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <!-- Create your profile home challenge here! -->\n    \n</body>\n</html>"
        }
    },
    {
        "id": 2,
        "badge_icon": "🖼️",
        "badge_title": "Media & Links Medal",
        "title": "Station 2: Embedded Images & Hyperlinks",
        "desc": "Make your pages colorful with images and navigate the web with links!",
        "story": "<h3>🚀 Let's add images and links!</h3>"
                 "Web pages look amazing when we add images and allow users to hop between pages using links!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>&lt;img&gt;</code>: Embeds an image. It's an empty element (no closing tag!).</li>"
                 "<li><b>Attributes:</b> <code>src</code> (image path/URL), <code>alt</code> (description text), <code>width</code>, and <code>height</code> (in px).</li>"
                 "<li><code>&lt;a&gt;</code>: The hyperlink tag. Uses <code>href</code> to specify the target link.</li>"
                 "<li><b>Target Attribute:</b> <code>target=\"_blank\"</code> opens the link in a new tab; <code>_self</code> is the default (same tab).</li>"
                 "</ul>",
        "simple": "Hyperlinks are like teleport portals, and images are windows to other worlds!",
        "hint": "Use <code>&lt;img src=\"...\" alt=\"Beach\" width=\"300\"&gt;</code> and <code>&lt;a href=\"...\" target=\"_blank\"&gt;</code>.",
        "challenge": "Embed an image with a width of 300px and create a link to Megaminds Academy opening in a new tab!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <h1>Welcome to My Gallery</h1>\n    <!-- Add your image and link below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Image tag", "code": "<img src=\"https://images.unsplash.com/photo-1507525428034-b723cf961d3e\" alt=\"Beach\" width=\"300\">"},
            {"label": "Add Link tag", "code": "<a href=\"https://megamindaccademy.github.io\" target=\"_blank\">Visit Megaminds!</a>"}
        ],
        "validation_rules": {
            "required_output_text": "Megaminds",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Teleporting Image",
            "desc": "Write code at home that renders an image of your favorite hobby, followed by a link that opens a tutorial about it in a new tab!",
            "code": "<img src=\"https://images.unsplash.com/photo-1542751371-adc38448a05e\" alt=\"Gaming\" width=\"300\">\n<a href=\"https://youtube.com\" target=\"_blank\">Watch gaming videos!</a>",
            "starter_code": "<!-- Create your teleporting image challenge here! -->"
        }
    },
    {
        "id": 3,
        "badge_icon": "📊",
        "badge_title": "Lists & Tables Medal",
        "title": "Station 3: HTML Lists & Data Tables",
        "desc": "Keep your data perfectly organized in lists and structured tables!",
        "story": "<h3>📊 Stay Organized!</h3>"
                 "Let's learn how to group items together using lists and display tables! <br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>&lt;ul&gt;</code>: Unordered (bulleted) list. Customize markers using <code>disc</code>, <code>circle</code>, or <code>square</code>.</li>"
                 "<li><code>&lt;ol&gt;</code>: Ordered (numbered) list. Use <code>type</code> (A, a, I, i, 1), <code>start</code> (starting number), and <code>reversed</code> (descending).</li>"
                 "<li><code>&lt;li&gt;</code>: List item. Put these inside lists!</li>"
                 "<li><code>&lt;table&gt;</code>: Defines the table. Contains: <code>&lt;tr&gt;</code> (rows), <code>&lt;th&gt;</code> (headers), and <code>&lt;td&gt;</code> (cells).</li>"
                 "<li><b>Advanced Elements:</b> <code>&lt;thead&gt;</code>, <code>&lt;tbody&gt;</code>, <code>&lt;tfoot&gt;</code>, and <code>&lt;caption&gt;</code>.</li>"
                 "<li><b>Spanning:</b> <code>colspan</code> spans cells across multiple columns.</li>"
                 "</ul>",
        "simple": "Tables are like grids of chocolates, and lists are like shopping menus!",
        "hint": "Create a table with a border attribute: <code>&lt;table border=\"1\"&gt;</code>.",
        "challenge": "Create a 2x2 table displaying Names and Ages of students, and make sure it has a border!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <!-- Add your list or table below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Unordered List", "code": "<ul>\n  <li>Apples</li>\n  <li>Bananas</li>\n</ul>"},
            {"label": "Add Ordered List", "code": "<ol type=\"A\" start=\"1\">\n  <li>First Item</li>\n  <li>Second Item</li>\n</ol>"},
            {"label": "Add Basic Table", "code": "<table border=\"1\" width=\"100%\">\n  <caption>Student Table</caption>\n  <tr>\n    <th>Name</th>\n    <th>Age</th>\n  </tr>\n  <tr>\n    <td>Adam</td>\n    <td>12</td>\n  </tr>\n</table>"}
        ],
        "validation_rules": {
            "required_output_text": "Age",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Shopping Catalog",
            "desc": "Create a food shopping list using an ordered list `<ol>` reversed, followed by a table displaying 3 items and their prices with a header row!",
            "code": "<h3>Shopping Catalog</h3>\n<ol reversed>\n  <li>Fresh Chicken</li>\n  <li>Tasty Pasta</li>\n</ol>\n<table border=\"1\">\n  <tr>\n    <th>Item</th>\n    <th>Price</th>\n  </tr>\n  <tr>\n    <td>Chicken</td>\n    <td>$10</td>\n  </tr>\n</table>",
            "starter_code": "<!-- Create your Shopping Catalog here! -->"
        }
    },
    {
        "id": 4,
        "badge_icon": "🎵",
        "badge_title": "HTML5 Media Medal",
        "title": "Station 4: HTML Audio & Video Players",
        "desc": "Embed sounds and movies directly into your page using HTML5!",
        "story": "<h3>🎵 Bring Your Site to Life!</h3>"
                 "Let's play audio and video files directly in our website using native controls!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>&lt;audio&gt;</code>: Embeds sound. Requires the <code>controls</code> attribute to display play/pause buttons.</li>"
                 "<li><code>&lt;video&gt;</code>: Embeds video. Set <code>width</code> and <code>height</code> to prevent lag/flickering.</li>"
                 "<li><b>Interactive Attributes:</b> <code>autoplay</code> (starts instantly), <code>loop</code> (plays infinitely), and <code>muted</code> (silent).</li>"
                 "<li><code>&lt;source&gt;</code>: Nested inside media elements to define file pathways (<code>src</code>) and safe formats (<code>type=\"video/mp4\"</code>).</li>"
                 "<li><code>poster</code>: Cover picture displayed on the video player before play.</li>"
                 "</ul>",
        "simple": "The controls attribute is the steering wheel that gives the user control over play, pause, and volume!",
        "hint": "Set up a video tag: <code>&lt;video width=\"320\" height=\"240\" controls&gt;&lt;source src=\"...\" type=\"video/mp4\"&gt;&lt;/video&gt;</code>.",
        "challenge": "Embed a video player with width 320px, height 240px, controls, muted, and a high-quality sample mp4 source!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <h1>My Video Channel</h1>\n    <!-- Add your video tag with source below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Audio Player", "code": "<audio controls loop>\n  <source src=\"https://www.w3schools.com/html/horse.mp3\" type=\"audio/mpeg\">\n</audio>"},
            {"label": "Add Video Player", "code": "<video width=\"320\" height=\"240\" controls muted>\n  <source src=\"https://www.w3schools.com/html/mov_bbb.mp4\" type=\"video/mp4\">\n</video>"}
        ],
        "validation_rules": {
            "required_output_text": "video",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Music Box",
            "desc": "Embed an audio element at home that loops automatically, and a video element that is muted by default with a beautiful placeholder cover poster!",
            "code": "<audio controls loop autoplay>\n  <source src=\"https://www.w3schools.com/html/horse.mp3\" type=\"audio/mpeg\">\n</audio>\n<br>\n<video width=\"300\" controls muted poster=\"https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7\">\n  <source src=\"https://www.w3schools.com/html/mov_bbb.mp4\" type=\"video/mp4\">\n</video>",
            "starter_code": "<!-- Create your Music Box code here! -->"
        }
    },
    {
        "id": 5,
        "badge_icon": "📝",
        "badge_title": "HTML Forms Medal",
        "title": "Station 5: Level 2 Session 1: Interactive HTML Forms",
        "desc": "Collect user input with forms, inputs, selections, and checkboxes!",
        "story": "<h3>📝 Forms are Everywhere!</h3>"
                 "From sign-ups to surveys, we use forms to interact with users and capture inputs!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>&lt;form&gt;</code>: The parent container for input elements.</li>"
                 "<li><code>&lt;label&gt;</code>: Labels input fields so users know what to type.</li>"
                 "<li><code>&lt;input&gt;</code>: The powerhouse of forms. Dynamic types include: <code>text</code>, <code>email</code>, <code>password</code>, <code>number</code> (min/max), <code>radio</code> (single pick, group using <code>name</code>), <code>checkbox</code> (multi-pick), <code>color</code>, <code>file</code>, <code>submit</code>, and <code>reset</code>.</li>"
                 "<li><code>&lt;select&gt;</code> & <code>&lt;option&gt;</code>: Renders drop-down menus. Add <code>selected</code> to pre-select.</li>"
                 "<li><code>&lt;textarea&gt;</code>: Multi-line description box (controlled by <code>rows</code> and <code>cols</code>).</li>"
                 "<li><code>&lt;fieldset&gt;</code> & <code>&lt;legend&gt;</code>: Groups inputs together with a visual frame.</li>"
                 "<li><b>Useful Attributes:</b> <code>value</code> (starting text), <code>placeholder</code> (faint hint text), and <code>required</code> (must fill!).</li>"
                 "</ul>",
        "simple": "A placeholder is like a ghost text that vanishes the second the user starts typing!",
        "hint": "Create an input tag like: <code>&lt;input type=\"email\" placeholder=\"email\" required&gt;</code>.",
        "challenge": "Design a sign-up form with a required Text field, an Email field with a placeholder, a password field, and a submit button!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <!-- Create your sign-up form below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Text Field", "code": "<label>Name: <input type=\"text\" placeholder=\"Enter name\" required></label>"},
            {"label": "Add Radio Group", "code": "<label><input type=\"radio\" name=\"gender\" value=\"m\"> Male</label>\n<label><input type=\"radio\" name=\"gender\" value=\"f\"> Female</label>"},
            {"label": "Add Select Menu", "code": "<select>\n  <option value=\"web\">Web Design</option>\n  <option value=\"python\" selected>Python Basics</option>\n</select>"},
            {"label": "Add Textarea", "code": "<textarea rows=\"4\" cols=\"30\" placeholder=\"Enter bio...\"></textarea>"},
            {"label": "Add Fieldset frame", "code": "<fieldset>\n  <legend>User Info</legend>\n  <input type=\"submit\" value=\"Submit\">\n</fieldset>"}
        ],
        "validation_rules": {
            "required_output_text": "Submit",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Feedback Survey",
            "desc": "Create a feedback form at home with a `<fieldset>` and `<legend>`. Include a required Name input, a drop-down list `<select>` to rate the session from 1 to 5, a `<textarea>` for suggestions, and a submit button!",
            "code": "<form>\n  <fieldset>\n    <legend>Session Feedback</legend>\n    <label>Name: <input type=\"text\" placeholder=\"Your Name\" required></label><br><br>\n    <label>Rating: \n      <select>\n        <option>5 - Excellent</option>\n        <option>4 - Very Good</option>\n      </select>\n    </label><br><br>\n    <textarea placeholder=\"Suggestions...\" rows=\"3\"></textarea><br>\n    <input type=\"submit\" value=\"Submit Feedback\">\n  </fieldset>\n</form>",
            "starter_code": "<!-- Create your Feedback Survey here! -->"
        }
    },
    {
        "id": 6,
        "badge_icon": "📦",
        "badge_title": "Layout Elements Medal",
        "title": "Station 6: Layout Elements, Class & ID Selectors",
        "desc": "Group your tags inside structural containers and style them with classes!",
        "story": "<h3>📦 Structural Layout Containers!</h3>"
                 "Let's learn how to group elements into structural blocks using layout containers and tag them for CSS styling!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>&lt;div&gt;</code>: Block container. Always starts on a new line and takes up full width. Used to group big sections!</li>"
                 "<li><code>&lt;span&gt;</code>: Inline container. Stays on the same line. Used to highlight specific words inside text!</li>"
                 "<li><code>class</code>: Group tag. Multiple HTML elements can share the same class name for uniform styling.</li>"
                 "<li><code>id</code>: Unique tag. MUST be unique in the entire page! Perfect for identifying one specific element.</li>"
                 "</ul>",
        "simple": "Think of divs as storage boxes in your room, and spans as small labels placed directly on items!",
        "hint": "Wrap words with <code>&lt;span class=\"highlight\"&gt;text&lt;/span&gt;</code> and wrap sections in a <code>&lt;div class=\"container\"&gt;</code>.",
        "challenge": "Create a `div` block with a class of 'hero-box', containing a heading and a paragraph with a word wrapped in a `span` styled with class 'special-text'!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <!-- Write your div, span, class, and id layout elements below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Div with Class", "code": "<div class=\"hero-box\" id=\"header-section\">\n  <h1>My Site Heading</h1>\n</div>"},
            {"label": "Add Span highlight", "code": "<p>I am a coder, <span class=\"special-text\">and I love HTML</span>.</p>"}
        ],
        "validation_rules": {
            "required_output_text": "hero-box",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Blog Post Layout",
            "desc": "Build a simple blog post layout using a parent `div` with a class of 'blog-post'. Inside, put a heading with class 'blog-title' and a paragraph where the date is styled inside a `span` with an ID of 'post-date'!",
            "code": "<div class=\"blog-post\">\n  <h2 class=\"blog-title\">The HTML Journey</h2>\n  <p>Published on: <span id=\"post-date\">May 20, 2026</span></p>\n  <p>Today we explored divisions and spans. It was awesome!</p>\n</div>",
            "starter_code": "<!-- Create your Blog Post Layout here! -->"
        }
    },
    {
        "id": 7,
        "badge_icon": "🎨",
        "badge_title": "CSS Selector Medal",
        "title": "Station 7: Level 2 Session 2: Intro to CSS & Colors",
        "desc": "Paint your website beautiful with CSS rules, selectors, and color styles!",
        "story": "<h3>🎨 Welcome to CSS!</h3>"
                 "CSS stands for <b>Cascading Style Sheets</b>. It defines how our HTML tags look on screen!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Three Ways to Insert CSS:</b>"
                 "  <ul>"
                 "    <li><b>Inline:</b> Directly on tags using the <code>style</code> attribute.</li>"
                 "    <li><b>Internal:</b> Inside a <code>&lt;style&gt;</code> block inside <code>&lt;head&gt;</code>.</li>"
                 "    <li><b>External:</b> Inside a separate <code>.css</code> file linked with <code>&lt;link rel=\"stylesheet\" href=\"styles.css\"&gt;</code>.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>CSS Selectors:</b>"
                 "  <ul>"
                 "    <li><b>Element Selector:</b> e.g. <code>h1 { color: red; }</code>.</li>"
                 "    <li><b>Class Selector:</b> e.g. <code>.title { color: blue; }</code> (uses a period <code>.</code>).</li>"
                 "    <li><b>ID Selector:</b> e.g. <code>#main { color: green; }</code> (uses a hash <code>#</code>).</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>CSS Colors:</b> Specified by color names (<code>red</code>), RGB (<code>rgb(255, 0, 0)</code>), RGBA with opacity (<code>rgba(255, 0, 0, 0.5)</code>), and Hexadecimal codes (<code>#ff0000</code>).</li>"
                 "</ul>",
        "simple": "CSS is the paintbrush and makeup of a website. HTML makes the face, but CSS makes it look gorgeous!",
        "hint": "Write: <code>&lt;style&gt; h1 { color: #2563eb; } .text { color: rgb(220, 38, 38); } &lt;/style&gt;</code>.",
        "challenge": "Write internal CSS styling the heading <code>&lt;h1&gt;</code> in royal blue and a paragraph with class 'text' in red!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <!-- Add your style block below! -->\n    \n</head>\n<body>\n    <h1>Colorful Heading</h1>\n    <p class=\"text\">This paragraph is red!</p>\n</body>\n</html>",
        "pills": [
            {"label": "Add Style Block", "code": "<style>\n  h1 {\n    color: #1d4ed8;\n    text-align: center;\n  }\n  .text {\n    color: rgba(220, 38, 38, 0.8);\n  }\n</style>"}
        ],
        "validation_rules": {
            "required_output_text": "style",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Colorful Rainbow",
            "desc": "Create a page at home with a heading styled internally using a HEX color value, and three paragraphs, each styled with a unique color class using RGB, RGBA, and standard color names!",
            "code": "<head>\n  <style>\n    h1 { color: #6366f1; }\n    .red-rgb { color: rgb(239, 68, 68); }\n    .green-rgba { color: rgba(16, 185, 129, 0.7); }\n    .blue-name { color: royalblue; }\n  </style>\n</head>\n<body>\n  <h1>Rainbow Headings</h1>\n  <p class=\"red-rgb\">RGB Red</p>\n  <p class=\"green-rgba\">RGBA Green</p>\n  <p class=\"blue-name\">Blue Name</p>\n</body>",
            "starter_code": "<!-- Create your Colorful Rainbow code here! -->"
        }
    },
    {
        "id": 8,
        "badge_icon": "🌄",
        "badge_title": "Background Magic Medal",
        "title": "Station 8: Advanced CSS Background Styling",
        "desc": "Style your container backgrounds with colors, images, sizing, and attachments!",
        "story": "<h3>🌄 Advanced CSS Backgrounds!</h3>"
                 "Let's learn how to add beautiful background textures, patterns, and full-screen covers to containers!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>background-color</code>: Set the background fill.</li>"
                 "<li><code>background-image</code>: Uses <code>url('image_url')</code> to specify the background image.</li>"
                 "<li><code>background-repeat</code>: Controls repeating (<code>repeat-x</code> horizontally, <code>repeat-y</code> vertically, or <code>no-repeat</code>).</li>"
                 "<li><code>background-attachment</code>: Sets scrolling behavior. <code>scroll</code> moves with page; <code>fixed</code> locks it in place!</li>"
                 "<li><code>background-position</code>: Centering image using values like <code>top</code>, <code>center</code>, <code>bottom</code>, and x/y alignments.</li>"
                 "<li><code>background-size</code>: <code>auto</code> (original size), <code>cover</code> (covers container completely, clipping if needed), or <code>contain</code> (fully visible inside).</li>"
                 "</ul>",
        "simple": "The cover value stretches your background picture to cover the entire page like a beautiful blanket!",
        "hint": "Set up background styles like: <code>background-image: url('...'); background-repeat: no-repeat; background-size: cover;</code>.",
        "challenge": "Style a division with a class of 'hero-banner' to have a height of 200px, a background color, a background image, set to no-repeat, cover, and centered!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .hero-banner {\n            height: 200px;\n            /* Add background styles below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <div class=\"hero-banner\"></div>\n</body>\n</html>",
        "pills": [
            {"label": "Add Background Image", "code": "background-image: url('https://images.unsplash.com/photo-1579546929518-9e396f3cc809');"},
            {"label": "Add no-repeat", "code": "background-repeat: no-repeat;"},
            {"label": "Add cover size", "code": "background-size: cover;"},
            {"label": "Add center position", "code": "background-position: center;"}
        ],
        "validation_rules": {
            "required_output_text": "hero-banner",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Fixed Hero Banner",
            "desc": "Style a full page background or banner division at home to have a fixed background image <code>background-attachment: fixed;</code> that does not scroll, centered on the screen, and sized as cover!",
            "code": "<style>\n  .banner {\n    height: 400px;\n    background-image: url('https://images.unsplash.com/photo-1579546929518-9e396f3cc809');\n    background-repeat: no-repeat;\n    background-position: center;\n    background-size: cover;\n    background-attachment: fixed;\n  }\n</style>\n<div class=\"banner\"></div>",
            "starter_code": "<!-- Create your Fixed Hero Banner here! -->"
        }
    },
    {
        "id": 9,
        "badge_icon": "📦",
        "badge_title": "Box Model Medal",
        "title": "Station 9: Level 3 Session 1: CSS Box Model & Borders",
        "desc": "Control spacings with margins, padding, custom borders, and width sizes!",
        "story": "<h3>📦 Master the CSS Box Model!</h3>"
                 "Every element in HTML is a rectangular box. Spacings are controlled by margins, borders, and padding!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Box Components:</b>"
                 "  <ul>"
                 "    <li><b>Content:</b> The text or image itself.</li>"
                 "    <li><b>Padding:</b> Space INSIDE the border, around the content.</li>"
                 "    <li><b>Border:</b> The boundary wrapping the padding and content.</li>"
                 "    <li><b>Margin:</b> Space OUTSIDE the border, keeping elements apart.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Shorthand Rules (Margins & Paddings):</b>"
                 "  <ul>"
                 "    <li>4 values: <code>top right bottom left</code> (Clockwise!).</li>"
                 "    <li>3 values: <code>top (right/left) bottom</code>.</li>"
                 "    <li>2 values: <code>(top/bottom) (right/left)</code>.</li>"
                 "    <li>1 value: <code>all-four-sides</code>.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Borders:</b> Style using <code>border-style</code> (<code>solid</code>, <code>dashed</code>, <code>dotted</code>, <code>double</code>), <code>border-width</code>, <code>border-color</code>, or shorthand (e.g. <code>border: 3px solid #10b981;</code>).</li>"
                 "<li><b>Width:</b> Size boxes using percentages (<code>%</code>) or absolute pixels (<code>px</code>).</li>"
                 "</ul>",
        "simple": "Margin pushes away other elements, while padding pushes contents inside, inflating the element's box!",
        "hint": "Set up a box with padding, margin, border, and width: <code>width: 300px; padding: 20px; border: 2px solid green; margin: 15px;</code>.",
        "challenge": "Style a class 'info-box' to have a width of 80%, margin set to '10px auto' (centered), padding of 20px, and a 3px solid border!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .info-box {\n            /* Add Box Model properties below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <div class=\"info-box\">We love the Box Model!</div>\n</body>\n</html>",
        "pills": [
            {"label": "Add Width 80%", "code": "width: 80%;"},
            {"label": "Add Centered Margin", "code": "margin: 10px auto;"},
            {"label": "Add Padding 20px", "code": "padding: 20px;"},
            {"label": "Add Border Shorthand", "code": "border: 3px solid #10b981;"}
        ],
        "validation_rules": {
            "required_output_text": "info-box",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Double Border Box",
            "desc": "Design a box division at home styled with a double border of 5px size, colored in purple, with a 30px padding on the inside and a 50px margin on the bottom!",
            "code": "<style>\n  .magic-box {\n    border-style: double;\n    border-width: 5px;\n    border-color: darkmagenta;\n    padding: 30px;\n    margin-bottom: 50px;\n  }\n</style>\n<div class=\"magic-box\">Double Border Magic!</div>",
            "starter_code": "<!-- Create your Double Border Box here! -->"
        }
    },
    {
        "id": 10,
        "badge_icon": "🔤",
        "badge_title": "Typography Medal",
        "title": "Station 10: Level 3 Session 2: CSS Typography",
        "desc": "Format font-families, font weights, text alignments, capitalization, and spacings!",
        "story": "<h3>🔤 Make Text Beautiful!</h3>"
                 "Let's learn how to style texts and load custom font families using CSS Typography properties!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>color</code>: Set text color.</li>"
                 "<li><code>text-align</code>: Alignment (<code>left</code>, <code>right</code>, <code>center</code>).</li>"
                 "<li><code>direction</code>: Control reading direction (<code>ltr</code> for English, <code>rtl</code> for Arabic).</li>"
                 "<li><code>text-transform</code>: Text capitalization (<code>uppercase</code>, <code>lowercase</code>, <code>capitalize</code>).</li>"
                 "<li><code>letter-spacing</code> & <code>word-spacing</code>: Spacings between letters and words (in px).</li>"
                 "<li><code>font-family</code>: Defines fonts. Uses fallbacks separated by commas (e.g. <code>Arial, sans-serif</code>). Wrap multi-word font names in quotation marks!</li>"
                 "<li><code>font-size</code>: Sized in pixels (<code>px</code>).</li>"
                 "<li><code>font-weight</code>: Boldness (<code>normal</code>, <code>bold</code>).</li>"
                 "</ul>",
        "simple": "When a font name has two words like 'Times New Roman', you must wrap it in quotation marks so the browser doesn't get confused!",
        "hint": "Set up text styles: <code>font-size: 24px; font-weight: bold; text-align: center; text-transform: uppercase;</code>.",
        "challenge": "Style the heading with class 'main-heading' to have a bold Arial font of 24px size, centered alignment, and transform text to uppercase!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .main-heading {\n            /* Add typography styles below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <h1 class=\"main-heading\">Megaminds is Awesome</h1>\n</body>\n</html>",
        "pills": [
            {"label": "Add Arial Font", "code": "font-family: Arial, sans-serif;"},
            {"label": "Add Font Size 24px", "code": "font-size: 24px;"},
            {"label": "Add Bold Font", "code": "font-weight: bold;"},
            {"label": "Add Uppercase", "code": "text-transform: uppercase;"},
            {"label": "Add Center Alignment", "code": "text-align: center;"}
        ],
        "validation_rules": {
            "required_output_text": "main-heading",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Book Title Styling",
            "desc": "Design a book title display at home. Use a serif font, uppercase styling, bold text, 3px letter-spacing, and deep indigo color!",
            "code": "<style>\n  .book-title {\n    font-family: 'Times New Roman', serif;\n    font-size: 32px;\n    font-weight: bold;\n    text-transform: uppercase;\n    letter-spacing: 3px;\n    color: indigo;\n    text-align: center;\n  }\n</style>\n<h1 class=\"book-title\">The Story of Coding</h1>",
            "starter_code": "<!-- Create your Book Title layout here! -->"
        }
    },
    {
        "id": 11,
        "badge_icon": "⛵",
        "badge_title": "Float & Flow Medal",
        "title": "Station 11: Level 3 Session 3: Float & Overflow",
        "desc": "Float images next to paragraphs, clear floats, and control overflow scrolls!",
        "story": "<h3>⛵ Floating & Content التدفق!</h3>"
                 "Let's master alignment using floats and control what happens when content exceeds its box borders!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>float</code>: Positions elements to float to the <code>left</code>, <code>right</code>, or <code>none</code> of their containers (allowing paragraphs to wrap around them!).</li>"
                 "<li><code>clear</code>: Stops floating elements from hugging sides. Pushes next elements below left floats (<code>left</code>), right floats (<code>right</code>), or both (<code>both</code>).</li>"
                 "<li><code>overflow</code>: Controls content exceeding height/width boxes. Values: <code>visible</code> (renders outside, default), <code>hidden</code> (clops and hides content), <code>scroll</code> (adds scrollbars), and <code>auto</code> (scrollbars only when needed!).</li>"
                 "</ul>",
        "simple": "When you float an image to the left, the text surrounding it wraps around it on the right side like water flowing past a stone!",
        "hint": "Set up floating image and overflow-scroll container using: <code>float: left; overflow: auto;</code>.",
        "challenge": "Style the class 'avatar' to float left with margin-right of 10px, and style class 'box' to have height 100px and auto overflow scrollbars!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .avatar {\n            /* Float this! */\n            \n        }\n        .box {\n            height: 100px;\n            border: 2px solid #ccc;\n            /* Add overflow control below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <div class=\"box\">\n        <img class=\"avatar\" src=\"https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe\" width=\"50\" height=\"50\">\n        This is a scrolling box that handles very long paragraphs using overflow configurations!\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Add Float Left", "code": "float: left;"},
            {"label": "Add Margin Right", "code": "margin-right: 10px;"},
            {"label": "Add Overflow Auto", "code": "overflow: auto;"}
        ],
        "validation_rules": {
            "required_output_text": "avatar",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Double Column Layout",
            "desc": "Create a layout at home with an image floated to the right of a story, and place a footer paragraph underneath that uses <code>clear: both;</code> so it always starts on a fresh line below the image!",
            "code": "<img src=\"img.jpg\" style=\"float: right; margin-left: 10px;\" width=\"100\">\n<p>This is paragraph text describing the beautiful float alignments.</p>\n<p style=\"clear: both; background: #e2e8f0; padding: 10px;\">I am a cleared footer text safely appearing below!</p>",
            "starter_code": "<!-- Create your Double Column Layout here! -->"
        }
    },
    {
        "id": 12,
        "badge_icon": "👁️",
        "badge_title": "Display States Medal",
        "title": "Station 12: Level 3 Session 4: CSS Display & States",
        "desc": "Master block vs inline elements, hide containers, and style links with hover effects!",
        "story": "<h3>👁️ Display Behaviors & Interactive Links!</h3>"
                 "Let's master how elements sit on screen and how hyperlinks transition dynamically when hovered!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>display</code>: Sets element display properties."
                 "  <ul>"
                 "    <li><code>block</code>: Starts fresh line, takes full width (e.g. <code>&lt;div&gt;</code>, <code>&lt;h1&gt;</code>).</li>"
                 "    <li><code>inline</code>: Same line, only takes needed width; top/bottom padding/margin ignored (e.g. <code>&lt;span&gt;</code>, <code>&lt;a&gt;</code>).</li>"
                 "    <li><code>inline-block</code>: Same line, but allows setting custom width/height and respects all margins/paddings!</li>"
                 "    <li><code>none</code>: Hides element completely (layout acts as if it is not there!).</li>"
                 "  </ul>"
                 "</li>"
                 "<li><code>visibility: hidden;</code>: Hides element, but retains its structural blank space!</li>"
                 "<li><b>Interactive Links:</b> Style text color, add/remove underlines (<code>text-decoration: none;</code>), and customize hover transitions using the <code>a:hover</code> pseudo-class!</li>"
                 "</ul>",
        "simple": "display: none hides the element and deletes its space, while visibility: hidden hides it but leaves an empty ghost space!",
        "hint": "Set style: <code>text-decoration: none;</code>, and <code>a:hover { color: #f59e0b; text-decoration: underline; }</code>.",
        "challenge": "Style standard links to have no underline (none) and change color to gold on hover using `a:hover`!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        a {\n            color: #3b82f6;\n            /* Remove underline below! */\n            \n        }\n        /* Add hover selector below! */\n        \n    </style>\n</head>\n<body>\n    <a href=\"#\">Hover Over Me!</a>\n</body>\n</html>",
        "pills": [
            {"label": "Remove Underline", "code": "text-decoration: none;"},
            {"label": "Add Hover pseudo", "code": "a:hover {\n  color: #ffb703;\n  text-decoration: underline;\n}"}
        ],
        "validation_rules": {
            "required_output_text": "hover",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Interactive Navigation Links",
            "desc": "Design navigation menu links at home! Display them in a line using <code>display: inline-block;</code>, remove lines under them, and change background and color when hovered!",
            "code": "<style>\n  .nav-link {\n    display: inline-block;\n    padding: 10px 20px;\n    color: #fff;\n    background-color: #023047;\n    text-decoration: none;\n    border-radius: 5px;\n  }\n  .nav-link:hover {\n    background-color: #ffb703;\n    color: #023047;\n  }\n</style>\n<a href=\"#\" class=\"nav-link\">Dashboard</a>",
            "starter_code": "<!-- Create your Interactive Navigation Links here! -->"
        }
    },
    {
        "id": 13,
        "badge_icon": "📍",
        "badge_title": "Positioning Medal",
        "title": "Station 13: Level 4 Session 1: CSS Positioning & Shadows",
        "desc": "Position containers (relative, fixed, absolute), add shadows, and load Font Awesome icons!",
        "story": "<h3>📍 Positioning, Shadows & Icon Libraries!</h3>"
                 "Let's master absolute placing coordinates, create gorgeous dimensional shadows, and load beautiful scalable vector icons!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>position</code>: Positioning models."
                 "  <ul>"
                 "    <li><code>relative</code>: Positioned relative to its normal position.</li>"
                 "    <li><code>fixed</code>: Locked relative to viewport window (doesn't scroll, stays in place!).</li>"
                 "    <li><code>absolute</code>: Positioned relative to its closest positioned parent.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Shadow Effects:</b>"
                 "  <ul>"
                 "    <li><code>text-shadow</code>: Shadow on texts (horizontal, vertical, blur, color).</li>"
                 "    <li><code>box-shadow</code>: Shadow on box boxes (horizontal, vertical, blur, color).</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Icon Libraries:</b> Link **Font Awesome** CDN inside `<head>` and display icons inside inline elements (like `&lt;i class=\"fas fa-fire\"&gt;&lt;/i&gt;`).</li>"
                 "</ul>",
        "simple": "A fixed element does not scroll with the page. It sits in the exact same spot like a sticky note on your screen!",
        "hint": "Set box styles: <code>box-shadow: 5px 5px 10px gainsboro; position: absolute; top: 10px; right: 10px;</code>.",
        "challenge": "Style class 'card' to have relative positioning and a subtle box-shadow, and load a star icon inside it!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css\">\n    <style>\n        .card {\n            width: 200px;\n            padding: 20px;\n            background: #fff;\n            /* Add position and box-shadow below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <div class=\"card\">\n        <!-- Add star icon here! -->\n        Best Choice\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Add Position Relative", "code": "position: relative;"},
            {"label": "Add Box Shadow", "code": "box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.1);"},
            {"label": "Add Star Icon tag", "code": "<i class=\"fas fa-star\" style=\"color:gold;\"></i>"}
        ],
        "validation_rules": {
            "required_output_text": "fa-star",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Glow Card with Icons",
            "desc": "Create a glowing card at home! Include a fire icon, a text heading with an orange text-shadow glow, and styled with relative coordinates!",
            "code": "<head>\n  <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css\">\n  <style>\n    .glow-card {\n      position: relative;\n      padding: 30px;\n      background: #111;\n      color: #fff;\n      box-shadow: 0 0 15px #f59e0b;\n      border-radius: 10px;\n      text-align: center;\n    }\n    h2 {\n      text-shadow: 0 0 8px #f59e0b;\n    }\n  </style>\n</head>\n<body>\n  <div class=\"glow-card\">\n    <i class=\"fas fa-fire\" style=\"color:orange; font-size: 2rem;\"></i>\n    <h2>Mega Fire!</h2>\n  </div>\n</body>",
            "starter_code": "<!-- Create your Glow Card here! -->"
        }
    },
    {
        "id": 14,
        "badge_icon": "🎬",
        "badge_title": "Animation Medal",
        "title": "Station 14: Level 4 Session 2: CSS Keyframe Animations",
        "desc": "Bring elements to life with @keyframes, durations, delays, and loop counts!",
        "story": "<h3>🎬 Animation Magic!</h3>"
                 "CSS lets us animate elements from one style to another without Javascript! Let's learn how!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>@keyframes</code>: The animation script. Define key moments using keywords <code>from</code> & <code>to</code>, or percentages (<code>0%</code>, <code>50%</code>, <code>100%</code>).</li>"
                 "<li><code>animation-name</code>: Links keyframes rule to elements.</li>"
                 "<li><code>animation-duration</code>: Defines duration in seconds (e.g. <code>2s</code>). Default is <code>0s</code> (no animation!).</li>"
                 "<li><code>animation-delay</code>: Set standard delay before animation begins.</li>"
                 "<li><code>animation-iteration-count</code>: Loop counts. Set to <code>infinite</code> to run forever!</li>"
                 "</ul>",
        "simple": "Think of keyframes like pages in a flipbook. When you flip them fast, the drawing starts moving!",
        "hint": "Create code: <code>animation: slide 2s infinite;</code> and define <code>@keyframes slide { from { left: 0px; } to { left: 100px; } }</code>.",
        "challenge": "Create a pulse keyframes animation (from scale 1 to 1.1) and apply it to a button infinitely with a 1.5s duration!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        /* Define keyframes below! */\n        \n        .pulse-btn {\n            padding: 10px 20px;\n            background: #ec4899;\n            color: white;\n            border: none;\n            border-radius: 5px;\n            /* Apply animation below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <button class=\"pulse-btn\">Animate Me!</button>\n</body>\n</html>",
        "pills": [
            {"label": "Add Keyframes Pulse", "code": "@keyframes pulse {\n  0% { transform: scale(1); }\n  50% { transform: scale(1.1); }\n  100% { transform: scale(1); }\n}"},
            {"label": "Apply Pulse Animation", "code": "animation: pulse 1.5s infinite;"}
        ],
        "validation_rules": {
            "required_output_text": "pulse",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Infinite Spinner",
            "desc": "Build an infinite loader spinning wheel at home! Create keyframes that rotate the element 360 degrees and run infinitely!",
            "code": "<style>\n  @keyframes spin {\n    from { transform: rotate(0deg); }\n    to { transform: rotate(360deg); }\n  }\n  .spinner {\n    width: 50px;\n    height: 50px;\n    border: 5px solid #ccc;\n    border-top: 5px solid #3b82f6;\n    border-radius: 50%;\n    animation: spin 1s linear infinite;\n  }\n</style>\n<div class=\"spinner\"></div>",
            "starter_code": "<!-- Create your Infinite Spinner here! -->"
        }
    },
    {
        "id": 15,
        "badge_icon": "🍔",
        "badge_title": "Delicious Part 1 Medal",
        "title": "Station 15: Level 4 Session 3: Delicious Restaurant - Part 1",
        "desc": "Setup the layout, navbar links, and header banner for the final Delicious Project!",
        "story": "<h3>🍔 Delicious Restaurant Website - Part 1!</h3>"
                 "It's final capstone project time! We are building a high-end restaurant landing page called <b>Delicious Restaurant</b>!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Setup:</b> Link custom Google Fonts (like <code>Pacifico</code> and <code>Great Vibes</code>) and **Font Awesome** CDN inside `<head>`.</li>"
                 "<li><b>Header & Navbar:</b> Create a structural navbar containing a left logo (using fire/fork icons) and right navigation menu links (Home, Products, Our Offers, Services, Contact) styled in a horizontal line.</li>"
                 "<li><b>Banner Hero Content:</b> Style a welcome banner with high-quality headers and taglines.</li>"
                 "</ul>",
        "simple": "We use flexbox to align our logo on the left and our links on the right, keeping our menu neat and clean!",
        "hint": "Build your navbar layout using standard flex displays: <code>display: flex; justify-content: space-between;</code>.",
        "challenge": "Setup a navigation bar for Delicious with a class of 'nav-container', displaying the logo and a list of links side by side!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <title>Delicious Restaurant</title>\n    <link href=\"https://fonts.googleapis.com/css2?family=Pacifico&display=swap\" rel=\"stylesheet\">\n    <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css\">\n    <style>\n        body { font-family: 'Pacifico', cursive; margin:0; }\n        /* Style the navbar display below! */\n        \n    </style>\n</head>\n<body>\n    <nav class=\"nav-container\">\n        <div class=\"logo\"><i class=\"fas fa-utensils\"></i> Delicious</div>\n        <ul class=\"links\" style=\"display:flex; list-style:none; gap:20px;\">\n            <li><a href=\"#\" style=\"color:#fff; text-decoration:none;\">Home</a></li>\n            <li><a href=\"#\" style=\"color:#fff; text-decoration:none;\">Products</a></li>\n        </ul>\n    </nav>\n</body>\n</html>",
        "pills": [
            {"label": "Style Nav Container", "code": ".nav-container {\n  display: flex;\n  justify-content: space-between;\n  align-items: center;\n  background: #333;\n  color: #fff;\n  padding: 15px 30px;\n}"}
        ],
        "validation_rules": {
            "required_output_text": "nav-container",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Delicious Welcome Banner",
            "desc": "Build the welcome banner for your restaurant at home! Align text in the center, style it with custom fonts, and add a Book Table button with glowing box-shadows!",
            "code": "<div class=\"welcome-banner\">\n  <h1 style=\"font-family:'Pacifico', cursive; font-size:3rem;\">Welcome To Delicious</h1>\n  <p>Savour delightful dishes made with fresh ingredients daily!</p>\n  <button style=\"padding:12px 24px; background:orange; border:none; border-radius:5px; font-weight:bold; cursor:pointer;\">BOOK NOW</button>\n</div>",
            "starter_code": "<!-- Create your Welcome Banner here! -->"
        }
    },
    {
        "id": 16,
        "badge_icon": "🦞",
        "badge_title": "Delicious Part 2 Medal",
        "title": "Station 16: Level 4 Session 4: Delicious Restaurant - Part 2",
        "desc": "Add food product cards (Chicken & Seafood), styling, borders, and footer details!",
        "story": "<h3>🦞 Delicious Restaurant Website - Part 2!</h3>"
                 "Let's complete our beautiful <b>Delicious Restaurant</b> landing page by adding food product cards, styled tables, and contact details!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Product Sections:</b> Create two cards: <b>Chicken</b> (\"We offer you the best types of chicken...\") and <b>Seafood</b> (\"fresh seafood with a variety of unique recipes...\").</li>"
                 "<li><b>Visual Cards:</b> Style cards with borders, border-radius, centered layouts, and add nice hover scaling transitions.</li>"
                 "<li><b>Address Footer:</b> Add a styled footer with a nice map-address \"1 St Mostafa Kamel, Somouha, Alexandria\" and Font Awesome social icons!</li>"
                 "</ul>",
        "simple": "The transition property makes image card scaling smooth and elegant, preventing jarring changes!",
        "hint": "Set up food product cards using nice borders and hover: <code>.card:hover { transform: scale(1.05); transition: 0.3s; }</code>.",
        "challenge": "Create a seafood product card styled with borders and hover scale transitions, and add a footer displaying the Somouha, Alexandria address!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .menu-container { display: flex; gap: 20px; justify-content: center; padding: 20px; }\n        .card { border: 1px solid #ddd; padding: 15px; border-radius: 8px; text-align: center; width: 220px; }\n        /* Add hover scale animation below! */\n        \n        footer { background: #222; color: #fff; text-align: center; padding: 15px; margin-top: 30px; }\n    </style>\n</head>\n<body>\n    <div class=\"menu-container\">\n        <div class=\"card\">\n            <h3>Seafood</h3>\n            <p>Mouth-watering fresh seafood recipes!</p>\n        </div>\n    </div>\n    <footer>\n        <!-- Add footer content below! -->\n        \n    </footer>\n</body>\n</html>",
        "pills": [
            {"label": "Add Hover Animation", "code": ".card:hover {\n  transform: scale(1.05);\n  transition: transform 0.3s ease;\n  box-shadow: 0 4px 15px rgba(0,0,0,0.1);\n}"},
            {"label": "Add Footer Content", "code": "<p><i class=\"fas fa-map-marker-alt\" style=\"color:orange;\"></i> 1 St Mostafa Kamel, Somouha, Alexandria</p>"}
        ],
        "validation_rules": {
            "required_output_text": "Somouha",
            "required_canvas": False
        },
        "homework": {
            "title": "🎉 Magic Home Challenge: Completed Restaurant Website!",
            "desc": "Assemble all sections at home! Put together your styled navigation bar, hero banner, food product cards (chicken & seafood) with hover animations, and the Somouha, Alexandria footer. You have built a production-grade restaurant page! Excellent work! 🌟",
            "code": "<!-- Completed Delicious Restaurant Landing Page! -->",
            "starter_code": "<!-- Completed Delicious Restaurant Landing Page! -->"
        }
    }
]

# ----------------- SENIOR WEB DESIGN ADVANCED (BOOTSTRAP & JS) - 16 SESSIONS -----------------
adv_stations = [
    {
        "id": 1,
        "badge_icon": "⚡",
        "badge_title": "Bootstrap CDN Medal",
        "title": "Station 1: Web Development Advanced - Bootstrap 1 Intro",
        "desc": "Link Bootstrap CDN, load responsive Navbars, and design layout cards!",
        "story": "<h3>⚡ Welcome to Web Advanced!</h3>"
                 "Let's learn how to build professional websites in minutes using **Bootstrap**, the world's most popular CSS framework!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>What is Bootstrap?</b> A pre-styled collection of CSS and JS utilities for fast, responsive web design.</li>"
                 "<li><b>Linking CDN:</b> Reference the Bootstrap stylesheet link inside the `<head>` tag.</li>"
                 "<li><b>Bootstrap Components:</b> Create gorgeous **Navbar** and **Card** elements without writing custom CSS!</li>"
                 "</ul>",
        "simple": "Bootstrap gives you pre-made CSS classes. Type the class name, and your button or layout instantly looks awesome!",
        "hint": "Link Bootstrap inside head: <code>&lt;link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\"&gt;</code>.",
        "challenge": "Link the Bootstrap 5.3 CDN inside the head section, and create a Bootstrap styled Card division with a class of 'card'!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <!-- Link Bootstrap CDN below! -->\n    \n</head>\n<body class=\"p-4\">\n    <!-- Add Bootstrap Card below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Link Bootstrap CDN", "code": "<link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">"},
            {"label": "Add Bootstrap Card", "code": "<div class=\"card\" style=\"width: 18rem;\">\n  <div class=\"card-body\">\n    <h5 class=\"card-title\">Bootstrap Card</h5>\n    <p class=\"card-text\">Linked successfully!</p>\n  </div>\n</div>"}
        ],
        "validation_rules": {
            "required_output_text": "bootstrap",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Bootstrap Navbar",
            "desc": "Link Bootstrap at home and design a fully styled navigation bar using classes like <code>navbar</code>, <code>navbar-dark</code>, and <code>bg-dark</code>!",
            "code": "<head>\n  <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">\n</head>\n<body>\n  <nav class=\"navbar navbar-expand-lg navbar-dark bg-dark\">\n    <div class=\"container-fluid\">\n      <a class=\"navbar-brand\" href=\"#\">My Brand</a>\n    </div>\n  </nav>\n</body>",
            "starter_code": "<!-- Create your Bootstrap Navbar here! -->"
        }
    },
    {
        "id": 2,
        "badge_icon": "🗂️",
        "badge_title": "Flexbox Wrap Medal",
        "title": "Station 2: Flexbox Core: Wrapping & Justification",
        "desc": "Align items in horizontal rows and handle line wrapping automatically!",
        "story": "<h3>🗂️ Flexbox Wrapping & Justification!</h3>"
                 "Let's master alignment using CSS Flexbox layout systems!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>display: flex;</code>: Initializes flex display layout on parents.</li>"
                 "<li><code>flex-wrap</code>: Sets row wrapping behavior when items exceed parents' width. Values: <code>nowrap</code> (stay in one line), <code>wrap</code> (wrap into multiple lines), and <code>wrap-reverse</code>.</li>"
                 "<li><code>justify-content</code>: Horizontal alignments inside flex rows. Values: <code>flex-start</code>, <code>flex-end</code>, <code>center</code>, <code>space-between</code>, <code>space-around</code>, and <code>space-evenly</code>.</li>"
                 "</ul>",
        "simple": "Flex-wrap is like text-wrapping. When you run out of room in a row, the next box drops to the next line!",
        "hint": "Set flex styles on parents: <code>display: flex; flex-wrap: wrap; justify-content: space-between;</code>.",
        "challenge": "Style the parent class 'flex-container' to display as flex, wrap items, and justify them with space-between spaces!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .flex-container {\n            /* Add flex alignments below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <div class=\"flex-container\">\n        <div style=\"width:100px; background:red;\">Item 1</div>\n        <div style=\"width:100px; background:blue;\">Item 2</div>\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Add display flex", "code": "display: flex;"},
            {"label": "Add flex-wrap wrap", "code": "flex-wrap: wrap;"},
            {"label": "Add space-between", "code": "justify-content: space-between;"}
        ],
        "validation_rules": {
            "required_output_text": "flex-container",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Flex Centering Layout",
            "desc": "Design a display parent at home that perfectly centers children horizontally and wraps them automatically using flex wrap!",
            "code": "<style>\n  .centered-flex {\n    display: flex;\n    flex-wrap: wrap;\n    justify-content: center;\n    gap: 15px;\n  }\n</style>",
            "starter_code": "<!-- Create your Flex Centering Layout here! -->"
        }
    },
    {
        "id": 3,
        "badge_icon": "↕️",
        "badge_title": "Flex Directions Medal",
        "title": "Station 3: Flexbox Directions & Alignments",
        "desc": "Align items vertically and flip axis orientations from rows to columns!",
        "story": "<h3>↕️ Vertical Flex Alignments!</h3>"
                 "Let's master item directions and vertical centering using Flexbox properties!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>flex-direction</code>: Sets main layout axis. Directions: <code>row</code> (horizontal line, default), <code>row-reverse</code>, <code>column</code> (stacked vertically), and <code>column-reverse</code>.</li>"
                 "<li><code>align-items</code>: Vertical alignment along the cross-axis. Configurations: <code>stretch</code> (expands full height, default), <code>flex-start</code> (align to top), <code>flex-end</code> (align to bottom), and <code>center</code> (perfect vertical centering!).</li>"
                 "</ul>",
        "simple": "When you set flex-direction to column, justify-content controls vertical alignment, and align-items controls horizontal alignment!",
        "hint": "Write CSS: <code>flex-direction: column; align-items: center;</code>.",
        "challenge": "Style the parent class 'column-container' to have vertical column direction and center items horizontally!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <style>\n        .column-container {\n            display: flex;\n            /* Add direction and alignment below! */\n            \n        }\n    </style>\n</head>\n<body>\n    <div class=\"column-container\">\n        <div>Item 1</div>\n        <div>Item 2</div>\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Add direction column", "code": "flex-direction: column;"},
            {"label": "Add align-items center", "code": "align-items: center;"}
        ],
        "validation_rules": {
            "required_output_text": "column-container",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Vertical Profile Box",
            "desc": "Create a layout at home where profile pictures, names, and buttons are stacked vertically and centered perfectly using flex columns!",
            "code": "<style>\n  .profile-box {\n    display: flex;\n    flex-direction: column;\n    align-items: center;\n    padding: 20px;\n    border: 1px solid #ccc;\n  }\n</style>",
            "starter_code": "<!-- Create your Vertical Profile Box here! -->"
        }
    },
    {
        "id": 4,
        "badge_icon": "🛠️",
        "badge_title": "Bootstrap Utilities Medal",
        "title": "Station 4: Bootstrap Layout Utilities",
        "desc": "Speed up coding using pre-made classes for spacing, borders, and displays!",
        "story": "<h3>🛠️ Bootstrap Utility Power!</h3>"
                 "Let's master pre-styled utility classes in Bootstrap to handle margins, paddings, backgrounds, and display states without writing CSS!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Spacing shorthand:</b> <code>m-</code> (margin), <code>p-</code> (padding), <code>mt-</code> (margin-top), <code>pe-</code> (padding-end/right) from 1 to 5. E.g. <code>p-3</code> adds medium padding.</li>"
                 "<li><b>Borders:</b> <code>border</code>, <code>border-primary</code>, <code>rounded</code>, and <code>rounded-circle</code>.</li>"
                 "<li><b>Text Utilities:</b> <code>text-center</code>, <code>text-primary</code> (blue), <code>text-danger</code> (red), and <code>text-white</code>.</li>"
                 "<li><b>Display:</b> <code>d-block</code>, <code>d-inline</code>, and <code>d-inline-block</code>.</li>"
                 "</ul>",
        "simple": "Instead of writing padding: 15px; in CSS, you can just add the class p-3 to your element in Bootstrap. It's incredibly fast!",
        "hint": "Link Bootstrap and apply helper classes: <code>class=\"p-5 bg-dark text-white rounded text-center\"</code>.",
        "challenge": "Style a division in Bootstrap with a dark background, white text, 48px padding (p-5), centered text, and rounded corners!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">\n</head>\n<body>\n    <!-- Add Bootstrap classes below! -->\n    <div class=\"\">\n        <h3>Speedy Utilities!</h3>\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Apply spacing utilities", "code": "class=\"p-5 bg-dark text-white rounded text-center\""}
        ],
        "validation_rules": {
            "required_output_text": "bg-dark",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Avatar Thumbnail",
            "desc": "Design a rounded circle avatar at home using Bootstrap classes for padding, borders, round shape <code>rounded-circle</code>, and centered alignment!",
            "code": "<img src=\"avatar.png\" class=\"p-2 border border-primary rounded-circle\" width=\"100\">",
            "starter_code": "<!-- Add your Avatar classes here! -->"
        }
    },
    {
        "id": 5,
        "badge_icon": "🕸️",
        "badge_title": "Bootstrap Grid Medal",
        "title": "Station 5: Level 2 Session 1: Grid System Intro",
        "desc": "Rely on structural Bootstrap containers, rows, and columns for grids!",
        "story": "<h3>🕸️ The Powerful 12-Column Grid!</h3>"
                 "Bootstrap layout works on a flexible 12-column grid. Let's learn how rows and cols divide space!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>.container</code>: Sets center-aligned layout boundaries.</li>"
                 "<li><code>.row</code>: Group container for columns (acts like a flex parent).</li>"
                 "<li><code>.col</code>: Column block. Automatically divides row space evenly!</li>"
                 "<li><b>12-Column Rule:</b> You can specify size using classes like <code>col-6</code> (takes half row) or <code>col-4</code> (takes 1/3 row). Sum of columns in one row should equal 12!</li>"
                 "</ul>",
        "simple": "Think of the row as a box that fits exactly 12 small books. A col-6 is a book that takes the space of 6 columns!",
        "hint": "Set up a grid with columns: <code>&lt;div class=\"row\"&gt;&lt;div class=\"col-6\"&gt;Half&lt;/div&gt;&lt;div class=\"col-6\"&gt;Half&lt;/div&gt;&lt;/div&gt;</code>.",
        "challenge": "Create a Bootstrap layout row with two columns, each taking exactly half the screen (col-6)!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">\n</head>\n<body>\n    <div class=\"container\">\n        <!-- Create your grid row and columns below! -->\n        \n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Add Grid Row", "code": "<div class=\"row\">\n  <div class=\"col-6 bg-info p-3\">Column A</div>\n  <div class=\"col-6 bg-warning p-3\">Column B</div>\n</div>"}
        ],
        "validation_rules": {
            "required_output_text": "col-6",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Three-Column Card Layout",
            "desc": "Build a grid system row at home that holds exactly three equal columns (col-4), each containing a styled card product!",
            "code": "<div class=\"row\">\n  <div class=\"col-4\">Card 1</div>\n  <div class=\"col-4\">Card 2</div>\n  <div class=\"col-4\">Card 3</div>\n</div>",
            "starter_code": "<!-- Create your Three Column row here! -->"
        }
    },
    {
        "id": 6,
        "badge_icon": "📱",
        "badge_title": "Responsive Grid Medal",
        "title": "Station 6: Responsive Screen Sizes & Columns",
        "desc": "Make layouts responsive across different screens using breakpoint classes!",
        "story": "<h3>📱 Layouts that fit every device!</h3>"
                 "Let's master responsive grid sizing based on target screens (phones, tablets, and laptops)!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Five Sizing Breakpoints:</b>"
                 "  <ul>"
                 "    <li><code>col-</code> (Extra small phones).</li>"
                 "    <li><code>col-sm-</code> (Small tablet, >576px).</li>"
                 "    <li><code>col-md-</code> (Medium tablets, >768px).</li>"
                 "    <li><code>col-lg-</code> (Laptop screen, >992px).</li>"
                 "    <li><code>col-xl-</code> (Extra large screen, >1200px).</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Responsiveness:</b> Write mixed grid sizes like <code>class=\"col-12 col-md-6\"</code> (takes full width on phone, but half on tablet!).</li>"
                 "</ul>",
        "simple": "When you specify col-12 col-md-6, your columns automatically stack on top of each other on mobile phones, but sit side by side on desktop computers!",
        "hint": "Set classes: <code>class=\"col-12 col-md-4\"</code>.",
        "challenge": "Style three column divisions to take full width (col-12) on mobile, but take 1/3 of the width (col-md-4) on tablet screens!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">\n</head>\n<body>\n    <div class=\"container\">\n        <div class=\"row\">\n            <!-- Add responsive column classes below! -->\n            <div class=\"\">Card A</div>\n            <div class=\"\">Card B</div>\n            <div class=\"\">Card C</div>\n        </div>\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Apply responsive classes", "code": "class=\"col-12 col-md-4 bg-light p-3 border\""}
        ],
        "validation_rules": {
            "required_output_text": "col-md-4",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Responsive Profile Cards",
            "desc": "Build a responsive grid layout at home that holds 2 profile cards taking 100% width on phone, but 50% width <code>col-sm-6</code> on tablet screens!",
            "code": "<div class=\"row\">\n  <div class=\"col-12 col-sm-6\">Profile Card A</div>\n  <div class=\"col-12 col-sm-6\">Profile Card B</div>\n</div>",
            "starter_code": "<!-- Create your Responsive Profile Cards grid here! -->"
        }
    },
    {
        "id": 7,
        "badge_icon": "🏨",
        "badge_title": "Royal Hotel Part 1 Medal",
        "title": "Station 7: Level 2 Session 2: Royal Hotel Template - Part 1",
        "desc": "Build a luxurious hotel home banner layout using Bootstrap Grids!",
        "story": "<h3>🏨 Final Project: Royal Hotel Landing Page!</h3>"
                 "Let's combine all Bootstrap elements to build a gorgeous, premium website landing page called <b>Royal Hotel</b>!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Navigation Header:</b> Create a sticky header with a dark brand and clean navigation links (Home, Rooms, Services, Gallery, Booking).</li>"
                 "<li><b>Hero Carousel Banner:</b> Create a stunning welcome slider with centered responsive text, customized with buttons.</li>"
                 "</ul>",
        "simple": "We use Bootstrap helper classes to quickly format full-width dark headers and add glowing buttons to book hotel rooms!",
        "hint": "Set up a grid container: <code>&lt;div class=\"container\"&gt;&lt;div class=\"row\"&gt;...&lt;/div&gt;&lt;/div&gt;</code>.",
        "challenge": "Setup the header container and home landing row using grid system rows styled with Bootstrap text alignments!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">\n</head>\n<body>\n    <!-- Setup Royal Hotel banner markup below! -->\n    \n</body>\n</html>",
        "pills": [
            {"label": "Add Royal Hero Banner", "code": "<div class=\"bg-dark text-white text-center py-5\">\n  <h1 class=\"display-4\">Royal Hotel & Resort</h1>\n  <p class=\"lead\">Savour luxury in the heart of our paradise resort.</p>\n  <button class=\"btn btn-warning btn-lg\">Book Room</button>\n</div>"}
        ],
        "validation_rules": {
            "required_output_text": "Resort",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Royal Services Bar",
            "desc": "Design a 3-column services showcase for your Royal Hotel at home using Bootstrap classes. Display icons representing Spa, Free Wifi, and Restaurant food!",
            "code": "<div class=\"row text-center mt-4\">\n  <div class=\"col-md-4\"><i class=\"fas fa-wifi\"></i><h4>Free Wifi</h4></div>\n  <div class=\"col-md-4\"><i class=\"fas fa-spa\"></i><h4>Luxury Spa</h4></div>\n  <div class=\"col-md-4\"><i class=\"fas fa-utensils\"></i><h4>Restaurant</h4></div>\n</div>",
            "starter_code": "<!-- Create your Services grid here! -->"
        }
    },
    {
        "id": 8,
        "badge_icon": "🛎️",
        "badge_title": "Royal Hotel Completed Medal",
        "title": "Station 8: Level 2 Session 3: Royal Hotel Template - Part 2",
        "desc": "Add room cards, styled service columns, booking forms, and complete the template!",
        "story": "<h3>🛎️ Complete the Royal Hotel!</h3>"
                 "Let's complete our premium hotel website by adding beautiful room product cards, a contact booking form, and styled layouts!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Rooms section:</b> Create product cards showing room features, booking options, and pricing tags.</li>"
                 "<li><b>Contact Form:</b> Design an elegant hotel reservation form using form utilities.</li>"
                 "<li><b>Review:</b> Review and align all columns, making sure the entire landing page is perfectly responsive!</li>"
                 "</ul>",
        "simple": "We use the grid col-md-4 to showcase three luxurious room choices side by side on laptop screens!",
        "hint": "Set up a grid row of room cards: <code>&lt;div class=\"row\"&gt;&lt;div class=\"col-md-4\"&gt;&lt;div class=\"card\"&gt;...&lt;/div&gt;&lt;/div&gt;&lt;/div&gt;</code>.",
        "challenge": "Create a room product card styled with Bootstrap cards, badges, and a Book button, and add a footer with address!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<head>\n    <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css\" rel=\"stylesheet\">\n</head>\n<body>\n    <div class=\"container\">\n        <div class=\"row\">\n            <!-- Add Room card below! -->\n            \n        </div>\n    </div>\n</body>\n</html>",
        "pills": [
            {"label": "Add Room Card", "code": "<div class=\"col-md-4\">\n  <div class=\"card\">\n    <div class=\"card-body\">\n      <h5 class=\"card-title\">Deluxe Suite</h5>\n      <p class=\"card-text\">$150 / Night</p>\n      <button class=\"btn btn-primary\">Book Room</button>\n    </div>\n  </div>\n</div>"}
        ],
        "validation_rules": {
            "required_output_text": "Suite",
            "required_canvas": False
        },
        "homework": {
            "title": "🎉 Magic Home Challenge: Completed Royal Resort Page!",
            "desc": "Assemble your entire hotel website at home! Combine the dark brand navigation bar, custom carousel welcome hero banner, Wifi/Spa service columns, room suites cards, booking registration form, and hotel address. You've completed a high-end Bootstrap template! 🌟",
            "code": "<!-- Completed Royal Hotel Landing Page! -->",
            "starter_code": "<!-- Completed Royal Hotel Landing Page! -->"
        }
    },
    {
        "id": 9,
        "badge_icon": "🔀",
        "badge_title": "JS Intro Medal",
        "title": "Station 9: Level 3 Session 1: JavaScript programming Core",
        "desc": "Add script tags, load data variables, and write logs to the console!",
        "story": "<h3>🔀 Welcome to JavaScript!</h3>"
                 "JavaScript is the brain of a website! It brings static pages to life with math, animations, logic, and interactivity!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Where to write JS:</b> Put code inside <code>&lt;script&gt;</code> tags (internal or external).</li>"
                 "<li><b>JS Syntax:</b> Declare variables using <code>var</code> (or <code>let</code>/<code>const</code>).</li>"
                 "<li><b>Data Types:</b> <code>String</code> (\"text\"), <code>Number</code> (12), and <code>Boolean</code> (true/false).</li>"
                 "<li><b>Output Methods:</b>"
                 "  <ul>"
                 "    <li><code>console.log(value)</code>: Prints directly to the console debugger screen.</li>"
                 "    <li><code>window.alert(value)</code>: Triggers a pop-up window notification.</li>"
                 "    <li><code>document.getElementById().innerHTML</code>: Changes text inside HTML tags!</li>"
                 "  </ul>"
                 "</li>"
                 "</ul>",
        "simple": "HTML builds the skeleton, CSS paints the dress, but JS makes the website think and talk!",
        "hint": "Write JS output: <code>console.log('Hello from JS!');</code> or declare variable: <code>var score = 100;</code>.",
        "challenge": "Write a script declaring a variable 'studentName' containing 'Rowan', and print 'Activated Session 9!' to the console!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <h1>JavaScript Basics</h1>\n    <script>\n        // Declare variable and write console.log below!\n        \n    </script>\n</body>\n</html>",
        "pills": [
            {"label": "Console log code", "code": "console.log('Activated Session 9!');"},
            {"label": "Declare variables", "code": "var studentName = 'Rowan';\nconsole.log(studentName);"}
        ],
        "validation_rules": {
            "required_output_text": "Activated Session 9!",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Hello Alerts!",
            "desc": "Write code at home that declares two variables (first name and age), prints them to the console, and triggers a window alert popup saying 'Welcome to JS Coding!'!",
            "code": "<script>\n  var name = 'Rowan';\n  var age = 15;\n  console.log(name + ' is ' + age);\n  window.alert('Welcome to JS Coding!');\n</script>",
            "starter_code": "<!-- Write your script here! -->"
        }
    },
    {
        "id": 10,
        "badge_icon": "🔀",
        "badge_title": "JS Logic Medal",
        "title": "Station 10: Level 3 Session 2: JS Operators & Conditionals",
        "desc": "Compare values and run code selectively using IF-else and comparison operators!",
        "story": "<h3>🗂️ JS Logic & Decisions!</h3>"
                 "Let's master mathematical operators and make smart decisions using conditional statements!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Operators:</b>"
                 "  <ul>"
                 "    <li><b>Arithmetic:</b> <code>+</code>, <code>-</code>, <code>*</code>, <code>/</code>.</li>"
                 "    <li><b>Assignment:</b> <code>=</code>.</li>"
                 "    <li><b>Comparison:</b> <code>==</code> (equal), <code>!=</code> (not equal), <code>&gt;</code>, <code>&lt;</code>, <code>&gt;=</code>, <code>&lt;=</code>.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Conditional Statements:</b>"
                 "  <ul>"
                 "    <li><code>if (condition) { ... } else { ... }</code>: Runs code depending on logic.</li>"
                 "    <li><code>Nested-if</code> & <code>switch</code> statements.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Logical Operators:</b> <code>&&</code> (AND), <code>||</code> (OR), and <code>!</code> (NOT).</li>"
                 "</ul>",
        "simple": "Conditionals are like road signs. If the light is green, drive. Else, stop!",
        "hint": "Create condition: <code>if (score >= 50) { console.log('Pass'); } else { console.log('Fail'); }</code>.",
        "challenge": "Write an IF-else statement checking if a score variable (set to 85) is greater than or equal to 50, and print 'Pass'!",
        "starter_code": "<script>\n    var score = 85;\n    // Write your conditional statement below!\n    \n</script>",
        "pills": [
            {"label": "Add IF statement", "code": "if (score >= 50) {\n    console.log('Pass');\n} else {\n    console.log('Fail');\n}"}
        ],
        "validation_rules": {
            "required_output_text": "Pass",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Smart Alarm System",
            "desc": "Design a smart condition checking alarm status at home! If temperature is greater than 100 or smoke is true, print 'DANGER'; else print 'All Clear'!",
            "code": "<script>\n  var temp = 105;\n  var smoke = true;\n  if (temp > 100 || smoke == true) {\n    console.log('DANGER');\n  } else {\n    console.log('All Clear');\n  }\n</script>",
            "starter_code": "<!-- Create your Smart Alarm script here! -->"
        }
    },
    {
        "id": 11,
        "badge_icon": "🔄",
        "badge_title": "JS Loops Medal",
        "title": "Station 11: Level 3 Session 3: JS Loops: For & While",
        "desc": "Repeat block actions infinitely or conditionally using for, while, and do-while loops!",
        "story": "<h3>🔄 Repeat with Loops!</h3>"
                 "Let's master repeating operations in programming to save writing hundreds of redundant lines!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><code>for</code>: Repeats code a set number of times. Contains starting counter, limit condition, and step increment (e.g. <code>for (var i = 0; i &lt; 5; i++)</code>).</li>"
                 "<li><code>while</code>: Repeats as long as a condition remains true.</li>"
                 "<li><code>do-while</code>: Always runs the code block at least ONCE before checking the condition!</li>"
                 "</ul>",
        "simple": "A loop is like running laps around a playground. You keep going until you complete your target count!",
        "hint": "Write loop: <code>for (var i = 1; i <= 5; i++) { console.log('Count ' + i); }</code>.",
        "challenge": "Write a `for` loop that prints numbers from 1 to 5 to the console!",
        "starter_code": "<script>\n    // Write your for loop below!\n    \n</script>",
        "pills": [
            {"label": "Add for loop", "code": "for (var i = 1; i <= 5; i++) {\n    console.log('Count ' + i);\n}"}
        ],
        "validation_rules": {
            "required_output_text": "Count 5",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Countdown Timer",
            "desc": "Create a loop at home that counts down backwards from 10 to 1, followed by printing 'Blast Off!' to the console!",
            "code": "<script>\n  for (var i = 10; i >= 1; i--) {\n    console.log(i);\n  }\n  console.log('Blast Off!');\n</script>",
            "starter_code": "<!-- Create your Countdown Timer here! -->"
        }
    },
    {
        "id": 12,
        "badge_icon": "🗃️",
        "badge_title": "JS Arrays Medal",
        "title": "Station 12: Level 3 Session 4: JS Arrays & Elements",
        "desc": "Group multiple elements into lists, pop, push, and loop arrays!",
        "story": "<h3>🗃️ Store Lists inside Arrays!</h3>"
                 "Let's learn how to organize multiple related variables inside a single data container called an **Array**!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Create:</b> Declare lists using brackets, e.g. <code>var fruits = [\"Apple\", \"Banana\"];</code>.</li>"
                 "<li><b>Access:</b> Access items using index numbers starting from 0 (e.g. <code>fruits[0]</code> is Apple).</li>"
                 "<li><code>length</code>: Property returning the count of items in an array.</li>"
                 "<li><code>push(item)</code>: Adds a new item to the END of an array.</li>"
                 "<li><code>pop()</code>: Removes the last item from an array.</li>"
                 "<li><b>Conversion:</b> Convert arrays to a single string using methods.</li>"
                 "</ul>",
        "simple": "Remember, computer indexing starts at 0, not 1! So the very first element of your array lives at index 0!",
        "hint": "Write code: <code>var colors = ['Red', 'Blue']; colors.push('Green'); console.log(colors[2]);</code>.",
        "challenge": "Create an array called 'hobbies' with 'Coding' and 'Gaming', push 'Robotics' to it, and log the array to the console!",
        "starter_code": "<script>\n    // Create array and push elements below!\n    \n</script>",
        "pills": [
            {"label": "Add Array operations", "code": "var hobbies = ['Coding', 'Gaming'];\nhobbies.push('Robotics');\nconsole.log(hobbies);"}
        ],
        "validation_rules": {
            "required_output_text": "Robotics",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Shopping List POP",
            "desc": "Declare an array of 3 grocery items at home. Push a 4th item, then pop the last item and log the length of your list to the console!",
            "code": "<script>\n  var list = ['Milk', 'Eggs', 'Bread'];\n  list.push('Butter');\n  list.pop();\n  console.log('List length: ' + list.length);\n</script>",
            "starter_code": "<!-- Create your Shopping List here! -->"
        }
    },
    {
        "id": 13,
        "badge_icon": "⚙️",
        "badge_title": "JS Functions Medal",
        "title": "Station 13: Level 4 Session 1: JS Functions & Event Calls",
        "desc": "Write reusable code blocks using functions and triggers!",
        "story": "<h3>⚙️ Reusable Code blocks with Functions!</h3>"
                 "Let's master reusable code scripts. Declare them once, and call them anywhere using functions!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Built-in vs User-defined:</b> JS has pre-made functions, but we can write our own!</li>"
                 "<li><b>Function Syntax:</b> Defined using the keyword <code>function name(params) { ... }</code>.</li>"
                 "<li><b>Calling:</b> Trigger functions directly in code or assign them to web element triggers (like button clicks!).</li>"
                 "<li><code>return</code>: Outputs values back from function scripts.</li>"
                 "<li><code>.value</code>: Read values typed inside input boxes!</li>"
                 "</ul>",
        "simple": "A function is like a recipe. You write the recipe down once, and cook it whenever you are hungry by calling it!",
        "hint": "Define: <code>function sayHello() { console.log('Welcome!'); }</code>.",
        "challenge": "Create a function called 'sayHello' that prints 'Welcome Rowan!' to the console, and call it!",
        "starter_code": "<script>\n    // Define and call function below!\n    \n</script>",
        "pills": [
            {"label": "Add function", "code": "function sayHello() {\n  console.log('Welcome Rowan!');\n}\nsayHello();"}
        ],
        "validation_rules": {
            "required_output_text": "Rowan",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Magic Multiplier",
            "desc": "Define a custom function at home that accepts two numbers as parameters, multiplies them together, returns the product, and logs the result to the console!",
            "code": "<script>\n  function multiply(a, b) {\n    return a * b;\n  }\n  var result = multiply(5, 6);\n  console.log('Product: ' + result);\n</script>",
            "starter_code": "<!-- Write your custom function here! -->"
        }
    },
    {
        "id": 14,
        "badge_icon": "🌴",
        "badge_title": "HTML DOM Medal",
        "title": "Station 14: Level 4 Session 2: HTML DOM Selectors",
        "desc": "Navigate HTML trees and select elements using IDs, classes, and tags!",
        "story": "<h3>🌴 The Document Object Model (DOM)!</h3>"
                 "The DOM represents your web page structure as a tree of objects. Let's learn how JavaScript selects tags to modify them!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>What is the DOM?</b> The structured tree map of a web page loaded in browsers.</li>"
                 "<li><b>Accessing Selectors:</b>"
                 "  <ul>"
                 "    <li><code>document.getElementById('id')</code>: Selects a single tag by unique ID.</li>"
                 "    <li><code>document.getElementsByClassName('class')</code>: Selects lists of classes.</li>"
                 "    <li><code>document.querySelector('selector')</code>: Modern selector matching CSS syntax!</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Accessing Core Objects:</b> Instantly access structural parts like <code>document.head</code>, <code>document.body</code>, and <code>document.title</code>!</li>"
                 "</ul>",
        "simple": "The querySelector works exactly like CSS selectors. Use a dot for class names and a hash for IDs!",
        "hint": "Select tag: <code>var header = document.getElementById('my-header'); console.log(header.innerHTML);</code>.",
        "challenge": "Select the heading with ID 'my-header' using DOM methods and log its innerHTML text to the console!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <h1 id=\"my-header\">Megaminds Studio</h1>\n    <script>\n        // Select element and log below!\n        \n    </script>\n</body>\n</html>",
        "pills": [
            {"label": "Select by ID", "code": "var header = document.getElementById('my-header');\nconsole.log(header.innerHTML);"}
        ],
        "validation_rules": {
            "required_output_text": "Megaminds",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Title grabber",
            "desc": "Write code at home that dynamically grabs the page title <code>document.title</code> and prints it to the console!",
            "code": "<script>\n  var pageTitle = document.title;\n  console.log('The document title is: ' + pageTitle);\n</script>",
            "starter_code": "<!-- Create your Title Grabber here! -->"
        }
    },
    {
        "id": 15,
        "badge_icon": "🪄",
        "badge_title": "DOM Manipulation Medal",
        "title": "Station 15: Level 4 Session 3: DOM Style & Event Triggers",
        "desc": "Modify HTML tags, inject custom CSS styles, and handle button clicks!",
        "story": "<h3>🪄 Modify Elements on Clicks!</h3>"
                 "Let's learn how JavaScript modifies elements and style colors dynamically in response to user actions!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>Modifying Styles:</b> Change layout CSS directly using <code>element.style.color = \"blue\";</code> or overwrite blocks with <code>element.style.cssText</code>.</li>"
                 "<li><b>Set Attributes:</b> Change element states dynamically.</li>"
                 "<li><b>Interactive Events:</b> Triggers code in response to user actions: <code>onclick</code> (mouse click), <code>onchange</code> (typing change), and <code>onmouseover</code> (hovering!).</li>"
                 "</ul>",
        "simple": "When you assign element.style.backgroundColor, you are painting your website dynamically behind the scenes using code!",
        "hint": "Set click event and modify style: <code>btn.onclick = function() { text.style.color = 'red'; };</code>.",
        "challenge": "Style the paragraph text color to green when the button is clicked using the `onclick` DOM trigger!",
        "starter_code": "<!DOCTYPE html>\n<html>\n<body>\n    <h1 id=\"text\">Magic Text</h1>\n    <button id=\"my-btn\">Change Color</button>\n    <script>\n        var btn = document.getElementById('my-btn');\n        var text = document.getElementById('text');\n        // Add click event below!\n        \n    </script>\n</body>\n</html>",
        "pills": [
            {"label": "Add Click Event", "code": "btn.onclick = function() {\n  text.style.color = 'green';\n};"}
        ],
        "validation_rules": {
            "required_output_text": "onclick",
            "required_canvas": False
        },
        "homework": {
            "title": "🏠 Magic Home Challenge: Toggle Light Mode",
            "desc": "Design a toggle button at home! When clicked, change the background color of the body <code>document.body.style.backgroundColor</code> to dark blue and text color to white!",
            "code": "<script>\n  var btn = document.getElementById('toggle-btn');\n  btn.onclick = function() {\n    document.body.style.backgroundColor = '#023047';\n    document.body.style.color = '#fff';\n  }\n</script>",
            "starter_code": "<!-- Create your Toggle Light Mode here! -->"
        }
    },
    {
        "id": 16,
        "badge_icon": "🏆",
        "badge_title": "Grand Master Medal",
        "title": "Station 16: Level 5 Session 1: Objects, BOM & Royal Hotel",
        "desc": "Construct Objects, interact with Window sizes, Local Storage, and final project!",
        "story": "<h3>🏆 JS Objects, Browser Windows & Graduation!</h3>"
                 "Congratulations, Grand Master! Let's complete the final hotel template with JS animations, storage, and explore modern ES6 variables!<br><br>"
                 "<b>💡 Key Lessons:</b>"
                 "<ul>"
                 "<li><b>JS Objects:</b> Group property data and functional methods together, e.g. <code>var room = { name: \"Suite\", price: 150 };</code>.</li>"
                 "<li><b>BOM (Browser Object Model):</b> Interact with window environments."
                 "  <ul>"
                 "    <li>Window size: <code>window.innerWidth</code> & <code>window.innerHeight</code>.</li>"
                 "    <li>Shorthand scrolling: <code>window.scrollTo()</code>.</li>"
                 "  </ul>"
                 "</li>"
                 "<li><b>Local Storage:</b> Save persistent data (<code>localStorage.setItem()</code>) and read it back (<code>localStorage.getItem()</code>) so user details survive browser page refreshes!</li>"
                 "<li><b>ES6 Variables:</b> Upgrade from <code>var</code> to block scoped <code>let</code> and constant <code>const</code> variables.</li>"
                 "</ul>",
        "simple": "Local Storage acts like a tiny drawer inside the browser. Put a note in it, and it will still be there tomorrow when you open the page!",
        "hint": "Set up a key in storage: <code>localStorage.setItem('username', 'Rowan');</code>.",
        "challenge": "Write code to save 'Rowan' in the local storage under key 'user', and declare a constant variable 'PI' set to 3.14!",
        "starter_code": "<script>\n    // Write local storage and const code below!\n    \n</script>",
        "pills": [
            {"label": "Add Storage & ES6 code", "code": "localStorage.setItem('user', 'Rowan');\nconst PI = 3.14;\nconsole.log(localStorage.getItem('user'));"}
        ],
        "validation_rules": {
            "required_output_text": "Rowan",
            "required_canvas": False
        },
        "homework": {
            "title": "🎉 Magic Graduation Challenge: Completed Hotel Landing Page!",
            "desc": "Connect JavaScript triggers to your Bootstrap Royal Hotel template at home! Add a reservation button that saves the booking details in Local Storage and alerts 'Welcome' when loaded! You have successfully mastered Web Design and Web Advanced Programming! Incredible work, Developer! 🎓🏆🌟",
            "code": "<!-- Completed Royal Hotel interactive landing page! -->",
            "starter_code": "<!-- Completed Royal Hotel interactive landing page! -->"
        }
    }
]

# Write Games JSON for senior_web_design
games_web = {
    "course_id": "senior_web_design",
    "course_title": "Web Design (HTML/CSS)",
    "course_subtitle": "Master the art of building beautiful websites from scratch!",
    "xp_total": 1600,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": web_stations
}
if not os.path.exists(web_path): os.makedirs(web_path)
with open(os.path.join(web_path, 'games.json'), 'w', encoding='utf-8') as f:
    json.dump(games_web, f, ensure_ascii=False, indent=2)

# Write Recap JSON for senior_web_design
recaps_web = []
for st in web_stations:
    recaps_web.append({
        "id": st["id"],
        "title": f"Session {st['id']} Summary",
        "sections": [
            {
                "heading": "🌟 Core Concept",
                "text": st["desc"]
            },
            {
                "heading": "📘 Student Homework",
                "text": st["homework"]["desc"]
            }
        ]
    })
with open(os.path.join(web_path, 'recap.json'), 'w', encoding='utf-8') as f:
    json.dump({"course_id": "senior_web_design", "recaps": recaps_web}, f, ensure_ascii=False, indent=2)


# Write Games JSON for senior_web_design_advanced
games_adv = {
    "course_id": "senior_web_design_advanced",
    "course_title": "Web Design Advanced (Bootstrap/JS)",
    "course_subtitle": "Speed up layout structures with Bootstrap grids and add programming logic with JavaScript!",
    "xp_total": 1600,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": adv_stations
}
if not os.path.exists(adv_path): os.makedirs(adv_path)
with open(os.path.join(adv_path, 'games.json'), 'w', encoding='utf-8') as f:
    json.dump(games_adv, f, ensure_ascii=False, indent=2)

# Write Recap JSON for senior_web_design_advanced
recaps_adv = []
for st in adv_stations:
    recaps_adv.append({
        "id": st["id"],
        "title": f"Session {st['id']} Summary",
        "sections": [
            {
                "heading": "🌟 Core Concept",
                "text": st["desc"]
            },
            {
                "heading": "📘 Student Homework",
                "text": st["homework"]["desc"]
            }
        ]
    })
with open(os.path.join(adv_path, 'recap.json'), 'w', encoding='utf-8') as f:
    json.dump({"course_id": "senior_web_design_advanced", "recaps": recaps_adv}, f, ensure_ascii=False, indent=2)

print("Web Design and Advanced Web Design databases successfully generated and strictly aligned with syllabus!")
