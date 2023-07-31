import json
import tkinter as tk
import tkinter.font as tkfont
from pathlib import Path

fontName = ''
fontColor = ''
fontSize = 0
backgroundColor = ''
valueColor = ''
highlightColor = ''

try:
    with open('config.json', 'r', encoding='utf-8-sig') as file:
        data = json.load(file)
        fontName = data['fontName']
        fontSize = data['fontSize']
        fontColor = data['fontColor']
        backgroundColor = data['backgroundColor']
        valueColor = data['valueColor']
        highlightColor = data['highlightColor']

except FileNotFoundError:
    print("Config file does not exists.")
except json.JSONDecodeError as e:
    print("Error on config file decode:")
    print(e)
except Exception as e:
    print("Error:")
    print(e)        


MarveSnapPath = str(Path.home() / "AppData" / "LocalLow" / "Second Dinner" / "SNAP")

def update_ticket_info():
    mode = ''
    try:
        with open(MarveSnapPath + '/Standalone/States/nvprod/GameState.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            mode = data['RemoteGame']['GameState']['LeagueDefId']
    except FileNotFoundError:
        print("GameState file does not exists.")
    except json.JSONDecodeError as e:
        print("Error on GameState file decode:")
        print(e)
    except Exception as e:
        print("Error:")
        print(e)        
    
    try:
        with open(MarveSnapPath + '/Standalone/States/nvprod/ConquestState.json', 'r', encoding='utf-8-sig') as file:
            data = json.load(file)
            tickets = data['ServerState']['Account']['Tickets']
            
            silver = tickets['Silver']
            gold = tickets['Gold']
            infinity = tickets['Infinity']
            
            valor_silver.config(text=silver, bg=backgroundColor, fg = highlightColor if mode == 'ConquestSilver' else valueColor)
            valor_gold.config(text=gold, bg=backgroundColor, fg = highlightColor if mode == 'ConquestGold' else valueColor)
            valor_infinity.config(text=infinity, bg=backgroundColor, fg = highlightColor if mode == 'ConquestInifity' else valueColor)
            
            root.after(5000, update_ticket_info)

    except FileNotFoundError:
        print("ConquestState file does not exists.")
    except json.JSONDecodeError as e:
        print("Error on ConquestState file decode:")
        print(e)
    except Exception as e:
        print("Error:")
        print(e)

# Main window
root = tk.Tk()

root.configure(bg=backgroundColor)

# Custom Font
fonte_personalizada = tkfont.Font(family=fontName, size=fontSize)

# Set default custom font
root.option_add("*Font", fonte_personalizada)

root.title("Tickets Conquest")

# Labels
def create_label_pair(row, text_label, text_value):
    label = tk.Label(root, text=text_label, fg=fontColor, bg=backgroundColor)
    label.grid(row=row, column=0, sticky='e', padx=5, pady=5)
    
    valor = tk.Label(root, text=text_value, fg=valueColor, bg=backgroundColor)
    valor.grid(row=row, column=1, sticky='w', padx=15, pady=5)

    return label, valor

label_silver, valor_silver = create_label_pair(0, "Silver:", "0")
label_gold, valor_gold = create_label_pair(1, "Gold:", "0")
label_infinity, valor_infinity = create_label_pair(2, "Infinity:", "0")

update_ticket_info()

root.mainloop()