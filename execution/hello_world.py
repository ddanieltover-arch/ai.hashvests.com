import os

def main():
    message = "Hello, World! This is a deterministic execution script."
    print(message)
    
    # Ensure .tmp exists (though it should already be there)
    tmp_dir = ".tmp"
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
        
    output_path = os.path.join(tmp_dir, "hello_output.txt")
    with open(output_path, "w") as f:
        f.write(message)
    
    print(f"Output saved to {output_path}")

if __name__ == "__main__":
    main()
