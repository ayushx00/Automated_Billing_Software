import os

# Step 1: Show current working directory
print("Current working directory:", os.getcwd())

# Step 2: Try to create 'bills' folder
bills_path = os.path.join(os.getcwd(), "bills")

try:
    if not os.path.exists(bills_path):
        os.makedirs(bills_path)
        print("✅ 'bills' folder created.")
    else:
        print("ℹ️ 'bills' folder already exists.")

    # Step 3: Create a sample file inside it
    file_path = os.path.join(bills_path, "test123.txt")
    with open(file_path, "w") as f:
        f.write("Hello, this is a test file.")

    print("✅ Test file created at:", file_path)

except Exception as e:
    print("❌ Error:", e)
