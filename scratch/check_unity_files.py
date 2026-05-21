import os

unity_dir = r"C:\Users\rowan\OneDrive\Megaminds curriculum\AGES (10-16)\Programming\Game Development\unity"

print("Scanning directory:", unity_dir)
if not os.path.exists(unity_dir):
    print("Error: Directory does not exist!")
else:
    for item in sorted(os.listdir(unity_dir)):
        item_path = os.path.join(unity_dir, item)
        if os.path.isdir(item_path):
            print(f"\nLevel Folder: {item}")
            # Scan sessions
            for sess in sorted(os.listdir(item_path)):
                sess_path = os.path.join(item_path, sess)
                if os.path.isdir(sess_path):
                    summary_dir = os.path.join(sess_path, "summary")
                    hw_dir = os.path.join(sess_path, "H.W")
                    has_summary = os.path.exists(summary_dir) and len(os.listdir(summary_dir)) > 0
                    has_hw = os.path.exists(hw_dir) and len(os.listdir(hw_dir)) > 0
                    print(f"  - {sess}: has_summary={has_summary}, has_hw={has_hw}")
                    if has_summary:
                        print(f"    Summary files: {os.listdir(summary_dir)}")
                    if has_hw:
                        print(f"    HW files: {os.listdir(hw_dir)}")
        else:
            print(f"File in root: {item}")
