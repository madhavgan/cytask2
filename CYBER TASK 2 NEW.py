from PIL import Image
import numpy as np

def encrypt_image(image_path, key):
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Encrypting by applying XOR operation with the key to each pixel value
    encrypted_array = image_array ^ key
    encrypted_image = Image.fromarray(encrypted_array)
    
    return encrypted_image

def decrypt_image(encrypted_image, key):
    encrypted_array = np.array(encrypted_image)
    
    # Decrypting by applying XOR operation with the key to each pixel value
    decrypted_array = encrypted_array ^ key
    decrypted_image = Image.fromarray(decrypted_array)
    
    return decrypted_image

def main():
    print("Image Encryption Tool")
    choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? ").lower()
    
    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the encryption/decryption key (an integer): "))
    
    if choice in ['e', 'encrypt']:
        encrypted_image = encrypt_image(image_path, key)
        encrypted_image.save("encrypted_image.png")
        print("Image encrypted and saved as 'encrypted_image.png'")
    
    elif choice in ['d', 'decrypt']:
        encrypted_image = Image.open(image_path)
        decrypted_image = decrypt_image(encrypted_image, key)
        decrypted_image.save("decrypted_image.png")
        print("Image decrypted and saved as 'decrypted_image.png'")
    
    else:
        print("Invalid choice! Please choose 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
