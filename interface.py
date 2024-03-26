import tkinter as tk
from tkinter import messagebox, scrolledtext
from googletrans import Translator

# Função para detecção de idioma
def detect_language():
    text = entry.get().strip()  # Remover espaços em branco
    if not text:
        messagebox.showerror("Erro na Detecção", "Por favor, insira texto antes de detectar o idioma.")
        return
    translator = Translator()
    detected_language = translator.detect(text)
    messagebox.showinfo("Idioma Detectado", f"O idioma detectado é: {detected_language.lang}")

# Função para traduzir o texto
def translate_text():
    text = entry.get().strip()  # Remover espaços em branco
    if not text:
        messagebox.showerror("Erro na Tradução", "Por favor, insira texto antes de traduzir.")
        return
    translator = Translator()
    desired_language = language_var.get()
    try:
        translated_text = translator.translate(text, dest=desired_language).text
        history_text.insert(tk.END, f"Texto original: {text}\nTradução: {translated_text}\n\n")
        messagebox.showinfo("Tradução Realizada", "Tradução realizada com sucesso")
        entry.delete(0, tk.END)  # Limpa o campo de entrada
    except Exception as e:
        messagebox.showerror("Erro na Tradução", str(e))

# Configuração da interface gráfica
root = tk.Tk()
root.title("Tradutor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Digite o texto:")
label.grid(row=0, column=0, padx=5, pady=5)

entry = tk.Entry(frame, width=40)
entry.grid(row=0, column=1, padx=5, pady=5)

language_options = ['en', 'fr', 'es']  # Adicione mais idiomas conforme necessário
language_var = tk.StringVar()
language_var.set('en')  # Idioma padrão
language_menu = tk.OptionMenu(frame, language_var, *language_options)
language_menu.grid(row=0, column=2, padx=5, pady=5)

detect_button = tk.Button(frame, text="Detectar Idioma", command=detect_language, bg="lightblue", fg="black")
detect_button.grid(row=1, column=0, padx=5, pady=5)

translate_button = tk.Button(frame, text="Traduzir", command=translate_text, bg="lightgreen", fg="black")
translate_button.grid(row=1, column=1, padx=5, pady=5)

history_label = tk.Label(root, text="Histórico de Tradução:")
history_label.pack(padx=10, pady=(10, 0))

history_text = scrolledtext.ScrolledText(root, width=50, height=10)
history_text.pack(padx=10, pady=(0, 10))

root.mainloop()
