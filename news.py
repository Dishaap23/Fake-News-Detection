import tkinter as tk  # Import the tkinter library for creating GUI applications
from tkinter import messagebox  # Import messagebox for displaying alerts and messages
import pickle  # Import pickle for loading serialized objects

# Load your vectorizer and model
vector = pickle.load(open("vectorizer.pkl", 'rb'))  # Load the vectorizer from a pickle file
model = pickle.load(open("finalized_model.pkl", 'rb'))  # Load the trained model from a pickle file

def predict_news():
    """Function to predict news category based on input."""
    news = news_entry.get("1.0", tk.END).strip()  # Get text input from the user, stripping any extra whitespace
    if not news:  # Check if the input is empty
        messagebox.showwarning("Input Error", "Please enter a news headline.")  # Show a warning if input is empty
        return  # Exit the function if no input is provided

    try:
        # Transform and predict
        prediction = model.predict(vector.transform([news]))[0]  # Transform the input and predict the category
        result_label.config(text=f"News headline is -> {prediction}")  # Update the result label with the prediction
    except Exception as e:  # Catch any exceptions that occur during prediction
        messagebox.showerror("Error", f"An error occurred: {e}")  # Show an error message if an exception occurs

# Create the main Tkinter window
root = tk.Tk()  # Initialize the main window
root.title("Fake News Detection")  # Set the title of the window
root.geometry("400x300")  # Set the size of the window

# Create and place widgets
instructions = tk.Label(root, text="Enter a news headline below:", font=("Arial", 12))  # Create a label for instructions
instructions.pack(pady=10)  # Place the label in the window with padding

news_entry = tk.Text(root, height=5, width=40)  # Create a text entry widget for user input
news_entry.pack(pady=5)  # Place the text entry in the window with padding

predict_button = tk.Button(root, text="Predict", command=predict_news, font=("Arial", 10))  # Create a button to trigger prediction
predict_button.pack(pady=10)  # Place the button in the window with padding

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")  # Create a label to display the prediction result
result_label.pack(pady=10)  # Place the result label in the window with padding

# Run the application
root.mainloop()  # Start the Tkinter event loop to run the application