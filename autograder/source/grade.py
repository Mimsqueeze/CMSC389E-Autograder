import amulet
import os

# Load the submitted world
def grade_world(world_path):
    world = amulet.load_level(world_path)
    score = 0

    # Example: Check if there is a lever at (1, 56, 1) in the Overworld
    block = world.get_block(1, 56, 1, "minecraft:overworld")

    # Check if the block is a lever
    if block.base_name == "lever":
        # Check if the lever is powered (on)
        is_powered = block.properties.get("powered", "false")  # Default to "false" if not set
        if is_powered == "true":
            score += 10
            print("TEST PASSED: Lever is ON at (1, 56, 1)")
        else:
            print("TEST FAILED: Lever is OFF at (1, 56, 1)")
    else:
        print(f"TEST FAILED: Expected Lever at (1, 56, 1), found {block.base_name}")


    # Example: Check if there is a lever at (1, 56, 1) in the Overworld
    block = world.get_block(2, 56, 1, "minecraft:overworld")
    
    # Check if the block is a lever
    if block.base_name == "redstone_lamp":
        # Check if the lever is powered (on)
        is_powered = block.properties.get("powered", "false")  # Default to "false" if not set
        if is_powered == "true":
            score += 10
            print("TEST PASSED: Redstone Lamp is ON at (1, 56, 1)")
        else:
            print("TEST FAILED: Redstone Lamp is OFF at (1, 56, 1)")
    else:
        print(f"TEST FAILED: Expected Redstone Lamp at (1, 56, 1), found {block.base_name}")

    world.close()
    return score

# Main grading script
if __name__ == "__main__":

    score = grade_world("./autograder/source/world/")

    # DEPLOYMENT:
    # score = grade_world("/autograder/source/world/")
    
    # Path to the file
    file_path = "/autograder/results/results.json"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Output results
    with open(file_path, "w") as results_file:
        results_file.write(f'{{"score": {score}}}')
