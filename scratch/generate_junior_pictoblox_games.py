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
        "new_blocks_html": [
            '<div class="scratch-block scratch-motion">go to x: <span class="scratch-input">0</span> y: <span class="scratch-input">0</span></div>',
            '<div class="scratch-block scratch-motion">glide <span class="scratch-input">1</span> secs to x: <span class="scratch-input">100</span> y: <span class="scratch-input">50</span></div>',
            '<div class="scratch-block scratch-looks">say <span class="scratch-input">Let\'s race!</span> for <span class="scratch-input">2</span> seconds</div>',
            '<div class="scratch-block scratch-sound">start sound <span class="scratch-input-dark">cheering ▾</span></div>'
        ],
        "simple": "Imagine PicToBlox blocks are like Lego blocks! You snap one block on top of another to build a towering command that tells your sprite exactly where to go!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the race game in PicToBlox!",
        "challenge": "Build your Animal Racing game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 1: Animal Racing\n",
        "verify_phrase": "Animal Racing active!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-events">when 🟢 clicked</div>',
            '<div class="scratch-block scratch-control">forever [ 🔄 ]</div>',
            '<div class="scratch-block scratch-control">wait <span class="scratch-input">1</span> seconds</div>',
            '<div class="scratch-block scratch-looks">show</div>',
            '<div class="scratch-block scratch-looks">hide</div>',
            '<div class="scratch-block scratch-looks">switch backdrop to <span class="scratch-input-dark">Savanna ▾</span></div>'
        ],
        "simple": "Imagine a forever loop is like a musical box that repeats your favorite song over and over until you close the lid!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the elephant walk story in PicToBlox!",
        "challenge": "Build your Elephant Story animation in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 2: Elephant Story\n",
        "verify_phrase": "Elephant Story animation active!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-control">if <span class="scratch-input-hex">?</span> then</div>',
            '<span class="scratch-block scratch-sensing" style="border-radius: 20px; padding: 6px 14px;">key <span class="scratch-input-dark">space ▾</span> pressed?</span>',
            '<span class="scratch-block scratch-sensing" style="border-radius: 20px; padding: 6px 14px;">touching color <span style="display:inline-block; width:16px; height:16px; background-color:#ff0000; border-radius:50%; vertical-align:middle; border:1px solid #fff;"></span> ?</span>',
            '<div class="scratch-block scratch-motion">change x by <span class="scratch-input">10</span></div>',
            '<div class="scratch-block scratch-motion">change y by <span class="scratch-input">10</span></div>'
        ],
        "simple": "An If statement is like a traffic light! If the light is green, your hero walks forward. If it's red, they must stand still!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Maze Game in PicToBlox!",
        "challenge": "Build your interactive Maze Game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 3: Maze Game\n",
        "verify_phrase": "Maze controller activated!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-events">broadcast <span class="scratch-input-dark">jump_trigger ▾</span></div>',
            '<div class="scratch-block scratch-events">when I receive <span class="scratch-input-dark">jump_trigger ▾</span></div>',
            '<span class="scratch-block scratch-operators" style="border-radius: 20px; padding: 6px 14px;">pick random <span class="scratch-input">1</span> to <span class="scratch-input">10</span></span>'
        ],
        "simple": "Broadcasting is like a gym teacher blowing a whistle! When the whistle blows (broadcast), all students run (when I receive)!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Jumper Frog Game in PicToBlox!",
        "challenge": "Build your Jumper Frog Game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 4: Broadcast Syncs\n",
        "verify_phrase": "Broadcast message received successfully!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-variables">set <span class="scratch-input-dark">Score ▾</span> to <span class="scratch-input">0</span></div>',
            '<div class="scratch-block scratch-variables">change <span class="scratch-input-dark">Score ▾</span> by <span class="scratch-input">1</span></div>',
            '<div class="scratch-block scratch-control">stop <span class="scratch-input-dark">all ▾</span></div>',
            '<div class="scratch-block scratch-motion">set x to <span class="scratch-input">0</span></div>',
            '<div class="scratch-block scratch-motion">set y to <span class="scratch-input">0</span></div>'
        ],
        "simple": "A variable is like a small chalkboard! You start with a zero written on it, and every time you score, you erase it and write the new score!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Basketball Game in PicToBlox!",
        "challenge": "Build your Basketball Game with scoring scoreboard in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 5: Variables & Scoreboards\n",
        "verify_phrase": "Score variable updated to 10!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-events">when this sprite clicked</div>',
            '<div class="scratch-block scratch-variables">show variable <span class="scratch-input-dark">Score ▾</span></div>',
            '<div class="scratch-block scratch-variables">hide variable <span class="scratch-input-dark">Score ▾</span></div>',
            '<div class="scratch-block scratch-myblocks" style="border-top-left-radius: 20px; border-top-right-radius: 20px;">define <span class="scratch-input-dark">CustomJump</span></div>'
        ],
        "simple": "Custom blocks are like recipes! Instead of listing instructions every time you make a cake, you just name the recipe 'Bake Cake' and call it!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Giga-man Clicker Game in PicToBlox!",
        "challenge": "Build your Giga-man Clicker Game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 6: Click Actions\n",
        "verify_phrase": "Giga-man game interface loaded!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-pen">erase all</div>',
            '<div class="scratch-block scratch-pen">pen down</div>',
            '<div class="scratch-block scratch-pen">pen up</div>',
            '<div class="scratch-block scratch-pen">set pen color to <span style="display:inline-block; width:16px; height:16px; background-color:#ff00ff; border-radius:50%; vertical-align:middle; border:1px solid #fff;"></span></div>',
            '<div class="scratch-block scratch-pen">set pen size to <span class="scratch-input">5</span></div>'
        ],
        "simple": "The Pen block is like putting a crayon in your sprite's hand! Wherever they walk, they leave a beautiful colored trail on the paper!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Draw Shapes Project in PicToBlox!",
        "challenge": "Build your Draw Shapes Project in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 7: Pen Drawings\n",
        "verify_phrase": "Shape drawing functions loaded!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-control">create clone of <span class="scratch-input-dark">myself ▾</span></div>',
            '<div class="scratch-block scratch-events">when I start as a clone</div>',
            '<div class="scratch-block scratch-control">delete this clone</div>'
        ],
        "simple": "Cloning is like a magical stamp! Instead of drawing 100 pipes, you just stamp new ones into the game every few seconds!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Flappy Bird Game in PicToBlox!",
        "challenge": "Build your Flappy Bird Game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 8: Cloning & Physics\n",
        "verify_phrase": "Clone spawned successfully!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-motion">turn ↻ <span class="scratch-input">15</span> degrees</div>',
            '<div class="scratch-block scratch-motion">turn ↺ <span class="scratch-input">15</span> degrees</div>',
            '<div class="scratch-block scratch-motion">if on edge, bounce</div>'
        ],
        "simple": "Bouncing from edges is like a rubber ball! When you throw it against the wall, it instantly bounces back to you!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Car-Race Game in PicToBlox!",
        "challenge": "Build your Car-Race Game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 9: Painting & Steering\n",
        "verify_phrase": "Car-Race steering engine activated!",
        "pills": [],
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
        "new_blocks_html": [
            '<span class="scratch-block scratch-operators" style="border-radius: 20px; padding: 6px 14px;"><span class="scratch-input-hex">?</span> and <span class="scratch-input-hex">?</span></span>',
            '<span class="scratch-block scratch-operators" style="border-radius: 20px; padding: 6px 14px;"><span class="scratch-input-hex">?</span> or <span class="scratch-input-hex">?</span></span>'
        ],
        "simple": "The OR block is like choosing dessert! You will be happy if you get ice cream OR if you get cake!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Pong-ball Game in PicToBlox!",
        "challenge": "Build your Pong-ball Game in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 10: Logic Operators\n",
        "verify_phrase": "Pong bounce engine activated!",
        "pills": [],
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
        "new_blocks_html": [
            '<span class="scratch-block scratch-sensing" style="border-radius: 20px; padding: 6px 14px;">mouse down?</span>',
            '<span class="scratch-block scratch-sensing" style="border-radius: 20px; padding: 6px 14px;">touching <span class="scratch-input-dark">mouse-pointer ▾</span>?</span>'
        ],
        "simple": "Aiming to the mouse cursor is like a puppy following a treat in your hand! Wherever you move your hand, the puppy runs right to it!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Duck Hunter Game Part 1 in PicToBlox!",
        "challenge": "Build your Duck Hunter Game Part 1 in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 11: Cursor Aiming\n",
        "verify_phrase": "Duck Hunter controller initialized!",
        "pills": [],
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
        "new_blocks_html": [
            '<div class="scratch-block scratch-control">if <span class="scratch-input-hex">?</span> then / else</div>',
            '<div class="scratch-block scratch-looks">go to <span class="scratch-input-dark">front ▾</span> layer</div>'
        ],
        "simple": "An If-Else block is like a path split in a fairy tale! If you have the key, you open the castle gates. Else, you must take the detour path!",
        "hint": "Click the big green button below: <b>Done! Claim My Medal!</b> once you build the Duck Hunter Game Part 2 in PicToBlox!",
        "challenge": "Build your Duck Hunter Game Part 2 final graduation project in PicToBlox and click the green medal button below!",
        "starter_code": "# Simulate PicToBlox Session 12: Graduation Project\n",
        "verify_phrase": "Duck Hunter full game deployed!",
        "pills": [],
        "homework_desc": "Program a final script: if Score is greater than 10, say 'Winner!' and go to the front layer; else, say 'Keep trying!' and hide the sprite.",
        "homework_code": "# Home Challenge: Graduation Game Over\n# Write your solution here!"
    }
]

# Compile stations list
stations = []
for idx, s in enumerate(pictoblox_sessions):
    slider_id = f"kid_slider_{idx}"
    story_html = f"""
    <style>
        .kid-slider-container {{
            position: relative; width: 100%; overflow: hidden; border-radius: 15px; margin-top: 15px;
        }}
        .kid-slides-wrapper {{
            display: flex; overflow-x: auto; scroll-snap-type: x mandatory; scroll-behavior: smooth;
            gap: 15px; padding-bottom: 15px;
        }}
        .kid-slides-wrapper::-webkit-scrollbar {{ height: 10px; }}
        .kid-slides-wrapper::-webkit-scrollbar-track {{ background: #f1f5f9; border-radius: 10px; }}
        .kid-slides-wrapper::-webkit-scrollbar-thumb {{ background: #3b82f6; border-radius: 10px; }}
        
        .kid-slide {{
            flex: 0 0 100%; scroll-snap-align: start; background: linear-gradient(135deg, #ffffff, #f8fafc);
            padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 3px solid #e2e8f0;
            box-sizing: border-box; display: flex; flex-direction: column; gap: 10px;
        }}
        .kid-slide h4 {{ color: #023047; font-size: 1.4rem; font-weight: 900; margin: 0 0 10px 0; border-bottom: 3px dashed #fb8500; padding-bottom: 8px; display: inline-block; }}
        .kid-slide-point {{ background: #eff6ff; padding: 12px; border-radius: 10px; border-left: 5px solid #3b82f6; font-size: 1.15rem; font-weight: bold; color: #1e293b; margin-bottom: 8px; }}
        .kid-slide-obj {{ background: #ecfdf5; padding: 12px; border-radius: 10px; border-left: 5px solid #10b981; font-size: 1.15rem; font-weight: bold; color: #065f46; margin-bottom: 8px; }}
        
        .slider-controls {{ display: flex; justify-content: space-between; margin-top: 10px; }}
        .slider-btn {{ background: #ffb703; color: #023047; border: none; padding: 10px 20px; border-radius: 20px; font-weight: 900; font-size: 1.1rem; cursor: pointer; transition: transform 0.2s; box-shadow: 0 4px 10px rgba(255, 183, 3, 0.3); }}
        .slider-btn:hover {{ transform: scale(1.05); }}
    </style>
    
    <div style="text-align: center; margin-bottom: 20px;">
        <h3 style="font-size: 1.6rem; color: #fb8500; text-shadow: 1px 1px 0px rgba(0,0,0,0.1);">{mascot_emoji} Hello, creative future coder!</h3>
        <p style="font-size: 1.2rem; font-weight: 700; margin: 5px 0;">I am your friend <b style="color: #3b82f6;">{mascot_name}</b>!</p>
        <p style="font-size: 1.15rem; font-weight: bold; color: #64748b; margin: 0;">Today we will build <b>{s['title']}</b>! 🌟 Slide to learn!</p>
    </div>
    
    <div class="kid-slider-container">
        <div class="kid-slides-wrapper" id="{slider_id}">
            
            <!-- Slide 1: Points -->
            <div class="kid-slide">
                <h4>🎯 Slide 1: New Things to Learn!</h4>
    """
    for pt in s["points"]:
        story_html += f"<div class='kid-slide-point'>✨ {pt}</div>"
        
    story_html += f"""
                <div class="slider-controls" style="justify-content: flex-end;">
                    <button class="slider-btn" onclick="document.getElementById('{slider_id}').scrollBy({{left: document.getElementById('{slider_id}').clientWidth}})">Next 👉</button>
                </div>
            </div>
            
            <!-- Slide 2: Objectives -->
            <div class="kid-slide">
                <h4>⛳ Slide 2: Our Goals Today!</h4>
    """
    for obj in s["objectives"]:
        story_html += f"<div class='kid-slide-obj'>🚀 {obj}</div>"
        
    story_html += f"""
                <div class="slider-controls">
                    <button class="slider-btn" onclick="document.getElementById('{slider_id}').scrollBy({{left: -document.getElementById('{slider_id}').clientWidth}})">👈 Back</button>
                    <button class="slider-btn" onclick="document.getElementById('{slider_id}').scrollBy({{left: document.getElementById('{slider_id}').clientWidth}})">Next 👉</button>
                </div>
            </div>
            
            <!-- Slide 3: Project -->
            <div class="kid-slide">
                <h4>🏆 Slide 3: The Mission!</h4>
                <div style="font-size: 1.3rem; line-height: 1.6; background: #fffbeb; padding: 20px; border-radius: 12px; border: 3px dashed #fbbf24; color: #92400e; font-weight: bold; text-align: center;">
                    {s['project']}
                </div>
                <div class="slider-controls">
                    <button class="slider-btn" onclick="document.getElementById('{slider_id}').scrollBy({{left: -document.getElementById('{slider_id}').clientWidth}})">👈 Back</button>
                    <button class="slider-btn" onclick="document.getElementById('{slider_id}').scrollBy({{left: document.getElementById('{slider_id}').clientWidth}})">Next 👉</button>
                </div>
            </div>
            
            <!-- Slide 4: Blocks -->
            <div class="kid-slide">
                <h4>🧩 Slide 4: Magic Puzzle Blocks!</h4>
                <div style="background: rgba(2, 48, 71, 0.03); border: 2px solid rgba(2, 48, 71, 0.1); padding: 15px; border-radius: 12px; display: flex; flex-direction: column; gap: 8px;">
    """
    for block_markup in s["new_blocks_html"]:
        story_html += f"<div>{block_markup}</div>"
        
    story_html += f"""
                </div>
                <p style="font-size: 1.15rem; font-weight: 700; color: #ef4444; text-align: center; margin-top: 10px;">
                    Snap these blocks! When your game runs, click the Green Medal Button! 🏅
                </p>
                <div class="slider-controls" style="justify-content: flex-start;">
                    <button class="slider-btn" onclick="document.getElementById('{slider_id}').scrollBy({{left: -document.getElementById('{slider_id}').clientWidth}})">👈 Back</button>
                </div>
            </div>
            
        </div>
    </div>
    """
    
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

print("Successfully generated games.json with 12 visual-block styled sessions for junior_pictoblox!")
