from PIL import Image  # For handling images
import numpy as np  # For numerical operations

# Function to encrypt/decrypt pixel data using XOR
def xor_encrypt_decrypt(data, key):
    return bytearray([b ^ key for b in data])

# Function to encrypt an image
def encrypt_image(image_path, key, encrypted_image_path):
    with Image.open(image_path) as img:
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        pixel_data = np.array(img)  # Convert image to a NumPy array

    print("Original Pixel Data:")
    print(pixel_data)  # Log original pixel data for verification

    # Flatten the pixel data for encryption
    flat_pixel_data = pixel_data.flatten()

    # Encrypt the pixel data using XOR
    encrypted_pixel_data = xor_encrypt_decrypt(flat_pixel_data, key)

    # Reshape the encrypted data to the original image shape
    encrypted_pixel_data = np.array(encrypted_pixel_data).reshape(pixel_data.shape)

    print("Encrypted Pixel Data:")
    print(encrypted_pixel_data)  # Log encrypted pixel data for verification

    # Convert the encrypted data back to an image
    encrypted_img = Image.fromarray(encrypted_pixel_data.astype("uint8"), "RGB")

    # Save the encrypted image
    encrypted_img.save(encrypted_image_path)
    print(f"Encrypted image saved as {encrypted_image_path}")

# Function to decrypt an image
def decrypt_image(encrypted_image_path, key, decrypted_image_path):
    with Image.open(encrypted_image_path) as img:
        img = img.convert("RGB")  # Ensure the image is in RGB mode
        pixel_data = np.array(img)  # Convert image to a NumPy array

    print("Encrypted Pixel Data (From File):")
    print(pixel_data)  # Log encrypted pixel data for verification

    # Flatten the pixel data for decryption
    flat_pixel_data = pixel_data.flatten()

    # Decrypt the pixel data using XOR
    decrypted_pixel_data = xor_encrypt_decrypt(flat_pixel_data, key)

    # Reshape the decrypted data to the original image shape
    decrypted_pixel_data = np.array(decrypted_pixel_data).reshape(pixel_data.shape)

    print("Decrypted Pixel Data:")
    print(decrypted_pixel_data)  # Log decrypted pixel data for verification

    # Convert the decrypted data back to an image
    decrypted_img = Image.fromarray(decrypted_pixel_data.astype("uint8"), "RGB")

    # Save the decrypted image
    decrypted_img.save(decrypted_image_path)
    print(f"Decrypted image saved as {decrypted_image_path}")

# Main function to handle user input for encryption or decryption
def main():
    action = input("Enter 'encrypt' to encrypt the image or 'decrypt' to decrypt the image: ").strip().lower()

    if action == 'encrypt':
        image_path = input("Enter the path of the image to encrypt: ").strip()
        encrypted_image_path = input("Enter the path to save the encrypted image (with extension like .png, .jpg): ").strip()
        key = int(input("Enter the encryption key (integer): ").strip())
        encrypt_image(image_path, key, encrypted_image_path)

    elif action == 'decrypt':
        encrypted_image_path = input("Enter the path of the encrypted image to decrypt: ").strip()
        decrypted_image_path = input("Enter the path to save the decrypted image (with extension like .png, .jpg): ").strip()
        key = int(input("Enter the decryption key (integer): ").strip())
        decrypt_image(encrypted_image_path, key, decrypted_image_path)

    else:
        print("Invalid input! Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
