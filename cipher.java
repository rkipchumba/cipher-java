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
