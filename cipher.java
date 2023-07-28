'''
Class Design and Purpose:
This Cipher class is designed to perform encryption and decryption of alphabetic strings using a Caesar cipher. It takes an integer key between 1 and 25 (inclusive) and shifts the letters of the input string by that amount to encrypt and decrypt the text.

Constructor:
The constructor Cipher(int key) is well-designed. It ensures that the provided key is within the valid range (1 to 25) and throws an IllegalArgumentException if an invalid key is passed.

Encrypt Method:
The encrypt(String plaintext) method effectively encrypts the input string by shifting each letter (case-insensitive) by the given key. It properly handles both uppercase and lowercase letters. Non-alphabetic characters are not affected by the encryption process.

Decrypt Method:
The decrypt(String ciphertext) method correctly decrypts the input string by shifting each letter (case-insensitive) in the opposite direction of the encryption. It also handles both uppercase and lowercase letters and preserves non-alphabetic characters.

Handling of Negative Shift in Decrypt:
The approach of adding 26 to the key when decrypting to handle negative values is mathematically valid and ensures proper decryption. However, it could be explained better through comments to aid understanding.

Main Method:
The main method demonstrates how to use the Cipher class by encrypting and decrypting an example string. It would be useful to add additional examples to showcase more scenarios.

Code Reusability:
The Cipher class is simple and can be easily reused in other projects where Caesar cipher encryption and decryption are required.

Potential Improvements:

The class could benefit from additional methods to validate and handle input strings, such as removing special characters or converting the input to uppercase for consistency.
It may be worth considering other types of ciphers for a more advanced encryption solution.
The class name "Cipher" might be a bit too generic. Consider a more descriptive name, like "CaesarCipher," to make its purpose clearer.
Unit Testing:
For a production-level implementation, it is recommended to write unit tests to ensure the correctness of the encryption and decryption methods under various scenarios.

'''

public class Cipher {
    private int key;

    public Cipher(int key) {
        if (key < 1 || key > 25) {
            throw new IllegalArgumentException("Key must be an integer from 1 to 25.");
        }
        this.key = key;
    }

    public String encrypt(String plaintext) {
        StringBuilder encryptedText = new StringBuilder();
        for (char c : plaintext.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                char encryptedChar = (char) ((c - base + key) % 26 + base);
                encryptedText.append(encryptedChar);
            } else {
                encryptedText.append(c);
            }
        }
        return encryptedText.toString();
    }

    public String decrypt(String ciphertext) {
        StringBuilder decryptedText = new StringBuilder();
        for (char c : ciphertext.toCharArray()) {
            if (Character.isLetter(c)) {
                char base = Character.isUpperCase(c) ? 'A' : 'a';
                // We use 26 + key to handle negative values when decrypting
                char decryptedChar = (char) ((c - base - (26 - key)) % 26 + base);
                decryptedText.append(decryptedChar);
            } else {
                decryptedText.append(c);
            }
        }
        return decryptedText.toString();
    }

    public static void main(String[] args) {
        int key = 3; // Change the key value as desired

        Cipher cipher = new Cipher(key);

        // Example usage:
        String plaintext = "HELLO";
        String encryptedText = cipher.encrypt(plaintext);
        System.out.println("Encrypted: " + encryptedText);

        String decryptedText = cipher.decrypt(encryptedText);
        System.out.println("Decrypted: " + decryptedText);
    }
}
