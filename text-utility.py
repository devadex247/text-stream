import sys
import re
import subprocess

def copy_to_clipboard(text):
    """Copies text to the system clipboard based on the Operating System."""
    try:
        if sys.platform == "darwin":  # macOS
            process = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, text=True)
            process.communicate(text)
            return True
        elif sys.platform == "win32":  # Windows
            process = subprocess.Popen(['clip'], stdin=subprocess.PIPE, text=True)
            process.communicate(text)
            return True
        else:
            # Linux usually requires xclip or xsel, which aren't always built-in
            return False
    except Exception:
        return False

def analyze_text(text):
    if not text.strip():
        print("\nError: No text provided. Please paste some text!")
        return

    # Clean the text: remove duplicate whitespaces/newlines and trim edges
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    
    # Calculate metrics
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", "").replace("\n", "").replace("\r", ""))
    
    # Split by whitespace to get words
    words = text.split()
    word_count = len(words)
    
    # Rough sentence count using punctuation splitters
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip()])
    
    # Average reading speed is roughly 200 words per minute
    reading_time_seconds = round((word_count / 200) * 60)
    
    # Format reading time beautifully
    if reading_time_seconds < 60:
        reading_time = f"{reading_time_seconds} seconds"
    else:
        minutes = reading_time_seconds // 60
        seconds = reading_time_seconds % 60
        reading_time = f"{minutes} min {seconds} sec"

    # Try to copy the cleaned text to clipboard
    copied = copy_to_clipboard(cleaned_text)

    # Display Results
    print("\n" + "="*40)
    print(" 📊 TEXT ANALYSIS RESULTS")
    print("="*40)
    print(f"🔹 Words:             {word_count}")
    print(f"🔹 Sentences:         {sentence_count}")
    print(f"🔹 Characters (all):  {char_count_with_spaces}")
    print(f"🔹 Characters (none): {char_count_no_spaces}")
    print(f"🔹 Est. Reading Time: {reading_time}")
    print("-"*40)
    print("✨ CLEANED TEXT (Single line, normalized spaces):")
    
    preview = cleaned_text[:150] + "..." if len(cleaned_text) > 150 else cleaned_text
    print(f"   \"{preview}\"")
    print("-"*40)
    
    if copied:
        print("📋 Success: Cleaned text has been copied to your clipboard!")
    else:
        print("⚠️  Note: Cleaned text could not be auto-copied (Unsupported OS).")
    print("="*40 + "\n")

if __name__ == "__main__":
    print("📥 Paste your text below.")
    print("👉 Press Ctrl+D (Mac/Linux) or Ctrl+Z then Enter (Windows) when you are finished:")
    print("-" * 60)
    
    user_input = sys.stdin.read()
    analyze_text(user_input)