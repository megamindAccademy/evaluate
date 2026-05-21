import json
import os

db_dir = r"c:\Users\rowan\Desktop\ev\evaluate\database\senior_godot"
quiz_dir = os.path.join(db_dir, "quizzes")
os.makedirs(quiz_dir, exist_ok=True)

# ---------------------------------------------------------
# GAMES.JSON DATA GENERATION (ENGLISH VERSION)
# ---------------------------------------------------------
games_data = {
  "course_id": "senior_godot",
  "course_title": "Godot Game Development",
  "course_subtitle": "Develop your own games like a pro! 🎮✨",
  "xp_total": 1200,
  "mascot_img": "./assets/megaminds_mascot.png",
  "stations": [
    {
      "id": 1,
      "badge_icon": "🏰",
      "badge_title": "Medal of Magical Beginnings",
      "title": "Station 1: Welcome to the Magical World of Godot! 🏰",
      "desc": "A delightful introduction to game engines and the fun world of Godot with Toby the Teddy Bear!",
      "story": "<h3>🧸 Hello, creative game developer!</h3>I am your friend <b>Toby the Teddy Bear</b>, and I will accompany you on your journey to build your very first game! 🌟<br><br>Today we will discover the magic of the <b>Godot Engine</b>! A game engine is like a magical toy box containing everything we need to build games (movement tools, sounds, and colorful art!).<br><br><b>💡 Golden Knowledge from our official curriculum:</b><ul><li>🏗️ <b>Node:</b> Like a small colorful Lego block, it is the building block of every part of your game!</li><li>🏰 <b>Scene:</b> Like a big playroom where we gather all the Lego blocks (Nodes) to build a complete world!</li><li>👨‍👩‍👧‍👦 <b>Father-Child Structure:</b> The Child node inherits properties from its Parent node, just like a child following their loving parent's steps!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🧸 <b>Toby's Challenge:</b> Let's welcome the magical world of Godot by writing a sweet welcome message inside the start function <code>_ready()</code>!</div>",
      "simple": "A game engine is the magical toy box of games, and nodes are the colorful Lego blocks we use to build our dreams!",
      "hint": "Write the magical welcome message: <code>print(\"Welcome to the fun world of Godot!\")</code>",
      "challenge": "Add code to print Toby's sweet welcome: `Welcome to the fun world of Godot!` inside the start function.",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write the magic code here for Toby's sweet welcome!\n    ",
      "pills": [
        {
          "label": "Toby's Welcome",
          "code": "print(\"Welcome to the fun world of Godot!\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Welcome to the fun world of Godot!",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Creator's First Message",
        "desc": "Write code that prints your hero name with a sweet Godot welcome to finalize your first steps!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"I am a little hero and ready to make my game!\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your home message here, little genius!\n    "
      }
    },
    {
      "id": 2,
      "badge_icon": "📝",
      "badge_title": "Medal of Secret Codes",
      "title": "Station 2: Secret Codes and Smart Variables! 📝",
      "desc": "Learn the magic language of GDScript, variable boxes, and wake-up functions with Dino the Dinosaur!",
      "story": "<h3>🦖 Welcome, coding artist!</h3>I am your friend <b>Dino the little Dinosaur</b>, and today we will learn how to whisper secret words that Godot understands instantly! 🌟<br><br>We use a lovely and simple coding language called <b>GDScript</b>, which is very similar to Python. It lets us control our heroes and make them move and jump!<br><br><b>💡 Magic Info Capsule:</b><ul><li>📦 <b>Variable:</b> Like a smart box where we store the hero's energy or score. We use the magic word <code>var</code> to create it!</li><li>🔢 <b>Primitive Data Types:</b><ul><li><code>int</code>: Sweet whole numbers like the hero's hearts <code>5</code>!</li><li><code>float</code>: Precise decimal numbers like gravity speed <code>9.8</code>!</li><li><code>bool</code>: Magical choices (true or false) like 'is the hero flying?'</li></ul></li><li>⏳ <b>Special Functions:</b> <code>_ready()</code> runs once at the beginning to wake up our heroes, and <code>_process(delta)</code> runs at lightning speed to update game actions constantly!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🦖 <b>Dino's Challenge:</b> Let's create Dino's sweet energy box with a value of <code>100</code> and print it for everyone to see!</div>",
      "simple": "A variable is a magical box to store our heroes' energy, and GDScript is the language we use to tell Godot to move!",
      "hint": "Define the energy variable: <code>var energy = 100</code> and then print it: <code>print(energy)</code>",
      "challenge": "Define a variable named `energy` with a value of `100` and print it inside the ready function.",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Define variable energy and print it here!\n    ",
      "pills": [
        {
          "label": "Define & Print Energy",
          "code": "var energy = 100\n    print(energy)"
        }
      ],
      "validation_rules": {
        "required_output_text": "100",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Hero Heart Box",
        "desc": "Define a variable for the hero's hearts holding a value of 3 and print it at home to assist Dino!",
        "code": "extends Node\n\nfunc _ready():\n    var hearts = 3\n    print(\"Hero hearts count: \", hearts)",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your heart code here, little developer!\n    "
      }
    },
    {
      "id": 3,
      "badge_icon": "🎨",
      "badge_title": "Medal of the Little Artist",
      "title": "Station 3: The Little Artist and Animated Sprites! 🎨",
      "desc": "Design gorgeous 2D game worlds, Sprite nodes, and frame animation sheets with Kitty the active Kitten!",
      "story": "<h3>🐱 Welcome, creative artist!</h3>I am your friend <b>Kitty the active Kitten</b>, and today we will decorate our game with the most beautiful visual drawings and vibrant colors! ✨<br><br>To make our game come alive, let's learn about art styles and animated frames!<br><br><b>💡 Art & Animation Secrets from our PDFs:</b><ul><li>🎨 <b>Art Styles:</b> Cartoonish style full of bright colors, Pixel Art with classic retro vibes, and smooth Hand-Drawn drawings!</li><li>🖼️ <b>Sprite Node:</b> The node responsible for displaying any static (fixed) image in our lovely game.</li><li>🏃‍♀️ <b>AnimatedSprite Node:</b> Our magical node that displays the hero's actions frame-by-frame (Frame Animation) to make them look like they are running and jumping!</li><li>📜 <b>Sprite Sheet:</b> One large image containing all the hero's moves combined to save computer memory!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐱 <b>Kitty's Challenge:</b> Kitty is running at a speed of <code>150</code>! Let's print it to cheer her up!</div>",
      "simple": "AnimatedSprite combines consecutive images to make characters run, and colorful art makes players happy!",
      "hint": "Write the print statement for Kitty's speed: <code>print(\"Kitty's active speed is: 150\")</code>",
      "challenge": "Print the following text exactly: `Kitty's active speed is: 150`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to print Kitty's speed!\n    ",
      "pills": [
        {
          "label": "Print Kitty's Speed",
          "code": "print(\"Kitty's active speed is: 150\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Kitty's active speed is: 150",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Animation Frames",
        "desc": "Write code that prints the number of running frames of our hero (e.g. 8 frames) to help Kitty organize her sprite sheet!",
        "code": "extends Node\n\nfunc _ready():\n    var run_frames = 8\n    print(\"Hero running frames: \", run_frames)",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your frames count code here!\n    "
      }
    },
    {
      "id": 4,
      "badge_icon": "🐰",
      "badge_title": "Medal of Speedy Bunny",
      "title": "Station 4: Speedy Bunny and Smart Operators! 🐰",
      "desc": "Program speedy movement, mathematical operations, logic rules, and sizing with the set_scale function!",
      "story": "<h3>🐰 Welcome, my fast and smart friend!</h3>I am your friend <b>Speedy Bunny</b>, and today we will learn the magic language of math that moves our games and makes heroes jump and spin! 🌟<br><br>To design smart movement, we will use arithmetic and comparisons!<br><br><b>💡 Magic Math Box:</b><ul><li>➕ <b>Arithmetic Operators:</b> Addition <code>+</code>, Subtraction <code>-</code>, Multiplication <code>*</code>, and Division <code>/</code> to decide speeds and distances!</li><li>⚖️ <b>Comparison Operators:</b> Check if speed equals 50 (<code>==</code>), does not equal (<code>!=</code>), is greater than (<code>></code>), or less than (<code><</code>).</li><li>🛡️ <b>Logical Operators:</b> Combine conditions like (<code>and</code>, <code>or</code>, <code>not</code>) to set game rules precisely!</li><li>📐 <b>set_scale function:</b> We use <code>set_scale(Vector2(x, y))</code> to resize our lovely characters!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐰 <b>Bunny's Challenge:</b> Bunny runs at a basic speed of <code>50</code>, we want to double it by multiplying it by <code>2</code> and print his new speed <code>100</code>!</div>",
      "simple": "Arithmetic operations and logical conditions are the smart brain that decides when Bunny jumps and when he resizes!",
      "hint": "Multiply the basic speed by 2 and print the result: <code>print(\"Speedy Bunny's new speed is: \", base_speed * 2)</code>",
      "challenge": "Define a variable `base_speed = 50` and multiply it by 2, then print: `Speedy Bunny's new speed is: 100`",
      "starter_code": "extends Node\n\nfunc _ready():\n    var base_speed = 50\n    # Double the speed and print the result here!\n    ",
      "pills": [
        {
          "label": "Double Speed & Print",
          "code": "var double_speed = base_speed * 2\n    print(\"Speedy Bunny's new speed is: \", double_speed)"
        }
      ],
      "validation_rules": {
        "required_output_text": "Speedy Bunny's new speed is: 100",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Is Bunny a Giant?",
        "desc": "Compare the size of the paddle or Bunny, and print a boolean status using comparisons in code!",
        "code": "extends Node\n\nfunc _ready():\n    var is_giant = true\n    print(\"Is Speedy Bunny a giant? \", is_giant)",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your size comparison here!\n    "
      }
    },
    {
      "id": 5,
      "badge_icon": "💡",
      "badge_title": "Medal of the Game Idea",
      "title": "Station 5: Journey of a Game from Idea to Light! 💡🌱",
      "desc": "How do professional game engineers plan? Learn the SDLC phases and prototype your very first concept with Philo!",
      "story": "<h3>🐘 Welcome, genius game engineer!</h3>I am your friend <b>Philo the smart Elephant</b>! Today we will learn how game developers plan their incredible games! 🌟<br><br>Making a game is not just coding, it is an organized journey called the <b>Software Development Life Cycle (SDLC)</b>!<br><br><b>💡 The 6 Magic Stages of SDLC:</b><ul><li>💡 <b>1. Idea Generation:</b> Brainstorming ideas for our exciting game story!</li><li>🛠️ <b>2. Prototyping:</b> Building a quick, simple version to make sure the gameplay is fun!</li><li>🎨 <b>3. Design:</b> Designing art, characters, and sounds!</li><li>💻 <b>4. Development:</b> Writing the real GDScript code in Godot!</li><li>🧪 <b>5. Testing:</b> Playing the game to find and fix bugs!</li><li>🚀 <b>6. Release:</b> Sharing our game with friends and the world!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐘 <b>Philo's Challenge:</b> Print the first and most fundamental stage of game development!</div>",
      "simple": "SDLC is the magical map that transforms a simple idea into a real, playable game!",
      "hint": "Write the print statement: <code>print(\"The first step is idea generation!\")</code>",
      "challenge": "Print the following text exactly: `The first step is idea generation!`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to print the first amazing step!\n    ",
      "pills": [
        {
          "label": "Print First Stage",
          "code": "print(\"The first step is idea generation!\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "The first step is idea generation!",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Testing Games",
        "desc": "Write code printing the importance of testing games to eliminate bugs and avoid game crashes!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"Testing ensures the game is bug-free and perfect!\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your home testing statement here!\n    "
      }
    },
    {
      "id": 6,
      "badge_icon": "🖥️",
      "badge_title": "Medal of Magical Buttons",
      "title": "Station 6: Magical Buttons and Colorful Panels! 🖥️",
      "desc": "Discover the attractive world of UI nodes, Labels, Buttons, LineEdits, and layout Containers with Susu!",
      "story": "<h3>🐦 Welcome, visual panel designer!</h3>I am your friend <b>Susu the singing Bird</b>! Today we will learn to build UI panels to display scores, health, and buttons! 🌟<br><br>The User Interface <b>(UI)</b> is how players interact with our game!<br><br><b>💡 UI Nodes & Containers:</b><ul><li>📝 <b>Label Node:</b> Displays text on the screen like score or player name!</li><li>🔘 <b>Button Node:</b> An interactive button players click to start or purchase items!</li><li>📥 <b>LineEdit:</b> A box where players can type their name!</li><li>📦 <b>Containers:</b> <code>VBoxContainer</code> organizes buttons vertically, and <code>HBoxContainer</code> organizes them horizontally!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐦 <b>Susu's Challenge:</b> Let's print the score panel text <code>Score: 50</code> to display it!</div>",
      "simple": "Label nodes display sweet text like scores, and Buttons open the gates of interactive gameplay!",
      "hint": "Print the score text: <code>print(\"Score: 50\")</code>",
      "challenge": "Print the following text exactly to show the score: `Score: 50`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to display the score!\n    ",
      "pills": [
        {
          "label": "Print Score UI",
          "code": "print(\"Score: 50\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Score: 50",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Start Button Trigger",
        "desc": "Write code simulating the message printed when the start button is clicked (e.g. game launched)!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"Start button was successfully pressed!\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your button click logic simulation!\n    "
      }
    },
    {
      "id": 7,
      "badge_icon": "📡",
      "badge_title": "Medal of Signal Language",
      "title": "Station 7: Signal Language and Interactive Buttons! 📡",
      "desc": "Program button triggers, scene switching, quitting functions, and connect Godot signals with Maymoon!",
      "story": "<h3>🐒 Welcome, smart interactive programmer!</h3>I am your friend <b>Maymoon the playful Monkey</b>! Today we will make our games alive by responding to player clicks! 🌟<br><br>When a player clicks buttons, we use a genius system in Godot called <b>Signals</b> to tell the game what to do immediately!<br><br><b>💡 Signals & Scene Control:</b><ul><li>📡 <b>Signals:</b> A way for nodes to send events (like <code>pressed()</code> from a Button) to trigger code!</li><li>🔄 <b>Scene Switching:</b> Switch from main menu to game scene using: <code>get_tree().change_scene(\"res://Scenes/Game.tscn\")</code>!</li><li>🚪 <b>Quitting:</b> Exit the game peacefully using <code>get_tree().quit()</code>!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐒 <b>Maymoon's Challenge:</b> Let's simulate switching to the game scene by printing the confirmation message!</div>",
      "simple": "Signals are magical telephone lines that call code immediately when a player clicks a button to switch scenes!",
      "hint": "Print the scene switch message: <code>print(\"Scene changed to Game.tscn\")</code>",
      "challenge": "Print the following text exactly to simulate switching scenes: `Scene changed to Game.tscn`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code to print the scene transition!\n    ",
      "pills": [
        {
          "label": "Print Scene Switch",
          "code": "print(\"Scene changed to Game.tscn\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Scene changed to Game.tscn",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Quit Game Trigger",
        "desc": "Write code printing a simulation of quitting the game when players click Exit, using get_tree().quit()!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"Exit game called. Goodbye!\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your exit simulation here!\n    "
      }
    },
    {
      "id": 8,
      "badge_icon": "🎵",
      "badge_title": "Medal of Joyful Sounds",
      "title": "Station 8: Joyful Sounds and Dreamy Music! 🎵",
      "desc": "Add exciting sound effects, dreamy background music, and trigger AudioStreamPlayer2D with Shahdour!",
      "story": "<h3>🐶 Welcome, creative sound engineer!</h3>I am your friend <b>Shahdour the sweet Puppy</b>! Today we will add sound effects and music to make our game joyful! 🌟<br><br>Sound in games increases fun and makes players feel the actions!<br><br><b>💡 Golden Sound Box:</b><ul><li>💥 <b>Sound Effects (SFX):</b> Short sounds like jumping, bouncing, or scoring!</li><li>🎶 <b>Background Music (BGM):</b> Continuous music playing in the background to set the game mood!</li><li>📢 <b>AudioStreamPlayer2D Node:</b> The node responsible for playing sound files in Godot.</li><li>🎛️ <b>Properties:</b> <code>Stream</code> holds the sound file, <code>Volume</code> controls loudness, and <code>Pitch</code> controls speed/tone!</li><li>🎮 <b>Functions:</b> We use <code>play()</code> to start the sound and <code>stop()</code> to stop it!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐶 <b>Shahdour's Challenge:</b> Let's simulate playing the jumping sound by printing the play message!</div>",
      "simple": "AudioStreamPlayer2D plays sweet sounds using play() and stop() to make our games alive and interactive!",
      "hint": "Print the sound playing message: <code>print(\"Playing sweet sound!\")</code>",
      "challenge": "Print the following text exactly: `Playing sweet sound!`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code to simulate playing sound!\n    ",
      "pills": [
        {
          "label": "Play Sweet Sound",
          "code": "print(\"Playing sweet sound!\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Playing sweet sound!",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Stop Music",
        "desc": "Write code simulating the stopping of background music by calling stop() on our audio players!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"Background music stopped completely!\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your stop sound simulation!\n    "
      }
    },
    {
      "id": 9,
      "badge_icon": "📸",
      "badge_title": "Medal of the Smart Camera",
      "title": "Station 9: Magic Camera and Moving Backgrounds! 📸🌌",
      "desc": "Follow players smoothly, design deep parallax scrolling backgrounds, and load assets with Battoota!",
      "story": "<h3>🦆 Welcome, visual world explorer!</h3>I am your friend <b>Battoota the swimming Duck</b>! Today we will make our game world vast and learn the secrets of cameras! 🌟<br><br>The camera is the player's eye inside our game, allowing them to explore big worlds!<br><br><b>💡 Camera & Background Secrets:</b><ul><li>📸 <b>Camera2D Node:</b> A camera node that follows our player when <code>current</code> is set to true!</li><li>✨ <b>Smoothing:</b> A setting that makes the camera follow the player smoothly without stuttering!</li><li>🌌 <b>Parallax Background:</b> A layered background where far layers move slower than near layers to create depth!</li><li>📜 <b>preload:</b> A magic method like <code>preload(\"res://RainDrop.tscn\")</code> that loads assets into memory before playing to avoid lag!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🦆 <b>Battoota's Challenge:</b> Let's simulate preloading a raindrop asset by printing the success message!</div>",
      "simple": "Cameras follow the player smoothly, and Parallax backgrounds create amazing depth in our game worlds!",
      "hint": "Print the preloading success message: <code>print(\"Raindrop loaded successfully!\")</code>",
      "challenge": "Print the following text exactly to confirm the preload: `Raindrop loaded successfully!`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to print the preload success!\n    ",
      "pills": [
        {
          "label": "Print Preload",
          "code": "print(\"Raindrop loaded successfully!\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Raindrop loaded successfully!",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Camera Tracking Active",
        "desc": "Write code that checks and prints the camera tracking status, verifying current is active at home!",
        "code": "extends Node\n\nfunc _ready():\n    var camera_active = true\n    print(\"Is Camera2D active tracking? \", camera_active)",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write camera check code here!\n    "
      }
    },
    {
      "id": 10,
      "badge_icon": "🚀",
      "badge_title": "Medal of Polished Games",
      "title": "Station 10: Polishing Games and Launching to the Universe! 🚀✨",
      "desc": "Master game polishing, responsiveness, exporting to HTML5, and sharing free games on itch.io with Sanjoob!",
      "story": "<h3>🐿️ Welcome, future game publisher!</h3>I am your friend <b>Sanjoob the explorer Squirrel</b>! Today we will polish our game, fix all bugs, and make it ready to play on the web! 🌟<br><br>Polishing is the final creative touch that makes players happy and removes errors!<br><br><b>💡 Polishing & Publishing Secrets:</b><ul><li>✨ <b>Polishing Factors:</b><ul><li>❤️ <b>Fun Factor:</b> Is the game highly entertaining and makes players want to play again?</li><li>🕹️ <b>Responsiveness:</b> Immediate reaction to inputs and buttons!</li><li>🌱 <b>Liveliness:</b> Making the world active with visual effects and movements!</li></ul></li><li>🛠️ <b>Exporting:</b> Choose <code>Project -> Export</code> and select <code>HTML5</code> to run the game in web browsers!</li><li>🌐 <b>itch.io:</b> The best free website to upload, publish, and share our games with friends!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🐿️ <b>Sanjoob's Challenge:</b> Let's print that our game is fully polished and ready for publishing!</div>",
      "simple": "Polishing removes bugs and makes games fun, and HTML5 export allows everyone to play instantly in a web browser!",
      "hint": "Print the readiness message: <code>print(\"Game is polished and ready!\")</code>",
      "challenge": "Print the following text exactly: `Game is polished and ready!`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to declare game readiness!\n    ",
      "pills": [
        {
          "label": "Print Game Readiness",
          "code": "print(\"Game is polished and ready!\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Game is polished and ready!",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Export Steps",
        "desc": "Write code printing the three golden steps of exporting projects in Godot to web platforms!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"1. Project -> 2. Export -> 3. Choose HTML5\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write export instructions here!\n    "
      }
    },
    {
      "id": 11,
      "badge_icon": "🏓",
      "badge_title": "Medal of Pong Paddles",
      "title": "Station 11: Birth of the Legendary Pong Game - Part 1! 🏓",
      "desc": "Build the lovely Pong field, physics boundaries, moving player paddles, and keyboard input maps with Toby!",
      "story": "<h3>🧸 Welcome, game builder champion!</h3>I am your friend <b>Toby the Teddy Bear</b>! Today we start building a classic masterpiece: <b>The Pong Game</b>! 🌟<br><br>Pong is a fun duel between two players using paddles to hit a ball!<br><br><b>💡 Pong Foundations in Godot:</b><ul><li>🧱 <b>StaticBody2D (Walls):</b> Strong physical walls that do not move, keeping the ball inside the screen!</li><li>🏓 <b>KinematicBody2D (Paddles & Ball):</b> Physical bodies we control with code so they respond to inputs!</li><li>⌨️ <b>Inputs:</b> Left paddle moves with <code>W / S</code> keys, and right paddle moves with <code>Up / Down Arrows</code>!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🧸 <b>Toby's Challenge:</b> Let's write the code to print that the paddle is moving upward!</div>",
      "simple": "StaticBody2D boundaries protect the ball, and KinematicBody2D paddles move with keyboard keys to block the ball!",
      "hint": "Print the paddle moving upward: <code>print(\"Moving paddle up\")</code>",
      "challenge": "Print the following text exactly: `Moving paddle up`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to move the paddle!\n    ",
      "pills": [
        {
          "label": "Print Paddle Movement",
          "code": "print(\"Moving paddle up\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Moving paddle up",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Ball Initial Speed",
        "desc": "Define the ball's initial speed variable at home and print it to prepare for the ball launching!",
        "code": "extends Node\n\nfunc _ready():\n    var ball_speed = 300\n    print(\"Initial ball speed set to: \", ball_speed)",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write ball speed initialization!\n    "
      }
    },
    {
      "id": 12,
      "badge_icon": "🏆",
      "badge_title": "Medal of Bounce Challenge",
      "title": "Station 12: Return of Pong and the Ultimate Climax - Part 2! 🏆💥",
      "desc": "Program collision triggers, bounce physics, update scoreboard labels, and sketch trailer concepts with Toby!",
      "story": "<h3>🏆 You are a game developing champion!</h3>I am your friend <b>Toby the Teddy Bear</b>! Today we finish our Pong game with scores, ball bounces, and trailers! 🌟<br><br>To complete the excitement, we will code collision reflections and track points!<br><br><b>💡 Pong Physics & Climax:</b><ul><li>💥 <b>Area2D (Collisions):</b> A node that detects when the ball enters the goal or hits paddles!</li><li>🔄 <b>Ball Bounce Physics:</b> We reflect the ball's direction by multiplying its speed by negative one (<code>speed.x = -speed.x</code>)!</li><li>📊 <b>Updating Score:</b> We update the Label node immediately when the ball scores a point!</li><li>🎬 <b>Game Trailer:</b> A short, exciting video clip showcasing our game to invite players on itch.io!</li></ul><div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🧸 <b>Toby's Final Challenge:</b> Let's code the bounce of the ball off the paddle and print the message!</div>",
      "simple": "Area2D detects collisions, bounce math reflects the ball direction, and labels display scores!",
      "hint": "Print the bounce message: <code>print(\"Ball bounced off the paddle!\")</code>",
      "challenge": "Print the following text exactly: `Ball bounced off the paddle!`",
      "starter_code": "extends Node\n\nfunc _ready():\n    # Write code here to handle the bounce!\n    ",
      "pills": [
        {
          "label": "Print Paddle Bounce",
          "code": "print(\"Ball bounced off the paddle!\")"
        }
      ],
      "validation_rules": {
        "required_output_text": "Ball bounced off the paddle!",
        "required_canvas": False
      },
      "homework": {
        "title": "🏠 Magic Home Challenge: Game Slogan Idea",
        "desc": "Create a short and engaging marketing slogan for your Pong game and print it with joy!",
        "code": "extends Node\n\nfunc _ready():\n    print(\"Play the fastest and most fiery Pong game ever!\")",
        "starter_code": "extends Node\n\nfunc _ready():\n    # Write your promotional slogan here!\n    "
      }
    }
  ]
}

with open(os.path.join(db_dir, "games.json"), "w", encoding="utf-8") as f:
    json.dump(games_data, f, ensure_ascii=False, indent=2)
print("games.json generated successfully!")

# ---------------------------------------------------------
# RECAP.JSON DATA GENERATION (ENGLISH VERSION)
# ---------------------------------------------------------
recap_data = {
  "course_id": "senior_godot",
  "recaps": [
    {
      "id": 1,
      "title": "Session 1 Recap: Welcome to the Magical World of Godot! 🏰",
      "sections": [
        {
          "heading": "🧱 What are Nodes and Scenes?",
          "text": "A Node is the primary building block in Godot, like a small colorful Lego piece! We combine these blocks to create a Scene, representing a complete room or level in our game!"
        },
        {
          "heading": "🏗️ Parent-Child Hierarchy",
          "text": "Children follow parents! A Child node inherits all properties and coordinates from its Parent node, moving together inside the Godot world smoothly!"
        }
      ]
    },
    {
      "id": 2,
      "title": "Session 2 Recap: Secret Codes and Smart Variables! 📝",
      "sections": [
        {
          "heading": "📦 Smart Variables Box",
          "text": "We use the var keyword to create smart boxes storing values like int whole numbers, float decimals, or bool logic choices!"
        },
        {
          "heading": "⏳ ready and process Functions",
          "text": "The ready() function runs once at the beginning to wake up nodes, while the process() function runs repeatedly to update movement at lightning speed!"
        }
      ]
    },
    {
      "id": 3,
      "title": "Session 3 Recap: The Little Artist and Animated Sprites! 🎨",
      "sections": [
        {
          "heading": "🖌️ Game Art & Styles",
          "text": "We learned about retro Pixel Art, cartoonish styles, and hand-drawn visuals that make our game world beautiful and friendly!"
        },
        {
          "heading": "🏃‍♀️ Frame-by-Frame Animations",
          "text": "We used AnimatedSprite nodes to chain consecutive animation frames from a single Sprite Sheet, making our character walk and jump smoothly!"
        }
      ]
    },
    {
      "id": 4,
      "title": "Session 4 Recap: Speedy Bunny and Smart Operators! 🐰",
      "sections": [
        {
          "heading": "➕ Arithmetic & Operators",
          "text": "Addition, subtraction, multiplication, and division are mathematical tools we use in GDScript to calculate speed, double scores, or reverse directions!"
        },
        {
          "heading": "📐 Sizing and set_scale",
          "text": "We studied logical comparisons like and/or to control when actions happen, and utilized the set_scale function to shrink or grow nodes!"
        }
      ]
    },
    {
      "id": 5,
      "title": "Session 5 Recap: Journey of a Game from Idea to Light! 💡🌱",
      "sections": [
        {
          "heading": "🗺️ The 6 Steps of SDLC",
          "text": "A game developer brainstorms Ideas, creates a simple Prototype, designs visual assets, codes the game, tests for bugs, and finally releases it!"
        },
        {
          "heading": "🔬 Prototyping & Playtesting",
          "text": "Prototyping ensures our gameplay is fun, while thorough testing resolves unexpected crashes and bugs to please our players!"
        }
      ]
    },
    {
      "id": 6,
      "title": "Session 6 Recap: Magical Buttons and Colorful Panels! 🖥️",
      "sections": [
        {
          "heading": "📝 Labels and Buttons",
          "text": "Labels display dynamic game texts (scores, health, warnings), while Buttons let players interact with the game with a single click!"
        },
        {
          "heading": "📦 Organizing layouts with Containers",
          "text": "Layout containers like VBoxContainer and HBoxContainer automatically organize UI items vertically or horizontally in a clean grid!"
        }
      ]
    },
    {
      "id": 7,
      "title": "Session 7 Recap: Signal Language and Interactive Buttons! 📡",
      "sections": [
        {
          "heading": "📡 Signals System",
          "text": "Signals are like internal phones in Godot, enabling a node like a Button to send a pressed() signal to execute corresponding codes!"
        },
        {
          "heading": "🔄 Scene Transitions & Exit",
          "text": "We switch scenes smoothly in GDScript using get_tree().change_scene(), and exit the application instantly using get_tree().quit()!"
        }
      ]
    },
    {
      "id": 8,
      "title": "Session 8 Recap: Joyful Sounds and Dreamy Music! 🎵",
      "sections": [
        {
          "heading": "💥 SFX vs Background Music",
          "text": "Sound effects (SFX) play short triggers upon jumping or bouncing, while background music (BGM) loops to create a magical atmosphere!"
        },
        {
          "heading": "🎛️ Audio Nodes & Controls",
          "text": "We use AudioStreamPlayer2D nodes to hold sound files, adjusting volume and pitch, and running play() and stop() methods!"
        }
      ]
    },
    {
      "id": 9,
      "title": "Session 9 Recap: Magic Camera and Moving Backgrounds! 📸🌌",
      "sections": [
        {
          "heading": "📸 Camera2D and Smoothing",
          "text": "The Camera2D follows the player smoothly when smoothing is turned on, keeping the camera centered on the active world player!"
        },
        {
          "heading": "🌌 Parallax Background & preload()",
          "text": "ParallaxBackground layer scales move far backgrounds slower to create depth, and preload() loads scenes in advance to avoid lag!"
        }
      ]
    },
    {
      "id": 10,
      "title": "Session 10 Recap: Polishing Games and Launching to the Universe! 🚀✨",
      "sections": [
        {
          "heading": "✨ Game Polishing",
          "text": "Polishing makes games feel complete by boosting responsiveness, increasing fun factor, and removing minor visual glitches!"
        },
        {
          "heading": "🌐 Web Exporting & itch.io",
          "text": "Exporting games to HTML5 format prepares web-ready files, allowing us to upload and share our games freely on itch.io!"
        }
      ]
    },
    {
      "id": 11,
      "title": "Session 11 Recap: Birth of the Legendary Pong Game - Part 1! 🏓",
      "sections": [
        {
          "heading": "🧱 Collisions & Kinematic Bodies",
          "text": "We designed solid outer boundaries using StaticBody2D nodes, and built moving paddles and ball using KinematicBody2D nodes!"
        },
        {
          "heading": "⌨️ Player Input Mappings",
          "text": "Mapped keyboard W/S keys to control the left player, and arrow keys to control the right player, configuring interactive duels!"
        }
      ]
    },
    {
      "id": 12,
      "title": "Session 12 Recap: Return of Pong and the Ultimate Climax - Part 2! 🏆💥",
      "sections": [
        {
          "heading": "💥 Collision Area2D & Scoring",
          "text": "Area2D sensors catch ball overlaps to score points, updating scoreboard labels, and multiplying speed by negative one for bounces!"
        },
        {
          "heading": "🎬 Creating Game Trailers",
          "text": "A game trailer showcases gameplay highlights in a short video clip to promote our newly published games on itch.io!"
        }
      ]
    }
  ]
}

with open(os.path.join(db_dir, "recap.json"), "w", encoding="utf-8") as f:
    json.dump(recap_data, f, ensure_ascii=False, indent=2)
print("recap.json generated successfully!")

# ---------------------------------------------------------
# QUIZZES GENERATION (1 to 6) (ENGLISH VERSION)
# ---------------------------------------------------------
quizzes_content = {
  "quiz1.json": {
    "quiz_title": "Godot Game Development - Challenge 1",
    "quiz_name": "Quiz 1: Nodes, Scenes, and Magic GDScript! 🏰📝",
    "questions": [
      {
        "q": "What is the primary building block of every object and feature in the Godot Engine?",
        "opts": [
          "A sweet Node",
          "A code script file",
          "A physics engine",
          "A camera node only"
        ],
        "correct": 0,
        "exp": "A Node is the fundamental building block and Lego piece in Godot used to build everything from characters to backgrounds!"
      },
      {
        "q": "What do we call a tree-like organization of nodes representing a complete world or screen level?",
        "opts": [
          "An Event",
          "A sweet Scene",
          "A database",
          "A sound library"
        ],
        "correct": 1,
        "exp": "A Scene is like a playroom where we combine various nodes together to represent a level or menu screen!"
      },
      {
        "q": "In the Parent-Child hierarchy inside Godot, what happens to the Child node's properties?",
        "opts": [
          "They disappear completely",
          "The child inherits properties (like position) from the parent",
          "They override the parent node entirely",
          "They convert to complex text files"
        ],
        "correct": 1,
        "exp": "The Child node inherits coordinate scales and movements from its Parent node, walking with it everywhere in the game!"
      },
      {
        "q": "What is the primary scripting language in Godot, designed to be simple and similar to Python?",
        "opts": [
          "JavaScript",
          "C++",
          "GDScript language",
          "Visual Blocks"
        ],
        "correct": 2,
        "exp": "GDScript is a sweet, simple scripting language created specifically for Godot, making it very easy for beginners to learn!"
      },
      {
        "q": "Which magic keyword do we use to declare a smart box (variable) to store game values?",
        "opts": [
          "var",
          "func",
          "const",
          "print"
        ],
        "correct": 0,
        "exp": "The keyword 'var' stands for variable, which prepares a smart memory box to hold scores, health, or speeds!"
      },
      {
        "q": "If we want to store our hero's health hearts count (e.g. 3) as a whole number, what is the type of data?",
        "opts": [
          "Float decimal values",
          "Bool logic values",
          "String text values",
          "int integer values"
        ],
        "correct": 3,
        "exp": "An 'int' (integer) data type is used specifically for storing whole numbers without any fractions, like hearts or counts!"
      },
      {
        "q": "Which data type stores only two logical choices: true or false?",
        "opts": [
          "bool logic values",
          "float decimal values",
          "int values",
          "Lego nodes"
        ],
        "correct": 0,
        "exp": "A 'bool' (boolean) data type holds only true or false choices, telling us if our hero is flying, alive, or grounded!"
      },
      {
        "q": "When is the ready() function automatically called in Godot?",
        "opts": [
          "Continuously on every single frame",
          "Once at the beginning when the scene loads and node enters the tree",
          "Only when objects collide",
          "When the application exits"
        ],
        "correct": 1,
        "exp": "The _ready() function runs once like a morning alarm, waking up nodes to configure their initial states!"
      },
      {
        "q": "Which fast function is called continuously on every frame to update movements and character positions?",
        "opts": [
          "ready()",
          "quit()",
          "_process(delta) process update",
          "change_scene()"
        ],
        "correct": 2,
        "exp": "The _process(delta) function runs constantly at high speeds to keep game loops updating movements smoothly!"
      },
      {
        "q": "What is the primary benefit of using a Game Engine like Godot?",
        "opts": [
          "To browse websites only",
          "To program giant office spreadsheets",
          "To provide ready-made tools for physics, rendering, and sound to easily build games",
          "To paint digital canvases only"
        ],
        "correct": 2,
        "exp": "A game engine provides pre-built libraries for graphics, sounds, and physics, saving developers from writing systems from scratch!"
      }
    ],
    "tasks": [
      {
        "title": "Godot Sweet Welcome Challenge",
        "desc": "Write code printing a warm welcome text in the _ready() function to test your project startup!"
      },
      {
        "title": "Smart Energy Variable",
        "desc": "Define a variable storing Dino's energy value and print it to verify memory box creations!"
      }
    ]
  },
  "quiz2.json": {
    "quiz_title": "Godot Game Development - Challenge 2",
    "quiz_name": "Quiz 2: Art Styles, Animation, and Bunny Mathematics! 🎨🐰",
    "questions": [
      {
        "q": "Which art style relies on small colored square grids to represent retro classic games?",
        "opts": [
          "3D Art",
          "Pixel Art style",
          "Vector graphics",
          "Realistic styles"
        ],
        "correct": 1,
        "exp": "Pixel Art is made of tiny, visible colored squares, giving games a classic, retro, and cute look!"
      },
      {
        "q": "What do we call the individual 2D images representing characters and items in game worlds?",
        "opts": [
          "Audio nodes",
          "Sprites",
          "Large Scenes",
          "Math formulas"
        ],
        "correct": 1,
        "exp": "Sprites are the 2D images used to display players, items, and decorations inside our colorful levels!"
      },
      {
        "q": "What is a Sprite Sheet in 2D game development?",
        "opts": [
          "A folder full of sound clips",
          "One large image combining all animation frames of a character to save memory",
          "A list of variables",
          "A physics boundary node"
        ],
        "correct": 1,
        "exp": "A Sprite Sheet aggregates all poses and frames of a character into one single image file, conserving memory and improving speed!"
      },
      {
        "q": "Which node in Godot is specifically designed to play frame-by-frame sequences of player running frames?",
        "opts": [
          "StaticBody2D",
          "AnimatedSprite node",
          "AudioStreamPlayer2D",
          "Camera2D"
        ],
        "correct": 1,
        "exp": "The AnimatedSprite node handles playing frame sequences smoothly to animate characters while walking or jumping!"
      },
      {
        "q": "Which arithmetic operator do we use in code to multiply speeds or double scores?",
        "opts": [
          "Plus sign (+)",
          "Asterisk sign (*)",
          "Slash sign (/)",
          "Percent sign (%)"
        ],
        "correct": 1,
        "exp": "We use the asterisk symbol (*) for multiplication in scripting to scale speeds, double values, or calculate dimensions!"
      },
      {
        "q": "Which comparison operator checks if two values are exactly equal to each other?",
        "opts": [
          "Single equals (=)",
          "Double equals (==)",
          "Exclamation equals (!=)",
          "Greater than sign (>)"
        ],
        "correct": 1,
        "exp": "Double equals (==) is the equality checker in programming, whereas single equals (=) assigns values to variables!"
      },
      {
        "q": "What does the logical 'and' operator require to make the whole condition true?",
        "opts": [
          "Only one of the combined conditions must be true",
          "All combined conditions must be true",
          "None of the conditions must be true",
          "The scale must equal 1"
        ],
        "correct": 1,
        "exp": "The logical 'and' operator demands that all connected conditions evaluate to true for the final statement to be true!"
      },
      {
        "q": "Which function allows us to resize (grow or shrink) our characters in Godot?",
        "opts": [
          "set_scale(Vector2)",
          "change_scene()",
          "play()",
          "stop()"
        ],
        "correct": 0,
        "exp": "We use set_scale(Vector2(x, y)) to multiply the scaling size of characters or objects in both axes!"
      },
      {
        "q": "In vector coordinates Vector2(x, y), what does the 'x' axis represent?",
        "opts": [
          "Vertical up-and-down movement",
          "Horizontal left-and-right coordinate",
          "Audio volume level",
          "The color palette"
        ],
        "correct": 1,
        "exp": "In 2D coordinate spaces, x coordinates represent horizontal positions (left-and-right) and y coordinates represent vertical positions!"
      },
      {
        "q": "If a character's base speed is 40 and we want to divide it by 2 in code, which symbol do we use?",
        "opts": [
          "Plus (+)",
          "Slash (/)",
          "Minus (-)",
          "Ampersand (&)"
        ],
        "correct": 1,
        "exp": "We use the forward slash (/) for division in scripting languages to calculate quotients and split speeds!"
      }
    ],
    "tasks": [
      {
        "title": "Animated Sprite Setup",
        "desc": "Configure an AnimatedSprite with a Sprite Sheet containing player running frames and adjust frame speed!"
      },
      {
        "title": "Speed Doubler",
        "desc": "Write code to double character movement speed and resize the player's scale Vector2!"
      }
    ]
  },
  "quiz3.json": {
    "quiz_title": "Godot Game Development - Challenge 3",
    "quiz_name": "Quiz 3: Game SDLC, UI Controls, and Container Layouts! 🖥️💡",
    "questions": [
      {
        "q": "What does SDLC stand for in game and software engineering?",
        "opts": [
          "Simple Design Level Control",
          "Software Development Life Cycle",
          "Sound Dynamic Loop Code",
          "Static Body Layer Collision"
        ],
        "correct": 1,
        "exp": "SDLC (Software Development Life Cycle) represents the structured steps developers follow from initial concept to release!"
      },
      {
        "q": "Which phase of the SDLC is dedicated to brainstorming initial features, story settings, and game play themes?",
        "opts": [
          "Idea Generation phase",
          "Testing phase",
          "Development phase",
          "HTML Export phase"
        ],
        "correct": 0,
        "exp": "Idea Generation is the very first golden phase, hosting brainstorming sessions to establish rules, characters, and gameplay!"
      },
      {
        "q": "Why is the Prototyping phase crucial during game development?",
        "opts": [
          "To sell the game to players immediately",
          "To build a quick, simple test version of gameplay mechanics to verify if the core idea is fun",
          "To program rich sounds",
          "To publish files on itch.io"
        ],
        "correct": 1,
        "exp": "A prototype lets developers test simple mechanics quickly, ensuring the game is engaging before investing effort in art and code!"
      },
      {
        "q": "What do we call the SDLC phase where developers play the game repeatedly to hunt and resolve bugs?",
        "opts": [
          "Idea phase",
          "Testing phase",
          "Design phase",
          "Release phase"
        ],
        "correct": 1,
        "exp": "The Testing phase is where playtesters hunt down errors, visual glitches, and bugs to ensure a smooth, stable experience!"
      },
      {
        "q": "What is UI (User Interface) in games?",
        "opts": [
          "The code that controls physics gravity",
          "The visual layer (scores, buttons, health) that lets players interact with and read game info",
          "A folder of audio recordings",
          "The camera node"
        ],
        "correct": 1,
        "exp": "User Interface (UI) is the presentation layer consisting of health bars, buttons, and scores that lets players communicate with the game!"
      },
      {
        "q": "Which Godot UI node is used specifically to render and display static or dynamic texts like 'Score: 50'?",
        "opts": [
          "Button node",
          "Label node",
          "LineEdit node",
          "VBoxContainer"
        ],
        "correct": 1,
        "exp": "The Label node displays any text sentences, scores, or titles on the screen for players to view!"
      },
      {
        "q": "Which UI node is used to receive mouse click interactions to start levels or open panels?",
        "opts": [
          "Label node",
          "Button node",
          "LineEdit node",
          "AudioStreamPlayer2D"
        ],
        "correct": 1,
        "exp": "The Button node triggers pressed signals when clicked, allowing players to launch games, select options, or buy upgrades!"
      },
      {
        "q": "Which UI node allows players to type in customized text strings like entering their custom hero name?",
        "opts": [
          "Label node",
          "LineEdit node",
          "Button node",
          "HBoxContainer"
        ],
        "correct": 1,
        "exp": "The LineEdit node provides a text entry box where players can type names, inputs, or secret cheat codes!"
      },
      {
        "q": "What is the primary function of Container nodes like VBoxContainer in Godot?",
        "opts": [
          "To play sound effects",
          "To automatically align and organize child UI controls vertically (above each other)",
          "To move paddles up and down",
          "To create parallax depth"
        ],
        "correct": 1,
        "exp": "VBoxContainer stands for Vertical Box Container, which aligns all child buttons and labels neatly in a vertical column!"
      },
      {
        "q": "Which container aligns child controls horizontally side-by-side in a neat row?",
        "opts": [
          "VBoxContainer",
          "HBoxContainer",
          "GridContainer",
          "Sprite node"
        ],
        "correct": 1,
        "exp": "HBoxContainer stands for Horizontal Box Container, which arranges buttons or icons side-by-side in a row!"
      }
    ],
    "questions_count": 10,
    "tasks": [
      {
        "title": "UI Dashboard Assembly",
        "desc": "Build a main menu with a Title Label, Start Button, and VBoxContainer aligning your layouts!"
      },
      {
        "title": "Player Name Box",
        "desc": "Integrate a LineEdit box for player name entry, displaying a welcome message on a Label!"
      }
    ]
  },
  "quiz4.json": {
    "quiz_title": "Godot Game Development - Challenge 4",
    "quiz_name": "Quiz 4: Connected Signals, Scene Transitions, and Audio Streams! 📡🎵",
    "questions": [
      {
        "q": "What is a Signal in the Godot Engine architecture?",
        "opts": [
          "A physics barrier node",
          "An event trigger sent by a node to communicate with code immediately when an action occurs",
          "A background music sound file",
          "A folder of graphic sheets"
        ],
        "correct": 1,
        "exp": "Signals are internal notification networks that tell scripts immediately when buttons are pressed, timers tick, or bodies collide!"
      },
      {
        "q": "Which default signal is emitted by the Button node when a player clicks it?",
        "opts": [
          "button_up()",
          "pressed()",
          "focus_entered()",
          "mouse_entered()"
        ],
        "correct": 1,
        "exp": "The pressed() signal is fired by buttons immediately when a mouse click or finger tap is fully pressed and released!"
      },
      {
        "q": "Which code command switches the current active scene in Godot (e.g. from Menu to Gameplay)?",
        "opts": [
          "get_tree().quit()",
          "get_tree().change_scene(\"path\")",
          "play()",
          "set_scale()"
        ],
        "correct": 1,
        "exp": "We switch scenes in scripts using get_tree().change_scene() by providing the path to our target Scene template (.tscn)!"
      },
      {
        "q": "Which command closes and shuts down the game application immediately?",
        "opts": [
          "get_tree().change_scene()",
          "get_tree().quit()",
          "stop()",
          "preload()"
        ],
        "correct": 1,
        "exp": "The command get_tree().quit() requests the OS to shut down and close our game client peacefully and cleanly!"
      },
      {
        "q": "What are sound effects (SFX) in video games?",
        "opts": [
          "Long looping musical themes",
          "Short, interactive sound prompts triggered by specific events like jumps, strikes, or points",
          "The layout containers",
          "Static physical bodies"
        ],
        "correct": 1,
        "exp": "Sound Effects (SFX) are quick sound triggers activated by actions like coin collecting, bounces, or level completions!"
      },
      {
        "q": "What is background music (BGM) in games?",
        "opts": [
          "Quick collision warning chimes",
          "Continuous, looping musical tracks that set the atmospheric mood and tone of levels",
          "Code that changes scenes",
          "The scale of the viewport"
        ],
        "correct": 1,
        "exp": "Background Music (BGM) plays looping musical tracks continuously, keeping players relaxed or excited during gameplay!"
      },
      {
        "q": "Which node is responsible for loading and playing audio streams inside Godot levels?",
        "opts": [
          "StaticBody2D",
          "AudioStreamPlayer2D node",
          "Camera2D",
          "Label node"
        ],
        "correct": 1,
        "exp": "The AudioStreamPlayer2D node is our magical loudspeaker, playing audio files, sounds, and musical tracks!"
      },
      {
        "q": "Which property in the AudioStreamPlayer2D holds the actual audio file (.mp3 or .wav)?",
        "opts": [
          "Volume_db",
          "Pitch_scale",
          "Stream resource",
          "Autoplay"
        ],
        "correct": 2,
        "exp": "The 'Stream' property holds the sound resource file, telling the player which file to execute when triggered!"
      },
      {
        "q": "Which command triggers the AudioStreamPlayer2D node to play its loaded audio stream?",
        "opts": [
          "play()",
          "stop()",
          "start()",
          "preload()"
        ],
        "correct": 0,
        "exp": "We invoke the play() function on our audio nodes to start playing sound streams from the beginning!"
      },
      {
        "q": "How can we stop the music or mute sounds when players request a pause in code?",
        "opts": [
          "By deleting the node resource",
          "By calling the stop() function on our audio players",
          "By shutting down Godot entirely",
          "By shrinking camera boundaries"
        ],
        "correct": 1,
        "exp": "Invoking the stop() method immediately halts playback on the player node, muting its stream instantly!"
      }
    ],
    "tasks": [
      {
        "title": "Signal Connection Challenge",
        "desc": "Connect a Start Button's pressed() signal to a custom function that prints a launch message!"
      },
      {
        "title": "Play Jumping SFX",
        "desc": "Add an AudioStreamPlayer2D and write a script invoking play() whenever Bunny jumps!"
      }
    ]
  },
  "quiz5.json": {
    "quiz_title": "Godot Game Development - Challenge 5",
    "quiz_name": "Quiz 5: Smoothing Cameras, Parallax Backgrounds, and Game Polishing! 📸🚀",
    "questions": [
      {
        "q": "What is the primary role of the Camera2D node in 2D platformers and adventure games?",
        "opts": [
          "To paint sprites",
          "To control what the player sees and follow characters smoothly around vast levels",
          "To trigger jump sound effects",
          "To resize UI buttons"
        ],
        "correct": 1,
        "exp": "The Camera2D acts as the player's eye, following character coordinates smoothly to show the active surrounding level!"
      },
      {
        "q": "How do we make a Camera2D node active, ensuring it is the main screen viewpoint?",
        "opts": [
          "Set the 'current' property to true in the inspector",
          "Delete the camera and leave the scene default",
          "Connect a button signal to the camera",
          "Call get_tree().quit()"
        ],
        "correct": 0,
        "exp": "Setting 'current' to true turns the Camera2D node into the active viewport controller, projecting its framing to the screen!"
      },
      {
        "q": "What does the 'Smoothing' property do when enabled in a Camera2D node?",
        "opts": [
          "It makes the screen shake violently",
          "It creates a smooth, lag-free transition as the camera catches up to player movements, reducing screen stutter",
          "It converts graphics to pixel art",
          "It silences audio nodes"
        ],
        "correct": 1,
        "exp": "Smoothing enables the camera to glide gently after the character rather than centering instantly, offering comfortable views!"
      },
      {
        "q": "What is the Parallax Background effect and how does it enhance game worlds?",
        "opts": [
          "A physics code to speed up ball bounces",
          "A layered visual system where distant background layers move slower than near layers to create depth",
          "An exit button system",
          "A looping sound player"
        ],
        "correct": 1,
        "exp": "Parallax scrolling moves far layers (like mountains) slowly and near layers quickly, mimicking realistic depth!"
      },
      {
        "q": "What is the key benefit of preloading scenes in code using preload(\"path\")?",
        "opts": [
          "To load resources into memory before gameplay starts to avoid sudden stutter when spawning items",
          "To delete items to save disk space",
          "To scale down button nodes",
          "To cancel camera smoothing properties"
        ],
        "correct": 0,
        "exp": "Preloading cache-loads assets like raindrops or bullets beforehand, avoiding lag when they spawn during gameplay!"
      },
      {
        "q": "What does game 'Polishing' refer to in the development life cycle?",
        "opts": [
          "Wiping computer monitors",
          "Adding fine visual details, refining controls responsiveness, adding sound effects, and fixing all minor bugs for smooth play",
          "Renaming games in itch.io files",
          "Writing ready() code blocks for the first time"
        ],
        "correct": 1,
        "exp": "Polishing adds sparkle! It enhances responsiveness, injects juicy effects, and removes minor glitches before public launch!"
      },
      {
        "q": "During game polishing, what does the 'Liveliness' factor represent?",
        "opts": [
          "The game client running without crashes",
          "Making game worlds feel alive and reactive with small details (wind, grass swaying, flying birds, particles)",
          "How fast buttons respond to keyboard keys",
          "The total file size of games"
        ],
        "correct": 1,
        "exp": "Liveliness injects ambient life, like clouds drifting, birds chirping, or grass swaying, making levels immersive!"
      },
      {
        "q": "Which export target do we configure in Godot to play our games directly inside any web browser?",
        "opts": [
          "Old retro phone packaging",
          "HTML5 platform export for Web",
          "Normal plain text files (.txt)",
          "Console format exclusively"
        ],
        "correct": 1,
        "exp": "HTML5 compiles game scenes into files readable by web browsers, allowing players to play instantly with one link!"
      },
      {
        "q": "What is itch.io in the indie game development ecosystem?",
        "opts": [
          "A cartoon streaming website",
          "A popular free platform where developers publish, share, and host indie games for the world to play",
          "A pixel art design software",
          "A game engine competitor to Godot"
        ],
        "correct": 1,
        "exp": "itch.io is the indie game playground! It lets you upload game builds easily, share links, and build portfolio pages!"
      },
      {
        "q": "What are the correct steps to export your Godot project to web HTML5 files?",
        "opts": [
          "Delete the project and write it again",
          "Go to Project -> Export -> Add HTML5 -> Click Export Project without debug marks",
          "Write quit() statements at ready",
          "Call itch.io support directly"
        ],
        "correct": 1,
        "exp": "Open project settings, choose export targets, add an HTML5 profile, and click export to generate playable directories!"
      }
    ],
    "tasks": [
      {
        "title": "Parallax Depth World",
        "desc": "Build a scene with a dual-layered parallax background (mountains and clouds) moving at different scales!"
      },
      {
        "title": "Publishing Preparation",
        "desc": "Export your polished game to HTML5, prepare it for upload, and design its promotional banner!"
      }
    ]
  },
  "quiz6.json": {
    "quiz_title": "Godot Game Development - Challenge 6",
    "quiz_name": "Quiz 6: Classic Pong Physics, Collisions, and Promos! 🏓🏆",
    "questions": [
      {
        "q": "What is the core gameplay mechanic in the classic game of Pong?",
        "opts": [
          "Jumping over hurdles and collecting coins",
          "Moving paddles vertically to hit and bounce a ball, preventing it from passing behind your boundary",
          "Programming cameras to follow birds",
          "Designing promotional flyers only"
        ],
        "correct": 1,
        "exp": "Pong is a legendary table-tennis duel where players control paddles vertically to bounce a ball back and forth!"
      },
      {
        "q": "Which physical body node in Godot is ideal for solid walls that do not move but serve to block and bounce objects?",
        "opts": [
          "KinematicBody2D",
          "StaticBody2D solid physics body",
          "Label node",
          "AudioStreamPlayer2D"
        ],
        "correct": 1,
        "exp": "StaticBody2D is perfect for solid, immovable barriers (walls, floors) designed to block and bounce moving bodies!"
      },
      {
        "q": "Which physics body is ideal for players paddles and balls, where we want custom script codes to drive movement?",
        "opts": [
          "KinematicBody2D controllable body",
          "StaticBody2D node",
          "Camera2D",
          "User Interface container"
        ],
        "correct": 0,
        "exp": "KinematicBody2D gives developers precise control over velocities, collisions, and movements through scripting!"
      },
      {
        "q": "How do players control paddle directions in our classic Pong level design?",
        "opts": [
          "Paddles move automatically without controls",
          "Left paddle uses W/S keys, and Right paddle uses keyboard Up/Down arrows",
          "Clicking randomly with mouse buttons",
          "Using microphone sounds"
        ],
        "correct": 1,
        "exp": "The left player controls with W (up) and S (down), and the right player controls with Up/Down Arrows!"
      },
      {
        "q": "Which dedicated update function in GDScript is used to process physics movements and collision velocities?",
        "opts": [
          "ready() function",
          "_physics_process(delta) loop",
          "change_scene() method",
          "quit() command"
        ],
        "correct": 1,
        "exp": "The _physics_process(delta) loop is synchronized with physics frames, making it ideal for moving paddles and balls!"
      },
      {
        "q": "Which collision sensor node is used in goals to detect when balls enter score zones?",
        "opts": [
          "Label node",
          "Area2D overlap sensor node",
          "Camera2D",
          "Music player node"
        ],
        "correct": 1,
        "exp": "Area2D registers overlaps and intersections rather than physical blocks, making it perfect for goal nets and trigger areas!"
      },
      {
        "q": "Script-wise in GDScript, how do we reflect the ball's horizontal direction when it collides with a paddle?",
        "opts": [
          "Multiply horizontal speed by zero",
          "Multiply horizontal speed by negative one (speed.x = -speed.x)",
          "Increase speed tenfold instantly",
          "Call get_tree().quit()"
        ],
        "correct": 1,
        "exp": "Multiplying velocity by -1 (speed.x = -speed.x) flips the sign, reversing the ball's horizontal direction!"
      },
      {
        "q": "How do we display and update current game scores on the screen during a Pong match?",
        "opts": [
          "Using audio playing triggers",
          "Adding a Label UI node and updating its text property when a goal Area2D triggers a point",
          "Drawing numbers on a Sprite Sheet",
          "Calling set_scale() to enlarge viewports"
        ],
        "correct": 1,
        "exp": "We place Label nodes on screen. When goal sensors detect scoring, scripts increment score variables and update Label texts!"
      },
      {
        "q": "What is a Game Trailer and why is it important?",
        "opts": [
          "A tool to fix bugs in Godot",
          "A short, engaging showcase video displaying gameplay actions to hook players and encourage downloads on itch.io",
          "A music loop file",
          "A static wall boundary"
        ],
        "correct": 1,
        "exp": "A trailer packs high-intensity highlights into a short clip, convincing viewers that the game is fun and worth playing!"
      },
      {
        "q": "How can we make our classic Pong game extremely fun and satisfying to play?",
        "opts": [
          "Delete all sound effects entirely",
          "Add satisfying bounce SFX, energetic BGM, juice visual sparks, and clean color schemes",
          "Disable left paddle control variables",
          "Turn off computers during play"
        ],
        "correct": 1,
        "exp": "Juicy sound effects upon hit, background tracks, screenshakes, and pleasant art styles turn simple mechanics into addictive fun!"
      }
    ],
    "tasks": [
      {
        "title": "Pong Physics Arena",
        "desc": "Set up a Pong scene with StaticBody2D boundaries, KinematicBody2D paddles, and configure movement scripts!"
      },
      {
        "title": "Goal Sensors Integration",
        "desc": "Add Area2D goal detectors, connect overlap signals to increment score variables, and print results!"
      }
    ]
  }
}

for fname, qdata in quizzes_content.items():
    with open(os.path.join(quiz_dir, fname), "w", encoding="utf-8") as f:
        json.dump(qdata, f, ensure_ascii=False, indent=2)
    print(f"{fname} generated successfully!")

print("\n=======================================================")
print("ALL ENGLISH GODOT CURRICULUM DATABASES REDESIGNED AND GENERATED!")
print("=======================================================")
