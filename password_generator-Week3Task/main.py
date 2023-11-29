import sys
import random
import string
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit


def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


def generate_multiple_passwords(number_of_passwords=1, length=12):
    passwords = [generate_password(length) for _ in range(number_of_passwords)]
    return passwords


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.length_label = QLabel("Password Length:")
        self.length_input = QLineEdit()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)

        self.number_label = QLabel("Number of Passwords:")
        self.number_input = QLineEdit()
        layout.addWidget(self.number_label)
        layout.addWidget(self.number_input)

        self.generate_button = QPushButton("Generate Passwords")
        self.generate_button.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_button)

        self.result_text = QTextEdit()
        layout.addWidget(self.result_text)

        self.setLayout(layout)
        self.setWindowTitle("Password Generator")

    def generate_passwords(self):
        try:
            password_length = int(self.length_input.text())
            number_of_passwords = int(self.number_input.text())

            generated_passwords = generate_multiple_passwords(
                number_of_passwords, password_length)
            output = "\nGenerated Passwords:\n" + \
                "\n".join(generated_passwords)
            self.result_text.setPlainText(output)
        except ValueError:
            self.result_text.setPlainText(
                "Please enter valid integers for length and number of passwords.")


def main():
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
