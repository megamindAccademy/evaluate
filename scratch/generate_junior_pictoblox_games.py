import os
import json

db_path = 'database'
course_id = 'junior_pictoblox'
mascot_name = 'Tobi the Coding Bear 🐻'
mascot_short = 'Tobi 🐻'
mascot_emoji = '🐻'

pictoblox_sessions = [
    {
        "id": 1,
        "badge_icon": "🏁",
        "badge_title": "Animal Racing Medal",
        "title": "Station 1: Introduction to PicToBlox & Animal Racing",
        "desc": "Learn how to navigate the PicToBlox workspace, drag color-coded puzzle blocks, and program your very first sprite race!",
        "points": [
            "<b>PicToBlox Workspace Layout</b>: Exploring the Stage (preview), Blocks Palette (drawers), and Script Area (workspace).",
            "<b>Dragging & Snapping Blocks</b>: Combining blocks vertically like Lego blocks to build sequences.",
            "<b>Stage Coordinate System</b>: Moving sprites along horizontal X and vertical Y grid axes."
        ],
        "objectives": [
            "Position the racing sprites on the left boundary using coordinate blocks.",
            "Make your favorite animal sprite glide smoothly to the finish line."
        ],
        "project": "<b>Animal Racing Game</b>: Program a rabbit and a turtle sprite to compete in a race to the finish line, playing cheering sounds when they cross!",
        "new_blocks": [
            ("go to x:() y:()", "Motion", "Instantly teleports the sprite to a specific X and Y spot on the Stage grid."),
            ("glide () secs to x:() y:()", "Motion", "Moves the sprite smoothly to a target spot on the grid over a specified time."),
            ("say () for () seconds", "Looks", "Displays a text bubble containing your message on the screen for a set duration."),
            ("start sound ()", "Sound", "Plays a fun sound effect instantly without pausing the rest of the block commands.")
        ],
        "simple": "Imagine PicToBlox blocks are like Lego blocks! You snap one block on top of another to build a towering command that tells your sprite exactly where to go!",
        "hint": "Type in the editor: <code>print(\"Animal Racing active!\")</code> and press Run!",
        "challenge": "Print the exact message: <code>Animal Racing active!</code> to simulate the race track startup.",
        "starter_code": "# Simulate PicToBlox Session 1: Animal Racing\n",
        "verify_phrase": "Animal Racing active!",
        "pills": [
            {
                "label": "Start Animal Race",
                "code": "print(\"Animal Racing active!\")"
            }
        ],
        "homework_desc": "Create a new project where a cat sprite says 'Get ready...', waits, and then glides smoothly across the stage to X=200, Y=50 while playing a meowing sound!",
        "homework_code": "# Home Challenge: Cat Racing Script\n# Write your solution here!"
    },
    {
        "id": 2,
        "badge_icon": "🐘",
        "badge_title": "Elephant Story Medal",
        "title": "Station 2: Events & Repeat Loops (Elephant Story)",
        "desc": "Master starting events (Hat blocks), show/hide visibility rules, and endless loop structures to animate character dialogue.",
        "points": [
            "<b>Hat Blocks (Events)</b>: Triggers that listen for user clicks or backdrop changes to run code.",
            "<b>Show & Hide Visibility</b>: Toggling whether sprites are visible or hidden on the stage canvas.",
            "<b>Infinite Looping</b>: Repeating character sprite animations over and over."
        ],
        "objectives": [
            "Use the Green Flag trigger to kickstart your story scripts.",
            "Animate walking legs using a loop that cycles costumes automatically."
        ],
        "project": "<b>Elephant Story</b>: Build a story where an elephant walks through the jungle, switches scenery to the savanna, and speaks with a friendly monkey.",
        "new_blocks": [
            ("when Green Flag clicked", "Events", "The yellow starting block that runs connected scripts when the game plays."),
            ("forever", "Control", "A loop container that runs the code blocks inside it repeatedly without stopping."),
            ("wait () seconds", "Control", "Pauses the execution of blocks for a short time to help sequence animations."),
            ("show / hide", "Looks", "Instantly shows or hides your character sprite from the Stage layout."),
            ("switch backdrop to ()", "Looks", "Changes the background graphics layout to a new scenery backdrop.")
        ],
        "simple": "Imagine a forever loop is like a musical box that repeats your favorite song over and over until you close the lid!",
        "hint": "Type in the editor: <code>print(\"Elephant Story animation active!\")</code> and press Run!",
        "challenge": "Print the message: <code>Elephant Story animation active!</code> to start the backdrop story.",
        "starter_code": "# Simulate PicToBlox Session 2: Elephant Story\n",
        "verify_phrase": "Elephant Story animation active!",
        "pills": [
            {
                "label": "Animate Elephant Story",
                "code": "print(\"Elephant Story animation active!\")"
            }
        ],
        "homework_desc": "Build a script where a phantom sprite stays hidden, waits 2 seconds, changes the background backdrop to 'Castle', and then pops up playing a magic sound!",
        "homework_code": "# Home Challenge: Castle Phantom Story\n# Write your solution here!"
    },
    {
        "id": 3,
        "badge_icon": "🌀",
        "badge_title": "Maze Solver Medal",
        "title": "Station 3: Sensing & Conditions (Maze Game)",
        "desc": "Learn how to make smart choices using conditions (If Statements), keyboard keys, and color detection borders.",
        "points": [
            "<b>Conditional Choices</b>: Using If statements to decide if a code path should be executed.",
            "<b>Keyboard Interactivity</b>: Sensing key presses to move characters around in 4 directions.",
            "<b>Collision Detection</b>: Sensing boundaries using color touches and sprite overlays."
        ],
        "objectives": [
            "Build keyboard steer controls (Arrow keys) to steer a player sprite.",
            "Program collision boundaries that block or bounce players when they touch red walls."
        ],
        "project": "<b>Maze Game</b>: Draw a maze backdrop and program a mouse sprite that moves with keyboard arrow keys, bouncing back to the start if it touches the walls!",
        "new_blocks": [
            ("if <> then", "Control", "Runs blocks inside only when the hexagonal condition inside is met."),
            ("key () pressed?", "Sensing", "Checks if a specific keyboard key (like arrow keys) is currently held down."),
            ("touching color ()?", "Sensing", "Detects if your sprite is overlapping with a specific background color."),
            ("change x by () / change y by ()", "Motion", "Moves the sprite left/right (x-axis) or up/down (y-axis) by coordinate points.")
        ],
        "simple": "An If statement is like a traffic light! If the light is green, your hero walks forward. If it's red, they must stand still!",
        "hint": "Type in the editor: <code>print(\"Maze controller activated!\")</code> and press Run!",
        "challenge": "Print the message: <code>Maze controller activated!</code> to run the collision grid check.",
        "starter_code": "# Simulate PicToBlox Session 3: Maze Game\n",
        "verify_phrase": "Maze controller activated!",
        "pills": [
            {
                "label": "Activate Maze Controller",
                "code": "print(\"Maze controller activated!\")"
            }
        ],
        "homework_desc": "Write code where a player moves right by 10 points when Right Arrow is pressed. If they touch the yellow chest color, play a victory fanfare!",
        "homework_code": "# Home Challenge: Chest Collector Script\n# Write your solution here!"
    },
    {
        "id": 4,
        "badge_icon": "🐸",
        "badge_title": "Frog Jumper Medal",
        "title": "Station 4: Sprite Communication (Jumper Frog)",
        "desc": "Master inter-sprite communication using Broadcast signals, obstacle spawning, and jump physics.",
        "points": [
            "<b>Broadcast Signals</b>: Shouting out a text message that tells other sprites to act.",
            "<b>Listen Triggers</b>: Running independent code paths when receiving broadcast signals.",
            "<b>Random Number Generators</b>: Making game physics surprise-driven using random ranges."
        ],
        "objectives": [
            "Broadcast a message to trigger obstacle movements.",
            "Use random ranges to position falling items across the stage."
        ],
        "project": "<b>Jumper Frog Game</b>: Code a game where a frog jumps in place when space is pressed, dodging insect obstacles that spawn at random spots using broadcast syncs.",
        "new_blocks": [
            ("broadcast ()", "Events", "Sends a global text message signal to all active sprites in the game."),
            ("when I receive ()", "Events", "Starts a script execution immediately when a matching broadcast is captured."),
            ("pick random () to ()", "Operators", "Selects a random surprise number within a set numerical range.")
        ],
        "simple": "Broadcasting is like a gym teacher blowing a whistle! When the whistle blows (broadcast), all students run (when I receive)!",
        "hint": "Type in the editor: <code>print(\"Broadcast message received successfully!\")</code> and press Run!",
        "challenge": "Print the message: <code>Broadcast message received successfully!</code> to verify communication.",
        "starter_code": "# Simulate PicToBlox Session 4: Broadcast Syncs\n",
        "verify_phrase": "Broadcast message received successfully!",
        "pills": [
            {
                "label": "Send Broadcast Message",
                "code": "print(\"Broadcast message received successfully!\")"
            }
        ],
        "homework_desc": "Create a script where a button sprite broadcasts 'Start Game' when clicked, making the main character say 'Game Started!' and glide onto the screen.",
        "homework_code": "# Home Challenge: Broadcast Trigger\n# Write your solution here!"
    },
    {
        "id": 5,
        "badge_icon": "🏀",
        "badge_title": "Basketball Pro Medal",
        "title": "Station 5: Variables as Scoreboards (Basketball)",
        "desc": "Discover variables, scoreboards, score tracking, and terminal game over conditions.",
        "points": [
            "<b>Variables</b>: Digital boxes in memory that store and update numbers or text.",
            "<b>Scoreboards</b>: Displaying parameters on screen to keep track of achievements.",
            "<b>Global Shutdown</b>: Halt all running code loops immediately."
        ],
        "objectives": [
            "Initialize the scoreboard variables at startup.",
            "Change score parameters dynamically on target touches."
        ],
        "project": "<b>Basketball Game</b>: Build a game where a ball drops from a random coordinate. Catching it with your net adds 1 point. If it hits the floor, trigger a 'stop all' game over!",
        "new_blocks": [
            ("set [variable] to ()", "Variables", "Sets the initial value of a variable when the game starts."),
            ("change [variable] by ()", "Variables", "Adds or subtracts a numerical amount from a variable score."),
            ("stop [all]", "Control", "Stops all running loops, scripts, and sounds in the entire game."),
            ("set x to () / set y to ()", "Motion", "Sets your character's position along a single axis layout.")
        ],
        "simple": "A variable is like a small chalkboard! You start with a zero written on it, and every time you score, you erase it and write the new score!",
        "hint": "Type in the editor: <code>print(\"Score variable updated to 10!\")</code> and press Run!",
        "challenge": "Print the message: <code>Score variable updated to 10!</code> to run the scoring scoreboard simulation.",
        "starter_code": "# Simulate PicToBlox Session 5: Variables & Scoreboards\n",
        "verify_phrase": "Score variable updated to 10!",
        "pills": [
            {
                "label": "Update Scoreboard",
                "code": "print(\"Score variable updated to 10!\")"
            }
        ],
        "homework_desc": "Write code to reset a 'Life' variable to 3. If a player touches an obstacle, subtract 1 life, and if 'Life' equals 0, stop all actions!",
        "homework_code": "# Home Challenge: Life System Simulator\n# Write your solution here!"
    },
    {
        "id": 6,
        "badge_icon": "👾",
        "badge_title": "Giga-man Clicker Medal",
        "title": "Station 6: Click Events & Custom Blocks (Giga-man)",
        "desc": "Learn how to use direct click event triggers, toggle scoreboard overlays, and structure code using custom blocks.",
        "points": [
            "<b>Click Interactive Triggers</b>: Running blocks instantly when a player clicks on a sprite.",
            "<b>Variable Visibility Toggle</b>: Hiding and showing scoreboard parameters dynamically.",
            "<b>Custom Procedures (My Blocks)</b>: Grouping long code chains into single reusable blocks."
        ],
        "objectives": [
            "Define custom blocks to perform repeating routines (like jumps).",
            "Show or hide variable displays during gameplay transitions."
        ],
        "project": "<b>Giga-man Clicker Game</b>: Build an interactive arcade game where clicking Giga-man makes him perform a custom jump definition and adds a score point, displaying the scoreboard.",
        "new_blocks": [
            ("when this sprite clicked", "Events", "Triggers code execution when the player clicks directly on the sprite's canvas area."),
            ("hide variable () / show variable ()", "Variables", "Shows or hides the variable's visual dashboard from the game screen."),
            ("define [My Block]", "My Blocks", "Creates a custom block to define a reusable function code sequence.")
        ],
        "simple": "Custom blocks are like recipes! Instead of listing instructions every time you make a cake, you just name the recipe 'Bake Cake' and call it!",
        "hint": "Type in the editor: <code>print(\"Giga-man game interface loaded!\")</code> and press Run!",
        "challenge": "Print the message: <code>Giga-man game interface loaded!</code> to launch the click engine.",
        "starter_code": "# Simulate PicToBlox Session 6: Click Actions\n",
        "verify_phrase": "Giga-man game interface loaded!",
        "pills": [
            {
                "label": "Initialize Giga-man Game",
                "code": "print(\"Giga-man game interface loaded!\")"
            }
        ],
        "homework_desc": "Write a script where clicking a coin sprite plays a 'Ding' sound, adds 10 to a score variable, and hides the coin sprite.",
        "homework_code": "# Home Challenge: Clickable Coin Script\n# Write your solution here!"
    },
    {
        "id": 7,
        "badge_icon": "🎨",
        "badge_title": "Shapes Artist Medal",
        "title": "Station 7: Functions & Drawings (Draw SHAPES)",
        "desc": "Master turtle drawing techniques, angles, and custom shape builders using Pen extension blocks.",
        "points": [
            "<b>Pen Drawing Trails</b>: Leaving colorful drawing tracks as characters move.",
            "<b>Angle Degrees Logic</b>: Turning correct degrees to draw squares (90°) and triangles (120°).",
            "<b>Parametric Custom Blocks</b>: Packaging shape logic into custom procedures."
        ],
        "objectives": [
            "Activate the drawing Pen Extension pack in PicToBlox.",
            "Draw a perfect geometric shape on the screen using loops."
        ],
        "project": "<b>Draw Shapes</b>: Create an artistic drawing engine where your sprite moves in loops, using Pen blocks to sketch colorful squares, triangles, and hexagons.",
        "new_blocks": [
            ("erase all", "Pen Extension", "Instantly clears all drawings and trails from the Stage canvas."),
            ("pen down / pen up", "Pen Extension", "Lowers the pen to start drawing lines, or raises it to move without drawing."),
            ("set pen color to ()", "Pen Extension", "Changes the ink color of the drawing pen."),
            ("set pen size to ()", "Pen Extension", "Changes the thickness of the sketched pen line.")
        ],
        "simple": "The Pen block is like putting a crayon in your sprite's hand! Wherever they walk, they leave a beautiful colored trail on the paper!",
        "hint": "Type in the editor: <code>print(\"Shape drawing functions loaded!\")</code> and press Run!",
        "challenge": "Print the message: <code>Shape drawing functions loaded!</code> to start drawing.",
        "starter_code": "# Simulate PicToBlox Session 7: Pen Drawings\n",
        "verify_phrase": "Shape drawing functions loaded!",
        "pills": [
            {
                "label": "Activate Pen Studio",
                "code": "print(\"Shape drawing functions loaded!\")"
            }
        ],
        "homework_desc": "Write a script to clear the screen, lower the pen, and draw a square by repeating 4 times: move 100 steps and turn clockwise 90 degrees.",
        "homework_code": "# Home Challenge: Draw Square Script\n# Write your solution here!"
    },
    {
        "id": 8,
        "badge_icon": "🦅",
        "badge_title": "Flappy Pilot Medal",
        "title": "Station 8: Clone Physics & Gravity (Flappy Bird)",
        "desc": "Understand gravity simulations, clone lifecycles, and automated pipe spawning mechanics.",
        "points": [
            "<b>Cloning</b>: Creating dynamic runtime copies of obstacle pipes.",
            "<b>Clone Lifecycle</b>: Spawning, moving, and deleting clones to keep games running fast.",
            "<b>Gravity Simulation</b>: Constant downward pull changes player Y velocity."
        ],
        "objectives": [
            "Use clones to generate endless moving gates.",
            "Simulate gravity pulling the character down."
        ],
        "project": "<b>Flappy Bird Game</b>: Build a flying bird game where pressing space makes the bird flap upward against constant gravity, dodging cloned pipes that spawn and scroll to the left.",
        "new_blocks": [
            ("create clone of [myself]", "Control", "Spawns a duplicate copy of the sprite at runtime."),
            ("when I start as a clone", "Control", "A starter block that runs script instructions for the newly created clone."),
            ("delete this clone", "Control", "Destroys the clone and removes it from the Stage grid to save memory.")
        ],
        "simple": "Cloning is like a magical stamp! Instead of drawing 100 pipes, you just stamp new ones into the game every few seconds!",
        "hint": "Type in the editor: <code>print(\"Clone spawned successfully!\")</code> and press Run!",
        "challenge": "Print the message: <code>Clone spawned successfully!</code> to run the cloning script.",
        "starter_code": "# Simulate PicToBlox Session 8: Cloning & Physics\n",
        "verify_phrase": "Clone spawned successfully!",
        "pills": [
            {
                "label": "Spawn Clone",
                "code": "print(\"Clone spawned successfully!\")"
            }
        ],
        "homework_desc": "Create a script that spawns a star clone every 2 seconds. When each clone starts, it should drift upwards and delete itself when it hits the top border.",
        "homework_code": "# Home Challenge: Spawning Stars\n# Write your solution here!"
    },
    {
        "id": 9,
        "badge_icon": "🏎️",
        "badge_title": "Steering Racer Medal",
        "title": "Station 9: Painting Sprites & Scenery (Car-Race)",
        "desc": "Explore custom vector art in the Paint Editor, and program steering controls with boundary bouncing.",
        "points": [
            "<b>Paint Editor Tools</b>: Designing vector sprites and tracks (circle, rectangle, reshape).",
            "<b>Steering Movement</b>: Turning sprites clockwise and counter-clockwise with key triggers.",
            "<b>Boundary Bouncing</b>: Preventing characters from walking out of bounds."
        ],
        "objectives": [
            "Draw custom roads and racing cars in the paint editor.",
            "Steer your car using Left and Right Arrow rotation keys."
        ],
        "project": "<b>Car-Race Game</b>: Design a custom race track scenery and a race car sprite, then program arrow-key steering and add track boundary constraints.",
        "new_blocks": [
            ("turn clockwise () degrees", "Motion", "Rotates the sprite to the right (clockwise) by a number of degrees."),
            ("turn counter-clockwise () degrees", "Motion", "Rotates the sprite to the left (counter-clockwise) by a number of degrees."),
            ("if on edge, bounce", "Motion", "Instantly reflects the sprite's direction if it collides with stage borders.")
        ],
        "simple": "Bouncing from edges is like a rubber ball! When you throw it against the wall, it instantly bounces back to you!",
        "hint": "Type in the editor: <code>print(\"Car-Race steering engine activated!\")</code> and press Run!",
        "challenge": "Print the message: <code>Car-Race steering engine activated!</code> to launch the car dashboard.",
        "starter_code": "# Simulate PicToBlox Session 9: Painting & Steering\n",
        "verify_phrase": "Car-Race steering engine activated!",
        "pills": [
            {
                "label": "Start Car Race",
                "code": "print(\"Car-Race steering engine activated!\")"
            }
        ],
        "homework_desc": "Create a script where pressing Left Arrow spins your character 15 degrees left, and pressing Right Arrow spins it 15 degrees right.",
        "homework_code": "# Home Challenge: Character Steering\n# Write your solution here!"
    },
    {
        "id": 10,
        "badge_icon": "🏓",
        "badge_title": "Paddle Master Medal",
        "title": "Station 10: Compound Operators (Pong-ball)",
        "desc": "Build a classic Pong game using paddle bounce calculations, speed increases, and logical operators.",
        "points": [
            "<b>Bounce Physics</b>: Reversing angles of moving ball sprites on target overlaps.",
            "<b>Boolean Logic</b>: Combining multiple checks using logical 'and' / 'or' blocks.",
            "<b>Multi-ball Spawning</b>: Cloning balls to increase gameplay difficulty."
        ],
        "objectives": [
            "Check if the ball is touching the paddle or the wall.",
            "Increase ball speeds as scores go up."
        ],
        "project": "<b>Pong-ball Game</b>: Build an arcade game where a ball bounces off walls and players move paddles with mouse/keys, combining logic operators to detect scoring zone drops.",
        "new_blocks": [
            ("<> and <>", "Operators", "Returns true only if both hexagonal checks inside evaluate to true."),
            ("<> or <>", "Operators", "Returns true if at least one of the checks evaluates to true.")
        ],
        "simple": "The OR block is like choosing dessert! You will be happy if you get ice cream OR if you get cake!",
        "hint": "Type in the editor: <code>print(\"Pong bounce engine activated!\")</code> and press Run!",
        "challenge": "Print the message: <code>Pong bounce engine activated!</code> to verify ball bounce parameters.",
        "starter_code": "# Simulate PicToBlox Session 10: Logic Operators\n",
        "verify_phrase": "Pong bounce engine activated!",
        "pills": [
            {
                "label": "Test Pong Game",
                "code": "print(\"Pong bounce engine activated!\")"
            }
        ],
        "homework_desc": "Write a script where the ball bounces (turns 180 degrees) if it touches Paddle OR if it touches a green boundary color.",
        "homework_code": "# Home Challenge: Paddle Bouncer\n# Write your solution here!"
    },
    {
        "id": 11,
        "badge_icon": "🎯",
        "badge_title": "Target Aim Medal",
        "title": "Station 11: Complex Scoring (Duck Hunter 1)",
        "desc": "Build target aiming locks, follow cursor sensors, and shooting triggers using mouse click handlers.",
        "points": [
            "<b>Cursor Tracking</b>: Programming crosshair aim nodes to follow mouse movements.",
            "<b>Mouse Click Sensing</b>: Detecting clicks (Mouse Down) to simulate shooting.",
            "<b>Score Target Thresholds</b>: Keeping track of successful target hits."
        ],
        "objectives": [
            "Lock the aiming crosshair to the mouse cursor.",
            "Sense mouse down clicks while overlapping with flying targets."
        ],
        "project": "<b>Duck Hunter Game (Part 1)</b>: Design a target shooting screen where ducks fly from bottom sky points and players click their mouse to shoot them, playing lasers!",
        "new_blocks": [
            ("mouse down?", "Sensing", "A hexagonal check block that returns true if the player clicks their mouse."),
            ("touching [mouse-pointer]?", "Sensing", "Checks if your character sprite is touching the mouse cursor.")
        ],
        "simple": "Aiming to the mouse cursor is like a puppy following a treat in your hand! Wherever you move your hand, the puppy runs right to it!",
        "hint": "Type in the editor: <code>print(\"Duck Hunter controller initialized!\")</code> and press Run!",
        "challenge": "Print the message: <code>Duck Hunter controller initialized!</code> to start target tracking.",
        "starter_code": "# Simulate PicToBlox Session 11: Cursor Aiming\n",
        "verify_phrase": "Duck Hunter controller initialized!",
        "pills": [
            {
                "label": "Initialize Duck Hunter",
                "code": "print(\"Duck Hunter controller initialized!\")"
            }
        ],
        "homework_desc": "Write code where a sprite constantly follows the mouse pointer. If the mouse is clicked, play a laser sound and show a blast effect!",
        "homework_code": "# Home Challenge: Crosshair Laser\n# Write your solution here!"
    },
    {
        "id": 12,
        "badge_icon": "🏆",
        "badge_title": "Grand Graduation Medal",
        "title": "Station 12: If-Else Statements (Duck Hunter 2)",
        "desc": "Finish your arcade game by writing two-way outcome branches, layout layer stacking, and ammunition counts.",
        "points": [
            "<b>Two-Way Decisions (If-Else)</b>: Executing code path A if true, or path B if false.",
            "<b>Layer Stacking</b>: Positioning sprites in front of or behind other graphical layers.",
            "<b>Final Publishing</b>: Polishing UI stats, score boundaries, and sounds."
        ],
        "objectives": [
            "Use If-Else blocks to show 'You Win' or 'Game Over' screens.",
            "Stack the targeting crosshair above all flying duck layers."
        ],
        "project": "<b>Duck Hunter Game (Part 2)</b>: Add ammunition counts, reload warnings, and layer stack order so the aiming sight is always in front. Display a Win screen if score exceeds 10, else a Game Over screen!",
        "new_blocks": [
            ("if <> then {} else {}", "Control", "Executes the top block sequence if the condition passes, and the bottom block sequence if it fails."),
            ("go to [front] layer", "Looks", "Moves your sprite layer ranking to the very front so it draws above other sprites.")
        ],
        "simple": "An If-Else block is like a path split in a fairy tale! If you have the key, you open the castle gates. Else, you must take the detour path!",
        "hint": "Type in the editor: <code>print(\"Duck Hunter full game deployed!\")</code> and press Run!",
        "challenge": "Print the message: <code>Duck Hunter full game deployed!</code> to celebrate graduating your first visual block game!",
        "starter_code": "# Simulate PicToBlox Session 12: Graduation Project\n",
        "verify_phrase": "Duck Hunter full game deployed!",
        "pills": [
            {
                "label": "Deploy Full Game",
                "code": "print(\"Duck Hunter full game deployed!\")"
            }
        ],
        "homework_desc": "Program a final script: if Score is greater than 10, say 'Winner!' and go to the front layer; else, say 'Keep trying!' and hide the sprite.",
        "homework_code": "# Home Challenge: Graduation Game Over\n# Write your solution here!"
    }
]

# Compile stations list
stations = []
for s in pictoblox_sessions:
    story_html = f"<h3>{mascot_emoji} Hello, creative future coder!</h3>" \
                 f"I am your friend <b>{mascot_name}</b>, and today I will accompany you on a magical block coding adventure to build <b>{s['title']}</b>! 🌟<br><br>"
    
    # 1. Key points (نقاط)
    story_html += "<b>🎯 Key Points Covered in this Session:</b><ul>"
    for pt in s["points"]:
        story_html += f"<li>{mascot_emoji} {pt}</li>"
    story_html += "</ul>"
    
    # 2. Objectives (الأهداف)
    story_html += "<b>⛳ Session Objectives:</b><ul>"
    for obj in s["objectives"]:
        story_html += f"<li>🎯 {obj}</li>"
    story_html += "</ul>"
    
    # 3. Project (المشروع الخاص بالسيشن)
    story_html += f"<div style='background: #eff6ff; border-left: 4px solid #3b82f6; padding: 10px; border-radius: 8px; margin-top: 10px;'>🏆 <b>Session Project:</b> {s['project']}</div><br>"
    
    # 4. New Blocks (البلوكس الجديدة وبتعمل ايه)
    story_html += "<b>🧱 New Puzzle Blocks Introduced:</b><ul>"
    for name, category, action in s["new_blocks"]:
        story_html += f"<li><span style='background: #f3f4f6; padding: 2px 6px; border-radius: 4px; font-family: monospace; font-weight: bold;'>{name}</span> ({category} drawer): {action}</li>"
    story_html += "</ul>"
    
    story_html += "<p>Let's drag or click the helper block pill below to run the simulation and unlock this station's medal! You've got this! 🌟🚀</p>"
    
    station = {
        "id": s["id"],
        "badge_icon": s["badge_icon"],
        "badge_title": s["badge_title"],
        "title": s["title"],
        "desc": s["desc"],
        "story": story_html,
        "simple": s["simple"],
        "hint": s["hint"],
        "challenge": s["challenge"],
        "starter_code": s["starter_code"],
        "pills": s["pills"],
        "validation_rules": {
            "required_output_text": s["verify_phrase"],
            "required_canvas": False
        },
        "homework": {
            "title": f"🏠 Magic Home Challenge: {s['title']} Builder",
            "desc": s["homework_desc"],
            "code": s["homework_code"],
            "starter_code": s["homework_code"]
        }
    }
    stations.append(station)

games_data = {
    "course_id": course_id,
    "course_title": "PicToBlox",
    "course_subtitle": f"Welcome, future coding hero! Embark on an exciting visual programming adventure with {mascot_short}. Snap colorful blocks, build amazing games, and unlock cool medals! 🐻🎮🚀",
    "xp_total": len(stations) * 100,
    "mascot_img": "./assets/megaminds_mascot.png",
    "stations": stations
}

# Write games.json
games_file = os.path.join(db_path, course_id, 'games.json')
with open(games_file, 'w', encoding='utf-8') as f:
    json.dump(games_data, f, indent=2, ensure_ascii=False)

print("Successfully generated games.json with 12 complete stations for junior_pictoblox!")
