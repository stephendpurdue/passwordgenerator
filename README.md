
# Password Generator

## 📌 Overview
`passwordgenerator.py` is a simple Python script that generates secure passwords based on user-defined criteria.  
The user specifies:
- Minimum password length
- Whether to include numbers
- Whether to include special characters

The program then generates a random password that meets those requirements.



## ✨ Features
- Adjustable **minimum length**  
- Option to include or exclude **numbers**  
- Option to include or exclude **special characters**  
- Ensures generated passwords meet selected criteria



## 🛠 Requirements
- Python 3.x  
- No additional libraries required (uses built-in `random` and `string` modules)



## 📖 Usage
1. Clone or download the script to your local machine.
2. Open a terminal in the script’s directory.
3. Run the script:
   ```bash
   python passwordgenerator.py


4. Follow the prompts:

   ```
   Enter the desired minimum length: 12
   Would you like numbers (y/n)? y
   Would you like special characters (y/n)? n
   ```
5. The generated password will be displayed:

   ```
   The generated password is AbCdEfGh1234
   ```



## 📂 File Structure

```
passwordgenerator.py   # Main script
```



## ⚠ Notes

* Passwords are generated randomly using Python's `random.choice` method.
* The script ensures inclusion of selected character types.
* For improved cryptographic security, consider replacing `random` with `secrets` in production environments.



## 📜 License

This project is open-source. You may use, modify, and distribute it freely.

